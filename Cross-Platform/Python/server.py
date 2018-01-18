#!/usr/bin/env python
""" Reverse Shell Script -- By: @BlackVikingPro """
""" Current Version: v1.0 """

import sys, socket, threading, signal

def signal_handler(signal, frame):
	print ( 'Caught ( ^C ) - Exiting now...' )
	sys.exit(0)
	pass

try:
	server = ('', int(sys.argv[1]))
	pass
except IndexError as e:
	if sys.argv[0].startswith('./'):
		print ( "Usage: %s <port>" % sys.argv[0] )
		exit()
	else:
		print ( "Usage ./%s <port>" % sys.argv[0] )
		exit()
		pass

def handle(conn):
	while True:
		request = conn.recv(1028)
		if request:
			print request.decode('utf-8')
			data = raw_input()
			conn.send(data.encode())
			pass
		pass
	pass

def listen():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # define a TCP socket
	sock.bind( server )
	sock.listen( 5 )
	print "[*] Listening on %s:%s" % server

	while True:
			conn, addr = sock.accept()
			print "[*] Accepted connection from: %s:%d\n" % addr
			signal.signal(signal.SIGINT, signal_handler)
			try:
				handle(conn)
				pass
			except Exception as e:
				conn.close() # always close socket, no matter what.
				raise e
			pass
	pass

if __name__ == '__main__':
	listen()