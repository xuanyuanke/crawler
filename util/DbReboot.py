#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import requests
import sys
import DbUtil
import sys
from RedisUtil import *
from StringUtil import *
import random


reload(sys)
sys.setdefaultencoding('utf8')


class DbReboot:

    # 机器人自动回复
    def robootSay(self, msg, ip):
        retMsg = ""
        global conn
        try:
            index = -1
            if r.get(ip) == None:
                r.set(ip, index)
            index = int(r.get(ip)) + 1
            if index > 5:
                index = 0
            #设置redis过期时间是 10分钟
            r.set(ip, index,600)
            conn = DbUtil.getConn()
            cur = conn.cursor()
            sql = "select * from auto_talk_msg where  tindex = " + \
                str(index)
            print sql
            cur.execute(sql)
            results = cur.fetchall()  # 获取查询的所有记录
            retMsg = ""
            # 遍历结果
            for row in results:
                text = row[1]
                retMsg = text
            randomStr = random.random()
            if randomStr > 0.5:
                retMsg = retMsg.replace("$name", "男士")
            else:
                retMsg = retMsg.replace("$name", "女士")

            retMsg = retMsg.replace("$phone", MyUtil.createPhone())
            retMsg = retMsg.replace("$weixin", MyUtil.createPhone())
        except Exception as e:
            print '#db# err is : ', e
        finally:
            conn.close()
            print '回复信息：' + retMsg
            return retMsg
