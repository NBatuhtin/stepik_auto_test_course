from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects2.html")
    value = str(int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text))
    print(value)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value)
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
finally:
    time.sleep(15)
    browser.quit()


