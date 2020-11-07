# -*- coding:utf-8 -*-

import requests
import os

url = "https://pvp.qq.com/web201605/js/herolist.json"  # 获取json文件


def start_img():
    respond = requests.get(url).json()
    count = len(respond)
    for i in range(count):
        name = respond[i]['cname']  # 获取英雄名字
        number = respond[i]['ename']    # 获取英雄对应得编号
        hero_skin = respond[i]['skin_name'].split("|")  # 获取英雄得皮肤名称
        if not os.path.exists(name):    # 判断是否存在英雄得文件夹，没有则创建一个
            os.mkdir(name)
        for j in range(len(hero_skin)):
            name_img = hero_skin[j]
            re_num = j + 1
            download_img(name, number, name_img, re_num)    # 传递到下载方法中


def download_img(name, number, name_img, re_num):
    url1 = "https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg".format(number, number,
                                                                                                    re_num)
    response = requests.get(url1).content
    f = open('./{}/{}.jpg'.format(name, name_img), 'wb')
    f.write(response)
    f.close()


if __name__ == "__main__":
    start_img()
