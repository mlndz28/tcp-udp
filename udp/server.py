#!/usr/bin/env python2

import socket
import threading
import common

def serve(s, data, addr, data_callback):
	print("Received from " + repr(addr) + ": " + repr(data))
	response = data_callback(data)		# manipulate the received data
	s.sendto(response, addr)			# send the response	
	print("Sending to " + repr(addr) + ": " + repr(response) + "\n")
	
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	# create a socket
s.bind((common.HOST, common.PORT))						# bind the address to the socket

while 1:
	msg, addr = s.recvfrom(1024)
	callback = lambda d : d.upper()										# make the text upper case
	x = threading.Thread(target=serve, args=(s, msg, addr, callback))	# create a thread so the main thread only listens to new requests
	x.daemon = True														# the child thread must exit when the main thread does
	x.start()