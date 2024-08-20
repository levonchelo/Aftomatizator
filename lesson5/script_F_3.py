from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.maximize_window()
driver.get('http://uitestingplayground.com/classattr')

for i in range(3):
    driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()
    alert = driver.switch_to.alert
    alert.accept()
    driver.refresh()

sleep(5)
driver.quit()