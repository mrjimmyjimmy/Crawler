from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from pyquery import PyQuery as pq
import json






def get_house(page_number):
    brower = webdriver.Chrome()
    wait = WebDriverWait(brower, 20)
    brower.get('https://www.domain.com.au/rent/?ssubs=1&suburb=melbourne-vic-3000&page=' + str(page_number))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.search-results__main ul.search-results__results li.search-results__listing')))
    html = brower.page_source
    doc = pq(html).html()
    return doc


def parse_one_page(html):

    pattern = re.compile(

        'listingModel.*?url":"(.*?)"'
        # '.*?images":\["(.*?)"' +
        # '.*?price":"\$(.*?)"' +
        # 'brandName":"(.*?)"' +
        # '.*?agentPhoto":(.*?),' +
        # 'agentName":"(.*?)"' +
        # '.*?address":{"street":"(.*?)"' +
        # '.*?suburb":"(.*?)"' +
        # '.*?state":"(.*?)"' +
        # '.*?postcode":"(.*?)"' +
        # '.*?beds":(.*?),' +
        # '.*?baths":(.*?),' +
        # '.*?propertyType":"(.*?)"'



    )

    items = re.findall(pattern, html)

    for item in items:
        yield {

            'urlDetail': 'https://www.domain.com.au' + item[0],
            # 'houseType': item[12],
            # 'housePic': item[1],
            # 'agentPic': item[4],
            # 'agent': item[5] + ',' + item[3],
            # 'price': item[2],
            # 'location': item[6] + ',' + item[7] + ',' + item[8] + ',' + item[9],
            # 'bed': item[10],
            # 'bathroom': item[11]


        }


def gather_domain_info():

    html = get_house(1)
    print(type(html))
    print(html)
    result = parse_one_page(html)
    for item in result:

        print(item)


gather_domain_info()




