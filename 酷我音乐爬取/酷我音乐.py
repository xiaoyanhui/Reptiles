import requests

heard = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    "Cookie": "_ga=GA1.2.689315263.1579101205; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1588072571,1588072944,1588341420; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1588341420; _gid=GA1.2.700222710.1588341420; kw_token=ZX9ROK9VOH",
    "Referer": "http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6",
    "csrf": "ZX9ROK9VOH"

}


def download_music(rid, name):
    url2 = "http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&from=web&t=1582862150788&reqId=35c42441-59de-11ea-b210-0740ce874a3c".format(
        rid)
    result = requests.get(url=url2, headers=heard).json()
    music_url = result['url']
    music = requests.get(music_url)
    with open("./酷我/{}.mp3".format(name), "wb")as f:
        print("正在下载{}".format(name))
        f.write(music.content)



def main():
    search = input("请输入歌手名字")
    search1 = int(input("要获取的页数"))
    for i in range(1, search1 + 1):
        url1 = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}&rn=30&reqId=35c312d1-59de-11ea-b210-0740ce874a3c".format(
            search, search1)
        res = requests.get(url=url1, headers=heard).json()
        datas = res['data']['list']
        for data in datas:
            rid = data['rid']
            name = data['name']
            print(rid, name)
            download_music(rid, name)


if __name__ == "__main__":
    main()
