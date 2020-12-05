import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

print('Input SheetsId:')
sheet_id = input()

creds=None

if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('sheets', 'v4', credentials=creds)


spreadsheet_id = sheet_id 
sheetname='spreadsheet_test' 
range_ = sheetname+"!A1:B10"

# シートの作成
# requests=[]
# requests.append({
#     'addSheet':{
#         "properties":{
#             "title": sheetname,
#             "index": "0",
#             }

#         }
#     })

# body={'requests':requests}
# response=service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
# sheetid=response['replies'][0]['addSheet']['properties']['sheetId']

# #セルに文字列を入れる
# range_ = sheetname+"!A1:B10"
# v={}
# v['range']=range_
# v['majorDimension']="ROWS"
# v['values']=[
#         [1,  2],
#         [3,  4],
#         [4,  5],
#         [5,  6],
#         [6,  7],
#         [7,  8],
#         [8,  9],
#         [10, 11],
#         [12, 13],
#         ['test', 'spreadsheet_test'],
#         ]
# value_input_option = 'USER_ENTERED'
# insert_data_option='OVERWRITE'
# result = service.spreadsheets().values().update( spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=v).execute()

# #セルのフォーマットを変更する
# requests = []
# requests.append({
#     "updateBorders":{
#         "range": {
#             "sheetId": sheetid,
#             "startRowIndex": 0,
#             "endRowIndex": 1,
#             "startColumnIndex": 0,
#             "endColumnIndex": 2,
#             },
#         "bottom": {
#             "style": "SOLID",
#             "width": "1",
#             "color": { "red": 0, "green":0, "blue":0 },
#             },
#         },
#     })

# requests.append({
#     "repeatCell": {
#         "range": {
#             "sheetId": sheetid,
#             "startRowIndex": 0,
#             "endRowIndex": 1,
#             "startColumnIndex": 0,
#             "endColumnIndex": 2,
#             },
#         "cell": {
#             "userEnteredFormat": {
#                 "horizontalAlignment" : "LEFT",
#                 "textFormat": {
#                     "fontSize": 11,
#                     "bold": True,
#                     "foregroundColor": {
#                         "red": 1.0,
#                         },
#                     }
#                 }
#             },
#         "fields": "userEnteredFormat(textFormat,horizontalAlignment)"
#         },
#     })
# body = { 'requests': requests }
# response = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()


response = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_).execute()
print(response)

