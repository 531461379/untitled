#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/9 8:59

import unittest
from selenium import webdriver
import time,os
from web_h5_test.Common.log import Log
import faker
import pyautogui
from web_h5_test.Common.test_room_stu import Enteromm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
fake = faker.Faker()
logger = Log()
logger.get_log()

class Testcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_driver = r'D:/python3.6/chromedriver'
        os.environ["webdriver.Chrome.driver"] = chrome_driver
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        option.add_experimental_option("excludeSwitches",
                                       ['enable-automation'])  # 设置chrome浏览器的参数，使其不弹框提示（chrome正在受自动测试软件的控制）
        prefs = {'profile.default_content_setting_values.media_stream_camera': 1,
                 'profile.default_content_setting_values.media_stream_mic': 1,
                 'profile.default_content_setting_values.notifications': 1,
                 'profile.default_content_setting_values.geolocation': 1}
        # 设置chrome浏览器的参数，使其不弹框提示（是否保存密码）
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        option.add_experimental_option('prefs', prefs)
        cls.driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=option)
        cls.base_url = "https://demo.talk-cloud.net/434643659/10873/1/0"
        logger.logger.info(cls.base_url)
        cls.driver.maximize_window()


        #进入教室
    def test01_enter_room(cls):
        cls.driver.get(cls.base_url)
        cls.driver.find_element_by_name("nickname").send_keys(fake.name())
        cls.driver.find_element_by_id("roompwd").send_keys(1)
        cls.driver.find_element_by_xpath('//*[@id="form_signin"]/div/div[3]/p').click()
        WebDriverWait(cls.driver, 15).until(
            EC.element_to_be_clickable((By.ID, 'start-detection'))).click()
        time.sleep(1)
        cls.driver.find_element_by_xpath('//*[@id="main_detection_device"]/div/div[2]/div[5]/button[2]').click() #检测视频
        cls.driver.find_element_by_xpath('//*[@id="main_detection_device"]/div/div[3]/div[4]/button[2]').click() #扬声器检测
        cls.driver.find_element_by_xpath('//*[@id="main_detection_device"]/div/div[4]/div[7]/button[2]').click()  # 扬声器检测
        cls.driver.find_element_by_xpath('//*[@id="main_detection_device"]/div/div[6]/div/button[2]').click() #进入教室
        cls.driver.implicitly_wait(5)
        next = cls.driver.find_element_by_xpath(
            '//*[@id="all_root"]/body/div[5]/div/div[3]/div[2]/div/div/div[3]/button').text
        if next == '下一个':
            cls.driver.execute_script('document.getElementsByClassName("Popover")[0].style.display="none";')  # 跳过帮助提示
        else:
            begin = cls.driver.find_element_by_xpath('//*[@id="room_classBegin"]').text
            cls.assertEqual(begin, "上课")
        #画笔右侧工具栏
    def test02_room_tools(cls):
        time.sleep(2)
        cls.driver.find_element_by_id("room_classBegin").click()
        time.sleep(1)
        cls.driver.find_element_by_xpath('//*[@id="all_root"]/body/div[6]/div/div[3]/div[2]/div/div/div[3]/button').click()
        time.sleep(2)
        cls.driver.find_element_by_xpath('//*[@id="tool-bar-box"]/li[5]').click()
        time.sleep(1)
        pyautogui.moveTo(1000,600,duration=0.2)
        pyautogui.dragRel(300, 0, duration=0.2)  # move right
        time.sleep(1)
        cls.driver.find_element_by_xpath('//*[@id="tool-bar-box"]/li[6]/em').click() #汉字
        pyautogui.click(999,693,button="left")
        time.sleep(1)
        pyautogui.typewrite("hello") #发送键值
        time.sleep(1)
        pyautogui.doubleClick(x=999, y=600, button="left")

        #工具箱
    def test03_room_hold(self):
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-tools"]/span').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="holdAllBox"]/ul/li[1]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="answerDrag"]/div[2]/div/div/div[2]/span').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="answerDrag"]/div[3]/button').click()
        for i in range(2,9):
            self.driver.find_element_by_xpath('//*[@id="menu-tools"]/span').click()
            self.driver.find_element_by_xpath('//*[@id="holdAllBox"]/ul/li[%d]'%i).click()
            pyautogui.press('enter')

        #上传课件
    def test04_upload_file(cls):
        time.sleep(2)
        cls.driver.find_element_by_xpath('//*[@id="menu-courseware"]').click()
        cls.driver.find_element_by_xpath(
            '//*[@id="all_wrap"]/div[4]/article/div/div[1]/div[2]/button').click()
        cls.driver.find_element_by_xpath('//*[@id="all_wrap"]/div[4]/article/div[1]/div[2]/div[1]/div[1]/div/p[2]').click()
        os.system(r"D:\uploadfile.exe")
        time.sleep(3)
        cls.driver.find_element_by_xpath('//*[@id="all_wrap"]/div[4]/article/div[1]/div[2]/div[3]/div').click()

    #关联课件
    def test05_roombindfile(cls):
        time.sleep(5)
        WebDriverWait(cls.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="all_wrap"]/div[4]/article/div/div[1]/div[2]/button'))).click()
        time.sleep(1)
        cls.driver.find_element_by_xpath('//*[@id="all_wrap"]/div[4]/article/div[1]/div[1]/ul/li[2]').click()
        time.sleep(1)
        cls.driver.find_element_by_xpath('//*[@id="all_wrap"]/div[4]/article/div[1]/div[2]/div/div[1]/div[2]/ul/li[1]/span[4]').click()
        time.sleep(2)
        cls.driver.find_element_by_xpath('//*[@id="all_wrap"]/div[4]/article/div[1]/div[2]/div/div[2]/div').click()
        time.sleep(1)
        try:
            WebDriverWait(cls.driver, 15).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="fileItem_81429"]/div[2]/span[2]'))).click()
        except:
            print("课件不存在")

    #学生进入
    def test06_room_stu(self):
        loginfo = Enteromm("https://demo.talk-cloud.net/434643659/10873/0/2")
        loginfo.room_url()
        js = 'window.open("https://demo.talk-cloud.net/434643659/10873/0/2");'
        self.driver.execute_script(js)

        #发送消息
    def test07_send_message(self):
        time.sleep(1)
        pyautogui.moveTo(1280, 800, duration=0.2)
        pyautogui.dragRel(280, 0, button="left", duration=0.2)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="header_container"]/article[2]/div[1]/div[3]/button').click()
        self.driver.find_element_by_xpath('//*[@id="chatbox"]/div[2]/div[2]/div/div').send_keys(fake.company())
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="chatbox"]/div[2]/div[2]/button').click()

    #切换柄句
    # def test08_handle(self):
    #     time.sleep(2)
    #     handle = self.driver.current_window_handle
    #     print(handle)
    #     handles = self.driver.window_handles
    #     print(handles)
    #     self.driver.switch_to.window(handles[0])
    #     print(self.driver.title)


        #布局
    def test09_layout_switch(self):
        time.sleep(3)
        for i in range(1,7):
            self.driver.find_element_by_xpath('//*[@id="header_container"]/article[2]/div[1]/div[4]/div[1]/span').click()
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="header_container"]/article[2]/div[1]/div[4]/div[1]/div/div[1]/div[%d]'%i))).click()
            self.driver.find_element_by_xpath('//*[@id="header_container"]/article[2]/div[1]/div[4]/div[1]/div/div[2]/button').click()
            time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="header_container"]/article[2]/div[1]/div[4]/div[1]/span').click()


        #下课
    def test10_over_class(self):
        time.sleep(2)
        self.driver.find_element_by_id("room_classBegin").click()
        self.driver.find_element_by_id("alert-confrim").click()




    @classmethod
    def tearDownClass(cls):
        pass



if __name__ == '__main__':
    unittest.main()


