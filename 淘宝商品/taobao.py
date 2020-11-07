# -*- coding:utf-8 -*-
import requests
import re
import json
import xlwt
import time

qq = time.strftime('%F')

wb = xlwt.Workbook()
sheet1 = wb.add_sheet(u'电商数据', cell_overwrite_ok=True)

rowTitle = [u'商品名称', u'标价', u'购买人数', u'是否包邮', u'是否天猫', u'地区', u'店名', u'链接']
for i in range(0, len(rowTitle)):
    sheet1.write(0, i, rowTitle[i])

url = "https://s.taobao.com/search?q=python&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200323&ie=utf8"

headera = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",
    "cookie": "thw=cn; cna=uqYsFueWsHkCAXALFGIg8Nh2; miid=296260061845885094; tracknick=%5Cu7EAF%5Cu5C5E%5Cu9017%5Cu6BD4%5Cu8F89; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; _cc_=WqG3DMC9EA%3D%3D; t=fde428635421766be7c60e9940606092; tfstk=b#Jh1Br9omGjsSV223jTUgN2fSmVAwVKQ+dZt5v9C+bM/5u1Dn/r59WMcx6e8R; cookie2=13f63b5486b134d5939bbbe38231f51a; v=0; _tb_token_=e6d8de31e83ee; enc=AC5P0j2ILIUIZl3QqUDKZG04%2FH7N8TDVD%2FGWZho5dasWgPskDdv1oFNQkAsUuVlhTU4rnPgKJC9BQXVyT%2FPbaQ%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=17BD6C1E5FA00A34ADBCA30A8B99F4B2; isg=BISEcv4Phg9PuTEe9qzHQNTQVQJ2nagHqGlrup4m1M8SySeTx6k0l_8rCWkRV-Bf; l=dBgtn8Xrq-REcW7SBOfNIAJBFp79rQdf1sPy7svquICPOHCp526fWZ4tA_T9CnGNnspvJ37nEPh4BqY5myCqJxpsw3k_J_voXdYh."

}
k = 1
respond = requests.get(url=url, headers=headera)
html = respond.text
data = re.findall(r'g_page_config = (.*?)g_srp_loadCss', html, re.S)[0]
respond1 = data.strip(' \n;')
respond2 = json.loads(respond1)
respond3 = respond2['mods']['itemlist']['data']['auctions']
for item in respond3:
    str1 = item['title']
    str = re.compile('<[^>]+>')
    new1 = str.sub("",str1)
    item = {
        'title': new1,
        'view_price': item['view_price'],
        'view_sales': item['view_sales'],
        'view_fee': '否' if float(item['view_fee']) else '是',
        'isTmall': '是' if item['shopcard']['isTmall'] else '否',
        'item_loc': item['item_loc'],
        'name': item['nick'],
        'detail_url': item['detail_url']
    }
    sheet1.write(k, 0, item['title'])
    sheet1.write(k, 1, item['view_price'])
    sheet1.write(k, 2, item['view_sales'])
    sheet1.write(k, 3, item['view_fee'])
    sheet1.write(k, 4, item['isTmall'])
    sheet1.write(k, 5, item['item_loc'])
    sheet1.write(k, 6, item['name'])
    sheet1.write(k, 7, item['detail_url'])
    k += 1
wb.save('./淘宝{}数据.xls'.format(qq))
