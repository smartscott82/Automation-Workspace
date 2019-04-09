from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


def login(browser):
    browser.get("https://bntp-staging-pr-2316.bauerxcel.com/users/sign_in")
    un = browser.find_element_by_id("user_email")
    un.send_keys('sgriffin@bauerxcel.com')
    pw = browser.find_element_by_id("user_password")
    pw.send_keys('Scottm*g1978')
    browser.find_element_by_class_name("btn-default").click()
    assert "https://bntp-staging-pr-2316.bauerxcel.com/admin/posts" == browser.current_url, "Fail"


def select_tab(browser):
    imp = browser.find_element_by_link_text("Import")
    imp.click()

def search(browser):
    search = browser.find_element_by_xpath("//*[@id=\"import-interactive\"]/div/div/div[1]/input")
    search.send_keys("030-layered-peanut-butter-caramel-brownies")
    time.sleep(2)
    download = browser.find_element_by_xpath("//*[@id=\"import-interactive\"]/div/div/div[2]/table/tbody/tr/td[1]/div/div/a").click() 
    time.sleep(1)
    hidden_submenu = browser.find_element_by_css_selector("#import-interactive > div > div.rendered-file-browser > div.files > table > tbody > tr > td.name > div > div > a")
    download = ActionChains(browser)
    download.move_to_element(hidden_submenu)
    download.double_click(hidden_submenu)
    download.perform()
    time.sleep(3)
    browser.find_element_by_class_name("btn-primary").click()

browser = webdriver.Chrome()
login(browser)
select_tab(browser)
search(browser)