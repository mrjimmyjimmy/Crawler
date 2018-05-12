
import requests
from bs4 import BeautifulSoup



def get_one_page():
    url = 'https://www.realestate.com.au/rent/in-melbourne,+vic/list-1'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# -----------------Basic Learning
# url = 'https://www.realestate.com.au/rent/in-melbourne,+vic/list-1'
# html = get_one_page(url)
# soup = BeautifulSoup(html, "lxml")
# print(soup.title)
# print(soup.find_all('img'))
# for link in soup.find_all('img'):
#     print(link.get('src'))
# print(soup.get_text)

# ------------------Tag learning:
# soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', "lxml")
# tag = soup.b
# type(tag)
html = get_one_page()
soup = BeautifulSoup(html, 'lxml').prettify()
print(type(soup))