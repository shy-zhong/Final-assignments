import pymysql as a

class Mysql:
    host = "47.97.72.81"
    password = "123456"
    dictionary = {
        None:"",
        False:'_single_choice',
        True:'_multiple_choice'
    }

    @classmethod
    def connect(cls):
        db = a.connect(
            host=cls.host,  # MySQL服务器地址
            user="root",   # 用户名
            password=cls.password,  # 密码
            database="MyData"  # 数据库名称
        )
        return db
    @classmethod
    def select(cls,db,goal,mutipleorsingle:bool = None,index = None, username = None):
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
    @classmethod
    def setHost(cls,host):
        if len(host):
            cls.host = host
    @classmethod
    def setPassword(cls,password):
        if len(password):
            cls.password = password
