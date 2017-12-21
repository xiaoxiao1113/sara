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

    def test_usercomment(self):
        '''录播视频列表:'''
        list_url = self.base_url + "getKpointList"
        header={
            "miao-token": self.token,
            "miao-appcheckapisecurity":"cgjAXZkBcEbEYMZckgroPOJ89kVDsjuxQDE1MTA4OTk0NDY5Mjg="
        }
        list_data = {"user_id":self.UserId, "uid":self.Uid, "course_id":"4"}
        kpointList = requests.post(list_url,list_data,headers=header)

        kId = kpointList.json()['data']["page"][0]["kId"]
        courseId = kpointList.json()['data']["page"][0]["courseId"]
        video_name = kpointList.json()['data']["page"][0]["kPointName"]
        # print kId
        # print courseId

        '''用户评论:'''
        userComment_url = self.base_url + "insertAssessList"
        # print userComment_url
        userComment_data = {"user_id":self.UserId, "course_id":courseId, "content":"hhhhhh","grade":"5"}
        userComment_s = requests.post(userComment_url,userComment_data,headers=header)
        userComment_result = userComment_s.json()["message"]
        # print userComment_result
        if userComment_result == u"新增评论成功！":
            print "用户成功评论视频名称为  '%s'  课程id为%d"%(video_name,courseId)
        elif userComment_result == u"该课程已评论过，不能再次评论！":
            print "该课程名称为  '%s'  课程id为%d已评论过，不能再次评论！"%(video_name,courseId)




if __name__ == "__main__":
    unittest.main()