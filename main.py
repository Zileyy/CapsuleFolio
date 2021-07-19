#IMPORTS
from datetime import datetime
import api as api

#VARS
currency = 'EUR'                                    #Currency default set to EUR
buy_price = 0.2                                     #Buying price of the capsules
payload={}                                          #Payload for pushing data to the Google Sheet from pandas DF

#FUNCTIONS
#Function that makes new log on Google Spreadsheet file (quantity , sell_price)
def log(q , s_p):
    payload = {
        'Log number' : api.getNextLogNumber(),      #Number of log
        'Quantity' : q,                             #Quantity of the capusles you own
        'Date' : str(datetime.today()),             #Current date and time
        'Currency' : currency,                      #Currency default set to EUR
        'Buy price' : buy_price,                    #Price you bought capsules for
        'Sell price' : s_p,                         #Current selling price of the capsules
        'Profit per capsule' : s_p-buy_price,       #Profit per each capsule
        'Total profit' : (s_p*q) - (buy_price*q)    #Total profit for all capsules
    }
    #Attempts to add new row to Google Spreadsheet
    try:
        api.push(payload)
    #Raises exeption if error occurs
    except :
        print('Error accessing sheetDB make sure your program is setup correctly!')
        raise 
