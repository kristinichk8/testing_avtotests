from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver. Chrome()

browser.get('http://localhost:3000/')
time.sleep(1)
button=browser.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[1]/div[4]/a') 
button.click()
time.sleep(5)

try:
    assert 'ассортимент' in browser.title
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')