from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver. Chrome()

browser.get(' https://sso-mil.ru/ ')
time.sleep(1)

button=browser.find_element(by=By.XPATH, value='//*[@id="body"]/footer/div/div/div[6]/div/ul/li[6]/a')
button. click()
time.sleep(5)

button=browser.find_element(by=By.XPATH, value='//*[@id="bx_3218110189_58329"]') 
button.click()
time.sleep(5)

try:
    assert 'СКИДКИ ДО 20% С 1 ПО 4 ИЮЛЯ!' in browser.title
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')
