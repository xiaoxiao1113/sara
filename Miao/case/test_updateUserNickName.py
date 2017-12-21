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

    # def test_update_user_nickname_isEmpty(self):
    #     '''更改用户昵称:'''
    #     usersearch_url = self.base_url + "updateUserNickName"
    #     header={"miao-token": self.token}
    #     usernickname_data = {"user_id":self.UserId, "nickname":"11", "uid":self.Uid}
    #     usernickname_r = requests.post(usersearch_url, usernickname_data ,headers=header)
    #     usernickname_result =  usernickname_r.text
    #     print usernickname_result

        # if usernickname_result == "ok":
        #     print "昵称修改成功"

    def test_update_user_nickname(self):
        '''更改用户昵称:'''
        usernickname_url = self.base_url + "updateUserNickName"
        header={
            "miao-token": self.token,
            "miao-appcheckapisecurity":"cgjAXZkBcEbEYMZckgroPOJ89kVDsjuxQDE1MTA4OTk0NDY5Mjg="
        }
        usernickname_data = {"user_id":self.UserId, "nickname":"啦啦", "uid":self.Uid}
        usernickname_r = requests.post(usernickname_url, usernickname_data ,headers=header)
        usernickname_result =  usernickname_r.json()["message"]
        print usernickname_result

        if usernickname_result == "ok":
            print "昵称修改成功"


if __name__ == "__main__":
    unittest.main()