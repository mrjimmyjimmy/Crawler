from reaestate_crawler import spider


for i in range(10):
    items = (spider.main(i))
    print(items)
