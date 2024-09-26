#lab solution by Samuel Paul Yila

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = 'C:\\webdrivers\\chromedriver.exe'

url = 'https://chatscrum.com'

#Q1
driver_link = Service(chrome_driver_path)
driver = webdriver.Chrome(service=driver_link)

driver.get(url)
print(driver.title)

#Q2
#login = driver.find_element_by_xpath('/html/body/app-root/app-home/div[1]/nav/div/div/ul/li[1]/a/b')
login = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[1]/nav/div/div/ul/li[1]/a/b')
#3
print(login.is_displayed())

#Q4
print(login.is_enabled())

#Q5
login.click()
time.sleep(3)
email_field = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[1]/input')
p_word_field = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[2]/input')

print(f'Email field is displayed: {email_field.is_displayed()}')
print(f'Password field is displayed: {p_word_field.is_displayed()}')

print(f'Email field is enabled: {email_field.is_enabled()}')
print(f'Password field is enabled: {p_word_field.is_enabled()}')

#Q6.
if email_field.is_enabled() & p_word_field.is_enabled():
    if email_field.is_displayed() & p_word_field.is_displayed():
        email_field.send_keys('email_scrum@gmail.com')
        p_word_field.send_keys('password')

        login_in = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[4]/button')
        #login_in.click()

time.sleep(3)

#Q7
url2 = 'http://demo.automationtesting.in/Register.html'
driver.get(url2)

first_name = driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/form/div[1]/div[1]/input')
print(f'first name is enabled: {first_name.is_enabled()}')
print(f'first name field is displayed: {first_name.is_displayed()}')
time.sleep(3)

#Q8
hobbies = driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/form/div[6]/div/div[1]/input')

#Q9
print(hobbies.is_selected())

#Q10
hobbies.click()
print(hobbies.is_selected())
time.sleep(3)

driver.quit()
