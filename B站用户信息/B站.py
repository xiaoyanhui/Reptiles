import requests
import time
import xlwt


def download(n, m):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('B站用户信息', cell_overwrite_ok=True)
    rowTitle = [u'MID', u'名字', u'性别', u'头像', u'签名', u'rank', u'等级', u'生日', u'会员']
    for i in range(0, len(rowTitle)):
        sheet1.write(0, i, rowTitle[i])
    k = 1
    count = 1
    for j in range(n, m + 1):
        vip = '否'
        url = "https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp".format(j)
        respond = requests.get(url=url).json()['data']
        if respond is None:
            print("没有存在该ID:{}".format(j))
            continue
        mid = respond['mid']  # mid
        name = respond['name']  # 名字
        sex = respond['sex']  # 性别
        face = respond['face']  # 头像
        sign = respond['sign']  # 签名
        rank = respond['rank']  # rank
        level = respond['level']  # 等级
        birthday = respond['birthday']  # 生日
        fans_badge = respond['fans_badge']  # 会员
        if fans_badge:
            vip = '是'
        sheet1.write(k, 0, mid)
        sheet1.write(k, 1, name)
        sheet1.write(k, 2, sex)
        sheet1.write(k, 3, face)
        sheet1.write(k, 4, sign)
        sheet1.write(k, 5, rank)
        sheet1.write(k, 6, level)
        sheet1.write(k, 7, birthday)
        sheet1.write(k, 8, vip)
        k += 1
        count += 1
        print("正在爬取第:", k)
        if count == 100:
            print("爬取了{}暂停20S".format(k))
            time.sleep(1)
            count = 0
    print("总共爬取了:{} 个".format(k - 1))
    f.save('./{}B站用户数据.xls'.format(time.strftime('%F')))


if __name__ == "__main__":
    n = int(input("起始ID:"))
    m = int(int(input("结束ID:")))
    download(n, m)
