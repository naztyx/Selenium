# lab 23 by Samuel Paul Yila

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def setUpModule():
    print('Setting up module variables')
    email_text = 'testing_selenium@gmail.com'
    password_text = 'f56g45h23@B'
    return email_text, password_text


def tearDownModule():
    print('Tearing down module')


class RandomTestClass(unittest.TestCase):  # Q2

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service('C:\\webdrivers\\chromedriver.exe'))
        self.driver.get('https://chatscrum.com/')
        print(self.driver.title)

    @classmethod
    def setUpClass(cls):
        print('Opening Test Cases')

    @classmethod
    def tearDownClass(cls):
        print('Closing Test Cases')

    def test_login(self):
        sm = setUpModule()

        login = self.driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[1]/nav/div/div/ul/li[1]/a/b')
        login.click()

        email = self.driver.find_element(By.XPATH, '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[1]/input')
        password = self.driver.find_element(By.XPATH, '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[2]/input')
        email.send_keys(sm[0])
        password.send_keys(sm[1])

        project = self.driver.find_element(By.XPATH, '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[3]/input')
        project.send_keys('testjobber')

        login_in = self.driver.find_element(By.XPATH, '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[4]/button')
        login_in.click()

    def test_1(self):
        print('Test 1')

    def test_2(self):
        print('Test 2')

    def test_3(self):
        print('Test 3')

    def test_4(self):
        print('Test 4')

    @classmethod
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
