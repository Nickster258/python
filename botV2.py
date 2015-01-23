#!/usr/bin/env python3

import socket

SERVER = 'irc.freenode.net'
CHANNEL = "#OREServerChat"
BOTNICK = 'Nickster_Bot'
COMMAND_SIGN = '@'

def Send(target, message):
	sock.send(('PRIVMSG '+target+' :'+message+'\r\n').encode())
	print(message)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER,6667))
sock.send(('USER '+BOTNICK+' '+BOTNICK+' '+BOTNICK+" :hi.\r\n").encode())
sock.send(('NICK '+BOTNICK + "\r\n").encode())
sock.send(('JOIN '+CHANNEL + "\r\n").encode())

def main():
	while True:
		received = sock.recv(2048).decode('latin1')
		received = received[:len(received)-len('\r\n')]
		print(received)
		
#Greetings.		
		
		if received.find(COMMAND_SIGN+'welcome') != -1:
			try:
				Send(CHANNEL,'@'+received.split(COMMAND_SIGN+'welcome ',1)[1]+' Welcome to ORE! The place of Shenanigans!')
				Send(CHANNEL,'@'+received.split(COMMAND_SIGN+'welcome ',1)[1]+' For futher information, visit http://www.openredstone.org.')
				import time
				time.sleep(5)
			except:
				continue
				
#Applications.				
				
		if received.find(COMMAND_SIGN+'apply') != -1:
			try:
				Send(CHANNEL,'@'+received.split(COMMAND_SIGN+'apply ',1)[1]+' In order to build, you have to apply first!')
				Send(CHANNEL,'@'+received.split(COMMAND_SIGN+'apply ',1)[1]+' To apply, visit http://www.openredstone.org/apply for information.')
				import time
				time.sleep(5)
			except:
				continue				
		if received.find(COMMAND_SIGN+'school') != -1:
			try:
				Send(CHANNEL,'@'+received.split(COMMAND_SIGN+'school ',1)[1]+' You seem interested in the school server!')	
				Send(CHANNEL,'@'+received.split(COMMAND_SIGN+'school ',1)[1]+' You should visit http://forum.openredstone.org/forumdisplay.php?fid=36')
				import time
				time.sleep(5)
			except:
				continue
		if received.find(COMMAND_SIGN+'help') != -1:
			try:
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' Help page for Nickster_Bot:')
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' To greet a new player, type "@welcome [player name]"')
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' To give a player info on the school server, type "@school [player name]"')
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' To give information on applying to build/school, type "@apply [player name]"')
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' To view some community made tutorials, type "@tutorials"')
				import time
				time.sleep(5)
			except:
				continue	
				
#Tutorials.	

		if received.find(COMMAND_SIGN+'tutorials') != -1:
			try:
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' This is the tutorials page for Nickster_Bot!')
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' There are multiple tutorials, so type @list for a list of them!')
				import time
				time.sleep(5)
			except:
				continue
		if received.find(COMMAND_SIGN+'list') != -1:
			try:
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' Type "@binary" for a list of tutorials for binary.')
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' Type "@gates" for a list of tutorials for logic gates.')
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' Type "@ALUs" for a list of tutorials on adders, subtractors, and ALUs.')
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' Type "@advanced" for a list of advanced tutorials.')
				import time
				time.sleep(5)
			except:
				continue	
		if received.find(COMMAND_SIGN+'binary') != -1:
			try:
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' This page is still under constructions!')
				import time
				time.sleep(5)
			except:
				continue
		if received.find(COMMAND_SIGN+'gates') != -1:
			try:
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' This page is still under constructions!')
				import time
				time.sleep(5)
			except:
				continue
		if received.find(COMMAND_SIGN+'ALUs') != -1:
			try:
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' This page is still under constructions!')
				import time
				time.sleep(5)
			except:
				continue
		if received.find(COMMAND_SIGN+'advanced') != -1:
			try:
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' This page is still under constructions!')
				import time
				time.sleep(5)
			except:
				continue

#Shenanigans.
				
		if received.find(COMMAND_SIGN+'test') != -1:
			try:
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' Yes, I am working. You idiot...')
				import time
				time.sleep(5)
			except:
				continue				
		if received.find(COMMAND_SIGN+'snakes') != -1:
			try:
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' I am not afraid of ghosts.')
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' I am not afraid of sharks.')
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' I am not afraid of cancer.')
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' I am just afraid of snakes!')
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' They really creep me out!')
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' Where are their arms and legs?!')
				Send(CHANNEL,'@'+received.split(CHANNEL,1)[1].split(' ')[1].replace(':','')+' It is not okay!')
				import time
				time.sleep(5)
			except:
				continue	
		
#For connection purposes.
				
		if received.find('PING') != -1:
			try:
				sock.send(('PONG '+received.split(': ')[-1]+'\r\n').encode())
				continue
			except:
				import smtplib
				from email.mime.text import MIMEText

				s = smtplib.SMTP('smtp.uk.xensource.com')
				s.set_debuglevel(1)
				msg = MIMEText("""body""")
				sender = 'nickster258@gmail.com'
				recipients = ['nickster258@gmail.com', 'john.smith@example.co.uk']
				msg['Build is offline!'] = "Offline"
				msg['From'] = sender
				msg['To'] = ", ".join(recipients)
				s.sendmail(sender, recipients, msg.as_string())
				print('loopdy loop finished')
	
if __name__ == "__main__":
	main()
