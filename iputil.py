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
	    'Referer': 'http://www.xicidaili.com/wt',
	    'Connection': 'keep-alive'
	}
	global currentIndex	
	currentIndex=0
	# 指定爬取范围（这里是第1~1000页）
	@staticmethod
	def  saveIp():
		print '开始重新拉取ip....'
		for i in range(1,1000):
		    url = 'http://www.xicidaili.com/wt/' + str(i)
		    req = urllib2.Request(url=url,headers=headers)
		    res = urllib2.urlopen(req).read()
		    # 提取ip和端口
		    ip_list = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{2,6})", res, re.S)
		    # 将提取的ip和端口写入文件
		    f = open("ip.txt","w")
		    for li in ip_list:
		        ip = li[0] + ':' + li[1] + '\n'
		        print ip
		        f.write(ip)
		    time.sleep(2)       # 每爬取一页暂停两秒
		print 'ip已保存完毕:'

	@staticmethod
	def getIp():				
		inf = open("ip.txt")    # 这里打开刚才存ip的文件
		lines = inf.readlines()
		proxys = []
		for i in range(0,len(lines)):
		    proxy_host = "http://" + lines[i].replace('\n','').replace(' ','')		    
		    proxy_temp = {"http":proxy_host}
		    proxys.append(proxy_temp)

		# 用这个网页去验证，遇到不可用ip会抛异常
		url = "http://httpbin.org/ip"
		# 将可用ip写入valid_ip.txt
		#ouf = open("valid_ip.txt", "a+")
		#for proxy in proxys:
		global currentIndex		
		i= currentIndex
		global proxyStr
		proxyStr=''
		
		if i>=(len(proxys)-1):
			print '所有ip已校验完毕。。再次拉取ip'
			currentIndex=0
			#IpUtils.saveIp()
			#currentIndex=0
			#IpUtils.getIp()
			proxyStr='-1'	
			return 	proxyStr

		try:								
			print 'currentIndex==='+str(currentIndex)+',i===='+str(i)
			currentIndex+=1			
			#res = urllib.urlopen(url,proxies=proxys[i]).read()
			#print '=='+proxys[i]['http']
			#return 
			# print '开始验证'+proxys[i]['http']
			res=requests.get(url, proxies=proxys[i],timeout=3)
			# print '验证结果:'+res.text
			#valid_ip = proxys[i]['http'][7:]
			#print 'valid_ip: ' + valid_ip			
			proxyStr=proxys[i]['http']
		# ouf.write(valid_ip)
		except Exception,e:		
			# print '验证失败：'+proxys[i]['http']
			# try:
			# 	# print '验证https：'+proxys[i]['http'].replace('http','https')
			# 	proxy_temp = {"https":proxys[i]['http'].replace('http','https')}
			# 	proxys[i] = proxy_temp
			# 	# print '--------'+str(proxys[i])
			# 	res=requests.get(url, proxies=proxys[i],timeout=3)
			# 	# print 'https验证结果:'+res.text
			# 	#valid_ip = proxys[i]['http'][7:]
			# 	#print 'valid_ip: ' + valid_ip			
			# 	proxyStr=proxys[i]['https']
			# except Exception as e:
			# 	# print 'https验证失败：'+proxys[i]['https']
			IpUtils.getIp()
		else:
			print '返回 代理Ip==='+proxyStr
			return proxyStr
		#finally:

		return proxyStr

		# http://221.7.255.168:8080
