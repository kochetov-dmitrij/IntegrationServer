#!/usr/bin/python3
import sys

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select

jenkins_url = sys.argv[1]
login = sys.argv[2]
password = sys.argv[3]

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(jenkins_url + "/login")
assert "Sign in" in driver.title
login_form = driver.find_element_by_name("j_username")
login_form.clear()
login_form.send_keys(login)
pass_form = driver.find_element_by_name("j_password")
pass_form.clear()
pass_form.send_keys(password)
button = driver.find_element_by_name("Submit")
button.click()

driver.get(jenkins_url + "/configure")
assert "Configure System" in driver.title

# delete header, it blocks click()
header = driver.find_element_by_id("breadcrumbBar")
driver.execute_script("var element = arguments[0]; element.parentNode.removeChild(element);", header)

block = driver.find_element_by_xpath("//td[text()='GitLab connections']/..//div[@name='connections']//tbody")

connection_name = block.find_element_by_xpath("//input[@name='_.numExecutors']")
connection_name.clear()
connection_name.send_keys("7")

apply_btn = block.find_element_by_xpath("//button[text()='Apply']")
apply_btn.click()

driver.close()
