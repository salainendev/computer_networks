import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Функция для поиска товаров
def search_products(driver, query):
    search_box = driver.find_element_by_name("text")  # Замените на правильный ID поля поиска на вашем сайте
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

# Функция для парсинга страницы с товарами
def parse_page(driver:webdriver.Firefox):
    parsed_products = []
    product_list = driver.find_element_by_class_name("ix") # Замените на правильный класс элемента товаров
    for product in product_list:
        # Дополнительные проверки и фильтрация товаров, чтобы оставить только мужские штаны
        # Например, поиск по ключевым словам, сравнение категорий товаров и т.д.
        
        title = product.find_element_by_class_name("product-title").text.strip()
        price = product.find_element_by_class_name("product-price").text.strip()
        link = product.find_element_by_class_name("product-link").get_attribute("href")
        parsed_products.append({'title': title, 'price': price, 'link': link})
    return parsed_products

# Функция для записи данных в CSV файл
def write_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'price', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for product in data:
            writer.writerow(product)

# Основная функция
def main():
    query = str(input("ваш запрос: "))  # Укажите ваш запрос
    num_pages = int(input("сколько страниц надо спарсить: "))  # Укажите количество страниц для парсинга
    options = webdriver.FirefoxOptions()
    options.binary_location="/snap/bin/geckodriver"
    service = webdriver.FirefoxService()
    
    # Инициализация драйвера браузера Firefox
    driver = webdriver.Firefox(options=options)# Укажите путь к драйверу Firefox
    driver.get("https://www.ozon.ru/")
    # Поиск товаров
    search_products(driver, query)

    # Парсинг страниц с товарами
    parsed_data = []
    for page_num in range(1, num_pages + 1):
        # Парсинг товаров на текущей странице
        parsed_products = parse_page(driver)
        parsed_data.extend(parsed_products)
        # Переход на следующую страницу, если есть
        next_button = driver.find_element_by_class_name("next-page")  # Замените на правильный класс кнопки перехода на следующую страницу
        if next_button and next_button.is_enabled():
            next_button.click()
            WebDriverWait(driver, 10).until(EC.staleness_of(next_button))

    # Закрыть браузер
    driver.quit()

    # Запись данных в CSV файл
    write_to_csv(parsed_data, 'products_data.csv')

if __name__ == '__main__':
    main()
