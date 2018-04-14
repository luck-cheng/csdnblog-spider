# coding=UTF-8
import logging
import random
import time

import requests
from lxml import etree

aListUrl = 'https://blog.csdn.net/qq_20032995/article/list/'


# 遍历item的方法 无返回值
def itemListFunc(html):
    articleHrefList = html.xpath('//span[@class="link_title"]/a/@href')
    for articleHrefItem in articleHrefList:
        randomInt = random.randint(5, 120)
        time.sleep(randomInt)
        itemRes = requests.get(articleHrefItem)
        itemHTML = etree.HTML(itemRes.text)
        logging.info('start tilte: ' + itemHTML.xpath('//span[@class="link_title"]/a/text()')[0])


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='BlogByRequest.log',
                        filemode='w')
    # 获取了当前时间的年月日
    now = time.strftime('%Y%m%d%H')
    while now != '2018040118':
        for n in range(1, 7):
            response = requests.get(aListUrl + str(n))
            html = etree.HTML(response.text)
            logging.info('start page: ' + str(n))
            itemListFunc(html)
