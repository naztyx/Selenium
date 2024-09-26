#Lab 13 solution by Samuel Paul Yila

#Q1
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait #Q7
from selenium.webdriver.support import expected_conditions as EC #Q7

mail_text = 'testing_selenium@gmail.com'
password_text = 'f56g45h23@B'
f_name_text = 'Testing selenium'

chrome_driver_path = 'C:\\webdrivers\\chromedriver.exe'

url = 'https://chatscrum.com'

driver_link = Service(chrome_driver_path)
driver = webdriver.Chrome(service=driver_link)

driver.get(url)
print(driver.title)
driver.maximize_window()

#Q2
login = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[1]/nav/div/div/ul/li[1]/a/b')
login.click()

email = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[1]/input')
email.send_keys(mail_text)

password = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[2]/input')
password.send_keys(password_text)

project = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[3]/input')
project.send_keys('testjobber')

login_in = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[4]/button')
login_in.click()

#Q3
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[3]/div/div[3]/button')))

pop_up_cancel = driver.find_element(By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[3]/div/div[3]/button')
#print(pop_up_cancel.is_displayed())
time.sleep(2)
if pop_up_cancel.is_displayed():
    pop_up_cancel.click()

mytask = driver.find_element(By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[1]/div/nav/div/ul/li[1]/a')
mytask.click()

#Q4 Inspected and copied

#Q5
add_note = driver.find_element(By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[1]/button[2]/span')
add_note.click()

#Q6
high = driver.find_element(By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[4]/div/div[1]/div[2]/form/div[2]/input[1]')
medium = driver.find_element(By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[4]/div/div[1]/div[2]/form/div[2]/input[2]')
low = driver.find_element(By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[4]/div/div[1]/div[2]/form/div[2]/input[3]')

#Q7
status = high.is_selected()
print('High button is selected:', status)
status = medium.is_selected()
print('Medium button is selected:', status)
status = low.is_selected()
print('Low button is selected:', status)

#Q8
high.click()
status = high.is_selected()
print('High button is selected:', status)

medium.click()
status = medium.is_selected()
print('Medium button is selected:', status)

low.click()
status = low.is_selected()
print('Low button is selected:', status)

time.sleep(3)
driver.quit()
