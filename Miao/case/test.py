# -*- coding: UTF-8 -*-

import requests
import  base64
import  json
import unittest
from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
from Crypto import Random

from selenium import webdriver

# url='http://47.93.117.116:6080/MiaoCai/Login'
# data = {'phone':'18600393689', 'pwd':'123456', 'flag':'zh'}
#
# encode = base64.b64encode(json.dumps(data))
#
# r = requests.post(url, data={"data":encode})
#
# print r.text
#
# if __name__ == "__main__":
#     unittest.main()
# s1 = base64.encodestring("123456")
# s2 = base64.decodestring(s1)
# print s1, s2
#
# obj =AES.new("this is a key123", AES.MODE_CBC, "This is an IV456")
#
# message = "the answer is no"
# ciphertext = obj.encrypt(message)
# print ciphertext
#
# obj2  = AES.new("this is a key123", AES.MODE_CBC, "This is an IV456")
# result = obj2.decrypt(ciphertext)
# print result
# class prpcrypt():
#     def __init__(self, key):
#         self.key = key
#         self.mode = AES.MODE_CBC
#     '''加密函数，如果text不是16的倍数(加密文本text必须为16的备注)，那就补足为16的倍数'''
#     def encrypt(self, text):
#         cryptor = AES.new(self.key, self.mode, self.key)
#         length = 16
#         count = len(text)
#         add = length - (count%length)
#         text = text + ('\0' * add)
#         self.ciphertext = cryptor.encrypt(text)
#         return b2a_hex(self.ciphertext)
#     def decrypt(self, text):
#         cryptor = AES.new(self.key, self.mode, self.key)
#         plain_text = cryptor.decrypt(a2b_hex(text))
#         return plain_text.rstrip('\0')
#
# if __name__ == '__main__':
#     pc = prpcrypt('keyskeyskeyskeys')      #初始化密钥
#     e = pc.encrypt("00000")
#     d = pc.decrypt(e)
#     print e
#     print d
#
# key = '1234567890!@#$%^'
# iv = Random.new().read(16)
#
# cipher1 = AES.new(key, AES.MODE_CBC ,iv)
# encrypt_msg = iv + cipher1.encrypt('123456')
# result =  b2a_hex(encrypt_msg)
# print result
s1 = base64.encodestring("95ba71dc9d8912177d4ce04123f42151")
print s1
