# -*- coding: utf-8 -*-
import csv
import os
import mysql.connector

db_env = []
cnt  = 0
with open("db_env.csv") as f:
    for row in csv.reader(f):
        if cnt > 0 :
            db_env.append(row)
        cnt = cnt + 1
print('user:{0}, pass:{1}, host:{2}, db:{3}'.format(db_env[0][0],db_env[0][1],db_env[0][2],db_env[0][3]))
user = db_env[0][0]
password = db_env[0][1]
host = db_env[0][2]
db = db_env[0][3]

query = []
cnt  = 0
with open("query.csv") as f:
    for row in csv.reader(f):
        if cnt > 0 :
            query.append(row)
        cnt = cnt + 1
print(query[0][0])

conn = mysql.connector.connect(user=user, password=password, host=host, database=db)
cur = conn.cursor()

cur.execute(query[0][0])

'''
CSVへ出力
memo:newline無しだと、1行空行が挟まれる
'''
with open('output.csv', 'w',newline="") as f:
    writer = csv.writer(f)
    for row in cur.fetchall():
        writer.writerow(row)

cur.close
conn.close


