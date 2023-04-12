from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
 return str(math.log(abs(12*math.sin(x))))


try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    number = browser.find_element(By.ID, "input_value").text
    x = int(number)
    c = calc(x)

    browser.execute_script("window.scrollBy(0, 150)", "")

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(c)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()