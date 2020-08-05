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

#クエストボタンクリック
quest_btn_x = 1454
quest_btn_y = 773
pgui.click(quest_btn_x,quest_btn_y)
print('quest click')
time.sleep(5)

#クエスト一覧から女王杯(PvPバトル)を選択する
pgui.vscroll(1500)
queen_cup_btn_x = 1588
queen_cup_btn_y = 699
pgui.click(queen_cup_btn_x,queen_cup_btn_y)
print('queen cup click')
time.sleep(5)

#女王杯の画面から一番上の対戦相手を選択する
enemy_select_x = 928
enemy_select_y = 453
pgui.click(enemy_select_x,enemy_select_y)
print('select enemy click')
time.sleep(5)

#女王杯出撃画面から出撃する
sortie_btn_x = 1432
sortie_btn_y = 945
pgui.click(sortie_btn_x,sortie_btn_y)
print('sortie click')
time.sleep(95)

#画面の任意の場所をタッチして女王杯の対戦相手選択
return_x = 500
return_y = 500
pgui.click(return_x,return_y)
print('return select enemy')



