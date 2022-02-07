import threading 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
from KThread import *

count = 1

def timeout(image, save_path, driver): #timeout
    global count
    try:
        image.click()
        imgUrl = driver.find_element_by_xpath(
            '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")
        opener = urllib.request.build_opener()
        opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgUrl, save_path)
        count = count + 1
    
    except Exception:
        print('image download error')
        pass

def crawling(eng_list, search, manu):
    global count
    limit_time = 10
    for name, s_name in zip(eng_list, search):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
        elem = driver.find_element_by_name("q")
        elem.send_keys(s_name)
        elem.send_keys(Keys.RETURN)

        if not os.path.isdir('result/%s/%s' %(manu, name)):
            os.mkdir('result/%s/%s' %(manu, name))

        outpath = "result\\" + manu + "\\" + name + "\\"
        SCROLL_PAUSE_TIME = 1
        # Get scroll height
        last_height = driver.execute_script(
            "return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                try:
                    driver.find_element_by_css_selector(".mye4qd").click()
                except:
                    break
            last_height = new_height

        images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
        count = 1 + len(os.listdir('result/%s/%s' %(manu, name)))
        
        for image in images:
            outfile = ('%s_%.4d.jpg' %(name, count))
            save_path = outpath + outfile
            timer = KThread(target=timeout, args=(image, save_path, driver))
            
            try:                
                timer.start()
                start = time.time()
                while True:
                    if time.time() - start > limit_time:
                        timer.kill()
                        break
                    if not timer.is_alive():
                        break

            except Exception as e:
                print('Error occurred.')
                pass
            
        driver.close()
