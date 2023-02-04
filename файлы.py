import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[1]')
    input1.send_keys("Petr")
    input2 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[2]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[3]')
    input3.send_keys("Petrov@jhfjdf.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '1.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.XPATH, '//*[@id="file"]') #поиск кнопки загрузки
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()