import requests
from requests.exceptions import RequestException
import re
import json


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

data = get_one_page('https://www.domain.com.au/rent/melbourne-vic-3000/?ssubs=1&page=1')
print(data)