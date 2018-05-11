from bs4 import BeautifulSoup

html = 'asb'
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
