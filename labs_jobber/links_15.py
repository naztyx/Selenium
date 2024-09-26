#Lab 15 solution by Samuel Paul Yila

#Q1
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

chrome_driver_path = 'C:\\webdrivers\\chromedriver.exe'

url = 'https://chatscrum.com'

driver_link = Service(chrome_driver_path)
driver = webdriver.Chrome(service=driver_link)

driver.get(url)
print(driver.title)
driver.maximize_window()

#Q2
links = driver.find_elements(By.TAG_NAME, 'a')

#Q3
num_of_links = len(links)
print(num_of_links)

#Q4
for link in links:
    print(link.get_attribute('href'))

#Q5
#request module installed

#Q6
for link in links:
    link = link.get_attribute('href')
#Q8
    if link is None:
        continue
    status = requests.head(link)
#Q7
    if status.status_code == 404:
        print(f'{link} link is broken')
    else:
        print(f'{link} link is not broken')

time.sleep(3)
driver.quit()
