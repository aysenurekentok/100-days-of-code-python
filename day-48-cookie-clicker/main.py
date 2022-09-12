from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import time

service = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

cookie_button = driver.find_element(By.XPATH, '//*[@id="cookie"]')

time_to_buy = time() + 5
five_min = time() + 60*5
while True:
    cookie_button.click()

    if time() > time_to_buy:

        store = driver.find_elements(By.CSS_SELECTOR, "#store b")
        store_costs = [int(item.text.split(" - ")[1].replace(",", "")) for item in store[:8]]

        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))

        for cost in store_costs:
            if money > cost:
                index = store_costs.index(cost)
        store[index].click()

        time_to_buy = time() + 5

    if time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        driver.quit()
        break
