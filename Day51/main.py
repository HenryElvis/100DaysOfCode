from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

from time import sleep

USERNAME = "@python12983740"
PASSWORD = "pythontwitter"

PROMISED_DOWN = 150
PROMISED_UP = 10

class InternetSpeedTwitterBot:
    
    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("detach", True)
        
        self.driver = webdriver.Chrome(options=self.option, service=Service(ChromeDriverManager().install()))
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        sleep(0.5)

        accept_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_button.click()

        sleep(0.5)

        go_button = self.driver.find_element(By.CSS_SELECTOR, '.start-button a')
        go_button.click()

        sleep(60)

        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        print(self.up, self.down)

    def tweet_at_provider(self):
        pass

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()