# MySQL専用 (Postgresql対応も本来必須)

import MySQLdb

class DbManagert():
    def __init__(self):
        self.connection = None

    def connect(self,params):
        if self.checkConnectParams(params) == True :
            self.connection = MySQLdb.connect(
                host= params['host'],
                user= params['user'],
                passwd= params['password'],
                db= params['db'],
                charset='utf8'
            )
        else :
            print('debug')
        return self.connection

    #本来正規表現で厳密にチェックを行う必要がある
    def checkConnectParams(self,params):
        is_params = True

        if 'dbms' not in params :
            print('dbms key not in params')
            is_params = False
        
        if 'host' not in params :
            print('host key not in params')
            is_params = False
        
        if 'user' not in params :
            print('user key not in params')
            is_params = False

        if 'password' not in params :
            print('password key not in params')
            is_params = False
        
        if 'db' not in params :
            print('db key not in params')
            is_params = False
        
        return is_params
    
    def getCursor(self):
        return self.connection.cursor()

    def execute(self,query):
        cursor = self.getCursor()
        cursor.execute(query)
        return cursor
    
    def commit(self):
        self.connection.commit()
    
    def close(self):
        self.connection.close()

        

# 基本的な機能はOK 12/5
dbm = DbManagert()
params = {'dbms':'mysql', 'host':'localhost', 'user':'root', 'password':'root', 'db':'sql_jissen'}
connection = dbm.connect(params)
cursor = dbm.execute("SELECT * FROM Population")
rows = cursor.fetchall()
dbm.commit()
dbm.close()
print(rows)


        

    
        
