import requests
import urllib.request
import json
# import re
import pandas as pd


def loadPage(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    r = requests.get(url, timeout=30, headers=headers)
    #         print(r.text)
    return (r.text)


def parserPage(html, furl):
    s = json.loads(html)
    commentlist = []
    #     hlist = []
    #     hlist.append("video_url")
    #     hlist.append("video_playback")
    #     hlist.append("video_barrage_num")
    #     hlist.append("video_like_num")
    #     hlist.append("video_coin_num")
    #     hlist.append("video_favorite_num")
    #     hlist.append("ideo_forward_num")

    comment = s['data']
    #     print(comment)
    blist = []

    view = comment['view']
    danmaku = comment['danmaku']
    share = comment['share']
    favorite = comment['favorite']
    coin = comment['coin']
    like = comment['like']
    aid = comment['aid']

    blist.append(aid)
    blist.append(view)
    blist.append(danmaku)
    blist.append(like)
    blist.append(coin)
    blist.append(favorite)
    blist.append(share)

    commentlist.append(blist)
    print(blist)

    writePage(commentlist, furl)


#     print(commentlist)
def writePage(urating, furl):
    dataframe = pd.DataFrame(urating)
    dataframe.to_csv(furl, mode='a', index=False, sep=',', header=False)


if __name__ == '__main__':
    urlpool = ["63215184", "65163392", "67098514", "70559375", "70569247", "70637706", "75453295", "70958402",
               "71751850", "71772842", "71886437", "72049382", "73238251", "73325317", "73745370", "70223811",
               "74043053", "74108103", "74604209", "74517160", "74740467", "74798387", "74939377", "75244790",
               "75253065", "75873413", "75771115", "76037414", "76353765", "76585479", "76672033", "77120400"]
    furl = "D:\\bilibili\\result.csv"
    for i in urlpool:
        try:
            url = "http://api.bilibili.com/archive_stat/stat?aid=" + i

            #         furl="D:\\bilibili\\result.txt"
            #         url_tag="https://api.bilibili.com/x/tag/archive/tags?callback=jqueryCallback_bili_48078431259079357&aid=63215184"
            html = loadPage(url)

            #               print(html.encode('utf-8'))
            parserPage(html, furl)

        except:
            continue
