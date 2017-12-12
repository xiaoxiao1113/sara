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
        login_data = {'phone':18513112593, 'pwd':'aOic7k6K7n0=', 'flag':'zh'}
        r = requests.post(url_login, login_data)
        self.UserId = r.json()["data"]["memberRecord"]["userId"]
        self.Uid = r.json()["data"]["uid"]
        self.token =  r.json()['data']['token']

    def tearDown(self):
        pass

    def test_member_activation(self):
        '''会员卡激活接口'''
        Merber_url = self.base_url + "getActEduCard"
        header={
            "miao-token": self.token,
            "miao-appcheckapisecurity":"cgjAXZkBcEbEYMZckgroPOJ89kVDsjuxQDE1MTA4OTk0NDY5Mjg="
        }
        merber_data = {"user_id":self.UserId , "card_code":"N1217020009", "card_code_password":"S1U08A"}
        s = requests.post(Merber_url,merber_data,headers=header)
        result1 = s.json()
        result = s.json()["message"]
        print result1
        print result
        if result == u"该会员卡已激活！":
            print "该会员卡已激活！！！"
        elif result == u"恭喜您,VIP年卡激活成功！":
            print "该会员卡已成功激活!!!"
        elif result == u"会员卡卡号密码错误！":
            print "请输入正常的会员卡号密码"

if __name__ == "__main__":
    unittest.main()






