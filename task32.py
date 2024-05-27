import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Nissan_Skyline#Skyline_GT-R_M%C2%B7spec_(2001%E2%80%9302)'

page_text = requests.get(url).text
soup = BeautifulSoup(page_text, 'html.parser')
print(soup.get_text())

