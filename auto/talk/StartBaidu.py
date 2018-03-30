#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyquery import PyQuery as pq
import time
import sys
sys.path.append("../../")
import util.TulingReboot as tuling
from util.StringUtil import *
from util.IpUtil import *
from auto.talk.BaiduSayHello import *

# IpUtils.saveIp()
while 1:
    ip = str(IpUtils.getIp())
    if ip == '-1':
        print 'ip不够了.....'
        IpUtils.saveIp()
    elif ip:
        print 'ip：' + ip + ' 打开'
        try:
            say = BaiduSayHello()
            say.hello(ip)
        except Exception, e:
            print e
            continue
