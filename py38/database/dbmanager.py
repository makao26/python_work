# MySQL専用 (Postgresql対応も本来必須)

import MySQLdb
import traceback
import json

class DbManager():
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
    
    def rollback(self):
        self.connection.commit()
    
    def closeConnect(self):
        self.connection.rollback()

    def closeCursor(self, cursor):
        if cursor is None:
            pass
        else :
            cursor.close()
    
    def readDbEnv(self):
        json_open = open('./env.json', 'r')
        json_load = json.load(json_open)
        print(json_load)
        dbenv = json_load['dbenv']
        print(dbenv)
        return dbenv   

# 基本的な機能 OK 12/5
# dbm = DbManagert()
# params = {'dbms':'mysql', 'host':'localhost', 'user':'root', 'password':'root', 'db':'sql_jissen'}
# connection = dbm.connect(params)
# cursor = dbm.execute("SELECT * FROM Population")
# rows = cursor.fetchall()
# dbm.commit()
# dbm.close()
# print(rows)

# トランザクションサンプル  OK 12/6
# json 読み取り OK 12/6
dbm = DbManager()
# params = {'dbms':'mysql', 'host':'localhost', 'user':'root', 'password':'root', 'db':'sql_jissen'}
params = dbm.readDbEnv()
connection = dbm.connect(params)
rows = None
cursor = None
try:
    print('dsebug01')
    cursor = dbm.execute("SELECT * FROM Population")
    rows = cursor.fetchall()
    # 後処理（正常時）
    dbm.commit()
except Exception as e:
    print('dsebug02')
     # 後処理（例外時）
    traceback.print_exc()
    dbm.rollback()
finally:
    print('dsebug03')
    dbm.closeCursor(cursor)
    dbm.closeConnect()

print(rows) 