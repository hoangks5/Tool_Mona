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
            #chrome_options.add_extension('metamask.crx')
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
        try:
            #Đoạn này là lấy username
            driver.get('https://monaconft.io/profile')
            time.sleep(5000)
            text = driver.find_element_by_xpath('/html/body/div[1]/div/div/section[2]/div/div/div/div[3]/div[1]/div[5]').text
            z = open('linkclone.txt','r',encoding='utf-8').read().splitlines()
            z.append(text)
            zz = '\n'.join(z)
            w = open('linkclone.txt','w',encoding='utf-8')
            w.write(zz)
            w.close()
            #Đoạn này là đăng bài lấy link
            """ time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section[2]/div/div/div[4]/div[2]/div[1]/div/div/p').send_keys(random.choice(open('status.txt','r',encoding='utf-8').read().splitlines()))
            time.sleep(5)
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section[2]/div/div/div[4]/div[2]/div[3]/div[7]').click()
            time.sleep(5)
            driver.find_element_by_xpath('/html/body/div[1]/div/div/section[2]/div/div/div[6]/div[1]').click()      
            time.sleep(5)       
            linktt = driver.current_url
            a = open('link.txt','r',encoding='utf-8').read().splitlines()
            a.append(linktt)
            upa = '\n'.join(a)
            b = open('link.txt','w',encoding='utf-8')
            b.write(upa)
            b.close() """

            #Đoạn này là login acc
            """ f = open("vi2.txt",'r',encoding='utf-8').read().splitlines()[n]
            driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome')
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/button').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[4]/div[1]/div/input').send_keys(f)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[5]/div/input').send_keys('iamhao00')
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[6]/div/input').send_keys('iamhao00')
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[7]/div').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/button').click()
            time.sleep(5)


             try:
                driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/button').click()
                time.sleep(2)
            except:
                try:
                    driver.quit()
                finally:
                    return daluong(n)

            driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/unlock')
            time.sleep(5)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div/form/div/div/input').send_keys('iamhao00')
            driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div/form/div/div/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/button').click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/button[1]').click()
            time.sleep(1)
            driver.get('https://monaconft.io/login/wallet')
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div/div/div[2]/section/div[2]').click()
            time.sleep(2)
           
            main_page = driver.current_window_handle
            for handle in driver.window_handles:
                if handle != main_page:
                    print(handle)
                    login_page = handle
                    break
            driver.switch_to.window(login_page)
            time.sleep(1)
            try:
                driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[4]/div[2]/button[2]').click()
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
                time.sleep(5)
                for handle in driver.window_handles:
                    if handle != main_page:
                        print(handle)
                        login_page = handle
                        break
                driver.switch_to.window(login_page)
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/button[2]').click()
                time.sleep(1)
            except:
                driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/button[2]').click()
            driver.switch_to.window(main_page)
            time.sleep(2)
            input('Pass :') """
        except:
            return daluong(n) 
    except: pass
def run():
    #for i in range(0,10):
        for j in range(0,81,1):
            daluong(j)
run()