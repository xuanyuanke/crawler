import pymysql
import datetime


def getConn():
    conn = pymysql.connect(

        host="127.0.0.1",

        port=3306,

        user="root",

        password="root",

        db="autos",

        charset="utf8")
    return conn
