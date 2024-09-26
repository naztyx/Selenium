# lab 24 by Samuel Paul Yila

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

flag = False
#flag = True
feature = 'Not Implemented'


# feature = 'Implemented'  # Q6


class chatscrumProductApp(unittest.TestCase):

    # @unittest.SkipTest  # Q3
    @unittest.expectedFailure  # Q8
    def test_login_func(self):
        print('login')

    @unittest.skip('signup function needs to be worked on')  # Q4
    def test_signup(self):
        print('Signup')

    if feature == 'Implemented':
        flag = True
    else:
        flag

    # @unittest.skipIf(flag, f'Flag is {str(flag)}')
    @unittest.skipUnless(flag == True, f'Flag is {str(flag)}')
    def test_drag_n_drop(self):
        print('drag and drop')

    def test_create_task(self):
        print('create task')

    def test_chat_collab(self):
        print('chat collab')
