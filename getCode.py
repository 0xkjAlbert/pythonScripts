import requests
import re
from lxml import etree

def getCodeAll(URL:str, xPath, headers:dict = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}):
    rsp = requests.get(url = URL, headers = headers)
    context = etree.HTML(rsp.text)
    codeList = []
    for i in range(1,1000):
        try:
            realxPath = xPath[0] + str(i) + xPath[1]
            info = context.xpath(realxPath)
            codeList.append(info[0].xpath('string(.)'))
        except IndexError:
            break
    return codeList

if __name__ == '__main__':
    xPath = str(input('Please input xpath:'))
    xPath = xPath[::-1]
    xPath = re.split(r'\d+', xPath, 1)
    for i in range(len(xPath)):
        xPath[i] = xPath[i][::-1]
    xPath.reverse()
    if xPath[0] == '':
        xPath = ["""//*[@id="content_views"]/pre[""","""]/code"""]
    if not len(xPath) == 2:
        print('xpath error.')
        exit()
    code = getCodeAll(URL = str(input('Please input URL:')), xPath = xPath)
    for i in code:
        print(i)
        while input('Press any key to continue:'):
            break
