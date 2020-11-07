import requests
from lxml import etree
import time
import xlwt

"""
使用前请更换cookie
一个cookie只能爬取两个页面
"""
f = xlwt.Workbook()
sheet1 = f.add_sheet(u'BOSS直聘信息', cell_overwrite_ok=True)
rowTitle = [u'岗位', u'薪资', u'位置', u'工作经历', u'学历', u'公司名称', u'行业', u'融资状况', u'公司人数', u'链接']

for i in range(0, len(rowTitle)):
    sheet1.write(0, i, rowTitle[i])

head = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",
    "cookie": "_bl_uid=XtkRg81bejIhyk6wky92n8stvRzw; lastCity=101210100; __c=1586231928; __g=-; __l=l=%252Fgongsi%252Ffa2f92669c66eee31Hc%257E.html&r=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253DLtIUH_tkOcPgUt0ZeRK86zKQG0TRvR3XT_3enCeNquku5SEjb-uG6sFgl_5f25_ejBzgAEoIZTNsZqhR6Tf_QpgMOdRDECN9psGpzPTDXxS%2526ck%253D4599.3.215.256.264.134.171.734%2526shh%253Dwww.baidu.com%2526sht%253Dbaidu%2526wd%253D%2526eqid%253Dfb0d4a6f0004934d000000065e8bfa71&friend_source=0&friend_source=0; __zp_seo_uuid__=718c854e-3e17-4848-9685-2673a6672a75; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1585628894,1585654128,1586231931,1586233359; __zp_stoken__=94e4OpCJi2pxxCmkfuRvmZo1DLEkOcjbW2R07wcFv2JK%2FoblXMg3xo9KBgKRwKwAIkjtX30rBi6cAiU55v4dYkZM4pAgqMD%2B6E0IgMSQHv1VbOKPBCGSUuryBGhCCxmKo9ru; __a=81728435.1582721358.1585654127.1586231928.126.7.9.126; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1586233926"

}


# 数据爬取
def data_crawling():
    k = 1
    search = input('请入搜索的职位:')
    num = int(input('请输入爬取的页数:'))
    a = 0
    for h in range(1, num + 1):
        url = "https://www.zhipin.com/c100010000/?query={}&page={}&ka=page-2".format(search, h)
        if a % 2 == 0:
            print('请打开下面的网页获取cookie输入')
            print(url)
            head['cookie'] = input('填写当前页面的cookie:')
            a = 0
        qq = time.strftime('%F')
        respond = requests.get(url=url, headers=head).content.decode('utf-8')
        html = etree.HTML(respond)
        gw = html.xpath('//div[@class="job-title"]//span//a/text()')  # 工作岗位
        dl = html.xpath('//div[@class="job-title"]//span[@class="job-area"]/text()')  # 工作位置
        xz = html.xpath('//div[@class="job-limit clearfix"]//span[@class="red"]/text()')  # 薪资
        gzjy = html.xpath('//div[@class="job-limit clearfix"]//p/text()[1]')  # 工作经历
        xl = html.xpath('//div[@class="job-limit clearfix"]//p/text()[2]')  # 学历
        gsmc = html.xpath('//div[@class="info-company"]//h3/a/text()')  # 公司名称
        hy = html.xpath('//div[@class="info-company"]//p//a/text()')  # 行业
        rzqk = html.xpath('//div[@class="info-company"]//p/text()[1]')  # 融资情况
        gsrs = html.xpath('//div[@class="info-company"]//p/text()[2]')  # 公司人数
        zplj = html.xpath('//div[@class="primary-box"]/@href')  # 招聘链接
        print(dl)
        a += 1
        time.sleep(1)
        for j in range(0, len(gw)):
            zplj1 = "https://www.zhipin.com"
            gw1 = gw[j]
            dl1 = dl[j]
            xz1 = xz[j]
            gzjy1 = gzjy[j]
            xl1 = xl[j]
            gsmc1 = gsmc[j]
            hy1 = hy[j]
            rzqk1 = rzqk[j]
            gsrs1 = gsrs[j]
            zplj1 += zplj[j]
            print(gsrs1)
            sheet1.write(k, 0, gw1)
            sheet1.write(k, 1, xz1)
            sheet1.write(k, 2, dl1)
            sheet1.write(k, 3, gzjy1)
            sheet1.write(k, 4, xl1)
            sheet1.write(k, 5, gsmc1)
            sheet1.write(k, 6, hy1)
            sheet1.write(k, 7, rzqk1)
            sheet1.write(k, 8, gsrs1)
            sheet1.write(k, 9, zplj1)
            k += 1
    f.save('./BOSS直聘{}数据.xls'.format(qq))


if __name__ == "__main__":
    data_crawling()
