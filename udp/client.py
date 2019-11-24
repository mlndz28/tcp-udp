#!/usr/bin/env python2

from __future__ import print_function
import socket
import common

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	# define the address family (IPv4) and the data transfer protocol (UDP)
s.settimeout(1)											# set a timeout in case the server doesn't respond

while 1:
	print(">> ", end= "")
	msg = raw_input()
	s.sendto(msg, (common.HOST, common.PORT))		# send input text
	try:
		data = s.recvfrom(1024)						# sync wait for a response from the server
		print('Received', repr(data), "\n")
	except:
		print('\nThe socket timed out. No response from the server.\n')


