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
        # print self.UserId

    def tearDown(self):
        pass

    def test_user_logout(self):
        '''用户退出:'''
        user_logout_url = self.base_url + "logout"
        header={
            "miao-token": self.token,
            "miao-appcheckapisecurity":"cgjAXZkBcEbEYMZckgroPOJ89kVDsjuxQDE1MTA4OTk0NDY5Mjg="
        }
        user_logou_data = {"userid":self.UserId}
        user_logou_r = requests.post(user_logout_url, user_logou_data ,headers=header)
        # print user_logou_r.content
        user_logou_result = user_logou_r.json()["message"]
        # print user_logou_result
        if user_logou_result == u"退出成功！":
            print "退出成功！"





if __name__ == "__main__":
    unittest.main()