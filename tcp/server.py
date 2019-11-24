#!/usr/bin/env python2

import socket
import threading
import sys
import common

def serve(conn, addr, data_callback):
	print('Connected to', addr)
	while 1:
		data = conn.recv(1024)
		if not data: break				# when the stream has been lost, close the connection
		print("Received: " + repr(data))
		response = data_callback(data)	# manipulate the received data
		conn.sendall(response)			# send the response	
		print("Sending: " + repr(response) + "\n")
	common.on_quit(conn, addr)	# close the connection
	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# create a socket
s.bind((common.HOST, common.PORT))	# bind the address to the socket

while 1:
	s.listen(1)	# wait for a connection request
	conn, addr = s.accept()
	callback = lambda d : d.upper()	# make the text upper case
	x = threading.Thread(target=serve, args=(conn, addr, callback))	# create a thread for the connection and goes on to listen for another request
	x.daemon = True	# so the thread will exit when the main thread does
	x.start()