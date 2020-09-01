# -*- coding: utf-8 -*-
# @Time : 2020/8/29 9:26
# @Author : KevinHoo
# @Site :
# @Title : Youtube SingnatureCipher Decryptor
# @File : main.py
# @Software: PyCharm 
# @Email : hu.rui0530@gmail.com

import re
import urllib.request
import json
import URLdecoder
import copy
# import dictTraversal
# import callIDMan


# 正则
mediaTitle = re.compile(r'<meta name="title" content="(.*?)">', re.S)
ytplayerCfg = re.compile(r'<script >var ytplayer.*?</script>', re.S)
streamingData = re.compile(r'"streamingData":{', re.S)
streamingdata1 = re.compile("'streamingData':{(.*)},'playbackTracking'", re.S)
streamingdata0 = re.compile("'streamingData':{(.*)},'playerAds'", re.S)
sigCipher  = re.compile(r's=(.*?)&sp')
cipherUrl  = re.compile(r'&url=(.*)')


# Unicode字符集
replace_dict = {
    r'\\\"': '',
    r'\\u0026': '&',
    r'\u0026': '&',
    r'\\"': "'",
    r'\"': r"'",
    r'\\': '',
    r'\/': '/',
    r'\u003c': '<',
    r'\u003e': '>',
}
# 请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.76 Safari/537.36",
    "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7,ar;q=0.6"
}
# 路径
cfgPath = './config/'
downPath = './media/'


# 初始化目录
def cfgDirInit(path):
    import os
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path, '创建成功')
        return True
    else:
        print(path, '目录已存在')
        return False


# 过程文件保留
def write(file, filename):
    """
    :param file:str
    :param filename:str
    :return:None
    """
    cfgDirInit(cfgPath)
    f = open(cfgPath + filename, "w", encoding='utf-8')
    f.write(file)
    f.close()


# 原页面
def askURL(url):
    filename = 'oringin_video_page.html'

    res = urllib.request.Request(url=url, headers=headers)
    req = urllib.request.urlopen(res)
    html = req.read().decode('utf-8')

    write(html, filename)

    return html


# 替换掉unicode字符的页面
def prettify(html):
    filename = 'pre_video_page.html'

    for item in replace_dict:
        html = html.replace(item, replace_dict[item])

    title = re.findall(mediaTitle, html)[0]

    write(html, filename)

    return html, title


# 截取含有ytplayer播放器信息的js脚本
def process2Js(pre_html):
    filename = 'video_info_ytplayer_js.html'

    js_file = re.findall(ytplayerCfg, pre_html)[0]

    write(js_file, filename)

    return js_file


# 截取ytplayer中含有的流媒体信息
def process2Json(js_file):
    filename = 'video_page_json.json'

    if not re.findall(streamingdata0, js_file):
        json_file = '{' + '"streamingData": {' + re.findall(streamingdata1, js_file)[0] + '}' + '}'
    else:
        json_file = '{' + '"streamingData": {' + re.findall(streamingdata0, js_file)[0] + '}' + '}'
    json_file = json_file.replace("'", '"')

    write(json_file, filename)

    return json_file


# 全部格式音视频属性
def show2User(streamingList):
    print()
    show2user = copy.deepcopy(streamingList) # 深拷贝，有别于浅拷贝

    for item in show2user:
        try:
            del item['signatureCipher']
        except KeyError:
            del item['url']

    for i in range(len(show2user)):
        print(str(i), str(show2user[i]), '\n') # 展现给用户的部分


# 下载队列
def askUser(length):
    down_queue = re.split(' ', input('which to download:(0-%d，seperate with one space)' % (length-1)))
    return down_queue


# 装载json信息并转换为py中的字典
def getInfo(json_file):
    down_link_list = []

    video_info_dict = json.loads(json_file)
    streamingList = video_info_dict['streamingData']['adaptiveFormats']

    show2User(streamingList)

    down_queue = askUser(len(streamingList))

    for num in down_queue:
        media = streamingList[int(num)]
        if 'signatureCipher' in media:
            noneSperator = URLdecoder.seperatorOff(media['signatureCipher'])
            sig = URLdecoder.decode(re.findall(sigCipher, noneSperator)[0])
            baseurl = re.findall(cipherUrl, noneSperator)[0]
            down_link_list.append(baseurl + '&sig=' + sig)
        elif 'url' in media:
            down_link_list.append(media['url'])

    return down_link_list, down_queue


# idm调用时输入的链接除expire之外的参数都无法输入
def allocateURL(down_link_list, down_queue):
    cfgDirInit(downPath)
    for i in range(len(down_link_list)):
        print(down_queue[i] + '\n' + down_link_list[i])
        # callIDMan.call(link, downPath, title)


def main():
    url = input("input video address:")
    html = askURL(url)
    pre_html, title = prettify(html)
    js_file = process2Js(pre_html)
    json_file = process2Json(js_file)
    down_link_list, down_queue = getInfo(json_file)
    allocateURL(down_link_list, down_queue)


if __name__ == '__main__':
    main()
