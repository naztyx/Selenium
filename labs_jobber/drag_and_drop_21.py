#Lab 21 solution by Samuel Paul Yila

#Q1
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = 'C:\\webdrivers\\chromedriver.exe'

url = 'https://chatscrum.com/'

driver_link = Service(chrome_driver_path)
driver = webdriver.Chrome(service=driver_link)

driver.get(url)
print(driver.title)

driver.maximize_window()

mail_text = 'testing_selenium@gmail.com'
password_text = 'f56g45h23@B'
f_name_text = 'Testing selenium'

#Q2
login = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[1]/nav/div/div/ul/li[1]/a/b')
login.click()

email = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[1]/input')
email.send_keys(mail_text)

password = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[2]/input')
password.send_keys(password_text)

project = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[3]/input')
project.send_keys('new_new')

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

add_task = driver.find_element(By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[1]/button[1]')
add_task.click()

#Q4
new_task = driver.find_element(By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/form/div/button')
close_new_task = driver.find_element(By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/span[2]/span')

#Q5
text_area = driver.find_element(By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/form/textarea')
text_area.send_keys('new task')
new_task.click()

#Q6
text_area.send_keys('new_task1')
new_task.click()
time.sleep(1)

text_area.send_keys('new_task2')
new_task.click()
time.sleep(1)

text_area.send_keys('new_task3')
new_task.click()
time.sleep(1)

text_area.send_keys('new_task4')
new_task.click()
time.sleep(1)
close_new_task.click()

#Q7
first_move = ActionChains(driver)

first_task = driver.find_element(By.XPATH, '//*[contains(text(),"new_task1")]')
target = driver.find_element(By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[14]/div/div[1]/div[2]/div/div')
#first_move.drag_and_drop(first_task, target).perform()
first_move.click_and_hold(first_task).move_to_element(target).release(target).perform()
time.sleep(3)

#Q8
second_move = ActionChains(driver)
second_task = driver.find_element(By.XPATH, '//*[contains(text(),"new_task2")]')
target2 = driver.find_element(By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[14]/div/div[1]/div[2]/div/div')
second_move.click_and_hold(second_task).move_to_element(target2).release(target2).perform()
#second_move.drag_and_drop(second_task, target2).click().perform()
time.sleep(3)

third_move = ActionChains(driver)
third_task = driver.find_element(By.XPATH, '//*[contains(text(),"new_task3")]')
target3 = driver.find_element(By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[14]/div/div[1]/div[2]/div/div')
third_move.click_and_hold(third_task).move_to_element(target3).release(target3).perform()
#third_move.drag_and_drop(third_task, target3).click().perform()
time.sleep(3)

#Q9
move_to_verify = ActionChains(driver)
task_to_move = driver.find_element(By.XPATH, '//*[contains(text(),"new_task1")]')
target_verify = driver.find_element(By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[14]/div/div[1]/div[3]/div/div')
move_to_verify.click_and_hold(task_to_move).move_to_element(target_verify).release(target_verify).perform()

time.sleep(5)
print('All codes run successfully')

driver.quit()
