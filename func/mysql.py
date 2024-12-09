import pymysql as a

class Mysql:

    dictionary = {
        False:'_single_choice',
        True:'_multiple_choice'
    }

    @staticmethod
    def connect():
        db = a.connect(
            host="localhost",  # MySQL服务器地址
            user="root",   # 用户名
            password="zyy123456",  # 密码
            database="MyData"  # 数据库名称
        )
        return db
    @classmethod
    def select(cls,db,goal,mutipleorsingle:bool,index = None, username = None):
        cursor = db.cursor()
        command = "select * from " + goal + cls.dictionary[mutipleorsingle]
        if index != None :
            try:
                command += " where id = %s"
                cursor.execute(command, (index,))
                return cursor.fetchone()
            except:
                return None
        elif username != None:
            command += " where username = %s"
            cursor.execute(command, (username,))
            return cursor.fetchone()
    @staticmethod
    def execute(db,command:str)->None:
        cursor = db.cursor()
        cursor.execute(command)
        return cursor.fetchall()
    @classmethod
    def max(cls,db,goal,check:bool = None)->int:
        if check != None:
            goal += (cls.dictionary[check])
        command = "select max(id) from " + goal + ';'
        cursor = db.cursor()
        try:
            cursor.execute(command)
            results = cursor.fetchone()
        except:
            results = (0,0,)
        return results
