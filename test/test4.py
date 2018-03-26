#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36 Content-Type: application/x-www-form-urlencoded;charset=utf-8"
)
obj = webdriver.PhantomJS(desired_capabilities=dcap)


obj.get('http://www.baidu.com')
time.sleep(5)
print obj
obj.find_element_by_id('kw').send_keys("aaa")                    #通过ID定位
print(1111)
data = obj.find_element_by_class_name('s_ipt')         #通过class属性定位
obj.find_element_by_name('wd')                  #通过标签name属性定位
obj.find_element_by_tag_name('input')           #通过标签属性定位
obj.find_element_by_css_selector('#kw')         #通过css方式定位
obj.find_element_by_xpath("//input[@id='kw']")  #通过xpath方式定位
obj.find_element_by_link_text(u"贴吧")           #通过xpath方式定位
    
print obj.find_element_by_id('kw').tag_name   #获取标签的类型
