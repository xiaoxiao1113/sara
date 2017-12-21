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

    def test_user_del_favorite(self):
        '''新增收藏:'''
        userfavorite_url = self.base_url + "delAppCourseFavorites"
        header={"miao-token": self.token}
        userfavorite_data = {"user_id":self.UserId, "course_id":"606"}
        userfavorite_r = requests.post(userfavorite_url, userfavorite_data ,headers=header)
        userfavorite_result = userfavorite_r.json()["message"]
        print userfavorite_result
        if userfavorite_result == u"编辑成功！":
            print "取消收藏"
        elif userfavorite_result == u"编辑失败":
            print "该课程已取消收藏"


if __name__ == "__main__":
    unittest.main()