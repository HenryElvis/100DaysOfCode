from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))
driver.get("https://tinder.com/")

sleep(2)

login = driver.find_element(By.XPATH, '//*[@id="q888578821"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()

sleep(2)

phone_login = driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div[1]/div/div/div[3]/span/div[3]/button/div[2]/div[2]')
phone_login.click()

# google_login = driver.find_element(By.XPATH, '')
# google_login.click()