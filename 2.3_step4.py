from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
finally:
    time.sleep(15)
    browser.quit()



