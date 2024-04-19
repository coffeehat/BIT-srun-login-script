# Create date: 2021.08.31
# Author: Sunhr
# Keep BIT-Web online

import time
import random
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions,ChromeOptions


def loopLoad(usrname,passwd,browserChoice='firefox'):
    while(1):
        if browserChoice == 'firefox':
            opts = FirefoxOptions()
            opts.add_argument("--headless")
            browser = webdriver.Firefox(options=opts)
        elif browserChoice == 'chrome':
            opts = ChromeOptions()
            opts.add_argument("--headless")
            browser = webdriver.Chrome(options=opts)
        time.sleep(1)
        
        el = lambda id : browser.find_element(By.ID, id)
        try:
            browser.get('http://10.0.0.55/')
            time.sleep(1)
            try: 
                if el("logout"):
                    print("Bit-Web still OK!")
                    browser.close()
                    time.sleep(random.randint(3,7))
                    continue
            except:
                el("username").clear()
                el("password").clear()
                el("username").send_keys(usrname)
                el("password").send_keys(passwd)
                el("login").click()
                time.sleep(2)
                print("Bit-Web OK!")
            
        except:
            browser.close()
            print("Bit-Web Failed!")
            continue

if __name__ == '__main__':
    browerDict = {'1':'firefox','2':'chrome'}
    browerIdx = input('Please choose your brower number ( 1 for Firefox; 2 for Chrome ):')
    usrname = input("Please input username: ")
    passwd = input("Please input passwd: ")

    loopLoad(usrname,passwd,browerDict[browerIdx])

    # usrname = args.usrname
    # passwd = args.passwd
    # print(usrname,passwd)



