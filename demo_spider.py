#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/23 16:01

# ！/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/8/28 16:24

from selenium import webdriver
import os
import time
import faker
from pynput.mouse import Button, Controller
fake = faker.Faker()

class Enteromm():

    def __init__(self, url):
        chrome_driver = r'D:/python3.6/chromedriver'
        os.environ["webdriver.Chrome.driver"] = chrome_driver
        option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches", ['enable-automation'])# 设置chrome浏览器的参数，使其不弹框提示（chrome正在受自动测试软件的控制）
        prefs = {'profile.default_content_setting_values.media_stream_camera': 1,
                 'profile.default_content_setting_values.media_stream_mic': 1,
                 'profile.default_content_setting_values.notifications': 1,
                 'profile.default_content_setting_values.geolocation': 1}
        # 设置chrome浏览器的参数，使其不弹框提示（是否保存密码）
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        option.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=option)
        self.driver.maximize_window()
        self.url = url


    def close(self):
        self.driver.quit()

    def room_url(self):
        self.driver.get(self.url)
        self.driver.find_element_by_name("nickname").send_keys(fake.name())
        self.driver.find_element_by_name("roompwd").send_keys("1")
        self.driver.find_element_by_id("submit_btn").click()
        time.sleep(5)
        self.driver.find_element_by_id("start-detection").click()
        self.driver.find_element_by_xpath('//*[@id="main_detection_device"]/div/div[2]/div[4]/button[2]').click() #视频检测
        self.driver.find_element_by_xpath('//*[@id="main_detection_device"]/div/div[3]/div[4]/button[2]').click() #扬声器检测
        self.driver.find_element_by_xpath('//*[@id="main_detection_device"]/div/div[4]/div[6]/button[2]').click()
        self.driver.find_element_by_xpath('//*[@id="main_detection_device"]/div/div[6]/div/button[2]').click()

    def to_classroom(self, x=311, y=198):
        mouse = Controller()
        mouse.position = (x, y)
        mouse.click(button=Button.left)
        time.sleep(3)

loginino = Enteromm("https://global.talk-cloud.net/1364152026/10032/1/0")
loginino.room_url()


