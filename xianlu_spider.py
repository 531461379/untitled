#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/24 14:48

import requests
import json,time


class Spider():

    def __init__(self):
        self.url1 = "https://{}.talk-cloud.net/ClientAPI/getconfig"
        self.url2 = "https://global.talk-cloud.net/ClientAPI/getserverarea"
        self.data = {"serial":"981527802","userrole":0,"coursename": None}

    def getserver(self):
        res = requests.get(self.url2)
        res_json = json.loads(res.text)
        json_serverarealist = res_json.get("serverarealist")
        coursename_list = []
        for i in json_serverarealist:
            servernames = i.get("serverareaname")
            # print(servernames)
            coursename_list.append(servernames)
        return coursename_list

    def getconfig(self):
        for i in self.getserver():
            time.sleep(1)
            self.data['coursename'] = i
            res = requests.get(self.url1.format(i), self.data)
            print(res.text)
            time.sleep(1)
            new_json = json.loads(res.text)
            newcour_seaddrs = new_json.get("newcourseaddr")[0]
            change = newcour_seaddrs.get("change")
            print(change)

aaa = Spider()
aaa.getconfig()
aaa.getserver()