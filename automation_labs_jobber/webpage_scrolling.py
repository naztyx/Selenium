#Lab 18 solution by Samuel Paul Yila

#Q1
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'C:\\webdrivers\\chromedriver.exe'

url = 'https://www.wikipedia.org/'

driver_link = Service(chrome_driver_path)
driver = webdriver.Chrome(service=driver_link)
driver.maximize_window()

#Q2
driver.get(url)

#Q3
input_search = driver.find_element(By.XPATH, '/html/body/div[3]/form/fieldset/div/input')
input_search.send_keys('python programming language')

#Q4
search_click = driver.find_element(By.XPATH, '/html/body/div[3]/form/fieldset/button/i')
search_click.click()

#Q5
driver.execute_script('window.scrollBy(0,3000)', '')
time.sleep(2)

#Q6
driver.execute_script('window.open('');')
driver.switch_to.window(driver.window_handles[1])
driver.get(url)

input_search = driver.find_element(By.XPATH, '/html/body/div[3]/form/fieldset/div/input')
input_search.send_keys('python programming language')
search_click = driver.find_element(By.XPATH, '/html/body/div[3]/form/fieldset/button/i')
search_click.click()

time.sleep(2)

#Q7
desc = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[5]/div[1]/table[2]/tbody/tr[1]/th[3]')
driver.execute_script('arguments[0].scrollIntoView();', desc)
time.sleep(3)

#Q8
driver.execute_script('window.open('');')
driver.switch_to.window(driver.window_handles[2])
driver.get(url)

input_search = driver.find_element(By.XPATH, '/html/body/div[3]/form/fieldset/div/input')
input_search.send_keys('python programming language')
search_click = driver.find_element(By.XPATH, '/html/body/div[3]/form/fieldset/button/i')
search_click.click()

time.sleep(2)

#Q9
driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')
time.sleep(2)

#Q10
driver.execute_script('window.open('');')
driver.switch_to.window(driver.window_handles[3])
driver.get(url)

input_search = driver.find_element(By.XPATH, '/html/body/div[3]/form/fieldset/div/input')
input_search.send_keys('python programming language')
search_click = driver.find_element(By.XPATH, '/html/body/div[3]/form/fieldset/button/i')
search_click.click()

time.sleep(2)

#Q11
html = driver.find_element(By.TAG_NAME, 'html')

#Q12
html.send_keys(Keys.END)
time.sleep(2)

driver.find_element(By.LINK_TEXT, 'web frameworks').click()
time.sleep(2)

#Q13
print('Code executions successful')
time.sleep(3)

driver.quit()
