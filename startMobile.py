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

words = IpUtils.getWord("baidu/word.txt")
unwords = IpUtils.getWord("baidu/unword.txt")
while 1:
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
			word=random.choice(words)
			# word = words[wordindex]
			print word
			name="wap.angel-usa.com"
			unword = random.choice(unwords)
			# unword = unwords[wordindex]	
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