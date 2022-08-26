""" from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())
 """

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://spb.hh.ru/?customDomain=1")


# Искать элемент можно по id, XPATH, css_selector
search_input = browser.find_element(By.ID, "a11y-search-input") # Ищем поле ввода названия профессии
search_input.send_keys("QA Engineer") # Вводим текст в найденное поле "a11y-search-input"


# Находим кнопку поиска вакансий
search_button = browser.find_element(By.CSS_SELECTOR, 'button[data-qa="search-button"]')
search_button.click() # Кликаем на кнопку


""" # Находим кнопку "Нет опыта"
noExperience_button = browser.find_element(By.XPATH, ".//input[type='radio'][value='noExperience']")
noExperience_button.click()  # Кликаем на кнопку """


# Находим заголовок общего количества вакансий
# Возможно придется подождать пока загрузится страница
header = browser.find_element(By.CSS_SELECTOR, '[data-qa="vacancies-total-found"]')


# Регулярные выражения
import re
# \D - означает "все что не цифра"
# re.sub - заменить один текст на другой
count = re.sub(r"\D", "", header.text)


print(f'Найдено вакансий: {count}')

time.sleep(5)
browser.close
