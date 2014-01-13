/*
 * Copyright (C) 2005 SerComm Corporation. All Rights Reserved.
 *
 * SerComm Corporation reserves the right to make changes to this document
 * without notice. SerComm Corporation makes no warranty, representation
 * or guarantee regarding the suitability of its products for any
 * particular purpose. SerComm Corporation assumes no liability arising
 * out of the application or use of any product or circuit. SerComm
 * Corporation specifically disclaims any and all liability, including
 * without limitation consequential or incidental damages; neither does
 * it convey any license under its patent rights, nor the rights of
 * others.
 */
/* ScMM */
#include <string.h>
#define SCM_MAGIC 0x53634d4d

#define DEFAULT_REMOTE_IP   "192.168.0.1"
#define DEFAULT_REMOTE_PORT 32764 
//#define DEFAULT_REMOTE_PORT 12345 

/* header struct*/
typedef struct scfgmgr_header_s{
	unsigned long   magic;
	int   cmd;
	unsigned long   len;
} scfgmgr_header;

enum {
	SCFG_WARNING=-2,
	SCFG_ERR,
	SCFG_OK,
	SCFG_GETALL,
	SCFG_GET,
	SCFG_SET,
	SCFG_COMMIT,
	SCFG_TEST,
	SCFG_ADSL_STATUS,
	SCFG_CONSOLE,
	SCFG_RECEIVE,
	SCFG_VERSION,
	SCFG_LOCAL_IP,
	SCFG_RESTORE,
	SCFG_CHECKSUM,
	SCFG_CFG_INIT,
}cmd_type;
