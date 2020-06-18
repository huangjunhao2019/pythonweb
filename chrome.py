from selenium import webdriver
import time

driver=webdriver.Chrome()

driver.get("https://www.neu.edu.cn")
time.sleep(10)
driver.quit()
