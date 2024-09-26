# Lab solutions by Samuel Paul Yila
# Please uncomment each task to run it

##Q1. Done!

##Q2. Done!

##Q3. Done!

##Q4
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

url = 'https://chatscrum.com'

##create link to downloaded driver locations
chrome_driver_path = ChromeService('C:\\webdrivers\\chromedriver.exe')

##Q5
chrome_driver = webdriver.Chrome(service=chrome_driver_path)

##Q6 (please uncomment to run the task below)
chrome_driver.get(url)
print(chrome_driver.title)
chrome_driver.close()

##Q7 (please uncomment to run this task below)
#firefox_driver_path = FirefoxService('C:\\webdrivers\\geckodriver.exe')
#firefox_driver = webdriver.Firefox(service=firefox_driver_path)
#firefox_driver.get(url)
#print(firefox_driver.title)
#firefox_driver.close()

##Q8 (please uncomment to run the task below)
#edge_driver_path = EdgeService('C:\\webdrivers\\msedgedriver.exe')
#edge_driver = webdriver.Edge(service=edge_driver_path)
#edge_driver.get(url)
#print(edge_driver.title)
#edge_driver.close()
