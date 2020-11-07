# -*- coding:utf-8 -*-
import requests
import time
from lxml import etree
import pymysql

db = pymysql.connect("127.0.0.1", "python", "python", "python")

cursor = db.cursor()

url = "http://news.cnstock.com/bwsd/index.html"


def start():
    text = None
    while True:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
            "Cookie": "__FTabcjffgh=2020-5-24-19-58-28; __NRUabcjffgh=1590321508818; __RTabcjffgh=2020-5-24-19-58-28; temp_uid=tp_15903215789560"
        }
        respond = requests.get(url=url, headers=headers).content.decode('utf-8')
        html = etree.HTML(respond)
        shijian = html.xpath('//ul[@id="j_waterfall_list"]//li[2]/span/text()')
        content = html.xpath('//ul[@id="j_waterfall_list"]//li[2]/p/a/text()')
        content1 = content[0]
        if content1 == text:
            print("===============没有新数据=====================")
        else:
            print(shijian[0])
            # print(content[0])
            data(shijian, content[0])
            text = content[0]
        time.sleep(60)


def data(shijian, content):
    sql = "INSERT INTO szkx(time, content) VALUES (%s, %s)"
    cursor.executemany(sql, [(shijian, content)])
    db.commit()


if __name__ == "__main__":
    start()
