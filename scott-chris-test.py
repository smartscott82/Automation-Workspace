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

# Specify functionality/Behavior
def navigate_to_login_page():
    browser.get("https://bntp-staging.bauerxcel.com/users/sign_in")

def assert_login_page():
    assert browser.current_url == "https://bntp-staging.bauerxcel.com/users/sign_in", "Login page URL is incorrect"


# Main Program
navigate_to_login_page()
assert_login_page()
browser.close()