from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select


#opens a browser
# browser = webdriver.Chrome()
# browser.get("https://bntp-staging.bauerxcel.com/users/sign_in")

#Log into bntp

# Input email & password details + click log in button

# email = browser.find_element_by_id("user_email")
# email.send_keys("sgriffin@bauerxcel.com")
# password = browser.find_element_by_id("user_password")
# password.send_keys("Scottm*g1978")
# browser.find_element_by_class_name("btn-default").click()

# assert login page

def assert_logic(browser):
    assert browser.current_url == "https://bntp-staging.bauerxcel.com/admin/posts", "QA FAIL"

def visit_login_page(browser):
    browser.get("https://bntp-staging.bauerxcel.com/users/sign_in")

def fill_in_email(browser):
    email = browser.find_element_by_id("user_email")
    email.send_keys("sgriffin@bauerxcel.com")

def fill_in_valid_password(browser):
    password = browser.find_element_by_id("user_password")
    password.send_keys("Scottm*g1978")

def fill_in_invalid_password(browser):
    password = browser.find_element_by_id("user_password")
    password.send_keys("BADPASSWORD")

def click_login_btn(browser):
    browser.find_element_by_class_name("btn-default").click()


# scenario 1 - happy path: visit login page > fill email > password > click > success
def happy_path():
    browser = webdriver.Chrome()
    visit_login_page(browser)
    fill_in_email(browser)
    fill_in_valid_password(browser)
    click_login_btn(browser)
    assert_logic(browser)

# reset browser session

# scenario 2 - invalid password path: visit login page > fill email > incorrect password > click > success
def invalid_password_path():
    browser = webdriver.Chrome()
    visit_login_page(browser)
    fill_in_email(browser)
    fill_in_invalid_password(browser)
    click_login_btn(browser)
    assert browser.current_url == "https://bntp-staging.bauerxcel.com/users/sign_in", "QA FAIL"

happy_path()
invalid_password_path()


