from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver. Chrome()

browser.get('https: // sso-mil.ru/ ')
time.sleep(1)
button=browser.find_element(by=By.XPATH, value='//[@id="responsive-menu"]/ul/li[1]/a') 
button.click()
time.sleep(5)

button=browser.find_element(by=By.XPATH, value='//*[@id="bx_3966226736_33000"]/div[2]/div/div[2]/div[4]/div/div[2]/button')
button.click()
time.sleep(5)

button=browser.find_element(by=By.XPATH, value='// [@id="addCart"]/div/div/div/div/p/a[1]') 
button.click()
time.sleep(5)

try:
    assert "Брюки КОМБАТ тип 3. Брюки боевые с интегрированной защитой коленей" in browser.page_source
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')
