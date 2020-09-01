# -*- coding: utf-8 -*-
# @Time : 2020/8/30 22:29
# @Author : KevinHoo
# @Site : 
# @File : getDecodeBase.py
# @Software: PyCharm 
# @Email : hu.rui0530@gmail.com


import urllib.request
from bs4 import BeautifulSoup
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.76 Safari/537.36",
    "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7,ar;q=0.6"
}
domain = "https://www.youtube.com"


def askURL(url):
    res = urllib.request.Request(url=url, headers=headers)
    req = urllib.request.urlopen(res)
    html = req.read().decode('utf-8')
    return html


def parseHtml(html):
    soup = BeautifulSoup(html, 'lxml')
    basejs = soup.select('script[name="player_ias/base"]')
    return basejs


def findBaseJs(basejs):
    backdrop = re.findall('src="(.*?)"', str(basejs))[0]
    url = domain + backdrop
    jsfile = askURL(url)
    return jsfile


def writeFile(jsfile, basepath):
    with open(basepath, "w", encoding='utf-8') as f:
        f.write(jsfile)
    return


def main():
    url = 'https://www.youtube.com/watch?v=LXb3EKWsInQ&t=3s'
    basepath = 'base.js'
    html = askURL(url)
    basejs = parseHtml(html)
    jsfile = findBaseJs(basejs)
    writeFile(jsfile, basepath)


if __name__ == '__main__':
    main()
