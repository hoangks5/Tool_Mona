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
        ip = open('proxy.txt','r',encoding='utf-8').read().splitlines()[n]
        PROXY_HOST = ip.split(':')[0]
        PROXY_PORT = int(ip.split(':')[1])
        PROXY_USER = ip.split(':')[2]
        PROXY_PASS = ip.split(':')[3]
        def get_chromedriver(use_proxy=False, user_agent=None):
            path = os.path.dirname(os.path.abspath(__file__))
            chrome_options = webdriver.ChromeOptions()
            if use_proxy:
                pluginfile = 'proxy_auth_plugin.zip'
                with zipfile.ZipFile(pluginfile, 'w') as zp:
                    zp.writestr("manifest.json", manifest_json)
                    zp.writestr("background.js", background_js)
                chrome_options.add_extension(pluginfile)
                chrome_options.add_argument("--user-data-dir=C:/Users/StarGear/AppData/Local/Google/Chrome/User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
                chrome_options.add_argument("""--profile-directory=Profile """+str(n+1)) #e.g. Profile 3



            if user_agent:
                chrome_options.add_argument('--user-agent=%s' % user_agent)
            chrome_options.add_extension('metamask.crx')
            driver = webdriver.Chrome(
                os.path.join(path, 'chromedriver'),
                chrome_options=chrome_options)
            return driver
        manifest_json = """
                {
                    "version": "1.0.0",
                    "manifest_version": 2,
                    "name": "Chrome Proxy",
                    "permissions": [
                        "proxy",
                        "tabs",
                        "unlimitedStorage",
                        "storage",
                        "<all_urls>",
                        "webRequest",
                        "webRequestBlocking"
                    ],
                    "background": {
                        "scripts": ["background.js"]
                    },
                    "minimum_chrome_version":"22.0.0"
                }
                """

        background_js = """
                var config = {
                        mode: "fixed_servers",
                        rules: {
                        singleProxy: {
                            scheme: "http",
                            host: "%s",
                            port: parseInt(%s)
                        },
                        bypassList: ["localhost"]
                        }
                    };

                chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

                function callbackFn(details) {
                    return {
                        authCredentials: {
                            username: "%s",
                            password: "%s"
                        }
                    };
                }

                chrome.webRequest.onAuthRequired.addListener(
                            callbackFn,
                            {urls: ["<all_urls>"]},
                            ['blocking']
                );
                """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

        driver = get_chromedriver(use_proxy=True)
        driver.get('https://whoer.net')
        time.sleep(1)
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
        time.sleep(1)
        input('ok')
    except: pass
def run():
        for j in range(0,50,1):
            daluong(j)
            
run()