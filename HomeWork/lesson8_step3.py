import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.ID, "num1").text
    b = browser.find_element(By.ID, "num2").text
    c = int(a) + int(b)

    select = Select (browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(c))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()