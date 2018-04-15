#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
from RedisUtil import *
# 随机生成手机号码
class MyUtil:
	@staticmethod
	def createPhone():
		prelist=r.get("CRAWLER_WEB_MOBILE").split(",")
		# prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
		return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))