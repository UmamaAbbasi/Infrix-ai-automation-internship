import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")

with open("training_data.txt", "w", encoding="utf-8") as file:
    for quote in quotes:
        file.write(quote.text + "\n")

print("Data scraped successfully!")
print(f"{len(quotes)} quotes saved.")