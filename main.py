# coding=UTF-8
import random

import requests
from lxml import etree

mainHost = 'http://120.78.177.83:8050'
waitTime = '&wait='
url = mainHost + '/render.html?url=https://blog.csdn.net/qq_20032995'
aListUrl = 'https://blog.csdn.net/qq_20032995/article/list/'


# 遍历item的方法 有返回值
def itemListFuncReturn(html):
    itemListFunc(html)
    # 下一页的链接
    nextPage = html.xpath('//li[@class="page-item"][last()]/a/@href')[0]
    return nextPage


# 遍历item的方法 无返回值
def itemListFunc(html):
    articleHrefList = html.xpath('//span[@class="link_title"]/a/@href')
    for articleHrefItem in articleHrefList:
        randomInt = random.randint(5, 600)
        itemRes = requests.get(mainHost + '/render.html?url=' + articleHrefItem + waitTime + str(randomInt))


if __name__ == "__main__":
    for n in range(1, 7):
        response = requests.get(mainHost + '/render.html?url=' + aListUrl + str(n))
        html = etree.HTML(response.text)
        itemListFunc(html)
