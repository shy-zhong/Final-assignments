import pymysql as a

class Mysql:
    @staticmethod
    def connect():
        db = a.connect(
            host="localhost",  # MySQL服务器地址
            user="root",   # 用户名
            password="zyy123456",  # 密码
            database="MyData"  # 数据库名称
        )
        return db
    @staticmethod
    def select(db,goal,index = None):
        cursor = db.cursor()
        command = "select * from " + goal
        if index != None :
            command += " WHERE id = %s"
        cursor.execute(command, (index,))
        return cursor.fetchone()
    @staticmethod
    def max(db,goal,cow):
        command = "select max(" + cow + ") from " + goal + ';'
        cursor = db.cursor()
        cursor.execute(command)

        results = cursor.fetchone()
        #print(results)
        return results
