#!/usr/bin/python
# -*- coding: UTF-8 -*-
import redis

pool = redis.ConnectionPool(host='122.14.213.241',password='123456', port=6397, db=0)
r = redis.Redis(connection_pool=pool)
