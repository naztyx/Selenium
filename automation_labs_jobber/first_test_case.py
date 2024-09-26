# lab 22 by Samuel Paul Yila

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# Q1 and Q2
class linuxjobberTest(unittest.TestCase):

    def test_chatscrum(self):  # Q3
        chrome_driver_path = 'C:\\webdrivers\\chromedriver.exe'
        url = 'https://chatscrum.com/'
        driver_link = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=driver_link)
        driver.get(url)  # Q4
        print(driver.title)  # Q5
        driver.close()

    def test_workntutor(self):
        chrome_driver_path = 'C:\\webdrivers\\chromedriver.exe'
        url = 'http:workntutor.com'
        driver_link = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=driver_link)
        driver.get(url)
        print(driver.title)
        driver.close()


if __name__ == '__main__':  # Q10
    unittest.main()
