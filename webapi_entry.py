# _*_ codingLutf-8 _*_

import unittest
import time
import requests
import hashlib
import datetime
import random
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import base64

AES_LENGTH = 16

class Entry():

    def __init__(self,key):
        self.url = "http://global.talk-cloud.net/WebAPI/entry"
        self.key = "l97lLyiwpjB15d6u"   #authkey值
        self.serial = "928082399"    #房间号
        self.usertype = "0"    #用户类型
        self.domain = "test"   #企业域名
        self.randoms = random.randint(1000, 9999)
        self.times = int(time.time())
        self.auth = self.key+str(self.times)+self.serial+self.usertype
        #userpassword参数,aes加密
        self.aes_key = key
        self.mode = AES.MODE_ECB
        self.cryptor = AES.new(self.pad_key(self.aes_key).encode(), self.mode)

    def pad(self,text):
        while len(text) % AES_LENGTH != 0:
            text += ' '
        return text

    # 加密密钥需要长达16位字符，所以进行空格拼接
    def pad_key(self,key):
        while len(key) % AES_LENGTH != 0:
            key += ' '
        return key

    def encrypt(self, text):
        self.ciphertext = self.cryptor.encrypt(self.pad(text).encode())
        return b2a_hex(self.ciphertext)

    def md5(self):
        md5_auth = hashlib.md5(self.auth.encode(encoding='UTF-8')).hexdigest()
        return md5_auth

    def res_get(self):
        data = {"domain":self.domain, "serial":self.serial,
                     "username": "entry_serial", "usertype":self.usertype,
                     "pid":self.randoms,"ts":self.times, "auth":self.md5(),"userpassword":self.encrypt("1111").decode(),"stuJumpUrl":"https://www.baidu.com/"}
        res = requests.get(self.url,data)
        print(res.url)

aaa = Entry("l97lLyiwpjB15d6u")
aaa.res_get()


