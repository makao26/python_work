from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
#ドライバーロード
driver = webdriver.Chrome(executable_path='./driver/mac/chromedriver')
#ページ遷移
driver.get('https://www.google.com/')
#ページが完全にロードされるまで最大で30秒間待機
driver.set_page_load_timeout(5)
#カレントウインドウのポジション(左上隅の座標)をX座標:200,Y座標:300に設定
driver.set_window_position(0,0)
#カレントウインドウのサイズを幅:100,高さ:200に設定する
driver.set_window_size(1000,1000)

