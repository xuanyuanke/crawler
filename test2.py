#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
#(executable_path='/usr/local/bin/chromedriver')
driver.get("https://www.baidu.com")
driver.set_page_load_timeout(5)
#print(driver)
#driver.quit()
driver.find_element_by_id("kw").send_keys(u"美国生孩子")
driver.find_element_by_id("su").click()
#driver.switch_to_window(driver.window_handles[-1])
# driver.set_page_load_timeout(5)
# print (driver.find_element_by_id("3001").text)
time.sleep(5)
link=driver.find_element_by_xpath("//div[@id='3001']/div/h3/a").get_attribute('href')
print("link:"+link)
js='window.open("'+link+'");'
driver.execute_script(js)
driver.quit()

# for link in  driver.find_element_by_xpath("//div[@id='3001']/div/h3/a").href
# 	print (link.get_attribute('href')) 
	#.find_element_by_xpath("//div/div/h3")
# for link in hrefs.find_elements_by_xpath("//*[@href]"):  
#     print (link.get_attribute('href'))  
#content_left 3001
# time.sleep(10)

# driver.find_element_by_id("bx-next").send_keys(u"请问这个需要多少费用")
#print(driver)
