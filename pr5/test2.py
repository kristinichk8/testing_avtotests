from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

browser=webdriver. Chrome()

browser.get('http://localhost:3000/')
time.sleep(1)

button=browser.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[1]/div[5]/a') 
button.click() 
time.sleep(5)
email=browser.find_element(by=By.XPATH, value='//*[@id="E_mail"]') 
email.send_keys(' aobywa@mailto.plus ')
time.sleep(1)
email=browser.find_element(by=By.XPATH, value='//*[@id="Password"]') 
email.send_keys('qazxsw12')
time.sleep(1)
button=browser.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div/form/button')
button.click()
time.sleep(5)

try:
    assert 'Добро пожаловать в наш интернет-магазин!' in browser.title
    assert "aobyw" in browser.page_source
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')