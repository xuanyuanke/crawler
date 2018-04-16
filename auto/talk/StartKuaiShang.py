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
sys.path.append("../")
from util.IpUtil import *
from KuaiShangSayHello import *
from util.RedisUtil import *

# IpUtils.saveIp()
while 1:
    if r.get("CRAWLER_OC_3_2")!='1' :
        log = LogByDb()
        logtype ='104'
        logstr = '快商（abcbabyvip.com）自动聊天已停止...'
        print logstr
        log.write(logstr,'',logtype)
        time.sleep(30)
        continue
    ip = str(IpUtils.getIp())
    if ip == '-1':
        print 'ip不够了.....'
        IpUtils.saveIp()
    elif ip and ip != 'None':
        print 'ip：' + ip + ' 打开'
        try:
            say = KuaiShangSayHello()
            say.hello(ip)
        except Exception, e:
            print e
            continue
