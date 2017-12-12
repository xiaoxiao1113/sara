# -*- coding: UTF-8 -*-

import unittest
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Live(unittest.TestCase):
    def setUp(self):
        self.base_url = host = "http://47.93.117.116:6080/MiaoCai/"
        u'''登录接口'''
        url_login = host + "Login"
        login_data = {'phone':18600393689, 'pwd':'aOic7k6K7n0=', 'flag':'zh'}
        r = requests.post(url_login, login_data)
        self.UserId = r.json()["data"]["memberRecord"]["userId"]
        self.Uid = r.json()["data"]["uid"]
        self.token =  r.json()['data']['token']

    def tearDown(self):
        pass

    def test_get_user_detail_account(self):
        '''用户账单明细:'''
        accountDetail_url = self.base_url + "getAccountHistoryList"
        header={
            "miao-token": self.token,
            "miao-appcheckapisecurity":"cgjAXZkBcEbEYMZckgroPOJ89kVDsjuxQDE1MTA4OTk0NDY5Mjg="
        }
        accountDetail_data = {"user_id":self.UserId,
                         "start":"1"}
        accountDetail_r = requests.post(accountDetail_url, accountDetail_data ,headers=header)
        accountDetail_result = accountDetail_r.json()["message"]
        accountDetail_page = accountDetail_r.json()["data"]["page"]
        if len(accountDetail_page):
            print "账单明细列表有内容"
        else:
            print "账单明细列表里面没有内容"
        # print accountDetail_page
        # print accountDetail_result
        # if accountDetail_result == u"苹果预支付成功！":
        #     print "苹果预支付成功！"


if __name__ == "__main__":
    unittest.main()