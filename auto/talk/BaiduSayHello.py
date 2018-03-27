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
import util.DbReboot as Reboot
from util.StringUtil import *
reload(sys)
sys.setdefaultencoding('utf8')


class BaiduSayHello:
    def hello(sa, ip):
        windowCount = 0
        # while 1:
        windowCount += 1
        print '打开窗口:' + str(windowCount)
        chromeOptions = webdriver.ChromeOptions()
        # 设置代理
        # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
        proxyStr = "--proxy-server=" + ip
        print ('baidu prox =', proxyStr)
        chromeOptions.add_argument(proxyStr)

        driver = webdriver.Chrome(chrome_options=chromeOptions)

        try:
            driver.get(
                "http://p.qiao.baidu.com//im/index?siteid=7956642&ucid=7729658")
            print 1
        except Exception, e:
            print '加载会话错误。。关闭窗口'
            try:
                driver.quit()
            except Exception, e:
                print '关闭窗口错误...'
            return
        print '窗口已打开'
        # 获取打开的多个窗口句柄
        #windows = driver.window_handles
        # 切换到当前最新打开的窗口
        # driver.switch_to.window(windows[-1])
        i = 0
        sessionTime = 0
        lastMsg = ''
        while 1:
            i = 5
            print '当前会话时间：(' + str(sessionTime) + ')'
            sessionTime += i
            time.sleep(i)
            try:
                d = pq(driver.page_source)
                time.sleep(i)
            except Exception, e:
                print e
                continue
            lastContent = d('.msg-sub:last .title').text();
            if lastMsg != lastContent:
                lastMsg = lastContent
                print '有新的客户消息。。。'
                print '客服说：' + lastContent
                reboot = Reboot.DbReboot()
                tulingSayMsg = reboot.robootSay(lastContent)
                addWeixin = False                
                if sessionTime > 60:
                    tulingSayMsg = '您加我微信详聊吧 ：' + StringUtil.createPhone()
                    addWeixin = True
                driver.execute_script(
                    "document.getElementById('editor').innerHTML='" + tulingSayMsg + "'")
                send = driver.find_element_by_id('send-wrap')
                send.click()
                if addWeixin:
                    time.sleep(i)
                    print '客服回复及时，1分钟内关闭会话...'
                    driver.quit()
                    break
            else:
                if sessionTime > 300:
                    print '回话超过5分钟 关闭当前会话..'
                    driver.quit()
                    break
                    # continue
