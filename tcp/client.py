#!/usr/bin/env python2

from __future__ import print_function
import socket
import atexit
import common

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# define the address family (IPv4) and the data transfer protocol (TCP)
try:
	s.connect((common.HOST, common.PORT))				# three-way handshake
except:
	print("\nCan't connect to server.\n")
	exit()
s.settimeout(1)											# set a timeout in case the server doesn't respond
atexit.register(common.on_quit, s) 						# register callback to exit signal

while 1:
	print(">> ", end= "")
	msg = raw_input()
	if msg == '': continue
	try:
		s.sendall(msg)				# send input text
		data = s.recv(1024)		# sync wait for a response from the server
		print('Received', repr(data), "\n")
	except:
		print('\nThe socket timed out. No response from the server.\n')
		exit()


