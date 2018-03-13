#coding=utf-8


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from ToBaidu import *


ip=str('122.72.18.34:80')
word=u"美国生孩子"
baidu = ToBaidu()
name="www.angel-usa.com"
baidu.specifiedOpen(ip,word,name)