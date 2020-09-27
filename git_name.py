#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/24 16:38

import requests
import time
import json
import os

def getserver(url,url_config):
    res = requests.post(url)
    res_json = json.loads(res.text)
    json_serverarealist = res_json.get("serverarealist")
    for i in json_serverarealist:
        servernames = i.get("serverareaname")
        url_wanzheng = servernames+url_config
        print(url_wanzheng)




getserver("http://global.talk-cloud.net/ClientAPI/getserverarea","1.talk-cloud.net")
