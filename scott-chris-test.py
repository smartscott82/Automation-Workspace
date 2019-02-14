from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Navigate to Login Page
# Go to ‘https://bntp.bauerxcel.com/users/sign_in’

#Authentication - Success Login
# IF url = ‘https://bntp.bauerxcel.com/users/sign_in’
#     Locate Email Field
#        Input ‘sgriffin@bauerxcel.com’
#     Locate Password field
#        Input ‘ ******** ’
#     Locate ‘Log In’ button
# IF url = ‘https://bntp.bauerxcel.com/admin/posts’   

browser = webdriver.Chrome()

def navigate_to_login_page():
    browser.get("https://bntp-staging.bauerxcel.com/users/sign_in")


navigate_to_login_page()

def assert_login_page():
    # browser = webdriver.Chrome()
    # assert 1+2==2, "Addition Error"
    # assert browser.current_url == 
    print("********")
    print(browser.current_url)
    assert browser.current_url == "https://bntp-staging.bauerxcel.com/users/sign_in", "Login page URL is incorrect"

assert_login_page()

browser.close()