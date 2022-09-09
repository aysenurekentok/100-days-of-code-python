import requests
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com.tr/gp/product/B001MZYPTE/ref=ppx_yo_dt_b_asin_image_o02_s00?ie=UTF8&th=1"

LOOK_FOR = 120

response = requests.get(url, headers={"User-Agent": "Defined"})
web_page = BeautifulSoup(response.text, "html.parser")

span = web_page.find(name="span", class_="a-offscreen")
price = span.get_text().split("T")[0]
price_float = float(price.replace(",", "."))
print(price_float)

title = web_page.find(id="productTitle").get_text()

email = ""
password = ""

if LOOK_FOR > price_float:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email,
                            msg=f"Subject:Price Alert!!!\n\n.{title} is now {LOOK_FOR}TL.")
