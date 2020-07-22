import requests
from lxml import etree

def getCodeAll(URL:str, headers:dict = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}):
    rsp = requests.get(url = URL, headers = headers)
    context = etree.HTML(rsp.text)
    codeList = []
    for i in range(1,60):
        try:
            xPath = """//*[@id="content_views"]/pre[{}]/code""".format(i)
            info = context.xpath(xPath)
            codeList.append(info[0].xpath('string(.)'))
        except IndexError:
            break
    return codeList

if __name__ == '__main__':
    code = getCodeAll(URL = str(input('Please input URL:')))
    for i in code:
        print(i)
        while input('Press any key to continue:'):
            break
