#IMPORTS
import os
import json
import shutil

#VARS
pip_install = "pip3 install "               #preset command for installing dependencies with pip
pip_upgrade = "pip3 install --upgrade pip"  #preset command for updating pip

#FUNCTIONS
#Function that installs dependencies
def install():
    try:
        print('Updating your PIP...')
        os.system(pip_upgrade)
        #Opens json file
        with open('data/req.json') as f:
            #Stores Json content in data var
            data = json.load(f)
            dependencies = data['dependencies']
        #Runs pip install command for every dependency
        for dependency in dependencies:
            print('Installing : ' + dependencies[dependency])
            os.system(pip_install+str(dependencies[dependency]))
    except:
        raise('[!] Error occured make sure you are running python 3 and have python and pip in your PATH')

#Function that stores needed user info in json file (sn - sheet_name)
def storeUserInfo():
    sn = input('[?] Input your google spreadsheet name: ')
    userInfo = {'userInfo':{'sheet_name':str(sn)}}
    #Opens json file
    with open('data/user.json', 'w') as json_file:
        json.dump(userInfo, json_file)

#Function that transfers credentials for gspread
def credentialsSet():
    appdata_path = os.popen('cd %appdata% & mkdir "gspread" & cd "gspread" & cd').read()
    appdata_path = appdata_path.rstrip("\n")
    data_path = os.getcwd()
    data_path = str(data_path+'\data\credentials.json')
    shutil.move(data_path , appdata_path)

#Function that runs all modules for setup
def all():
    print('[!] Installing dependencies...')
    install()
    print('[!] Moving your credentials to appdata/roaming/gspread...')
    credentialsSet()
    storeUserInfo()

#MAIN
while True:
    os.system('cls')
    #Display user options
    print('[?] Enter 1 : first time setup')
    print('[?] Enter 2 : change google spreadsheet')
    print('[?] Enter 3 : install dependencies')
    print('[?] Enter 4 : exit')
    #User input
    inp = input(': ')
    try:
        os.system('cls')
        if inp == '1': all()
        elif inp == '2': storeUserInfo()
        elif inp == '3': install()
        elif inp == '4': exit()
    except:
        raise('[!] Invalid input... ')
        os.system('pause')
