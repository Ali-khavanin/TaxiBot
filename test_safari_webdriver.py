import selenium
from selenium import webdriver

driver = webdriver.Safari()

with open('resources/main_page.url','r') as test_address :
    url = test_address.read()
    driver.get(url)

