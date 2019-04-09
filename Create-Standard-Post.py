from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
 
def login(browser):
    #login
    browser.get("https://bntp-staging.bauerxcel.com/users/sign_in")
    un = browser.find_element_by_id("user_email")
    un.send_keys('sgriffin@bauerxcel.com')
    pw = browser.find_element_by_id("user_password")
    pw.send_keys('Scottm*g1978')
    browser.find_element_by_class_name("btn-default").click()
    # Confirm URL
    assert "https://bntp-staging.bauerxcel.com/admin/posts" in browser.current_url, "Login Failed"
   
   
# time.sleep(2)


def select_magazine(browser):
    # Select a Magazine
    browser.find_element_by_class_name("btn-group").click()
    time.sleep(1)
    browser.find_element_by_link_text("First for Women").click()
    assert browser.current_url == "https://bntp-staging.bauerxcel.com/admin/posts/new?magazine_id=10", "QA FAIL"
    


def create_article(browser):
    # Creates the main components of a Standard Article
    HL = browser.find_element_by_name("post[title]")
    HL.send_keys("Test Headline - SG - Automated Test")
    time.sleep(1)
    # Create the Meta title
    MT = browser.find_element_by_id("post_seo_title")
    MT.send_keys("Meta Title Test 1")
    time.sleep(1)
    MD = browser.find_element_by_id("post_seo_description")
    MD.send_keys("Meta Description")
    time.sleep(1)
    # Create WYSIWYG text
    wys = browser.find_element_by_class_name("public-DraftEditor-content")
    wys.send_keys("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum""")
    # Create Social Media Headline
    SMH = browser.find_element_by_id("post_off_site_promo_title")
    SMH.send_keys("Social Media Headline Test 1")
    time.sleep(1)
    # Create Social Media Promotional Copy
    SMP = browser.find_element_by_id("post_off_site_promo_description")
    SMP.send_keys("Social Media Promotional Copy Test 1")

def insert_image(browser):
    #img_uploader = browser.find_element_by_link_text("select image").click()
    image_field = browser.find_element_by_name("post[image]")
    image_field.send_keys('/Users/sgriffin/Downloads/50910008-1 (dragged).tiff')
    # print(image_field)

# time.sleep(5)

def save_post(browser):
    # Save Post
    browser.find_element_by_class_name("btn-default").click()
    time.sleep(5)

def publish_post(browser):
    # Publish Post
    browser.find_element_by_link_text("Publish Now").click()
    browser.find_element_by_class_name("btn-preview-desktop").click()

# test functions

def logintest():
    browser = webdriver.Chrome()
    login(browser) 

def magazine_selection():
    browser = webdriver.Chrome()
    login(browser)
    select_magazine(browser)

def write_article():  # without saving article
    browser = webdriver.Chrome()
    login(browser)
    select_magazine(browser)
    create_article(browser)
    
def save_article():  # saving without publishing article
    browser = webdriver.Chrome()
    login(browser)
    select_magazine(browser)
    create_article(browser)
    save_post(browser)

def publish_article_no_image():  # save & publish article without an image
    browser = webdriver.Chrome()
    login(browser)
    select_magazine(browser)
    create_article(browser)
    save_post(browser) 
    publish_post(browser)

def publish_article():  # save & publish article with an image
    browser = webdriver.Chrome()
    login(browser)
    select_magazine(browser)
    create_article(browser)
    insert_image(browser)
    save_post(browser) 
    publish_post(browser)


#Run Test - Toggle between these test to run them

#logintest()
#magazine_selection()
#write_article()
#save_article()
#publish_article_no_image()
publish_article()