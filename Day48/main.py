from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.python.org")

search = driver.find_element("name", "q")
document_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
xpath = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/div/p/small/span[4]/a')

#print(search.get_attribute("placeholder"))
print(document_link.text)
print(xpath.text)

driver.quit()