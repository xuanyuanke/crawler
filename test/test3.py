#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

ip='http://101.205.70.128:9797'
word=u"天美极使 京北"
name="www.angel-usa.com"
# profile_dir='/home/xuanyuanke/Documents/geckodriver'
# profile = webdriver.FirefoxProfile(profile_dir)
driver = webdriver.Firefox()
driver.delete_all_cookies()

try:
	driver.get("https://www.baidu.com")
	driver.implicitly_wait(10) # 隐性等待，最长等30秒 
	driver.set_page_load_timeout(15)
	cookie= driver.get_cookies()
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