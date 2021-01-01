from selenium import webdriver

import time

driver = webdriver.Chrome('/Users/slusa/PycharmProjects/kurs/chromedriver.exe')

driver.get('https://fabrykatestow.pl')

search_tab = driver.find_element_by_css_selector('#menu-item-622 > a').click()

search_button = driver.find_element_by_class_name('elementor-button-text').click()

target = driver.find_element_by_xpath('/html/body/div/main/div/div/div/div/div/div/div/section[15]/div/div/div/div/div/div/div/h2')

target.location_once_scrolled_into_view

time.sleep(10)

driver.get_screenshot_as_file("screenshot.png")

time.sleep(30)

driver.quit()