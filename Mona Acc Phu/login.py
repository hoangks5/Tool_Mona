import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver.v2 as uc
import os
import random
import zipfile
def daluong(n):
    try:
        
        def get_chromedriver():
            path = os.path.dirname(os.path.abspath(__file__))
            chrome_options = webdriver.ChromeOptions()
            
                

            chrome_options.add_extension('metamask.crx')
            driver = webdriver.Chrome(
                os.path.join(path, 'chromedriver'),
                chrome_options=chrome_options)
            return driver
        
        driver = get_chromedriver()
        #driver.set_window_rect(x=(n%5)*1920/5,y=int(n/5)*540,width=1920/7,height=540)
        try:
            driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome')
            chld = driver.window_handles[1]
            driver.switch_to.window(chld)
            driver.close()
            chld = driver.window_handles[0]
            driver.switch_to.window(chld)
            time.sleep(1)
            try:
                driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/button').click()
            except:
                input('Loi')
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]').click()
            time.sleep(2)
            f = open("vi.txt",'r',encoding='utf-8').read().splitlines()[n]
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[4]/div[1]/div/input').send_keys(f)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[5]/div/input').send_keys('Hoang22041999')
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[6]/div/input').send_keys('Hoang22041999')
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[7]/div').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/button').click()
            time.sleep(5)
            try:
                driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/button').click()
                time.sleep(2)
            except:
                driver.quit()
            driver.get('https://monaconft.io/login/wallet')
            input('Pass: ')
            
        except:
            return daluong(n)
    except: pass
def run():
    ths = []
    for i in range(90,100,1):
        ths.append(threading.Thread(target=daluong,args={i,}))
    for th in ths:
        th.start()
        time.sleep(10)
run()