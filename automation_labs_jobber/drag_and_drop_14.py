#Lab 14 solution by Samuel Paul Yila

#Q1 and 2
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_driver_path = 'C:\\webdrivers\\chromedriver.exe'

url = 'https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407'

driver_link = Service(chrome_driver_path)
driver = webdriver.Chrome(service=driver_link)

driver.get(url)
print(driver.title)
driver.maximize_window()

#Q3 and 4
element = driver.find_element(By.XPATH, '/html/body/form/div[2]/div[19]/select')

#Q5 and 6
select_ = Select(element)

#Q7
#select_.select_by_visible_text('Morning')
#time.sleep(2)

#Q8
#select_.deselect_by_index('2')
#time.sleep(2)

#Q9
select_.select_by_value('Radio-2')

#Q10
options = select_.options

#Q11
for option in options:
    print(option.text)

#Q12
#Code run successfully

time.sleep(3)
driver.quit()
