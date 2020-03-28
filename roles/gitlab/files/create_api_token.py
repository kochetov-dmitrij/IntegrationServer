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

driver.get(gitlab_url + "/profile/personal_access_tokens")
assert "Personal Access Tokens" in driver.title

active_tokens = driver.find_elements_by_xpath("//table[@class='table active-tokens']/tbody/tr/td[1]")

if 'jenkins' not in map(lambda x: x.text, active_tokens):
    pass_form = driver.find_element_by_id("personal_access_token_name")
    pass_form.clear()
    pass_form.send_keys("jenkins")
    checkbox = driver.find_element_by_id("personal_access_token_scopes_api")
    checkbox.send_keys(Keys.SPACE)

    button = driver.find_element_by_name("commit")
    button.click()

    token = driver.find_element_by_id("created-personal-access-token")
    print(token.get_attribute("value"))

driver.close()
