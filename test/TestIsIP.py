# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
import os
sys.path.append("../")
from util.IpUtil import *

# IpUtils.getIp()


ip = str(IpUtils.getIp())
print ip
#project_dir = os.path.dirname(os.path.abspath(""))
# print project_dir
