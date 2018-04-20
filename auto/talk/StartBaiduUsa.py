#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("../../")
from util.IpUtil import *
from BaiduSayHelloUsa import *
from util.RedisUtil import *
from util.LogByDb import *


while 1:
    if r.get("CRAWLER_OC_9")!='1' :
        log = LogByDb()
        logtype ='109'
        logstr = '百度（angel-usa）自动聊天已停止...'
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
            say = BaiduSayHelloUsa()
            say.hello(ip)
        except Exception, e:
            print e
            continue
