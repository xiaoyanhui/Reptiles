import requests
from lxml import etree
import os
import sys
import io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
head = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",

}


def Page_turning():
    for i in range(1, 10):
        url = "https://www.17k.com/all/book/2_0_0_0_0_0_0_0_{}.html".format(i)
        respond = requests.get(url).content.decode('utf-8')
        html = etree.HTML(respond)
        url1 = html.xpath('//table//tbody//td[3]/span/a/@href')
        for j in range(0, len(url1)):
            uu = "https:" + url1[j]
            analysis(uu)


def analysis(url):
    respond = requests.get(url).content.decode('utf-8')
    html = etree.HTML(respond)
    ur1 = html.xpath('/html/body/div[5]/div[1]/div[1]/div[1]/dl/dt/a/@href')
    for i in range(0, len(ur1)):
        htt = "https://www.17k.com"
        url_Analysis(htt + ur1[i])


def url_Analysis(url):
    respond = requests.get(url, headers=head).content.decode('utf-8')
    html = etree.HTML(respond)
    name1 = html.xpath('//div[@class="Main List"]/h1/text()')  # 获取小说名称
    url_d = html.xpath('//dl[@class="Volume"]//dd//a/@href')  # 获取小说文章链接
    vip = html.xpath('//dl[@class="Volume"]//dd//span/@class')  # 小说VIP
    name = name1[0]
    my_file = Path("./{}".format(name))
    sss = 0
    if my_file.is_dir():
        sss = 1
    else:
        os.mkdir('./{}'.format(name))
    for i in range(0, len(url_d)):
        vip1 = vip[i]
        if vip1 == "ellipsis vip":
            print('VIP文章无法获取，结束爬虫,停止的小说名称为{}'.format(name))
            break
        if sss == 1:
            break
        url1 = "https://www.17k.com"
        url_do = url1 + url_d[i]
        url_download(url_do, name)


def url_download(url2, name3):
    download = requests.get(url2, headers=head).content.decode('utf-8')
    html = etree.HTML(download)
    title = html.xpath('//div[@class="readAreaBox content"]/h1/text()')
    content = html.xpath('//div[@class="p"]//p/text()')
    ss = "?/|\><:* "
    for i in range(0, len(title)):
        title1 = title[i]
        for k in ss:
            if k in title1:
                title1 = title1.replace(k, '')
        print('正在进行中:{}'.format(title1), flush=True)
        f = open('./{}/{}.txt'.format(name3, title1), 'w', encoding='gb18030')
        for j in range(0, len(content)):
            f.write(content[j])
            f.write('\r\n')
        f.close()


if __name__ == "__main__":
    Page_turning()
