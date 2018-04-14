#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time


chrome_options = Options()
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
driver = webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options)
driver.get("https://www.baidu.com")
driver.set_page_load_timeout(20)
print driver.page_source
driver.quit()
