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
from auto.talk.BaiduSayHelloJiiaa import *
from util.RedisUtil import *
from util.LogByDb import *


while 1:
    if r.get("CRAWLER_OC_8")!='1' :
        log = LogByDb()
        logtype ='108'
        logstr = '百度（jiiaaa.com）自动聊天已停止...'
        print logstr
        log.write(logstr,'',logtype)
        time.sleep(30)
        continue
    ip = str(IpUtils.getIp())
    if ip == '-1':
        print 'ip不够了.....'
        IpUtils.saveIp()
    elif ip:
        print 'ip：' + ip + ' 打开'
        try:
            say = BaiduSayHelloJiiaa()
            say.hello(ip)
        except Exception, e:
            print e
            continue
