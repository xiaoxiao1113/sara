# -*- coding: UTF-8 -*-

import unittest
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Live(unittest.TestCase):
    def setUp(self):
        #self.base_url = host = "http://47.93.117.116:6080/MiaoCai/"
        self.base_url = host = "http://192.168.1.208:6080/MiaoCai/"
        u'''登录接口'''
        url_login = host + "Login"
        login_data = {'phone':18600393689, 'pwd':'aOic7k6K7n0=', 'flag':'zh'}
        r = requests.post(url_login, login_data)
        self.UserId = r.json()["data"]["memberRecord"]["userId"]
        self.Uid = r.json()["data"]["uid"]
        self.token =  r.json()['data']['token']
        print self.UserId

    def tearDown(self):
        pass

    def test_get_apple_pay(self):
        '''用户预支付接口:edu_order_list'''
        applePay_url = self.base_url + "getApplePay"
        header={
            "miao-token": self.token,
            "miao-appcheckapisecurity":"cgjAXZkBcEbEYMZckgroPOJ89kVDsjuxQDE1MTA4OTk0NDY5Mjg="
        }
        applePay_data = {"userId":self.UserId,
                         "Spbill_create_ip":"192.168.1.23",
                         "address":"北京市北京市东城区啦啦啦哩",
                         "applytype":"9",
                         "isOpen":"0",
                         "receiver":"萧萧",
                         "telephone":"18513112593",
                         "title":"个人发票",
                         "titleType":"1",
                         "type":"3",
                         "vipId":"1"}
        applePay_r = requests.post(applePay_url, applePay_data ,headers=header)
        applePay_result = applePay_r.json()["message"]
        print applePay_r.content
        if applePay_result == u"苹果预支付成功！":
            print "苹果预支付成功！"
    def test_vister_apple_pay(self):
        '''游客预支付接口:edu_order_list_iosvisitor'''
        applePay_url = self.base_url + "getApplePayVisitor"
        header={
            "miao-token": "123456",
            "miao-appcheckapisecurity":"cgjAXZkBcEbEYMZckgroPOJ89kVDsjuxQDE1MTA4OTk0NDY5Mjg="
        }
        applePay_data = {"userId":self.UserId,
                         "Spbill_create_ip":"192.168.1.23",
                         "address":"北京市北京市东城区啦啦啦哩",
                         "applytype":"9",
                         "isOpen":"1",
                         "receiver":"萧萧",
                         "telephone":"18513112593",
                         "title":"个人发票",
                         "titleType":"1",
                         "type":"3",
                         "vipId":"1"}
        applePay_r = requests.post(applePay_url, applePay_data ,headers=header)
        applePay_result = applePay_r.json()["message"]
        if applePay_result == u"苹果预支付成功！":
            print "苹果预支付成功！"



if __name__ == "__main__":
    unittest.main()