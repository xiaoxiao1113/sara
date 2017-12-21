# -*- coding: UTF-8 -*-

import unittest
import requests
import json

class Live(unittest.TestCase):
    def setUp(self):
        self.base_url = host = "http://47.93.117.116:6080/MiaoCai/"
        u'''登录接口'''
        url_login = host + "Login"
        login_data = {'phone':18600393689, 'pwd':'aOic7k6K7n0=', 'flag':'zh'}
        r = requests.post(url_login, login_data)
        self.UserId = r.json()["data"]["memberRecord"]["userId"]
        self.token =  r.json()['data']['token']

    def tearDown(self):
        pass

    def test_OnlineLive(self):
        '''直播接口:听课方式：在线:数据表：edu_course_live_registration'''
        Merber_url = self.base_url + "insertLiveReg"
        # print Merber_url
        header={
            "miao-token": self.token,
            "miao-appcheckapisecurity":"cgjAXZkBcEbEYMZckgroPOJ89kVDsjuxQDE1MTA4OTk0NDY5Mjg="
        }
        merber_data = {"user_id":self.UserId, "course_id":"600", "type":0,"courts_id":0}
        s = requests.post(Merber_url,merber_data,headers=header)
        print s.text
        result = s.json()['message']
        if result == u"报名成功！":
            print "恭喜你，在线报名成功"
        elif result == u"对不起,已超过报名时限！":
            print "直播已结束！！"



    def test_CourseLive(self):
        '''直播接口:听课方式：分院'''
        Merber_url = self.base_url + "insertCourseReg"
        header={
            "miao-token": self.token,
            "miao-appcheckapisecurity":"cgjAXZkBcEbEYMZckgroPOJ89kVDsjuxQDE1MTA4OTk0NDY5Mjg="
        }
        member_data = {"user_id":self.UserId, "course_id":"600", "type":"1","courts_id":"90","username":"1111", "mobile":"18513112593"}
        # print Merber_url
        # print member_data
        s = requests.post(Merber_url ,member_data ,headers=header)
        print s.status_code
        print s.content
        result = s.json()['message']
        print result
        if result == u"报名成功！":
            print "分院报名成功"

if __name__ == "__main__":
    unittest.main()

