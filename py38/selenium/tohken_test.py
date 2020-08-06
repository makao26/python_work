#モジュールインポート
import pyautogui as pgui
import time

#ゲーム開始ボタンクリック
#ゲーム開始ボタンの座標 (600,790)で指定 
# pythonの対話モードで 「x, y = pgui.position()」で事前に取得しておく
#※ウィンドウの位置を動かしていしまうと座標の位置が変化するので動かさないように注意する
start_btn_x = 730
start_btn_y = 780
pgui.click(start_btn_x,start_btn_y)
print('start click')
time.sleep(5)