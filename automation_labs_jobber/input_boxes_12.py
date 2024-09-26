#Lab 12 solution by Samuel Paul Yila

#Q1
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.keys import Keys
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

#Q4
add_task = driver.find_element(By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[1]/button[1]')

#Q5
add_task.click()

#Q6
task = driver.find_element(By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/form/textarea')

#Q7
status = task.is_displayed()
print('Input box displayed:', status)
status = task.is_enabled()
print('Input box is enabled:', status)

#Q8
task.send_keys('To understand input boxes using selenium python')
