from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Anton")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Shustov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@gmail.com")

    with open("test.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file
        path = os.getcwd() + '/' + file.name

    attach1 = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    attach1.send_keys(path)
    os.remove(path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()