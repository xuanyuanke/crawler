#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
from GetIp import *
from ToBaidu import *

#IpUtils.saveIp()
while 1:
	ip=str(IpUtils.getIp())	
	if ip=='-1':		
		print 'ip不够了.....'
		IpUtils.saveIp()
		#break
	else:
		print 'ip：'+ip+' 打开'		
		try:
			word=u"天美极使 京北"
			name="www.angel-usa.com"	
			baidu = ToBaidu()
			baidu.specifiedOpen(ip,word,name)
			# time.sleep(10)
		except Exception,e:
				print e		
				continue