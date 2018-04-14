#!/usr/bin/python
# -*- coding: UTF-8 -*-
import DbUtil
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class LogByDb:
    # 机器人自动回复
    def write(self, msg, ip,type):
        global conn
        try:
            conn = DbUtil.getConn()
            cur = conn.cursor()
            sql ="insert cr_log   ( ip ,type , text , create_time  ) value ('"+ip+"','"+type+"','"+msg+"',NOW())"
            print sql
            # 执行SQL，并返回收影响行数
            effect_row = cur.execute(sql)
            cur.execute(sql)
            conn.commit()
            print 'insert log success is : ' ,effect_row
        except Exception as e:
            print '#db# err is : ', e
        finally:
            # conn.close()
            print 'log wirte'

