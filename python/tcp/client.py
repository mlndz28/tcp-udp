#!/usr/bin/env python2

from __future__ import print_function
import socket
import atexit
import common

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# Define the address family (IPv4) and the data transfer protocol (TCP)
s.connect((common.HOST, common.PORT))		# three-way handshake
atexit.register(common.on_quit, s) 	# registers callback to exit signal
while 1:
	print(">> ", end= "")
	msg = raw_input()
	s.sendall(msg)			# send input text
	data = s.recv(1024)		# sync wait for a response from the server
	print('Received', repr(data), "\n")


