#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/23 16:01

# ！/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/8/28 16:24

from selenium import webdriver
import time
import faker
from pynput.mouse import Button, Controller

fake = faker.Faker()


class Enteromm():

    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = url

    def close(self):
        self.driver.quit()

    def room_url(self):
        self.driver.get(self.url)
        self.driver.find_element_by_name("nickname").send_keys(fake.name())
        self.driver.find_element_by_id("submit_btn").click()
        time.sleep(3)
        self.to_classroom()

    def to_classroom(self, x=311, y=198):
        mouse = Controller()
        mouse.position = (x, y)
        mouse.click(button=Button.left)
        time.sleep(3)

loginino = Enteromm("https://demo.talk-cloud.net/340340104/10756/0/2")
loginino.room_url()


print("更新1")
