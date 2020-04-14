#!/usr/bin/python3
import sys

from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

artifactory_url = sys.argv[1]
login = sys.argv[2]
password = sys.argv[3]

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(artifactory_url + "/ui/login/")
assert "JFrog" in driver.title
try:
    login_form = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    login_form.clear()
    login_form.send_keys(login)
except Exception as e:
    print(e)
    print("Didn't load properly ffs :#")
    exit(1)
pass_form = driver.find_element_by_name("password")
pass_form.clear()
pass_form.send_keys("password") #todo
# delete header, it blocks click()
header = driver.find_element_by_class_name("pounding-heart-container")
driver.execute_script("var element = arguments[0]; element.parentNode.removeChild(element);", header)
button = driver.find_element_by_xpath("//button[@type='submit']")
button.click()

sleep(2)
print("Welcome screen")
try:
    button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='welcome-content']//button"))
    )
    button.click()
except Exception as e:
    print(e)
    print("Didn't load properly 2 ffs :#")
    exit(1)

sleep(2)
print("Enter new pass")
pass_elements = driver.find_elements_by_xpath("//input[@type='password']")
for el in pass_elements:
    el.clear()
    el.send_keys(password)

element = driver.find_element_by_xpath("//footer/button[3]")
element.click()

sleep(2)
print("Enter url")
element = driver.find_element_by_xpath("//form[contains(@class, 'el-form--label-top')]//input")
element.clear()
element.send_keys(artifactory_url)

element = driver.find_element_by_xpath("//footer/button[3]")
element.click()

sleep(2)
print("Skip stuff")
element = driver.find_element_by_xpath("//footer/button[2]")
element.click()

sleep(2)
print("Pick default")
element = driver.find_element_by_xpath("//a[contains(@class, 'iconrepo-generic')]")
element.click()

element = driver.find_element_by_xpath("//button[contains(@class, 'el-button--primary')]")
element.click()

sleep(2)
print("Done")
element = driver.find_element_by_xpath("//button[contains(@class, 'el-button--primary')]")
element.click()

driver.close()
