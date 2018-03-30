#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyquery import PyQuery as pq
import time
import sys
import pytesseract
import requests
from PIL import Image


sys.path.append("../../")
import util.DbReboot as Reboot
from util.StringUtil import *
reload(sys)
sys.setdefaultencoding('utf8')


class MeibaoSubmit:
    global windowCount
    windowCount = 0

    def submit(sa, ip):
        # global windowCount
        # windowCount = 0
        # # while 1:
        # windowCount += 1
        # print '打开窗口:' + str(windowCount)
        # chromeOptions = webdriver.ChromeOptions()
        # # 设置代理
        # # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
        # # proxyStr = "--proxy-server=" + ip
        # # print ('baidu prox =', proxyStr)
        # # chromeOptions.add_argument(proxyStr)
        # driver = webdriver.Chrome(chrome_options=chromeOptions)
        # driver.implicitly_wait(30)
        # try:
        #     driver.get("http://www.jiiaaa.com/")
        # except Exception, e:
        #     print '加载会话错误。。关闭窗口'
        #     try:
        #         driver.quit()
        #     except Exception, e:
        #         print '关闭窗口错误...'
        #     return
        # print '窗口已打开'

        # time.sleep(3)
        # phone = MyUtil.createPhone()
        # print '发送手机号：' + phone
        # driver.execute_script(
        #     "document.getElementById('callbF_text').value='" + phone + "'")

        # send = driver.find_element_by_id('callbF_sub')
        # send.click()
        # driver.get_screenshot_as_file('homepage.png')
        # 打开刚刚保存的图片
        img = Image.open('homepage.png')
        # 设置要裁剪的区域（验证码所在的区域）
        box = (1280, 500, 1500, 600)
        # 截图，生成只有验证码的图片
        region = img.crop(box)
        # 保存到本地路径
        region.save("image_code.png")
        print 'cutsuccess'
        # time.sleep(100)
        # d = pq(driver.page_source)
        # lastContent = d('.msg-sub:last .title').text();

        # print '333'
        # # 用Image模块打开上一步保存的验证码
        # image = Image.open('code.png')
        # # 识别验证码
        # optCode = pytesseract.image_to_string(image)
        # # 打印出验证码
        # print("验证码：", optCode)


meibaosub = MeibaoSubmit()
meibaosub.submit("")
