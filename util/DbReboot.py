#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import requests
import sys
import DbUtil
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class DbReboot:

    # 机器人自动回复
    def robootSay(self, msg):
        retMsg = ""
        global conn
        try:
            print 111111
            conn = DbUtil.getConn()
            cur = conn.cursor()
            sql = "select * from auto_talk_msg where id =1 "
            cur.execute(sql)
            results = cur.fetchall()  # 获取查询的所有记录
            retMsg = ""
            # 遍历结果
            for row in results:
                text = row[1]
                retMsg = text
                print 33333
        except Exception as e:
            print e
        finally:
            # conn.close()
            print '回复信息：' + retMsg
            return retMsg
