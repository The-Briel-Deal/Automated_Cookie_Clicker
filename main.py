from time import sleep

import selenium.common.exceptions
from selenium import webdriver
chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://orteil.dashnet.org/cookieclicker/')
big_cookie = driver.find_element_by_id('bigCookie')


def buy_product(current_cookies, product_number):
    try:

        cursor_price = int(driver.find_element_by_id(f'productPrice{product_number}').text.replace(',', ''))
        print(f'{current_cookies > cursor_price} {current_cookies} {cursor_price}')
        if current_cookies > cursor_price:
            driver.find_element_by_id(f'product{product_number}').click()
    except ValueError:
        print(f"{product_number} Does not yet exist on page")


click_counter = 0
while True:
    big_cookie.click()
    current_cookies = int(driver.find_element_by_id('cookies').text.split(' ')[0].replace(",", ""))
    if click_counter % 25 == 1:
        buy_product(current_cookies, 0)
        buy_product(current_cookies, 1)
        buy_product(current_cookies, 2)
        buy_product(current_cookies, 3)
        buy_product(current_cookies, 4)
    click_counter += 1

    # try:
    #     buy_item = driver.find_element_by_id("product0")
    #     buy_item.click()
    #
    # except selenium.common.exceptions.NoSuchElementException:
    #     print("I'm too poor )^:")


driver.quit()