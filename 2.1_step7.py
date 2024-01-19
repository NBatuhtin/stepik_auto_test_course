from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/get_attribute.html")
    x_element = browser.find_element(By.CSS_SELECTOR, "img")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
finally:
    time.sleep(15)
    browser.quit()


