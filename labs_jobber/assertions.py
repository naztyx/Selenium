# lab 25 by Samuel Paul Yila
import time

from selenium import webdriver
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class assertions(unittest.TestCase):
    def test_assertions(self):
        dl = Service('C:\\webdrivers\\chromedriver.exe')
        self.driver = webdriver.Chrome(service=dl)

        self.driver.get('https://chatscrum.com/')
        self.driver.maximize_window()

        # Q2
        title = self.driver.title
        # assert 'Scrum' == title, 'Title of page is verified'
        #self.assertEqual('Scrum', title, 'Title of page is not same')

        # Q3
        #self.assertNotEqual('Login', title, 'Title is not the same')

        # Q4
        email_text = 'testing_selenium@gmail.com'
        password_text = 'f56g45h23@B'

        login = self.driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[1]/nav/div/div/ul/li[1]/a/b')
        login.click()

        email = self.driver.find_element(By.XPATH,
                                         '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[1]/input')
        password = self.driver.find_element(By.XPATH,
                                            '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[2]/input')
        email.send_keys(email_text)
        password.send_keys(password_text)

        project = self.driver.find_element(By.XPATH,
                                           '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[3]/input')
        project.send_keys('testjobber')

        login_in = self.driver.find_element(By.XPATH,
                                            '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[4]/button')
        login_in.click()
        time.sleep(3)

        # Q5
        taskTitle = self.driver.find_element(By.XPATH, '/html/body/app-root/app-scrumboard/div[2]/div[1]/div/nav/div/ul/li[1]/a')
        taskTitle = taskTitle.text
        #print(taskTitle.text)

        # Q6
        self.assertTrue(taskTitle == 'My Tasks')

        # Q7
        self.assertIn('Scrumboard', self.driver.title)
        #print(self.driver.title)
        # Q8
        self.assertFalse('Scrum' == self.driver.title)

        time.sleep(3)
        self.driver.quit()
