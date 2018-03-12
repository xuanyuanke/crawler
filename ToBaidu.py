#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')
class ToBaidu:
	"""docstring for ClassName"""
	def open(self,ip,word):
		chrome_options = Options()
		# chrome_options.add_argument('window-size=1920x3000') #指定浏览器分辨率
		# chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
		# chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
		# chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
		chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
		chrome_options.add_argument("--proxy-server=http://" + ip) 
		driver = webdriver.Chrome('/usr/local/bin/chromedriver')
		#(executable_path='/usr/local/bin/chromedriver')
		try:
			driver.get("https://www.baidu.com")
			driver.set_page_load_timeout(5)
			driver.find_element_by_id("kw").send_keys(word)
			driver.find_element_by_id("su").click()
			time.sleep(5)
			link=[]
			index = [1,2,3,4]
			try:
				for i in range(0, len(index)):
					print index[i]
					xpath = "//div[@id='content_left']/div["+str(index[i])+"]/h3/a"
					print xpath
					try:
						link_d=driver.find_element_by_xpath(xpath).get_attribute('href')
					except Exception as e:
						print e
						print '尝试第二种方式'
						xpath = "//div[@id='content_left']/div["+str(index[i])+"]/div/h3/a"
						link_d=driver.find_element_by_xpath(xpath).get_attribute('href')
					# link=driver.find_element_by_xpath("//div[@id='3001']/div/h3/a").get_attribute('href')
					# 
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
			driver.quit()
		except Exception as e:
			print e
		finally:
			driver.quit()
