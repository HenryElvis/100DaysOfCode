from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
store = driver.find_elements(By.CSS_SELECTOR, "#store div")
store_id = [item.get_attribute("id") for item in store]

timeout = time.time() + 5
five = time.time() + 60 * 0.5

while True:
    cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        for price in all_prices:
            price_text = price.text
            if price_text != "":
                cost = int(price_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        upgrades = {}

        for n in range(len(item_prices)):
            upgrades[item_prices[n]] = store_id[n]

        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        affordable_upgrades = {}

        for cost, id in upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        most_expensive_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[most_expensive_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break