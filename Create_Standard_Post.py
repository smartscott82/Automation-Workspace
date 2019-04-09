from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class TestFoo(unittest.TestCase):
    def setUp(self):
        self.selenium = selenium('localhost', 4444, "*chrome", 'http://blackpearl/')
        self.selenium.start()

    def tearDown(self):
        self.selenium.stop()

    def test_bar(self):
        self.selenium.open("/somepage")

browser = webdriver.Chrome()
browser.get("https://bntp-staging.bauerxcel.com/users/sign_in")

# Input username details
un = browser.find_element_by_id("user_email")
un.send_keys('sgriffin@bauerxcel.com')

time.sleep(2)

# Input password details
pw = browser.find_element_by_id("user_password")
pw.send_keys('Scottm*g1978')

time.sleep(2)

# LOG IN
browser.find_element_by_class_name("btn-default").click()

# Confirm URL
assert "https://bntp-staging.bauerxcel.com/admin/posts" in browser.current_url


# Select a Magazine
browser.find_element_by_class_name("btn-group").click()
time.sleep(1)
browser.find_element_by_link_text("Closer Weekly").click()


# Create the Article Headline
HL = browser.find_element_by_id("post_title")
HL.send_keys("Test Headline - SG - Automated Test")
time.sleep(1)

# Create the Meta title
MT = browser.find_element_by_id("post_seo_title")
MT.send_keys("Meta Title Test 1")
time.sleep(1)

# Create Post Garnish
PG = browser.find_element_by_id("post_garnish")
PG.send_keys("Garnish Test 1")
time.sleep(1)

# Create the Short title
ST = browser.find_element_by_id("post_short_title")
ST.send_keys("Short Title Test 1")
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
time.sleep(4)

# Save Post
browser.find_element_by_class_name("btn-default").click()
time.sleep(5)

# Publish Post
# browser.find_element_by_link_text("Publish Now").click()
browser.find_element_by_class_name("btn-preview-desktop").click()
