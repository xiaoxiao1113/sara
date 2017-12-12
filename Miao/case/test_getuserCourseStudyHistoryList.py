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

    def test_study_history(self):
        '''用户录播观看记录:'''
        studyHistory_url = self.base_url + "getCourseStudyHistoryList"
        header={
            "miao-token": self.token,
            "miao-appcheckapisecurity":"cgjAXZkBcEbEYMZckgroPOJ89kVDsjuxQDE1MTA4OTk0NDY5Mjg="
        }
        studyHistory_data = {"user_id":self.UserId, "start":"1"}
        studyHistory_r = requests.post(studyHistory_url,studyHistory_data,headers=header)
        studyHistory_result = studyHistory_r.json()['data']["page"]
        studyHistory_courseId = studyHistory_r.json()['data']["page"][0]["courseId"]
        print studyHistory_courseId

        if len(studyHistory_result):
            print "你有观看记录！！"
        else:
            print "你还没有观看记录！！"
        return studyHistory_courseId

    def test_del_study_history(self, studyHistory_courseId):
        '''删除录播观看记录:'''
        studyHistory_url = self.base_url + "delStudyHistory"

        header={
            "miao-token": self.token,
            "miao-appcheckapisecurity":"cgjAXZkBcEbEYMZckgroPOJ89kVDsjuxQDE1MTA4OTk0NDY5Mjg="
        }
        studyHistory_data = {"user_id":self.UserId, "course_id":studyHistory_courseId}
        studyHistory_r = requests.post(studyHistory_url,studyHistory_data,headers=header)
        studyHistory_result = studyHistory_r.json()['data']["page"]
        # kId = studyHistory_r.json()['data']["page"][0]["kId"]
        # courseId = studyHistory_r.json()["data"]["page"][0]["courseId"]
        # video_name = kpointList.json()['data']["page"][0]["kPointName"]
        # print kId

        print studyHistory_result
        print len(studyHistory_result)
        if len(studyHistory_result):
            courseId = studyHistory_r.json()["data"]["page"][0]["courseId"]
            print courseId
        else:
            print "你还没有观看记录！！"




if __name__ == "__main__":
    unittest.main()