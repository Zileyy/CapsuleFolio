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
    #Checks if sheet has no previous logs and returns 1 for first log
    if len(df_sheet) == 0: return 1
    #If it's not first log get the the last log number from counting rows and add +1
    else: return int(len(df_sheet)+1)

#Function that pushes new row to Google Spreadsheet from pandas dataframe
def push(payload):
    df_sheet = pd.DataFrame(ws.get_all_records())     
    df_sheet = df_sheet.append(payload, ignore_index=True)
    set_with_dataframe(ws, df_sheet)
    print(df_sheet)
    