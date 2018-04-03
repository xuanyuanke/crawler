#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')
class ToBaiduMobile:
	"""docstring for ClassName"""
	def open(self,ip,word,hrefname,unword):
		chrome_options =webdriver.ChromeOptions()
		UA = 'iPad / Safari 10.3 [Mobile]: Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.3 (KHTML, like Gecko) Version/10.0 Mobile/14G5037b Safari/602.1'
		#UA ='Android Tablet / Chrome 57 [Mobile]: Mozilla/5.0 (Linux; Android 4.4.4; Lenovo TAB 2 A10-70L Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Safari/537.36'
		mobileEmulation = {"userAgent": UA}

		# mobileEmulation = {"deviceName":"Google Nexus 5"}  
		# chrome_options.add_experimental_option('mobileEmulation', mobileEmulation)
		# chrome_options.add_argument('window-size=1920x3000') #指定浏览器分辨率
		# chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
		# chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
		# chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
		# proxy="--proxy-server=http://" + ip
		# addargument['--headless',proxy]
		chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
		chrome_options.add_argument("--proxy-server="+ip) 
		driver = webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options)
		
		driver.set_page_load_timeout(20)
		driver.set_script_timeout(20)
		try:
			driver.get("https://m.baidu.com")
		except Exception as e:
			print '第一个窗口'+str(e)
		
		time.sleep(15)
		WebDriverWait(driver, 40).until(lambda x: x.driver.find_element_by_id("index-kw"))
		try:
			handles = driver.window_handles
			driver.switch_to_window(handles[0])
			driver.find_element_by_id("index-kw").send_keys(unword)
			time.sleep(2)
			driver.find_element_by_id("index-bn").click()
			# time.sleep(5)
			
		except Exception as e:
			print '打开百度窗口异常'
			print e
			driver.quit()
		try:
			link=[]
			index = [1,2]
			try:
				for i in range(0, len(index)):
					print index[i]
					xpath = "//div[@id='results']/div["+str(index[i])+"]/div/div/div/div/a"
					print xpath
					try:
						link_d=driver.find_element_by_xpath(xpath).get_attribute('href')
						print link_d
						link.append(link_d)
					except Exception as e:
						print e
						print '检索失败'
					# link=driver.find_element_by_xpath("//div[@id='3001']/div/h3/a").get_attribute('href')
					# 
			except Exception as e:
				print e
				print '未检索到推广数据'
				
				# driver.quit()
			if len(link) > 0:
				for url in link:
					print("url:"+url)
					js='window.open("'+url+'");'
					# print js
					driver.execute_script(js)
					time.sleep(2)
			else:
				print "元素未找到"
			# 切回到初始页面
			handles = driver.window_handles
			driver.switch_to_window(handles[0])
			# 等待
			time.sleep(1)
			try:
				xpath = "//span[text()='"+hrefname+"']/.."
				# locator = (By.LINK_TEXT, hrefname)
				# have = EC.text_to_be_present_in_element(hrefname,driver)
				# print have
				# url = driver.find_element_by_partial_link_text(str(hrefname)).get_attribute('href')
				print xpath
				WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath).get_attribute('href'))
				url = driver.find_element_by_xpath(xpath).get_attribute('href')

				print '获取到的url:'+str(url)
				if len(url)>0:
					js='window.open("'+url+'");'
					# print js
					driver.execute_script(js)
				print('PC执行成功ip[%s]word[%s]name[%s]unword[%s] :' % (ip,word,hrefname,unword))
			except Exception as e:
				print e
				print '未检索到推广数据'
			# driver.close()
			time.sleep(3)
			driver.delete_all_cookies()
			self.driver = driver
			return self.driver
		except Exception as e:
			print e
			driver.delete_all_cookies()
			driver.quit()
		

	def specifiedOpen(self,ip,word,name):
			driver= self.driver
			# driver.delete_all_cookies()
				#(executable_path='/usr/local/bin/chromedriver')
			print '1111'
			try:
				handles = driver.window_handles
				driver.switch_to_window(handles[0])
				# driver.execute_script(js)
				driver.implicitly_wait(10) # 隐性等待，最长等30秒 
				driver.set_page_load_timeout(15)
				# cookie= driver.get_cookies()
				driver.find_element_by_id("index-kw").clear()
				driver.find_element_by_id("index-kw").send_keys(word)
				driver.find_element_by_id("su").click()
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
				# driver.quit()
			finally:
				print '退出'
				driver.delete_all_cookies()
				# driver.quit()
		

	def __init__(self,ip,name,word,unword):
		# print 1111
		# word=u"美国生孩子"
		# word1 = u"天美极使 京北"
		# name="www.angel-usa.com"	
		# baidu = ToBaidu()
		# print '1111s

		self.driver = None

		try:
			# self.driver = self.getdriver(ip)
			self.driver = self.open(ip,word,name,unword)
			self.driver.delete_all_cookies()
			# self.specifiedOpen(ip,word,name)
		except Exception as e:
			print e
		finally:
			print ''
			self.driver.quit()
		
        # self.specifiedOpen(ip1,word1,name1)