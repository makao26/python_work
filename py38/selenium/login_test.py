from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv
import os

#csvファイル読み込み
user = []
cnt  = 0
with open("user_id_password.csv") as f:
    for row in csv.reader(f):
        if cnt > 0 :
            user.append(row)
        cnt = cnt + 1 

#自分のID、パスワード、ゲームのリンクなので固定値
user_id = user[0][0]
user_password = user[0][1]
user_game = user[0][2]

# driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
driver.get('http://sba-netgame.dmm.com/pc/my/login') #対象のURL

#Xpathで実装
#chromeのデベロッパーツールのElementを参照し構造を下記のように記述してゆく
id = driver.find_element_by_xpath("//form[@id='rogin']/table/tbody/tr[1]/td/div[@class='input text']/input[@name='data[My][id]']")
id.send_keys(user_id)
password = driver.find_element_by_xpath("//form[@id='rogin']/table/tbody/tr[2]/td/div[@class='input password']/input[@name='data[My][password]']")
password.send_keys(user_password)

time.sleep(1)

# ログインボタンをクリック
login_button = driver.find_element_by_xpath("//form[@id='rogin']/div/div/input[1]")
login_button.click()

#ゲームの画面に遷移
driver.get(user_game)