from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv
import json
import os
import pyautogui as pgui

# def process_browser_log_entry(entry):
#         response = json.loads(entry['message'])['message']
#         return response

user_game = 'http://sba-netgame.dmm.com/pc/gadget/index/363073'

#csvファイル読み込み
user = []
cnt  = 0
with open("user_id_password_021-030.csv") as f:
    for row in csv.reader(f):
        if cnt > 0 :
            user.append(row)
        cnt = cnt + 1

user_num = len(user)
cnt = 1


#ログインさせるユーザのID、パスワードを表示
# for user_login_info in user:
#     print('user_id:{0}, user_password:{1}'.format(user_login_info[0],user_login_info[1]))


for user_login_info in user:
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
    # # ウィンドウハンドルを取得する
    # handle_array = driver.window_handles
    # # 一番最後のdriverに切り替える
    # driver.switch_to.window(handle_array[-1])
    driver.get('http://sba-netgame.dmm.com/pc/my/login') #対象のURL(DMM開発環境のURL)
    driver.maximize_window() #ウィンドウは最大化しておく
    
    #必要変数宣言&値格納
    user_id = user_login_info[0]
    user_password = user_login_info[1]

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
    time.sleep(1)
    #ゲームの画面に遷移
    driver.get(user_game)
    time.sleep(30)

    if cnt < user_num :
        driver.quit()
    cnt = cnt + 1
    

    
    