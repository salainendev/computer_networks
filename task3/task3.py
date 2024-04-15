import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import csv
from time import sleep
from random import randint

# Функция для поиска товаров
def search_products(driver:webdriver.Firefox, query):
    search_box = driver.find_element(By.XPATH,"//*[@id=\"mc-horizontal-menu-collapse\"]/div/div/form/div/span[1]/input[2]")  # Замените на правильный ID поля поиска на вашем сайте
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)


# Функция для парсинга страницы с товарами
def parse_page(driver:webdriver.Firefox):
    parsed_products = []
    product_list = 0
    product_list = driver.find_element(By.XPATH,"/html/body/div[1]/section/div/div[2]/section/div/div[2]/div/div[1]/div") # Замените на правильный класс элемента товаров
    if (product_list):
        products = product_list.find_elements(By.CLASS_NAME,"product-item")
    for i in products:
        title = i.find_element(By.CLASS_NAME,"thumbnail_container").find_element(By.CLASS_NAME,"thumbnail-centered").find_element(By.TAG_NAME,"a").find_element(By.TAG_NAME,"picture").find_element(By.TAG_NAME,"img").get_attribute("alt")
        link= i.find_element(By.CLASS_NAME,"thumbnail_container").find_element(By.CLASS_NAME,"thumbnail-centered").find_element(By.TAG_NAME,"a").find_element(By.TAG_NAME,"picture").find_element(By.TAG_NAME,"img").get_attribute("src")
        source = i.find_element(By.CLASS_NAME,"thumbnail_container").find_element(By.CLASS_NAME,"thumbnail-centered").find_element(By.TAG_NAME,"a").get_attribute("href")
        price = i.find_element(By.CLASS_NAME,"prices").text
        
        parsed_products.append({'title':title,"imageLink":link,"link":source,"price":price})
    return parsed_products

# Функция для записи данных в CSV файл
def write_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'imageLink', 'link','price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for product in data:
            writer.writerow(product)

# Основная функция
def main():
    query = str(input("ваш запрос: "))  # Укажите ваш запрос
    
    
    # Инициализация драйвера браузера Firefox
    DRIVER="/snap/bin/geckodriver"
    service = Service(executable_path=DRIVER)
    options = webdriver.FirefoxOptions()
    options.add_argument('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0')

    driver = webdriver.Firefox(service=service, options=options)
    # Поиск товаров
    driver.get("https://amperkot.ru")
    sleep(randint(1,3))
    driver.refresh()
    
    search_products(driver, query)
    sleep(randint(2,4))
    parsed_data = parse_page(driver)
    # Парсинг страниц с товарами
    # parsed_data = []
    # for page_num in range(1, num_pages + 1):
    #     # Парсинг товаров на текущей странице
    #     parsed_products = parse_page(driver)
    #     parsed_data.extend(parsed_products)
    #     # Переход на следующую страницу, если есть
    #     next_button = driver.find_element_by_class_name("next-page")  # Замените на правильный класс кнопки перехода на следующую страницу
    #     if next_button and next_button.is_enabled():
    #         next_button.click()
    #         WebDriverWait(driver, 10).until(EC.staleness_of(next_button))

    # Закрыть браузер
    write_to_csv(parsed_data, 'products_data.csv')
    driver.quit()

    # Запись данных в CSV файл

if __name__ == '__main__':
    main()
