#Lab solutions by Samuel Paul Yila
#Please uncomment each task to run it

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service

#Q2.
url = 'https://chatscrum.com'

#driver = webdriver.Chrome(executable_path='C:\\webdrivers\\chromedriver.exe')
driver = webdriver.Chrome(service=Service('C:\\webdrivers\\chromedriver.exe'))
driver.get(url)

#3.
sign_up = driver.find_element_by_xpath('/html/body/app-root/app-home/div[1]/nav/div/div/ul/li[2]/a/button')
sign_up.click()

#4.
email = driver.find_element_by_xpath('/html/body/app-root/app-signup/div[1]/div/div/div[1]/div/form/div[1]/div[1]/input')
password = driver.find_element_by_xpath('/html/body/app-root/app-signup/div[1]/div/div/div[1]/div/form/div[1]/div[2]/input')
full_name = driver.find_element_by_xpath('/html/body/app-root/app-signup/div[1]/div/div/div[1]/div/form/div[1]/div[3]/input')

mail_text = 'testing_selenium@gmail.com'
password_text = 'f56g45h23@B'
f_name_text = 'Testing selenium'

email.send_keys(mail_text)
password.send_keys(password_text)
full_name.send_keys(f_name_text)

#Q5.
sign_up_click = driver.find_element_by_xpath('/html/body/app-root/app-signup/div[1]/div/div/div[1]/div/form/div[2]/button')
sign_up_click.click()
time.sleep(5)

#Q6.
login = driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/nav/div/div/ul/li[1]/a/b')

#Q7.
login_email = driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[1]/input')
login_password = driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[2]/input')
login_click = driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[4]/button')

login_email.send_keys(mail_text)
login_password.send_keys(password_text)
login_click.click()

#Q8
time.sleep(5)
