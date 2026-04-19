#https://www.scrapethissite.com/pages/

from bs4 import BeautifulSoup
import requests

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    countries = soup.find_all('h3')
    for name in countries:
        name = []
    

else: 
    print("There was an issue")