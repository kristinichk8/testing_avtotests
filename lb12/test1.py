from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

browser=webdriver. Chrome()

browser.get('https://sso-mil.ru/ ')
time.sleep(1)

button=browser.find_element(by=By.XPATH, value='//*[@id="body"]/div[3]/div/div[2]/a') 
button.click() 
time.sleep(5)

email=browser.find_element(by=By.XPATH, value='//*[@id="auth"]/div[1]/input') 
email.send_keys(' kristina.puma8@gmail.com ') 
time.sleep(1)
email=browser.find_element(by=By.XPATH, value='//*[@id="auth"]/div[2]/div/input') 
email.send_keys('qazxsw12')
time.sleep(1)
button=browser.find_element(by=By.XPATH, value='//*[@id="result_auth"]') 
button.click()
time.sleep(5)

try:
    # Проверка что пользователь находится на главной странице сайта
    assert 'ЦЕНТР ЭКИПИРОВКИ SSO-MIL.RU' in browser.title
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')