#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__="cdiaz"
__date__ ="$18-oct-2013 11:53:07$"



from comunicacion import botirc

HOST="irc.freenode.net"
PORT=6667
NICK="MakerBot"
IDENT="MakerBot"
REALNAME="MakerBot"
CHANNEL="#stgomakerspace"


bot = botirc.BotIrc(HOST,PORT,NICK,IDENT,REALNAME,CHANNEL)
bot.conectar()