#Lab 19 solution by Samuel Paul Yila

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
driver.get(url)

login = driver.find_element(By.XPATH, '/html/body/header/div/div/div/div[2]/div[2]/a[1]')
login.click()

#Q3
email = driver.find_element(By.ID, 'formGroupExampleInput')
password = driver.find_element(By.ID, 'formGroupExampleInput2')
login = driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/div/form/div[5]/button')

#Q4
email.send_keys('linuxtestingspyils@airadding.com')
password.send_keys('linuxtestingspyils')
login.click()

#Q5
learn = driver.find_element(By.XPATH, '/html/body/header/div/div/div/div[2]/div[1]/nav/ul/li[2]/a')
learn.click()
print(learn.text)
time.sleep(5)

#Q6
automation = driver.find_element(By.XPATH, '/html/body/header/div/div/div/div[2]/div[1]/nav/ul/li[2]/div/div/div[5]/ul/li[1]/a/span')
print(automation.text)

#Q7
action = ActionChains(driver)

#Q8 and #Q9
action.move_to_element(learn).move_to_element(automation).click().perform()
time.sleep(3)

#10
##print(driver.title) # verify test automation page was clicked successfully by returning the page title
print('Code run successfully!')
driver.quit()
