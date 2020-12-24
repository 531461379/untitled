#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/24 14:48

import requests
import json,time
import os


class Spider():

    def __init__(self):
        self.url1 = "https://{}.talk-cloud.net/ClientAPI/getconfig"
        self.url2 = "https://global.talk-cloud.net/ClientAPI/getserverarea"
        self.data = {"serial":"981527802","userrole":0,"coursename": None}
        self.server = "2" #输入集群几

    def getserver(self):
        res = requests.get(self.url2)
        res_json = json.loads(res.text)
        json_serverarealist = res_json.get("serverarealist")
        coursename_list = []
        msg = ""
        for i in json_serverarealist:
            servernames = i.get("serverareaname")
            url_ping = servernames+"{}.talk-cloud.net".format(self.server)
            re_replase = str(os.popen("ping -n 1 %s"%url_ping).read())
            ip = re_replase[(re_replase.find("[") + 1):re_replase.find("]")]
            msg += ip
            msg += '\n'
            with open("lines", 'w', encoding='utf-8') as f:
                f.write(msg)
            coursename_list.append(servernames)
        return coursename_list

    def getconfig(self):
        msg = ""
        for i in self.getserver():
            time.sleep(1)
            self.data['coursename'] = i
            res = requests.get(self.url1.format(i), self.data)
            time.sleep(1)
            new_json = json.loads(res.text)
            newcour_seaddrs = new_json.get("newcourseaddr")[0]
            change = newcour_seaddrs.get("change")
            print(change)

if __name__ == '__main__':
    aaa = Spider()
    aaa.getserver()
    aaa.getconfig()
