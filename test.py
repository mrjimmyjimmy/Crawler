import requests
from bs4 import BeautifulSoup



def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

url = 'https://www.realestate.com.au/rent/in-melbourne,+vic/list-1'
html = get_one_page(url)
soup = BeautifulSoup(html, "lxml")
print(soup.title)