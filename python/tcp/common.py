HOST = '127.0.0.1'    	# remote host
PORT = 42501            # port used by both server and client

def on_quit(s, addr=(HOST, PORT)):
	"""Common handler for closing sockets.
	
	Parameters
    ----------
    s : Socket
	"""
	s.close()
	print("Closed connection with", repr(addr))