# -*- coding: UTF-8 -*-

import unittest

import ddt
import requests

from common import excel_pub

filepath =  "E:\\Program\\Miao\\user.xls"
sheetname = "Sheet1"
data = excel_pub.ExcelRead(filepath, sheetname)
testData = data.dict_data()
print testData

host = "http://47.93.117.116:6080/MiaoCai/"
@ddt.ddt
class MemberCardAct():

    @ddt.data(*testData)
    def test_01(self,data):
        u'''登录接口'''
        url_login = host + "Login"
        login_data = {'phone':data["mobile"], 'pwd':'aOic7k6K7n0=', 'flag':'zh'}
        r = requests.post(url_login, login_data)
        UserId = r.json()["data"]["memberRecord"]["userId"]
        print UserId
        token =  r.json()['data']['token']
        '''会员卡激活接口'''
        Merber_url = host + "getActEduCard"
        header={"miao-token": token}
        merber_data = {"user_id":UserId, "card_code":data["Card"], "card_code_password":data["Act_mode"]}
        s = requests.post(Merber_url,merber_data,headers=header)
        result = s.json()['message']
        print result
        if result == u"该会员卡已激活！":
            print "该会员卡已激活！！！"
        elif result == u"恭喜您,会员卡激活成功！":
            print "该会员卡已成功激活!!!"
        elif result == u"会员卡卡号密码错误！":
            print "请输入正常的会员卡号密码"

if __name__ == "__main__":
    unittest.main()






