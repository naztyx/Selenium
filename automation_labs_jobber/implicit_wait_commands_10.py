# lab solution by Samuel Paul Yila

# Q1
import time
from _ast import Assert

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

mail_text = 'testing_selenium@gmail.com'
password_text = 'f56g45h23@B'
f_name_text = 'Testing selenium'

chrome_driver_path = 'C:\\webdrivers\\chromedriver.exe'

url = 'https://chatscrum.com'

driver_link = Service(chrome_driver_path)
driver = webdriver.Chrome(service=driver_link)

driver.get(url)
print(driver.title)

# Q2
assert 'Scrum' in driver.title, 'Page title is not Scrum'
print('Page title is Scrum')  # this line only runs if the assert statement returns true

# Q3
login = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[1]/nav/div/div/ul/li[1]/a/b')
login.click()

# Q4
email = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[1]/input')

# Q5
email.send_keys(mail_text)

# Q6
password = driver.find_element(By.XPATH,
                               '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[2]/input')
password.send_keys(password_text)

# Q7
project = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[3]/input')
project.send_keys('testjobber')

# Q8
login_in = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[4]/button')
login_in.click()

# Q9
driver.implicitly_wait(10)

time.sleep(3)
driver.quit()
