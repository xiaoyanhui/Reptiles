# -*- coding:utf-8 -*-
import requests
import xlwt
import time
search = int(input('爬取页数:'))
f = xlwt.Workbook()
sheet1 = f.add_sheet('虎牙直播数据', cell_overwrite_ok=True)
rowTitle = [u'房间ID', u'房间名称', u'主播名称', u'人气']
for i in range(0, len(rowTitle)):
    sheet1.write(0, i, rowTitle[i])
w = 1
for i in range(1, search + 1):

    url = "https://m.douyu.com/api/room/list?page={}&type=".format(i)

    respond = requests.get(url).json()['data']['list']
    # time.sleep(5)
    for j in range(len(respond)):
        list1 = []
        list1.append(respond[j]['rid'])
        list1.append(respond[j]['roomName'])
        list1.append(respond[j]['nickname'])
        try:
            list1.append(respond[i]['hn'])
        except IndexError:
            continue
        for k in range(len(list1)):
            sheet1.write(w, k, list1[k])
        w += 1
f.save('./{}斗鱼直播间数据.xls'.format(time.strftime('%F')))
