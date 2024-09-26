#Lab solutions by Samuel Paul Yila
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Cs
from selenium.webdriver.firefox.service import Service as Fs

chrome_driver_path = 'C:\\webdrivers\\chromedriver.exe'
ff_driver_path = 'C:\\webdrivers\\geckodriver.exe'

url = 'https://chatscrum.com'
url2 = 'https://www.google.com'
url3 = 'http://demo.automationtesting.in/Register.html'

#Q1.

#driver_link = Cs(chrome_driver_path)
#driver = webdriver.Chrome(service=driver_link)

#driver.get(url)
#print(driver.title)

#Q2
#driver.get(url2)
#print(driver.title)
#time.sleep(3)

#Q3
#driver.back()
#print(driver.title)
#time.sleep(3)

#Q4
#driver.forward()
#print(driver.title)
#time.sleep(3)

#driver.quit()

#Q5
#Done!

#Q6
f_driver_link = Fs(ff_driver_path)
f_driver = webdriver.Firefox(service=f_driver_link)

f_driver.get(url)
print(f_driver.title)
time.sleep(3)

f_driver.get(url2)
print(f_driver.title)
time.sleep(3)

#Q7
f_driver.get(url3)
print(f_driver.title)

#Q8
f_driver.back()
print(f_driver.title)
time.sleep(3)

f_driver.forward()
print(f_driver.title)
time.sleep(3)

#f_driver.close()
f_driver.quit()
