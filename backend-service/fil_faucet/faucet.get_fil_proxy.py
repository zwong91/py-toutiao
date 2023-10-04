# -*- coding: utf-8 -*-

import os
import sys
import json
import re
import subprocess
from time import sleep
from pathlib import Path
from random import random, choice
from datetime import datetime, date, timezone, timedelta
from time import time

# need to pip install
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent

def initializeDriver(proxy):

    tz_cst = timezone(timedelta(hours=8))

    print('START: {}'.format(datetime.now(tz_cst).isoformat(timespec='seconds')))
    # set virtual display via Xvfb
    #print('Setting virtual window ...')
    display = Display(visible=0, size=(1024, 768))
    display.start()
    #print('window start!')
    # set options
    #print('reading options ...')

    ua = fake_useragent.UserAgent()

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--user-agent=%s' % ua.random)
    options.add_argument("--proxy-server=http://{}".format(proxy))
    options.add_argument('--disable-infobars')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-extensions")
    options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--user-data-dir=/server/profile')
    # options.add_argument("--profile-directory='{}'".format('Profile 2'))
    # print('Options done!')

    # set webdriver
    print('Setting webDriver ...')
    #s = Service('/snap/bin/chromium.chromedriver')
    s = Service('./chromium.chromedriver')
    driver = webdriver.Chrome(service=s, options=options)
    driver.set_window_size(1024, 768)  # for Virtualdisplay
    driver.delete_all_cookies()
    with open('./stealth.min.js') as f:
        js = f.read()
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    print('webDriver is ready!')
    return driver, display


def solveReCaptcha(driver):
    cookie_list=driver.get_cookies()
    cookies =";".join([item["name"] +":" + item["value"] +"" for item in cookie_list])
    print(cookies)
    service_key = os.environ.get('SERVICE_KEY_2CAPCHA', 'a1a50af1cc64c2b0bf69fec1db5d2564')
    google_site_key = os.environ.get('GOOGLE_SITE_KEY_CWORK', '6LeoL1saAAAAADMS0kUieXFTEIYnrLr36FQtePPm')

    url = "http://2captcha.com/in.php?key=" + service_key + "&method=userrecaptcha&googlekey=" + google_site_key + "&pageurl=" + pageurl + "&invisible=1&json=1" +"&cookies="+cookies
    resp = requests.post(url) 
    state=json.loads(resp.text).get('status')
    if state != 1: 
        quit('Service error. Error code:' + resp.text) 
    captcha_id = json.loads(resp.text).get('request')

    # Make a 15-20 seconds timeout then submit a HTTP GET request to our API URL: https://2captcha.com/res.php to get the result.
    sleep(10 * random())
    fetch_url = "http://2captcha.com/res.php?key=" + service_key + "&action=get&id=" + captcha_id + "&json=1"

    for i in range(1, 50):
        sleep(5) # wait 5 sec.
        resp = requests.get(fetch_url)
        state=json.loads(resp.text).get('status')
        if state == 1:
            print('  fetch captcha code  OK.')
            break
    #print(resp.text)
    captcha_code = json.loads(resp.text).get('request')
    #print('Google response token: ', captcha_code)

    return captcha_code


def workerService(pageurl, driver):
    # config from ENVIRONMENT
    address = os.environ.get('WALLET_ADDRESS', 't3tcnwqzq7ur6elf244e7zsagcmmknqbquq2ubknyzhnvwfo36mzcn35meb3mfiuk4jemj4mpa2cd3tgajd36a')
    driver.get(pageurl)
    sleep(10)
    print(driver.page_source)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    driver.find_element(By.NAME, value='address').send_keys(address)
    sleep(30* random())
    captcha_code = solveReCaptcha(driver)
    driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="block";')
    sleep(30)
    driver.execute_script('document.getElementById("g-recaptcha-response").innerHTML = arguments[0]', captcha_code)
    sleep(30 * random())

    sendButton = driver.find_element(By.XPATH, value='//*[@id="funds-form"]/button')
    driver.execute_script("arguments[0].click();", sendButton)
    sleep(10)
    driver.switch_to.window(driver.window_handles[-1])
    sleep(10)
    print(driver.current_url)
    print(driver.page_source)

    page_result = driver.find_element(By.XPATH, value='/html/body/pre').text
    sleep(10 * random())
    outputJSON(page_result)

    return driver

def outputJSON(result_str):
    if re.findall('bafy2bzace', result_str):
        status = 'OK'
    else:
        status = 'failure'

    tz_cst = timezone(timedelta(hours=8))

    current_dir = Path.cwd()
    # volume = os.environ.get('DATA_VOLUME_CwORK', 'logs')
    target_dir = current_dir / datetime.now(tz_cst).strftime('%Y%m%d')
    target_dir.mkdir(exist_ok=True)
    filepath = target_dir / '{}_{}.json'.format(datetime.now(tz_cst).strftime('%Y%m%d_%H%M%S'), status)

    temp_dict = {
        'service': 'faucet',
        'timestamp': datetime.now(tz_cst).isoformat(timespec='seconds'),
        'status': status,
        'content': result_str
    }

    with open(filepath, mode='w') as f:
        f.write(json.dumps(temp_dict, indent=4, ensure_ascii=False))

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


if __name__ == '__main__':
    proxy = get_proxy().get("proxy")
    print('proxy: {}'.format(proxy))
    tz_cst = timezone(timedelta(hours=8))
    print('WALLET_ADDRESS: {}'.format(os.environ.get('WALLET_ADDRESS', 'ENV is not configured!')))
    pageurl = 'https://faucet.calibration.fildev.network/funds.html'
    driver, display = initializeDriver(proxy)
    retry_count = 5
    while retry_count > 0:
        try:
            workerService(pageurl, driver)
            print('execute success.', file=sys.stderr)
            break
        except Exception as cne:
            print('CALL EXCEPTION ! : {}'.format(cne), file=sys.stderr)
            retry_count -= 1
            continue
    if retry_count <= 0:
        # 删除代理池中代理
        delete_proxy(proxy)

    try:
        driver.quit()
        display.stop()
        print('Driver has stopped.\n')
    except NameError as ne:
        print(str(ne), file=sys.stderr)