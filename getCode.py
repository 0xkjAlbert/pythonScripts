import requests
from lxml import etree

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
URL = str(input("Please input url:"))
rsp = requests.get(url = URL, headers = headers)
for i in range(1,60):
    try:
        xpath1 = """//*[@id="content_views"]/pre[{}]/code""".format(i)
        a = etree.HTML(rsp.text)
        info = a.xpath(xpath1)
        print(info[0].xpath('string(.)'))
        while input('Press any key to continue:'):
            break
    except IndexError:
        break
