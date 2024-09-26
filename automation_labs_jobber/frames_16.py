#Lab 16 solution by Samuel Paul Yila

#Q1
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = 'C:\\webdrivers\\chromedriver.exe'

url = 'https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html'

driver_link = Service(chrome_driver_path)
driver = webdriver.Chrome(service=driver_link)

driver.get(url)
print(driver.title)
driver.maximize_window()

#Q2
#driver.find_element(By.LINK_TEXT, 'org.openqa.selenium.cli').click()
#time.sleep(3)

#Q3
#NoSuchElementException returned

#Q4
first_container_frame_name = 'packageListFrame'

#Q5
driver.switch_to.frame(first_container_frame_name)
driver.find_element(By.LINK_TEXT, 'org.openqa.selenium.cli').click()
time.sleep(3)

#Q6
#driver.switch_to.frame('')
#driver.switch_to.default_content() ##default content not working so i used the back() call.
#time.sleep(3)
driver.back()

second_container_frame_name = 'packageFrame'

#Q7
driver.switch_to.frame(second_container_frame_name)
driver.find_element(By.LINK_TEXT, 'AjaxElementLocator').click()
time.sleep(3)

driver.switch_to.default_content()

#Q8
print('Code run successfully')
time.sleep(3)
driver.quit()
