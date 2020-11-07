# -*- coding:utf-8 -*-
import requests
from lxml import etree
import xlwt
import time

qq = time.strftime('%F')
f = xlwt.Workbook()
sheet1 = f.add_sheet(u'电商数据', cell_overwrite_ok=True)
rowTitle = [u'商品名称', u'价格', u'店铺名称', u'商品链接']
for i in range(0, len(rowTitle)):
    sheet1.write(0, i, rowTitle[i])

url = "https://search.jd.com/Search?keyword=py&enc=utf-8&wq=py&pvid=1d7891fe3e284effb0681c8e6bce7d7b"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    "Cookie": "shshshfpa=461da9c3-e093-1f02-6a20-aedfc5b1a43f-1571994503; shshshfpb=mtYq5Rw3noXI3BX79rC3PkQ%3D%3D; qrsc=3; TrackID=12ncGUk2wOvt39JzffubWNEEQxHH0Mepusg1AyMZSI4N4afl6Uk9PBMYuBV-jOJ4FnB-Ppm-bS8UTp8_pyEezWVBoEPuZT2BGesls_bUDnbg; pinId=juVpiyMu4cS3hFh3DRZtbLV9-x-f3wj7; __jdu=1191388469; xtest=3297.cf6b6759; areaId=20; ipLoc-djd=20-1740-1743-23075; __jdv=76161171|direct|-|none|-|1588394516882; PCSYCityID=CN_450000_450400_450422; __jdc=122270672; __jda=122270672.1191388469.1571994502.1586768328.1588394517.21; shshshfp=b5e26465745e93047c273f2ce0badb0c; rkv=V0400; shshshsID=fa2d2237980740e7fd3ddfebb3248427_6_1588394575451; __jdb=122270672.8.1191388469|21.1588394517; 3AB9D23F7A4B3C9B=M6LEC7HF5N4QHZQH5EO5KH6AQR5YNASF4ZDSAIUAEH654YBG7LCW7ZZ7DCMOH2UO3ZRYQEILGTHPNCNZZL26DU43NI; wlfstk_smdl=qfb9t9py5ds6jdl69uzvq2aivp8k0fjq"
}
k = 1
respond = requests.get(url, headers=headers).content.decode('utf-8')
html = etree.HTML(respond)
title = html.xpath('//div[@id="J_goodsList"]//div[@class="p-name p-name-type-2"]//a/@title')
price = html.xpath('//div[@id="J_goodsList"]//div[@class="p-price"]//i/text()')
Shop_name = html.xpath('//div[@id="J_goodsList"]//span[@class="J_im_icon"]//a/text()')
link = html.xpath('//div[@id="J_goodsList"]//div[@class="p-name p-name-type-2"]//a/@href')
a = [len(title), len(price), len(Shop_name), len(link)]
a.sort()

for i in range(0, a[0]):
    title1 = title[i]
    price1 = price[i]
    Shop_name1 = Shop_name[i]
    link1 = "https:"+link[i]
    sheet1.write(k, 0, title1)
    sheet1.write(k, 1, price1)
    sheet1.write(k, 2, Shop_name1)
    sheet1.write(k, 3, link1)
    k += 1
f.save('./京东{}数据.xls'.format(qq))
