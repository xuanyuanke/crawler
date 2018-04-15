#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time


chrome_options = Options()


chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
driver = webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options)
driver.get("https://www.baidu.com")
time.sleep(2)
driver.find_element_by_id("index-kw").send_keys(unword)
time.sleep(2)
driver.find_element_by_id("index-bn").click()
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(12)
driver.set_page_load_timeout(20)
print driver.page_source
driver.quit()
