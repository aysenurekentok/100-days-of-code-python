import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

zillow_search_url = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.84716973355808%2C%22east%22%3A-122.22184268359375%2C%22south%22%3A37.70334422496088%2C%22west%22%3A-122.64481631640625%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"

response = requests.get(zillow_search_url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

soup = soup.findAll("script", attrs={"type": "application/json"})
rent_search = soup[1].text
rent_search = rent_search.replace("<!--", "")
rent_search = rent_search.replace("-->", "")
rent_search = json.loads(rent_search)

addresses = []
for item in rent_search["cat1"]["searchResults"]["listResults"]:
    address = item["address"]
    addresses.append(address)

prices = []
for item in rent_search["cat1"]["searchResults"]["listResults"]:
    try:
        price = item["unformattedPrice"]
    except KeyError:
        price = item["units"][0]["price"]
    prices.append(price)

links = []
for item in rent_search["cat1"]["searchResults"]["listResults"]:
    link = item["detailUrl"]

    if "https://www.zillow.com" in link:
        pass
    else:
        link = "https://www.zillow.com" + link

    links.append(link)

service = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)

google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLScGb37QpQ8GSnYsnx9eDh9RPCkwOtN1vNmp3QplxE6Jhd7TmQ/viewform?usp=sf_link"

for item in range(len(addresses)):
    driver.get(google_form_url)

    all_inputs = driver.find_elements(By.CSS_SELECTOR, "div.Xb9hP input")
    send_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    answer1 = all_inputs[0]
    answer1.send_keys(addresses[item])
    answer2 = all_inputs[1]
    answer2.send_keys(prices[item])
    answer3 = all_inputs[2]
    answer3.send_keys(links[item])

    send_button.click()
