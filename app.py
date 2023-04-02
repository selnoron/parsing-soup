import requests
from bs4 import BeautifulSoup

url = "https://www.putevka.com/hotels/russia/moskva?sort=1&id_resort=2395&date=07.04.2023&date_to=14.04.2023&adl=2&chd=0"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

hotels = soup.find_all("a", class_="product-title__link")
prices = soup.find_all("span", class_="found-price")

names: list[str] = []
pricess: list[str] = []

for hotel in hotels[:10]:
    names.append(hotel.text.strip())
for price in prices[:10]:
    pricess.append(price.text.strip())
    
for i in range(len(names)):
    print(f'name - {names[i]}\nprice - {pricess[i]} rub\n---------------------')
    
