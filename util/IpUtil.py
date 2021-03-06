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
    getIpUrl = "http://tvp.daxiangdaili.com/ip/?tid=555447088680131&num=10&delay=1&filter=on"
    #getIpUrl="http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=b7b6e615d8f348a29fe4afd38ad17642&count=5&expiryDate=5&format=2"

    # 文件的保存路径
    project_dir = os.path.dirname(os.path.abspath(""))
    filePath = "/tmp/ip.txt"

    @staticmethod
    def saveIp():
        try:
            print '开始重新拉取ip....'
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--headless')
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
        url = "http://httpbin.org/ip"
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
            res = requests.get(url, proxies=proxys[i], timeout=3)
            print '验证结果:' + res.text
            #valid_ip = proxys[i]['http'][7:]
            # print 'valid_ip: ' + valid_ip
            proxyStr = proxys[i]['http']
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
    def getWord(wordfile):
        inf = open(wordfile)

        lines = [line.decode('utf-8') for line in inf.readlines()]
        return lines

IpUtils.saveIp()