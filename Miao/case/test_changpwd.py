# -*- coding: UTF-8 -*-

import unittest
import requests
import json

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

    def test_changpwd(self):
        '''直播接口:听课方式：在线:数据表：edu_course_live_registration'''
        changepwd_url = self.base_url + "updatePassword"
        print changepwd_url
        header={"miao-token": self.token}
        merber_data = {"user_id":self.UserId, "uid":self.Uid, "old_password":"123456", "password":"111111"}
        s = requests.post(changepwd_url,merber_data,headers=header)
        # print s.text
        result = s.json()['message']
        if result == u"报名成功！":
            print "恭喜你，在线报名成功"




if __name__ == "__main__":
    unittest.main()

