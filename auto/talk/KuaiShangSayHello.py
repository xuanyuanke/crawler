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
import util.StringUtil as StringUtil
reload(sys)
sys.setdefaultencoding('utf8')
import util.DbReboot as Reboot
from util.RedisUtil import *
from util.LogByDb import *

global windowCount
windowCount = 0

class KuaiShangSayHello:
    def hello(sa, ip):
        global windowCount
        windowCount += 1
        log = LogByDb()
        logtype ='102'
        logstr = '打开窗口:' + str(windowCount)
        print logstr
        log.write(logstr,ip,logtype)

        chromeOptions = webdriver.ChromeOptions()
        # 设置代理
        # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
        proxyStr = "--proxy-server=" + ip
        print ('baidu prox =', proxyStr)
        prefs = {
            'profile.default_content_setting_values': {
                'images': 2
            }
        }
        chromeOptions.add_experimental_option('prefs', prefs)
        chromeOptions.add_argument(proxyStr)

        driver = webdriver.Chrome(chrome_options=chromeOptions)

        # driver.Manage().Timeouts().ImplicitlyWait(TimeSpan.FromSeconds(10))
        # driver.set_timeout(30)
        # driver.implicitly_wait(30)
        # driver.set_page_load_timeout(30)
        # driver.set_script_timeout(30)

        url = "http://kf9.kuaishang.cn/bs/im.htm?cas=55798___737336&fi=64318&dp=http://www.abcbabyvip.com/"

        try:
            driver.get(url)
        except Exception, e:
            print '加载会话。关闭窗口'
            print e
            try:
                print '等待会话.ex.10'
                # driver.quit()
            except Exception, e:
                print e
            # return
            time.sleep(10)
        print '窗口已打开'
        # 获取打开的多个窗口句柄
        #windows = driver.window_handles
        # 切换到当前最新打开的窗口
        # driver.switch_to.window(windows[-1])
        i = 0
        sessionTime = 0
        lastMsg = ''
        errorCount = 0
        while 1:
            errorCount += 1
            i = 5
            print '当前会话时间：(' + str(sessionTime) + ')'
            sessionTime += i
            time.sleep(i)
            try:
                d = pq(driver.page_source)
                time.sleep(i)
            except Exception, e:
                if errorCount > 3:
                    driver.quit()
                    return
                print e
                continue
            lastContent = d('.msg_cs:last .msg').text();
            if lastMsg != lastContent  or (sessionTime > 30 and sessionTime % 10 == 0):
                lastMsg = lastContent
                logstr = '客服说：' + lastContent
                print logstr
                log.write(logstr,ip,logtype)
                reboot = Reboot.DbReboot()
                tulingSayMsg = reboot.robootSay(lastContent, ip)
                addWeixin = False
                if int(r.get(ip)) > 4:
                    addWeixin = True
                try:
                    driver.execute_script(
                        "document.getElementById('ksEditInstance').innerHTML='" + tulingSayMsg + "'")
                    send = driver.find_element_by_id('ksDirSendBtn')
                    send.click()
                except Exception, e:
                    logstr ='客户关闭会话，关闭窗口..'
                    print logstr
                    log.write(logstr,ip,logtype)
                    return
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
                if sessionTime > 100:
                    print '回话超过3分钟 , 发送手机号 关闭当前会话..'
                    tulingSayMsg = '我手机,同微信 ：' + StringUtil.MyUtil.createPhone()
                    driver.execute_script(
                        "document.getElementById('ksEditInstance').innerHTML='" + tulingSayMsg + "'")
                    send = driver.find_element_by_id('ksDirSendBtn')
                    send.click()
                    driver.quit()
                    time.sleep(i)
                    logstr ='回话超过5分钟 关闭当前会话..'
                    print logstr
                    log.write(logstr,ip,logtype)
                    break
                    # continue
