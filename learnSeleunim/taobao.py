from selenium import webdriver

brower = webdriver.Chrome()


# 获取网页
def search():
    brower.get('https://www.taobao.com')
