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

    def test_kpointList(self):
        '''录播视频列表:'''
        list_url = self.base_url + "getKpointList"
        # print list_url
        header={"miao-token": self.token}
        list_data = {"user_id":self.UserId, "uid":self.Uid, "course_id":"480"}
        s = requests.post(list_url,list_data,headers=header)
        # print s.text
        result = s.json()['data']["page"][0]["kPointName"]
        # print result
        if result == u"规避涉税风险的思路和方法":
            print "恭喜你，成功打开页面"




if __name__ == "__main__":
    unittest.main()