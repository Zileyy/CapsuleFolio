#IMPORTS
import tkinter as tk
import main as sdb

#FUNCTIONS
#function that creates log for GSpread
def createLog():
    q = quantity.get()
    s_p = sell_price.get()
    sdb.log(q,s_p)
    root.quit()

#[START:TKINTER_UI]
root = tk.Tk()

#VARS
quantity = tk.IntVar()
sell_price = tk.DoubleVar()

#FRAMES 
main_frame = tk.Frame(root).pack(side='top')    #Main frame
input_frame = tk.Frame(root).pack(side='top')   #Input frame for all inputs needed

#header label for title
header_label = tk.Label(main_frame , width=60, bg='lightgreen', font=('Airal' , 12) , text='AjnaDB').pack(side='top')

#Quantity text+input field 
quantity_label = tk.Label(input_frame , text='Quantity: ').pack(side='left')
quantity_entry = tk.Entry(input_frame, textvariable=quantity).pack(side='left')

#Sell price text+input field 
sell_price_label = tk.Label(input_frame , text='Sell Price: ').pack(side='left')
sell_price_entry = tk.Entry(input_frame, textvariable=sell_price).pack(side='left')

#Button used for logging input into the gsheet
log_button = tk.Button(input_frame, text='Create Log', command=createLog).pack(side='left')

root.mainloop()
#[END:TKINTER_UI]