from selenium import webdriver

driver = webdriver.Chrome('/Users/slusa/PycharmProjects/kurs/chromedriver.exe')

driver.get('http://www.w3schools.com/')

target = driver.find_element_by_link_text('BROWSE TEMPLATES')

target.location_once_scrolled_into_view