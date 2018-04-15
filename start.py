#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys

import time
from util.IpUtil import *
from baidu.baidu import *
# from openbaidu import *
import random 
from util.RedisUtil import *
# IpUtils.saveIp()

# words = IpUtils.getWord("baidu/word.txt")
# unwords = IpUtils.getWord("baidu/unword.txt")
reload(sys)
sys.setdefaultencoding('utf-8')
while 1:
	if r.get("CRAWLER_OC_1")!='open' :
		print "PC 已停止"
		time.sleep(30);
		continue

	ip=str(IpUtils.getIp())	 
	if ip=='-1':		
		print 'ip不够了.....'
		time.sleep(2)
		try:
			IpUtils.saveIp()
		except Exception as e:
			continue
		#break
	else:
		print 'ip：'+ip+' 打开'		
		try:
			words=r.get("CRAWLER_WORD_TYPE_0_1").split("\n")
			unwords=r.get("CRAWLER_WORD_TYPE_1_1").split("\n")
			names = r.get("CRAWLER_WEB_ID_1").split(",")

			word=random.choice(words)
			print word
			name=random.choice(names)
			# "www.angel-usa.com"
			unword = random.choice(unwords)
			print ("ip :%s , name: %s , word :%s , unword :%s"  % (ip,name,word,unword))
			baidu = openbaidu(ip,name,word,unword)
			# baidu.specifiedOpen(ip,word,name)
			# time.sleep(100000000)
		except Exception,e:
				print e		
				continue

# word=u"天美极使 京北"
# name="www.angel-usa.com"	
# ip=''
# # baidu = openbaidu()
# baidu = ToBaidu(ip,name,word)

# baidu.specifiedOpen(ip,word,name)