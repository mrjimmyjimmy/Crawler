from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from pyquery import PyQuery as pq


brower = webdriver.Chrome()
wait = WebDriverWait(brower, 10)

# 获取网页
def search():
    try:
        brower.get("https://world.taobao.com")
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mq'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_PopSearch > div.sb-search > div > form > input[type="submit"]:nth-child(2)')))
        input.send_keys('美食')
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        get_product()
        return total.text
    except TimeoutException:
        return search()

def next_page(page_number):

    try:
        next_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        next_input.clear()
        next_input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))
        get_product()
    except TimeoutException:
        next_page(page_number)


def get_product():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = brower.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {

            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            # 'price': re.compile('(\d+)').search(item.find('.price').text()),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text,

        }
        print(product)



def main():
    total = search()
    total = int(re.compile('(\d+)').search(total).group(1))
    for i in range(2, total + 1):
        next_page(i)

if __name__ == '__main__':
    main()
