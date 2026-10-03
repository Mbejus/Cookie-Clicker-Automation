from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from time import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")
driver.implicitly_wait(10)

try:
    driver.find_element(By.CSS_SELECTOR, "#langSelect-EN").click()
    print("Language selection found")
except NoSuchElementException:
    print("Language selection not found")

time_10sec = time() + 5

while True:
    try:
        driver.find_element(By.CSS_SELECTOR, "#bigCookie").click()
    except StaleElementReferenceException:
        continue
    if time() > time_10sec:
        time_10sec = time() + 5
        #buy best item
        try:

            products= driver.find_elements(By.CSS_SELECTOR, "#products .product")

            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute("id")}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookies")
