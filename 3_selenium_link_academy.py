from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.link-academy.com")


input()
MENU_CLASS = "navCrte"
menu_button = driver.find_element(By.CLASS_NAME, MENU_CLASS)
menu_button.click()