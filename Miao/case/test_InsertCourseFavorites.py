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

    def test_user_insert_favorite(self):
        '''新增收藏:'''
        userfavorite_url = self.base_url + "insertAppCourseFavorites"
        header={
            "miao-token": self.token,
            "miao-appcheckapisecurity":"cgjAXZkBcEbEYMZckgroPOJ89kVDsjuxQDE1MTA4OTk0NDY5Mjg="
        }
        userfavorite_data = {"user_id":self.UserId, "course_id":"60"}
        userfavorite_r = requests.post(userfavorite_url, userfavorite_data ,headers=header)
        userfavorite_result = userfavorite_r.json()["message"]
        # print userfavorite_result
        if userfavorite_result == u"新增成功！":
            print "收藏成功"
        elif userfavorite_result == u"新增失败,已收藏该课程!":
            print "用户已收藏该课程!"




if __name__ == "__main__":
    unittest.main()