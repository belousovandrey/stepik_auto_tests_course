from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    button.click()


    new_window = browser.window_handles[2]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    y = calc(int(x.text))
    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
