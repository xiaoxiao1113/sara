# -*- coding: UTF-8 -*-

import unittest
import requests
import urllib
import json

class Login(unittest.TestCase):
    ''''用户登录'''
    def setUp(self):
        # self.base_url = 'http://47.93.117.116:6080/MiaoCai/Login'
        self.base_url = 'http://192.168.1.208:6080/MiaoCai/Login'
    def tearDown(self):
        print(type(self.result))
        #pass
    def test_login_user_and_password_success(self):
        s = requests.session()
        payload = {'phone':'18600393689', 'pwd':'aOic7k6K7n0=', 'flag':'zh'}
        r = requests.post(self.base_url, params=payload)
        # self.result = json.dumps( r.json())
        self.result = r.json()
        print self.result['message']
        print r.text
        print r.json()["data"]["memberRecord"]["userId"]
        # token = r.json()['data']['token']
        # post_url = "http://47.93.117.116:6080/MiaoCai/getActEduCard"
        # header = {
        #             "miao-token": token,
        #             "Host": "47.93.117.116:6080",
        #              "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0",
        #              "Accept": "*/*",
        #             "Accept-Language":"zh-CN,zh;q=0.9",
        #             "Accept-Encoding": "gzip, deflate",
        #             "Content-Type":"application/x-www-form-urlencoded",
        #             "Connection":"keep-alive",
        #             "Content-Length": "44",
        #             "charset":"UTF-8"
        #          }
        # header={"miao-token": token}
        # data = {"user_id":"5044", "card_code":"N1117080008", "card_code_password":"956S84"}
        # s = requests.post(post_url,data,headers=header)
        # self.result =s.json()
        # print self.result["message"]
        # print s.text
        # print self.result
        # print self.result['message']
        # print self.result['data']['token']
        # print self.result['data']['memberRecord']['userId']
        # self.assertEqual(self.result['body']['resultcode'], 0)



if __name__ == "__main__":
    unittest.main()



