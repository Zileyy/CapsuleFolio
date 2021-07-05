#IMPORTS
from gspread_dataframe import set_with_dataframe
import pandas as pd
import gspread
import json

#VARS
gc = gspread.oauth()                                            #Auth with google acc
#Stores data from user.json to sh (google spreadsheet name)
with open('data/user.json') as f:
            #Stores Json content in data var
            data = json.load(f)
            userInfo = data['userInfo']
            sn = userInfo['sheet_name']
            sh = gc.open(sn)                                   #Google spreadsheet name

ws = sh.get_worksheet(0)                                       #Get first worksheet
df_sheet = pd.DataFrame(ws.get_all_records())                  #Put contents of sheet to pandas dataframe

#FUNCTIONS
#Function that returns next log number
def getNextLogNumber():
    df_sheet = pd.DataFrame(ws.get_all_records())
    #Return only if value of the field contains actual number (not empty)
    if df_sheet.iloc[-1,0] != None or df_sheet.iloc[-1,0] != "":
        #Gets last row of first column which is 'Log number' and add +1 as it should be next log number
        return (df_sheet.iloc[-1,0]) + 1
    #Return int 1 if no other logs found
    else:
        return 1

#Function that pushes new row to Google Spreadsheet from pandas dataframe
def push(payload):
    df_sheet = pd.DataFrame(ws.get_all_records())     
    df_sheet = df_sheet.append(payload, ignore_index=True)
    set_with_dataframe(ws, df_sheet)
    print(df_sheet)
    