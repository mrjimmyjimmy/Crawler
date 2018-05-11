import urllib.request
import urllib.parse
import requests
import json


# decode是一个编码格式
# mothod: get; request a page and gather it
def url_request(url):
    response = urllib.request.urlopen(url)
    print(response.read().decode('utf-8'))

# url_request('http://www.baidu.com')

def url_():
    data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding = 'utf8')
    response = urllib.request.urlopen('http://httpbin.org/post', data = data)
    print(response.read)

# request 基本用法
def request_use():
    response = requests.get('http://www.baidu.com/')
    # print(type(response))
    # print(response.status_code)
    # print(type(response.text))
    # print(response.text)
    # print(response.cookies)
    print(response.json())
