from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://olx.ro")

COOKIE_BUTTON_ID = "onetrust-accept-btn-handler"
time.sleep(3)
cookie_button = driver.find_element(By.ID, COOKIE_BUTTON_ID)
cookie_button.click()

input()


driver.quit()