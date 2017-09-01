#!/usr/bin/python3
# -*- coding: utf-8 -*-
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telepot.delegate import (per_chat_id_in, per_application, call, create_open, pave_event_space)
import telepot
import time
from array import array
import feedparser
import pprint
import unidecode
import os
import commands
import urllib2
import sys
import datetime
import random
import urllib2
import string

TOKEN = '414669467:AAGlyVBS6FwndpVvjb-JK9IVcVxAuFj4rmk'
OWNER_ID = 'inewton'
rss = 'http://www.nature.com/nnano/current_issue/rss/index.html'

def handle(msg):
	msg_str = str(msg)

	global bot
	content_type, chat_type, chat_id = telepot.glance(msg)
	
	#print msg
	#msg_str = str(msg)
	
	content_type, chat_type, chat_id = telepot.glance(msg)
	m = telepot.namedtuple.Message(**msg)

	def getinfo(chat_id):
		if chat_id < 0:
			print 'Mensagem do tipo %s' % (content_type,)
			print '-------------------------------------'
			print 'Chat ID : %s' % m.chat[0]
			print 'Tipo de chat : %s' % m.chat[1]
			print 'Nome do Grupo: %s' % m.chat[2]
			print 'Username : %s' % m.from_[3]
			print 'First Name: %s' % m.chat[4]
			print 'Last Name: %s' % m.chat[5]
			print 'Enviada por %s' % (m.from_,)
			print time.strftime('%Y-%m-%d %H:%M:%S')
			print '--------------------------------------'
		else:
			print 'Messagem do tipo %s ' % (content_type,)
			print '--------------------------------------'
			print 'Chat ID : %s' % m.chat[0]
			print 'Tipo de chat : %s' % m.chat[1]
			print 'Username : %s' % m.chat[3]
			print 'First Name: %s' % m.chat[4]
			print 'Last Name: %s' % m.chat[5]
			print time.strftime('%Y-%m-%d %H:%M:%S')
			print '--------------------------------------'
	
	getinfo(chat_id)
	print m.from_[0]
	print m.from_[1]
	print m.from_[2]
	print m.from_[3]

	getinfo(chat_id)
	print msg_str

	feed = feedparser.parse(rss)
	bot.sendMessage(chat_id, str('*'+ feed['entries'][0]['title'] + '*' + '\n\n_' + feed['entries'][0]['summary'] + '_\n\nLINK: '+ feed['entries'][0]['link']), parse_mode='Markdown')
	#bot.sendMessage(chat_id, '*bold text*\n_italic text_\n[link](http://www.google.com)', parse_mode='Markdown')

bot = telepot.Bot(TOKEN)
bot.setWebhook()
bot.message_loop(handle)

while 1:
    time.sleep(5)
