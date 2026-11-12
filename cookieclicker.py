from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")
wait = WebDriverWait(driver, 30)

try:
    lan_selec = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#langSelect-EN"))
    )
    lan_selec.click()
    print("Language selection found")
except NoSuchElementException:
    print("Language selection not found")



timer = time() + 5

bigcookie = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#bigCookie"))
        )
while True:
    try:
        bigcookie.click()
    except StaleElementReferenceException:
        continue
    products= driver.find_elements(By.CSS_SELECTOR, "#products .product")
    upgrades= driver.find_elements(By.CSS_SELECTOR, "#upgrades .upgrade")
    if time() > timer:
        timer = time() + 5
        #buy best item
        try:
            best_upgrade = None
            for upgrade in reversed(upgrades):
                if "enabled" in upgrade.get_attribute("class"):
                    best_upgrade = upgrade
                    break
            if best_upgrade:
                upgrade_id = best_upgrade.get_attribute("id")
                best_upgrade.click()
                print(f"Bought upgrade: {upgrade_id}")

            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            if best_item:
                item_id = best_item.get_attribute("id")
                best_item.click()
                print(f"Bought item: {item_id}")

        except (NoSuchElementException, StaleElementReferenceException, ValueError):
            print("Couldn't find anything to buy")



