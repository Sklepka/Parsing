""" from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())
 """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from telegram.ext import ApplicationBuilder, MessageHandler, filters
from telegram import Update
import time
import re


TOKEN = '5685726029:AAHO-HHXEkUU6DcxAsdFsp_UoiTHbzdfDso11'


def parse_hh(job_title):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Включаем безоконный режим
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    browser.get("https://spb.hh.ru/?customDomain=1")

    # Искать элемент можно по id, XPATH, css_selector
    # Ищем поле ввода названия профессии
    search_input = browser.find_element(By.ID, "a11y-search-input")
    # Вводим текст в найденное поле "a11y-search-input"
    search_input.send_keys(job_title)

    # Находим кнопку поиска вакансий
    search_button = browser.find_element(
        By.CSS_SELECTOR, 'button[data-qa="search-button"]')
    search_button.click()  # Кликаем на кнопку

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

    time.sleep(5)
    browser.close
    return count

# Создаем бота
app = ApplicationBuilder().token(TOKEN).build()

async def hello(update: Update, _) :
    request = update.message.text
    await update.message.reply_text("Произвожу поиск, несколько секунд...")
    jobs_count = parse_hh(request)
    await update.message.reply_text(f'Найдено вакансий по запросу "{request}": {jobs_count}')

# Добавляем функцию hello как обработчик всех текстовых сообщений
app.add_handler(MessageHandler(filters.TEXT, hello))


# Запуск бота
app.run_polling()
