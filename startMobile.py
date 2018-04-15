#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
from util.IpUtil import *
from baidu.mobile import *
# from openbaidu import *
import random 
 
# IpUtils.saveIp()


while 1:
	if r.get("CRAWLER_OC_2")!='open' :
		print "wap 已停止"
		time.sleep(30);
		continue
	ip=str(IpUtils.getIp())	
	if ip=='-1':		
		print 'ip不够了.....'

		try:
			IpUtils.saveIp()
		except Exception as e:
			continue
		#break
	else:
		print 'ip：'+ip+' 打开'		
		try:
			# word=u"天美极使 京北"
			words=r.get("CRAWLER_WORD_TYPE_0_2").split("\n")
			unwords=r.get("CRAWLER_WORD_TYPE_1_2").split("\n")
			names = r.get("CRAWLER_WEB_ID_2").split(",")

			word=random.choice(words)
			# word = words[wordindex]
			print word
			name=random.choice(names)
			unword = random.choice(unwords)
			# unword = unwords[wordindex]	
			print ("ip :%s , name: %s , word :%s , unword :%s"  % (ip,name,word,unword))
			baidu = ToBaiduMobile(ip,name,word,unword)
			# baidu.specifiedOpen(ip,word,name)
			# time.sleep(100000000)
		except Exception,e:
				print e		
				continue
# word=u"天美极使 京北"
# name="wap.angel-usa.com"	
# # baidu = openbaidu()
# ip =''
# baidu = ToBaiduMobile(ip,name,word)

# baidu.specifiedOpen(ip,word,name)