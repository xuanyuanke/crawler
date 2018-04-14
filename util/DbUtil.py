import pymysql
import datetime


def getConn():
    conn = pymysql.connect(

        host="122.14.213.241",

        port=3306,

        user="root",

        password="123456",

        db="crawler",

        charset="utf8")

    return conn
