#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
sys.path.append("../../")
from util.StringUtil import *
from util.IpUtil import *
reload(sys)
sys.setdefaultencoding('utf8')
from util.RedisUtil import *
from util.LogByDb import *


class AbcbabyvipSubmit:
    global windowCount
    windowCount = 0
    def submit(sa, ip):
        global windowCount
        windowCount += 1
        log = LogByDb()
        logtype ='105'
        chromeOptions = webdriver.ChromeOptions()
        logstr='打开窗口:' + str(windowCount)
        print logstr
        log.write(logstr,ip,logtype)
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
        driver = webdriver.Chrome(chrome_options=chromeOptions)
        # driver.implicitly_wait(50)
        # driver.set_script_timeout(50)
        driver.set_page_load_timeout(3)
        try:
            driver.get("http://www.abcbabyvip.com/qzform/feedback5.asp")
        except Exception, e:
            print 'Exception is #1#:', str(e)
            time.sleep(10)
            try:
                driver.get("http://www.abcbabyvip.com/qzform/feedback5.asp")
            except Exception, e:
                print 'Exception is #1.1#:', str(e)
                logstr='关闭窗口:'
                print logstr
                log.write(logstr,ip,logtype)
                driver.quit()
                return
        print '窗口已打开'

        time.sleep(3)
        phone = MyUtil.createPhone()

        driver.execute_script(
            "document.getElementById('country').value='" + phone + "'")
        send = driver.find_element_by_name('B1')
        time.sleep(3)
        try:
            send.click()
        except Exception, e:
            print 'Exception  #2#', str(e)
            driver.quit()
        logstr='提交手机：'+ phone +',关闭窗口'
        print logstr
        log.write(logstr,ip,logtype)
        time.sleep(10)
        driver.quit()

while 1:
    if r.get("CRAWLER_OC_4_2")!='1' :
        log = LogByDb()
        logtype ='105'
        logstr = '（abcbabyvip.com）自动回拨已停止...'
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
            meibaosub = AbcbabyvipSubmit()
            meibaosub.submit(ip)
        except Exception, e:
            print 'Exception  #2#', str(e)
            continue


