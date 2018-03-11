#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

ip="88.12.131.1"
chrome_options = Options()
# chrome_options.add_argument('window-size=1920x3000') #指定浏览器分辨率
# chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
# chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
# chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
#chrome_options.add_argument(('--proxy-server=http://' + ip)) 

driver = webdriver.Chrome(r'/usr/local/bin/chromedriver',chrome_options = chrome_options)
driver.get("https://www.baidu.com")
driver.set_page_load_timeout(5)
try:
    driver.find_element_by_id("kw").send_keys(u"板蓝根")
    driver.find_element_by_id("su").click()

    time.sleep(4)
    link = driver.find_element_by_xpath("//div[@id='content_left']/div/h3/a").get_attribute('href')
    print(link)
    js='window.open("'+link+'");'
    driver.execute_script(js)
    
except Exception as e:
    print e