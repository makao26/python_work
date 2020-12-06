import MySQLdb
import dbmanager

class BaseModel():
    def __init__(self):
        self.dbmanager = dbmanager.DbManager()
        self.connection = None
        self.cursor = None
    
    def setConnection(self):
        params = dbmanager.readDbEnv()
        self.connection = dbm.connect(params)
    
    
