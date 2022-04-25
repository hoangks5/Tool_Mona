from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver.v2 as uc
import random
import threading
import re
import os
def daluong(n):
        f = open("vi.txt",'r',encoding='utf-8').read().splitlines()[n]
        ip = open('proxy.txt','r',encoding='utf-8').read().splitlines()[n]
        options = webdriver.ChromeOptions()
        #options.add_argument('--proxy-server='+ip)
        options.add_extension('metamask.crx')
        driver = webdriver.Chrome(chrome_options=options)
        #driver.maximize_window()
        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome')
        chld = driver.window_handles[1]
        driver.switch_to.window(chld)
        driver.close()
        chld = driver.window_handles[0]
        driver.switch_to.window(chld)
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/button').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]').click()
        time.sleep(2)
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
        time.sleep(100000)
        
def run():
    th = []
    for i in range(0,50,1):
        th.append(threading.Thread(target=daluong,args={i,}))
    for ths in th:
        ths.start()
        time.sleep(5)
run()
