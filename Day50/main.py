from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

from time import sleep

EMAIL = "elvispeureux@gmail.com"
PASSWORD = "IIMLDV"

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))
driver.get("https://tinder.com/")

sleep(2)

login = driver.find_element(By.XPATH, '//*[@id="q888578821"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()

sleep(2)

facebook = driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')
facebook.click()

sleep(2)

base_window = driver.window_handles[0]
loggin_window = driver.window_handles[1]

driver.switch_to.window(loggin_window)

# allow = driver.find_elements(By.CSS_SELECTOR, 'button')
# print(allow[0].text)

email = driver.find_element(By.ID, 'email')
email.send_keys(EMAIL)

password = driver.find_element(By.ID, 'pass')
password.send_keys(PASSWORD)

sleep(1)
password.send_keys(Keys.ENTER)

sleep(1)
driver.switch_to.window(base_window)

sleep(5)

location = driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
location.click()

sleep(1)

notification = driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
notification.click()

cookies = driver.find_element(By.XPATH, '//*[@id="q888578821"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookies.click()

#dark__theme = driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div[2]/button')
#dark__theme.click()

sleep(2)

for i in range(100):
    sleep(1)

    try:
        like = driver.find_element(By.XPATH, '//*[@id="q888578821"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button')
        like.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()