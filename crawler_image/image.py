import requests


def get_page_index(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

url = 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D'
info = get_page_index(url)
print(info)