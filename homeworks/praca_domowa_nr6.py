from selenium import webdriver

import time

driver = webdriver.Chrome('/Users/slusa/PycharmProjects/kurs/chromedriver.exe')

driver.maximize_window()

driver.get('https://fabrykatestow.pl')

time.sleep(5)

search_tab = driver.find_element_by_css_selector('#menu-item-622 > a').click()

time.sleep(5)

search_button = driver.find_element_by_class_name('elementor-button-text').click()

time.sleep(5)

target = driver.find_element_by_xpath('/html/body/div/main/div/div/div/div/div/div/div/section[15]/div/div/div/div/div/div/div/h2')

target.location_once_scrolled_into_view

time.sleep(5)

driver.get_screenshot_as_file("screenshot.png")

driver.quit()