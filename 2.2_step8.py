from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    firstname = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    firstname.send_keys("Ivan")
    lastname = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    lastname.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    email.send_keys("a@b.c")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(os.path.dirname(__file__), end='\n')
    print(os.path.abspath(os.path.dirname(__file__)))
    file_path = os.path.join(current_dir, 'file_2.2_8.txt')
    file_element = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
finally:
    time.sleep(10)
    browser.quit()

