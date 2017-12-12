#coding:utf-8
import MySQLdb

mysql_info = {"host":"rm-2ze4bi610e7245hvp.mysql.rds.aliyuncs.com",
              "port":3306,
              "user":"root",
              "password":"Xxx5696332",
              "db":"miaocai_sxytest",
              "charset":"utf8"}

class MysqlUtil():
    '''
    mysql 数据库相关操作
    连接数据库信息：mysql_info
    创建游标:mysql_execute
    查询某个字段对应的字符串：mysql_getstring
    查询一组数据：mysql_getrows
    关闭mysql连接：mysql_close
    '''
    def __init__(self):
        self.db_info = mysql_info
        u'''连接池方式'''
        self.conn = MysqlUtil.__getConnect(self.db_info)

        @staticmethod
        def __getCoonect(db_info):
            '''静态方法，从连接池中取出连接'''
            try:
                conn = MySQLdb.connect(host=db_info['host'],
                                       port = db_info['port'],
                                       user = db_info['user'],
                                       password = db_info['password'],
                                       db = db_info['db'],
                                       charset = db_info['charset'])
                return conn

            except Exception as a:
                print ("数据库连接异常：%s"%a)

        def mysql_execute(self,sql):
            '''执行sql语句'''
            cur = self.conn.cursor()
            try:
                cur.execute(sql)
            except Exception as a:
                self.conn.rollback()  #sql执行异常回滚
                print ("执行sql出现异常%s"%a)
            else:
                cur.close()
                self.conn.commit()  #sql无异常提交

        def mysql_getrows(self,sql):
            '''返回查询结果'''
            cur = self.conn.cursor
            try:
                cur.execute(sql)
            except Exception as a:
                print ("执行sql语句出现异常%s"%a)
            else:
                rows = cur.fetchall()
                cur.close()
                return rows

        def mysql_getstring(self,sql):
            '''查询某个字段的对应值'''
            rows = self.mysql_getrows(sql)
            if rows !=None:
                for row in rows:
                    for i in row:
                        return i

        def mysql_close(self):
            '''关闭close mysql'''
            try:
                self.conn.close()
            except Exception as a:
                print ("数据库关闭时异常%s"%a)
if __name__ == "__main__":
    mysql = MysqlUtil()
    sql = "select * from edu_course_live_registration WHERE user_id=33616"
    mysql.mysql_execute(sql)
    print mysql.mysql_getrows(sql)
    print mysql.mysql_getsting(sql)
    mysql.mysql_close()



