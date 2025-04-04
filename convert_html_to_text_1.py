from bs4 import BeautifulSoup
import requests

url = "https://sawtooth.splinter.dev/docs/1.2/app_developers_guide/creating_sawtooth_network.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

with open("sawtooth_network.txt", "w", encoding="utf-8") as file:
    file.write(soup.get_text())