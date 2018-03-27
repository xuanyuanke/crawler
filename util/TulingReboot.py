#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import requests


class TulingReboot:
    # 机器人自动回复
    def robootSay(self, msg):
        resp = requests.post("http://www.tuling123.com/openapi/api", data={
            "key": "57490e172d6a4b75a623dc536755217d",
            "info": msg,
            "userid": "212906"
        });
        resp = resp.json()
        retMsg = resp['text']
        print '回复信息：' + retMsg
        return retMsg
