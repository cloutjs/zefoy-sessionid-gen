from selenium import webdriver
from selenium.common.exceptions import TimeoutException,WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
import os

if os.path.isfile('key.txt'):
	os.remove("key.txt")
	e = open("key.txt", "w+")
else:
	e = open("key.txt", "w+")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)
browser.set_window_size(1920, 1080)
browser.get("https://zefoy.com/ ")
WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button')))
browser.set_window_position(-10000,0)
id = browser.get_cookie('PHPSESSID')
f = open('key.txt', 'a+')
f.write(id['value'])
print("Your SessionID: " + id['value'])
browser.quit()

