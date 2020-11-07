# -*- coding:utf-8 -*-
from typing import List, Any

import requests
from lxml import etree
import xlwt
import time
import csv

url = "https://book.douban.com/tag/?view=type&icn=index-sorttags-all"  # 豆瓣书签
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    'Cookie': 'bid=MQnzx3Z7ywo; ll="118175"; douban-fav-remind=1; __gads=ID=fad028d58115770c:T=1574904607:S=ALNI_MYt2ol3XgJCUcxVqoP05ihAGH7m4g; _vwo_uuid_v2=D287F9C8685A8C4779FC726EE92A61465|c1d0a309a4d4e1eb5e4a256989473528; __utmz=81379588.1582783650.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); gr_user_id=2c1483a7-3918-4bca-b2e5-5327413832dc; __utmz=30149280.1588053839.7.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; viewed="6082808"; __utma=30149280.1390856595.1572184743.1588053839.1588680790.8; __utmc=30149280; __utma=81379588.1898742360.1582783650.1582783650.1588680790.2; __utmc=81379588; ap_v=0,6.0; _pk_id.100001.3ac3=f02d87185aafeeaf.1582783650.2.1588682378.1582783650.'
}
list1 = []


def classification():
    #  获取豆瓣书签的分类
    respond = requests.get(url=url, headers=headers).content.decode('utf-8')
    html = etree.HTML(respond)
    classify_html = html.xpath('//tbody//tr//td/a/@href')
    classify_name = html.xpath('//tbody//tr//td/a/text()')
    for i in range(len(classify_html)):
        http = "https://book.douban.com"
        content_data(http + classify_html[i], classify_name[i])
        list1 = []


def content_data(classify_url, classify_name):
    #   获取分类的内容
    print(classify_name + "  " + classify_url)
    respond = requests.get(url=classify_url, headers=headers).content.decode('utf-8')
    html = etree.HTML(respond)
    Title = html.xpath('//ul[@class="subject-list"]//li//h2//a/@title')  # 获取书名
    if Title is None:
        saving(data=list1, name=classify_name)
        return
    href = html.xpath('//ul[@class="subject-list"]//li//h2//a/@href')  # 获取书籍链接
    information = html.xpath('//ul[@class="subject-list"]//li//div[@class="pub"]/text()')  # 获取书籍基本信息
    score = html.xpath('//ul[@class="subject-list"]//li//span[2]/text()')  # 获取评分
    evaluate = html.xpath('//ul[@class="subject-list"]//li//span[3]/text()')
    next = html.xpath('//*[@id="subject_list"]/div[2]/span[4]/a/@href')  # 获取下一页
    next_url = "https://book.douban.com" + next[0]
    for i in range(len(Title)):
        list2 = []
        if len(information[i].replace("  ", "").split("/")) < 4:
            continue
        sm = Title[i]
        zz = information[i].replace("  ", "").split("/")[0]
        cb = information[i].replace("  ", "").split("/")[-3]
        cbn = information[i].replace("  ", "").split("/")[-2]
        dj = information[i].replace("  ", "").split("/")[-1]
        try:
            score1 = score[i].replace(" ", "")
        except IndexError:
            score1 = " "
        try:
            evaluate1 = evaluate[i].replace(" ", "")
        except IndexError:
            evaluate1 = " "
        list2.append(sm)
        list2.append(zz)
        list2.append(cb)
        list2.append(cbn)
        list2.append(dj)
        list2.append(score1)
        list2.append(evaluate1)
        list2.append(href[i])
        list1.append(list2)
    time.sleep(2)  # 暂停20s
    content_data(classify_url=next_url, classify_name=classify_name)


def saving(data, neme):
    #   数据存储
    f = xlwt.Workbook()
    sheet1 = f.add_sheet("豆瓣")
    rowTitle = [u'书名', u'作者', u'出版社', u'出版年', u'定价', u'豆瓣评分', u'评价人数', u'链接']
    for i in range(0, len(rowTitle)):
        sheet1.write(0, i, rowTitle[i])
    k = 1
    for data1 in range(len(data)):
        for i in data1:
            sheet1.write(k, i, data1[i])
    f.save('./豆瓣读书{}.xls'.format(neme))


if __name__ == "__main__":
    classification()
