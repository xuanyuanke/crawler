#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2
import re
import time
import urllib
import socket
import requests
import telnetlib
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import random

reload(sys)
sys.setdefaultencoding('utf8')
socket.setdefaulttimeout(3)


class IpUtils:
    global headers
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Hosts': 'hm.baidu.com',
        'Referer': 'http://www.xicidaili.com/nn',
        'Connection': 'keep-alive'
    }
    # 指定爬取范围（这里是第1~1000页）
    global currentIndex
    currentIndex = 0

    global getIpUrl, filePath
    # 代理ip获取的URL
    getIpUrl = "http://tvp.daxiangdaili.com/ip/?tid=555447088680131&num=50&delay=3&sortby=time&foreign=none"
    # 文件的保存路径
    project_dir = os.path.dirname(os.path.abspath(""))
    filePath = "/tmp/ip.txt"

    @staticmethod
    def saveIp():
        try:
            print '开始重新拉取ip....'
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
            #driver = webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options)
            driver = webdriver.Chrome(chrome_options=chrome_options)
            #(executable_path='/usr/local/bin/chromedriver')
            driver.get(getIpUrl)
            driver.set_page_load_timeout(5)
            link = driver.find_element_by_tag_name("pre").text
            print link
            f = open(filePath, "w")
            f.write(link)
            # f.write("\n")
            driver.quit()
            time.sleep(1)
            print 'ip已保存完毕:'

        except Exception as e:
            print e
            print '错误'

    @staticmethod
    def getIp():

        try:
            inf = open(filePath)    # 这里打开刚才存ip的文件
            lines = inf.readlines()
        except Exception, e:
            print '读取ip文件错误，重新下载代理ip...'
            IpUtils.saveIp()
            IpUtils.getIp()
            return
        proxys = []
        for i in range(0, len(lines)):
            proxy_host = "http://" + \
                lines[i].replace('\n', '').replace(' ', '')
            proxy_temp = {"http": proxy_host}
            proxys.append(proxy_temp)

        # 用这个网页去验证，遇到不可用ip会抛异常
        #url = "http://httpbin.org/ip"
        url = "http://www.sohu.com"
        user_agent = IpUtils.get_user_agent()
        headers = {
            'User-Agent': user_agent
        }
        # 将可用ip写入valid_ip.txt
        #ouf = open("valid_ip.txt", "a+")
        # for proxy in proxys:
        global currentIndex
        i = currentIndex
        global proxyStr
        proxyStr = ''

        if i >= (len(proxys) - 1):
            print '所有ip已校验完毕。。再次拉取ip'
            currentIndex = 0
            # IpUtils.saveIp()
            # currentIndex=0
            # IpUtils.getIp()
            proxyStr = '-1'
            return proxyStr

        try:
            print 'currentIndex===' + str(currentIndex) + ',i====' + str(i)
            currentIndex += 1
            #res = urllib.urlopen(url,proxies=proxys[i]).read()
            # print '=='+proxys[i]['http']
            # return
            print '开始验证' + proxys[i]['http']
            res = requests.get(url, proxies=proxys[i],headers=headers, timeout=5)
            if res.status_code == 200:
                print '验证成功' 
                proxyStr = proxys[i]['http']
            else:
                IpUtils.getIp()
            
        # ouf.write(valid_ip)
        except Exception, e:
            print '验证失败：' + proxys[i]['http']
            # print e
            IpUtils.getIp()
        else:
            print '返回 代理Ip===' + proxyStr
            return proxyStr
        # finally:

        return proxyStr

    @staticmethod
    def get_user_agent():
        '''
        功能: 随机获取UA
        :return: 返回一个随机UA
        '''
        user_agents=[
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"
        ]
        user_agent = random.choice(user_agents)
        return user_agent

    @staticmethod
    def getWord(wordfile):
        inf = open(wordfile)

        lines = [line.decode('utf-8') for line in inf.readlines()]
        return lines
