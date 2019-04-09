from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



def login(browser):
    browser.get("https://bntp-staging.bauerxcel.com/users/sign_in")
    un = browser.find_element_by_id("user_email")
    un.send_keys('sgriffin@bauerxcel.com')
    pw = browser.find_element_by_id("user_password")
    pw.send_keys('Scottm*g1978')
    browser.find_element_by_class_name("btn-default").click()
    assert "https://bntp-staging.bauerxcel.com/admin/posts" == browser.current_url, "Fail"


def select_magazine(browser):
    # Select a Magazine
    browser.find_element_by_class_name("btn-group").click()
    time.sleep(1)
    browser.find_element_by_link_text("First for Women").click()
    assert browser.current_url == "https://bntp-staging.bauerxcel.com/admin/posts/new?magazine_id=10", "QA FAIL"

def article_type(browser):
    #select recepie
    browser.find_elements_by_xpath("//*[@id=\"post-interactive\"]/main/div[1]/button[2]")[0].click()  #woah
    time.sleep(2)

def image_upload(browser):
    iup = browser.find_element_by_name("post[remote_image_url]")
    iup.send_keys("https://images-stage.freetls.fastly.net/uploads/images/file/69474/gh-josslyn.jpg?fit=crop&w=750&h=422")
    
def select_category(browser): 
    # browser.find_element_by_xpath("//*[@id=\"post-interactive\"]/main/div[5]/div/div[1]/div[1]/div/div").click()   
    # cat = browser.find_element_by_css_selector("#post-interactive > main > div._2x5kQ_NydcP5jR-LzlrqAw > div > div._30CW2FMcL-o7K7kGc3XgHB > div:nth-child(1) > div > div > div.css-1hwfws3").click()
    # category_dropdown = browser.find_element_by_xpath("//*[@id=\"post-interactive\"]/main/div[5]/div/div[1]/div[1]/div/div").send_keys("Snacks")
    dropdown_label = browser.find_element_by_xpath("//*[contains(text(), 'Category')]")
    dropdown = dropdown_label.find_element_by_xpath("following-sibling::div")
    dropdown.click()
    dropdown.send_keys("Snacks")
    time.sleep(2)
    # category_dropdown.send_keys("Snacks")
    # category_dropdown.send_keys(Keys.ENTER)
   
browser = webdriver.Chrome()
login(browser)
select_magazine(browser)
article_type(browser)
image_upload(browser)
select_category(browser)


