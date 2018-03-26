#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')
class openbaiduMobile:
	"""docstring for ClassName"""
	def getdriver(self,ip):
		chrome_options = Options()
		# chrome_options.add_argument('window-size=1920x3000') #指定浏览器分辨率
		# chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
		# chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
		# chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
		# proxy="--proxy-server=http://" + ip
		# addargument['--headless',proxy]
		chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
		chrome_options.add_argument("--proxy-server=http://" + ip) 
		self.driver = webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options)
		return self.driver
		#(executable_path='/usr/local/bin/chromedriver')
		
	def openword(self,unword):
			try:
				driver = self.driver
				driver.get("https://www.baidu.com")
				# driver.set_page_load_timeout(5)
				driver.implicitly_wait(10) # 隐性等待，最长等30秒 
				driver.set_page_load_timeout(15)
				driver.find_element_by_id("kw").send_keys(unword)
				driver.find_element_by_id("su").click()
				
				time.sleep(5)
				# return driver
				link=[]
				index = [1,2,3,4]
				try:
					for i in range(0, len(index)):
						print index[i]
						xpath = "//div[@id='content_left']/div["+str(index[i])+"]/h3/a"
						print xpath
						try:
							link_d=self.driver.find_element_by_xpath(xpath).get_attribute('href')
						except Exception as e:
							print e
							print '尝试第二种方式'
							xpath = "//div[@id='content_left']/div["+str(index[i])+"]/div/h3/a"
							try:
								link_d=driver.find_element_by_xpath(xpath).get_attribute('href')
							except Exception as e:
						link.append(link_d)
				except Exception as e:
					print e
					print '未检索到推广数据'
					
					# driver.quit()
				if len(link) == 0:
					print "元素未找到"
				for url in link:
					print("url:"+url)
					js='window.open("'+url+'");'
					print js
					driver.execute_script(js)
					time.sleep(3)
				return driver
			except Exception as e:
				print e
			finally:
				driver.quit()
			

	def specifiedOpen(self,ip,word,name):
			driver = self.driver
			try:
				handles = driver.window_handles
				driver.switch_to_window(handles[0])
				driver.implicitly_wait(10) # 隐性等待，最长等30秒 
				driver.set_page_load_timeout(15)
				driver.find_element_by_id("kw").clear()
				driver.find_element_by_id("kw").send_keys(word)
				driver.find_element_by_id("su").click()
				# time.sleep(5)
				try:
					url = driver.find_element_by_partial_link_text(str(name)).get_attribute('href')
					print url
					driver.find_element_by_partial_link_text(str(name)).click()
					print '==========OK========='
				except Exception as e:
					print e
					print '未检索到推广数据'
					driver.quit()
				# time.sleep(5)
				driver.delete_all_cookies()
				# print "页面已打开，准备关闭"
				driver.quit()
			except Exception as e:
				print e
				print '异常退出'
				driver.quit()
			finally:
				print '退出'
				driver.delete_all_cookies()
				driver.quit()	

	def __init__(self):
		# print 1111
		ip="192.168.1.1"
		word=u"美国生孩子"
		name="www.angel-usa.com"	
		# baidu = ToBaidu()
		# print '1111'
		self.driver = None
		self.driver = self.getdriver(ip)
		self.driver = self.openword(word)
		# self.driver = self.openword(word,name)
		self.specifiedOpen(ip,word,name)
        # self.specifiedOpen(ip1,word1,name1)