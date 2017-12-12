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

    def test_search_course(self):
        '''新增收藏:'''
        usersearch_url = self.base_url + "getTopSearchCourse"
        header={"miao-token": self.token}
        usersearch_data = {"user_id":self.UserId, "topName":"111", "start":"1"}
        usersearch_r = requests.post(usersearch_url, usersearch_data ,headers=header)
        usersearch_message = usersearch_r.json()["message"]
        usersearch_result =  usersearch_r.json()["data"]["page"]
        # usersearch_result =  usersearch_r.json()["data"]["page"][0]["eduCourseKpoint"]["kPointName"]
        # usersearch_result1 =  usersearch_r.json()["data"]["page"][1]["eduCourseKpoint"]["kPointName"]
        # usersearch_result2 =  usersearch_r.json()["data"]["page"][2]["eduCourseKpoint"]["kPointName"]

        # print usersearch_result
        # print usersearch_result
        # print usersearch_result1
        # print usersearch_result2
        if len(usersearch_result):
            print "搜索到相关内容"
        else:
            print "目前还没有相关课程，请耐心等待"

    def test_search_teaacher(self):
        '''新增收藏:'''
        usersearch_url = self.base_url + "getTopSearchTeacher"
        header={"miao-token": self.token}
        usersearch_data = {"user_id":self.UserId, "topName":"邵励", "start":"1"}
        usersearch_r = requests.post(usersearch_url, usersearch_data ,headers=header)
        usersearch_result =  usersearch_r.json()["data"]["page"]

        if len(usersearch_result):
            print "搜索到相关老师"
        else:
            print "目前还没有相关老师，请耐心等待"



if __name__ == "__main__":
    unittest.main()