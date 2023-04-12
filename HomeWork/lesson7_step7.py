from selenium import webdriver
from selenium.webdriver.common.by import By
import math
def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))
import time

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_img = browser.find_element(By.ID, "treasure")
    x = treasure_img.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()