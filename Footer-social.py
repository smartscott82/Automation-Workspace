from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# lets see if this github workflow makes sense
# not that hard


browser = webdriver.Chrome()
browser.get("http://closerweekly.com.bntp-staging.bauerxcel.com/")

# Scrolls to bottom of the page with X + Y Coordinates sg
# browser.execute_script("window.scrollTo(0, 3080)")

# Scrolls to bottom of the page using body/document scroll Height
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
nav_list_social_links = browser.find_element_by_class_name('nav-list-social-links')
print(nav_list_social_links)
nav_lis = nav_list_social_links.find_elements_by_css_selector("li.nav-link")
print(nav_lis)
print(len(nav_lis))
#
# first_li = nav_links[0]
# first_a = first_li.find_element_by_tag_name('a')
# print(first_a.get_attribute("href"))

official_social_links = ['https://www.facebook.com/closerweekly',
    'https://twitter.com/closerweekly',
    'https://www.pinterest.com/closerweekly/',
    'https://www.instagram.com/closerweekly']


# appending to a list via for loop
web_links = []
for footer_li in nav_lis:
    footer_a = footer_li.find_element_by_tag_name('a')
    a_href = footer_a.get_attribute("href")
    print(a_href)
    web_links.append(a_href)

print(web_links)
print(official_social_links)


# does element exist in list?
# print error
# web_links = []
# for footer_li in nav_lis:
#     footer_a = footer_li.find_element_by_tag_name('a')
#     a_href = footer_a.get_attribute("href")
#     exists = (a_href in official_social_links)
#     if exists == False:
#         print("BIG ASS ERROR: " + a_href)
#     else:
#         print(exists)

# how many common elements?
# set intersection
web_links = []
for footer_li in nav_lis:
    footer_a = footer_li.find_element_by_tag_name('a')
    a_href = footer_a.get_attribute("href")
    web_links.append(a_href)

official_links_set = set(official_social_links)
web_links_set = set(web_links)

common_links = official_links_set.intersection(web_links_set)
print(common_links)
print(len(common_links))
