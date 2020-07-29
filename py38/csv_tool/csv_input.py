'''
あるCSVファイルから特定のカラムを特定の件数取得する
'''
import csv
cnt  = 0 
col_num = 0 
col_nm = 'id'
GET_NUM = 5 
result = []
with open("data01.csv") as f:
    for row in csv.reader(f):
        if cnt == 0:
            for col in row:
                if  col == col_nm:
                    break
                col_num = col_num + 1
            print('col_num',col_num,sep='=')
        
        else:
            result.append(int(row[col_num])) #一応int型へ変換
            if cnt >= GET_NUM:
                break

        cnt = cnt + 1
print(result)


#要素の型確認
# for rst in result:
#     print(type(rst))

'''
上記スクリプトで取得したリストの順にあるCSVファイルのデータを並べ替える
'''
output_list = []
input_list = []
cnt = 0
col_num = 0 
with open("data02.csv") as f:
    for row in csv.reader(f):
        if cnt == 0:
            cols = row
            for col in row:
                if  col == col_nm:
                    break
                col_num = col_num + 1
            print('col_num',col_num,sep='=')
        else:
            input_list.append(row)
        cnt = cnt + 1

cnt = 0;      
print(input_list)

for rst in result:
    print('rst',rst,sep='=')
    if len(input_list) > 0:
        for input_row in input_list:
            print('cnt',cnt,sep='=')
            print('input_row[col_num]',input_row[col_num],sep='=')
            if rst == int(input_row[col_num]):
                output_list.append(input_row)
                break
            cnt = cnt + 1
        print('cnt',cnt,sep='=')
        del input_list[cnt]
        cnt = 0
    else:
        break
print(cols)
print(output_list)

'''
CSVへ出力
newline無しだと、1行空行が挟まれる
'''
with open('output.csv', 'w',newline="") as f:
    writer = csv.writer(f)
    writer.writerow(cols)
    for row in output_list:
        writer.writerow(row)



