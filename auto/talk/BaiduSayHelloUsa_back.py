#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from pyquery import PyQuery as pq
import time
import sys
sys.path.append("../../")
import util.DbReboot as Reboot
from util.RedisUtil import *
reload(sys)
sys.setdefaultencoding('utf8')

from util.LogByDb import *

global windowCount
windowCount = 0

class BaiduSayHelloUsa:
    def hello(sa, ip):
        global windowCount
        log = LogByDb()
        logtype ='109'
        # while 1:
        windowCount += 1
        logstr = '打开窗口:' + str(windowCount)
        print logstr
        log.write(logstr,ip,logtype)
        chromeOptions = webdriver.ChromeOptions()
        # 设置代理
        # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
        proxyStr = "--proxy-server=" + ip
        print ('baidu prox =', proxyStr)
        chromeOptions.add_argument(proxyStr)

        prefs = {
            'profile.default_content_setting_values': {
                'images': 2
            }
        }
        chromeOptions.add_experimental_option('prefs', prefs)
        chromeOptions.add_argument('--disable-extensions')
        chromeOptions.add_argument('--disable-gpu')
        chromeOptions.add_argument('--no-sandbox')
        chromeOptions.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chromeOptions)

        driver.implicitly_wait(50)
        driver.set_script_timeout(50)
        driver.set_page_load_timeout(50)

        try:

            driver.get(
                "http://www.angel-usa.com/")
        except Exception, e:
            logstr='会话关闭，窗口关闭'+str(e)
            print logstr, e
            log.write(logstr,ip,logtype)
            print ''
            try:
                driver.quit()
                return
            except Exception, e:
                print '关闭窗口错误...', e
            return
        print '窗口已打开'
        send = driver.find_element_by_class_name('nb-icon-inner-wrap')
        send.click()
        # 获取打开的多个窗口句柄
        windows = driver.window_handles
        # 切换到当前最新打开的窗口
        driver.switch_to.window(windows[-1])

        i = 0
        sessionTime = 0
        lastMsg = ''
        while 1:
            i = 1
            print '当前会话时间：(' + str(sessionTime) + ')'
            sessionTime += i
            time.sleep(i)
            try:
                d = pq(driver.page_source)
                time.sleep(i)
            except Exception, e:
                print e
                continue
            lastContent = d('.msg-sub:last .content').text();
            if lastMsg != lastContent or (sessionTime > 5 and sessionTime % 2 == 0):
                lastMsg = lastContent
                logstr ='客服说：' + lastContent
                print logstr
                log.write(logstr,ip,logtype)
                reboot = Reboot.DbReboot()
                tulingSayMsg = reboot.robootSay(lastContent, ip)
                addWeixin = False
                if int(r.get(ip)) >= 4:
                    addWeixin = True
                driver.execute_script(
                    "document.getElementById('editor').innerHTML='" + tulingSayMsg + "'")
                send = driver.find_element_by_id('send-wrap')
                send.click()
                logstr ='回复：'+tulingSayMsg
                print logstr
                log.write(logstr,ip,logtype)
                if addWeixin:
                    time.sleep(i)
                    logstr ='聊天完成，关闭窗口'
                    print logstr
                    log.write(logstr,ip,logtype)
                    driver.quit()
                    break
            else:
                if sessionTime > 30:
                    time.sleep(i)
                    logstr ='回话超过5分钟 关闭当前会话..'
                    print logstr
                    log.write(logstr,ip,logtype)
                    driver.quit()
                    break
                    # continue


#
# say = BaiduSayHelloUsa()
# say.hello("")