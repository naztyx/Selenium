#Lab 17 solution by Samuel Paul Yila

#Q1
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

chrome_driver_path = 'C:\\webdrivers\\chromedriver.exe'

url = 'https://chatscrum.com'

driver_link = Service(chrome_driver_path)
driver = webdriver.Chrome(service=driver_link)

driver.get(url)
print(driver.title)
print(driver.current_window_handle)
driver.maximize_window()

#Q2
driver.execute_script('window.open('');')
time.sleep(2)

#Q3
driver.switch_to.window(driver.window_handles[1])
print(driver.current_window_handle)

#Q4
driver.get('https://linuxjobber.com/')
time.sleep(2)

#Q5
driver.execute_script('window.open('');')

#Q6
driver.switch_to.window(driver.window_handles[2])
print(driver.current_window_handle)
driver.get('https://www.google.com/')
time.sleep(2)

#Q7
driver.close()

#Q8
driver.switch_to.window(driver.window_handles[0])
driver.get('https://bing.com')
time.sleep(2)

#Q9
driver.close()

#Q10
driver.switch_to.window(driver.window_handles[0])
print(driver.title)
time.sleep(2)

#Q11
print('code execution successful')

driver.quit()
