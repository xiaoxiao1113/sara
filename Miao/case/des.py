# -*- coding: UTF-8 -*-

import base64
from pyDes import *

Des_Key = "miaocaiwang" # Key
Des_IV = "\x22\x33\x35\x81\xBC\x38\x5A\xE7" # 自定IV向量





class MyCrypt():
    def __init__(self, key):
        self.key = key

    def DesEncrypt(str):
        k = des(Des_Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)
        EncryptStr = k.encrypt(str)
        return base64.b64encode(EncryptStr) #转base64编码返回

if __name__ == '__main__':
    pc = MyCrypt("1234567890!@#$%^")      #初始化密钥
    e = pc.DesEncrypt("miaocaiwang")
    print e

