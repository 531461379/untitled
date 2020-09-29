#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/27 18:13

import requests
import re
import pymysql

class Mysqlserch(object):

    def __init__(self):
        self.get_conn()

    def get_conn(self):
        try:
            self.conn = pymysql.connect(
                host = "127.0.0.1",
                user = "root",
                password = "123456",
                port = 3306,
                db = "girls",
                charset = "utf8"
            )
        except pymysql.Error as e:
            print('Error:{}'.format(e))

    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print('Error:{}'.format(e))

    def get_one(self):
        '''
        查询一条数据
        :return:
        '''
        sql = 'SELECT `name` FROM beauty where name = "周冬雨";'
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rest = dict(zip([k[0] for k in cursor.description],cursor.fetchone()))
        cursor.close()
        self.close_conn()
        return rest

    def get_all(self):
        '''
        查询多条
        :return:
        '''
        sql = "SELECT * FROM beauty;"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rest = [dict(zip([k[0] for k in cursor.description],row)) for row in cursor.fetchall()]
        cursor.close()
        self.close_conn()
        return rest

def main():
    obj = Mysqlserch()
    # rest1 = obj.get_one()
    rest = obj.get_all()
    for item in rest:
        print(item)

if __name__ == '__main__':
    main()




