#!/usr/bin/env python

import socket

SERVER = 'irc.freenode.net'
CHANNEL = "#OREServerChat"
BOTNICK = 'Nickster_Bot'
COMMAND_SIGN = '@'

def Send(target, message):
	sock.send('PRIVMSG '+target+' :'+message+'\r\n')
	print(message)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER,6667))
sock.send('USER '+BOTNICK+' '+BOTNICK+' '+BOTNICK+" :hi.\r\n")
sock.send('NICK '+BOTNICK + "\r\n")
sock.send('JOIN '+CHANNEL + "\r\n")


if __name__ == "__main__":
	while True:
		received = sock.recv(2048)
		received = received[:len(received)-len('\r\n')]
		print received
		if received.find(COMMAND_SIGN+'school') != -1:
			try:
				Send(CHANNEL,'@'+received.split(COMMAND_SIGN+'school ',1)[1]+' You seem interested in the school server!')	
				Send(CHANNEL,'@'+received.split(COMMAND_SIGN+'school ',1)[1]+' You should visit http://forum.openredstone.org/forumdisplay.php?fid=36')
				continue
			except:
				continue
		if received.find(COMMAND_SIGN+'test') != -1:
			try:
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' Yes, I am working. You idiot...')
				continue
			except:
				continue
		if received.find(COMMAND_SIGN+'help') != -1:
			try:
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' Help page for Nickster_Bot:')
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' To greet a new player, type "@welcome [player name]"')
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' To give a player info on the school server, type "@school [player name]"')
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' To give information on applying to build/school, type "@apply [player name]"')
				continue
			except:
				continue				
		if received.find(COMMAND_SIGN+'welcome') != -1:
			try:
				Send(CHANNEL,'@'+received.split(COMMAND_SIGN+'welcome ',1)[1]+' Welcome to ORE! The place of Shennanigans!')
				Send(CHANNEL,'@'+received.split(COMMAND_SIGN+'welcome ',1)[1]+' For futher information, visit http://www.openredstone.org')
				continue
			except:
				continue
		if received.find(COMMAND_SIGN+'apply') != -1:
			try:
				Send(CHANNEL,'@'+received.split(COMMAND_SIGN+'apply ',1)[1]+' To apply, visit http://www.openredstone.org/apply for information')
				continue
			except:
				continue
		if received.find(COMMAND_SIGN+'stop') != -1:
			sock.send('QUIT\r\n')
			break
	print('hi')

