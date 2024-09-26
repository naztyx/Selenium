#Lab 20 solution by Samuel Paul Yila

#Q1
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ActionChains #Q7

chrome_driver_path = 'C:\\webdrivers\\chromedriver.exe'

url = 'https://linuxjobber.com/'

driver_link = Service(chrome_driver_path)
driver = webdriver.Chrome(service=driver_link)
driver.maximize_window()

#Q2
url = 'https://demo.guru99.com/test/simple_context_menu.html'
driver.get(url)

#Q3
double_click = driver.find_element(By.XPATH, '/html/body/button')

#Q4
#actions = ActionChains(driver)

#Q5
#actions.double_click(double_click).perform()

#Q6
right_click = driver.find_element(By.XPATH, '/html/body/span')

#Q7
new_actions = ActionChains(driver)

#Q8
new_actions.context_click(right_click).perform()

time.sleep(4)
#Q9
print('code run successfully!')
driver.quit()
