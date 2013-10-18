#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__="cdiaz"
__date__ ="$18-oct-2013 14:01:26$"


import socket
import string
from time import sleep


class BotIrc():
    
    def __init__(self,host,port,nick,ident,realName,channel):
        self.host=host
        self.port=port
        self.nick=nick
        self.ident=ident
        self.realName=realName
        self.channel=channel
        self.readbuffer = ""
        self.ircSocket=socket.socket( )
        self.away = []
        self.woman = False
        
    def conectar(self):
        self.ircSocket.connect((self.host, self.port))
        self.ircSocket.send("NICK %s\r\n" % self.nick)
        self.ircSocket.send("USER %s %s bla :%s\r\n" % (self.ident, self.host, self.realName))
        self.ircSocket.send("JOIN :%s\r\n" % self.channel)
        self.ircSocket.send("PRIVMSG %s :%s\r\n" % (self.channel, "Hola a todos en stgmakerspace!"))
        self.ircSocket.send("PRIVMSG %s :%s\r\n" % (self.channel, "Soy un botIrc"))
        self.interaccion()
        
    
    def send_msg(self,msg):
	self.ircSocket.send("PRIVMSG %s :%s" % (self.channel, msg))
        
        
    def interaccion(self):
	while 1:
            self.readbuffer=self.readbuffer+self.ircSocket.recv(1024)
            temp=string.split(self.readbuffer, "\n")
            self.readbuffer=temp.pop( )
            for line in temp:
                    print line
                    line=string.rstrip(line)
                    line=line.split(self.channel + ' :')
                    username = line[0].split('!')[0].split(':')[1]
                    
                    if line[0].find("PING") != -1:
			pingid = line[0].split()[1]
			self.ircSocket.send("PONG %s\r\n" % pingid)
                        
                    elif line[0].find('JOIN') != -1:
			if username != self.nick and username.find(self.host) == -1:
				sleep(5)
				self.send_msg("Bienvenid@ %s ^^\n" % username)
                                
                    if len(line) > 1:
                        
			if  line[1] == 'quien eres makerbot':
				self.send_msg("Hola, soy MakerBot 1.0.0 beta (desarrollado en python 2.7.5), saludos \n")

			if  line[1] == '$version':
				self.send_msg("MakerBot 1.0.0 beta\n")

			if line[1] == '$ mevoy' :
				print username
				if not username in self.away:
					self.send_msg("%s se marcha durante un tiempo. No molestar\n" % username)
					self.away.append(username)

				print self.away
                                
                        if line[1] == '$ volvi' :
				if username in self.away:
					self.send_msg("%s ha vuelto\n" % username)
					self.away.remove(username)

			for l in line[1].split():
				if l in self.away != -1 and username != 'MakerBot':
					self.send_msg("no molestar a %s \n" % l)

			if  line[1] == 'Hola MakerBot' or line[1] == 'hola makerbot':
				self.send_msg("Saludos a ti también %s\n" % username)