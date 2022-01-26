from selenium import webdriver
import time
import json

driver = webdriver.Chrome(r'E:\driver\chromedriver.exe')

driver.get('https://www.linkedin.com')

time.sleep(20)

with open('cookies.txt', 'w') as f:
    f.write(json.dumps(driver.get_cookies()))

driver.close()
