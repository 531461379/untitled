#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/11 14:57

import logging
import os
import datetime

class Log():

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        self.base_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'Logs')

        self.log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"

        self.log_name = os.path.join(self.base_dir, self.log_file)

        # #文件输出日志
        self.file_handle = logging.FileHandler(self.log_name,"a",encoding="utf-8")
        self.formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        self.file_handle.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()

if __name__ == '__main__':
    log = Log()
    log.get_log()

