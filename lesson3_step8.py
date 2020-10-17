from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    book_elem = browser.find_element_by_css_selector('#book')
    book_elem.click()
    value_elem = browser.find_element_by_css_selector('#input_value')
    answer_elem = browser.find_element_by_css_selector('#answer')
    solve_elem = browser.find_element_by_css_selector('#solve')
    answer_elem.send_keys(calc(value_elem.text))
    solve_elem.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()