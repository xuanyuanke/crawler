#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import os

#IpUtils.saveIp()
while 1:
	try:
		time.sleep(60*10)
		print '准备执行'
		os.system(" sh stopchrome.sh ")
	except Exception as e:
		e
	finally:
		pass