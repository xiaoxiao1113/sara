#coding=utf-8
import unittest
import HTMLTestRunner
import time
import os

#定义文件查找目录(也就是存放单元测试用例的目录)
# case_dir = "E:\\hongbaodai\\test_case"
# testcase = unittest.TestSuite()
# #定义discover方法的参数，找到test开头的用例
# discover = unittest.defaultTestLoader.discover(case_dir,#测试文件的路径
#                                                            pattern="test*.py",#匹配规则
#                                                            top_level_dir=None)#None，表示该文件就是顶层目录，没有子文件夹
# #discover方法筛选出来的用例，循环添加到测试套件中
# for test_suite in discover:
#     for test_case in test_suite:
#         testcase.addTests(test_case)
# print testcase
#######----------将用例添加到套件-----##
def creatsuite():
    #定义文件查找目录(也就是存放单元测试用例的目录)
    test_dir = "E:\\Program\\Miao"
    testunit = unittest.TestSuite()
    #定义discover方法的参数，找到test开头的用例
    discover = unittest.defaultTestLoader.discover(test_dir,#测试文件的路径
                                                   pattern="test*.py",#匹配规则
                                                   top_level_dir=None)#None，表示该文件就是顶层目录，没有子文件夹
    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
    print testunit
    return testunit



if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = "E:\\hongbaodai\\report\\"+now+"result.html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                     title=u'测试报告',
                                     description=u'用例执行情况：')
    runner.run(creatsuite())
    fp.close()
    # runner = unittest.TextTestRunner()
    # runner.run(creatsuite())