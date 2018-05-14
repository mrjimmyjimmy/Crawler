from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from pyquery import PyQuery as pq

brower = webdriver.Chrome()
wait = WebDriverWait(brower, 20)

# def search():
#     brower.get('https://www.domain.com.au/rent/?ssubs=1&suburb=melbourne-vic-3000')
#     text_input = wait.until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, '#react-select-2--value > div.Select-input > input'))
#     )
#     text_input.send_keys('melbourne')
#     # submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#domain-home-content > div > div > form > div.search-box-a__search-bar > button')))
#     submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '##domain-home-content > div > div > form > div.search-box-a__search-bar > button > span > span')))
#     submit.click


def get_house(page_number):
    brower.get('https://www.domain.com.au/rent/?ssubs=1&suburb=melbourne-vic-3000&page=' + str(page_number))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.search-results__main ul.search-results__results li.search-results__listing')))
    html = brower.page_source
    doc = pq(html).text()
    print(type(doc))
    return doc

def parse_one_page(html):
    pattern = re.compile(

        '"address":{"street":"(.*?)"' +
        ',"suburb":"().*?"'

    )

    items = re.findall(pattern, html)

    for item in items:
        yield {

            'location': item[0]
        }

def gather_domain_info():
    html = get_house(1)
    result = parse_one_page(html)
    print(result)


gather_domain_info()
