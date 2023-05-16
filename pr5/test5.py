from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

browser=webdriver. Chrome()

browser.get('http://localhost:3000/')
time.sleep(1)

button=browser.find_element(by=By.XPATH, value='//"[@id="root"]/div/div[1]/div[5]/a') 
button. click() 
time.sleep(5)
button=browser.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div/div[2]/span') 
button.click() 
time.sleep(5)
button=browser.find_element(by=By.XPATH, value='//"[@id="root"]/div/div/div/form/button"') 
button.click()
time.sleep(5)

try:
    assert 'Заполните поля' in browser.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div/form/div[2]')
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')