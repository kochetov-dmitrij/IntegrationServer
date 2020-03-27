#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import sys

gitlab_url = sys.argv[1]
login = sys.argv[2]
password = sys.argv[3]

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(gitlab_url + "/users/sign_in")
assert "Sign in" in driver.title
login_form = driver.find_element_by_id("user_login")
login_form.clear()
login_form.send_keys(login)
pass_form = driver.find_element_by_id("user_password")
pass_form.clear()
pass_form.send_keys(password)
button = driver.find_element_by_name("commit")
button.click()

driver.get(gitlab_url + "/admin/application_settings/network")
assert "Network" in driver.title
checkbox = driver.find_element_by_id("application_setting_allow_local_requests_from_web_hooks_and_services")
if not checkbox.get_attribute("checked"):
    checkbox.send_keys(Keys.SPACE)
    button = driver.find_element_by_id("js-outbound-settings").find_element_by_name("commit")
    button.click()

driver.close()
