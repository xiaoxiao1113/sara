# -*- coding: UTF-8 -*-

import requests
import  base64
import  json
import unittest
from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex

class MyCrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        length = 16
        count = len(text)
        print count
        if count < length:
            add = length - count
            text= text + ('\0' * add)

        elif count > length:
            add = (length -(count % length))
            text= text + ('\0' * add)

        cryptor = AES.new(self.key, self.mode, self.key)
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')

if __name__ == '__main__':
    pc = MyCrypt('1234567890!@#$%^')      #初始化密钥
    e = pc.encrypt("123456")
    print e

