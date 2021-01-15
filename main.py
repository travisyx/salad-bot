import requests
from bs4 import BeautifulSoup

# Scrape the duckduckgo images for salad pictures
url = "https://duckduckgo.com/?q=salad&t=ffab&atb=v1-1&iar=images&iax=images&ia=images"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
temp = soup.find('img')
print(temp)

print(response.text)

