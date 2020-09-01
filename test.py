import re
import json


# -------------找出存在于<script >标签内的视频信息----------
# video_part = re.compile('<script >(.*?)</script>', re.S)
# replace_list = {
#     '\\u0026': '&',
#     '\\': ''
# }
#
# f = open("demo.html", "r", encoding='utf-8')
# string = f.read()
# f.close()
# for item in replace_list:
#     string = string.replace(item, replace_list[item])
# test = re.findall(video_part, string)
# a = 1
# for item in test:
#     if re.findall('googlevideo', item):
#         print(item)
#         print(a)
#         print()
#         a += 1

# -------------------对找出的信息进行格式化-------------
# f = open("demo.js", "r", encoding='utf-8')
# string = f.read()
# f.close()
# warnning = re.compile('codecs=".*?"', re.S)
# wrong = re.findall(warnning, string)
# corrected = []
# for item in wrong:
#     item = item.replace(' ', '')
#     item = item.replace('\n', '')
#     item = item.replace('"', '\'')
#     corrected.append(item)
#
# print(corrected)

# corrected_string = ""
#
# for i in range(len(wrong)):
#     string = string.replace(wrong[i], corrected[i])
# corrected_string = string
# f = open("demo1.js", "w", encoding='utf-8')
# f.write(corrected_string)
# f.close()

# 到此为止包含不同码率的{'合并视频', '纯视频', '纯音频'}的js文件处理告一段落

# ---------------------json解码----------------------
# f = open("vidInfo.js", "r", encoding='utf-8')
# string = f.read()
# f.close()
# info_part = re.compile('ytplayer.config = {(.*?)};', re.S)
# pure_json = re.findall(info_part, string)[0]
# f = open("pure_json.json", "w", encoding='utf-8')
# f.write('{' + pure_json + '}')

# 到此为止，js文件向html写入的json格式信息被格式化提取保存为.json文件

# f = open("pure_json.json", "r", encoding='utf-8')
# string = f.read()
#
#
# s = json.loads(string)
# print(s) # 打印出json全部信息
# print(s.keys()) # 第一层的key
# print(s['args']['player_response']['streamingData']) # 按照json pointer指定路径打印其中value
# print(type(s))
# for item in s['args']['player_response']['streamingData']:
#     for item in item:
#         print(item)


# ----------------递归遍历多层嵌套字典查找键值-------------


# def get_dict_allkeys(key, dict_a):
#         """
#         多维/嵌套字典数据无限遍历，获取json返回结果的所有key值集合
#         :param dict_a:
#         :return: key_list
#         """
#         if isinstance(dict_a, dict):  # 使用isinstance检测数据类型
#             for x in range(len(dict_a)):
#                 temp_key = list(dict_a.keys())[x]
#                 temp_value = dict_a[temp_key]
#                 if temp_key == key:
#                     print(temp_key, ':', temp_value)
#                 get_dict_allkeys(key, temp_value)  # 自我调用实现无限遍历
#         elif isinstance(dict_a, list):
#             for k in dict_a:
#                 if isinstance(k, dict):
#                     for x in range(len(k)):
#                         temp_key = list(k.keys())[x]
#                         temp_value = k[temp_key]
#                         if temp_key == key:
#                             print(temp_key, ':', temp_value)
#                         get_dict_allkeys(key, temp_value)

# get_dict_allkeys('width', s)
# get_dict_allkeys('lastModified', s)
# get_dict_allkeys('streamingData', s)


# --------------------重新测试json，只取出streamingData部分-----------

# f = open("vidInfo.js", "r", encoding='utf-8')
# string = f.read()
# f.close()
# streamingdata = re.compile('"streamingData":{(.*)},"playerAds"', re.S)
# data = '{' + '"streamingData": {' + re.findall(streamingdata, string)[0] + '}' + '}'
# f = open("TEST.json", "w", encoding='utf-8')
# f.write(data)
# f.close()
# print(data)


# ---------------------又你妈崩了，重来正则部分---------------------

# replace_dict = {
#     '\\u0026': '&',
#     '\\': '',
# }
# replace_dict2 = {
#     '"{': '{',
#     '}}}}"': '}}}}'
# }
# replace_dict3 = {
#     ' ': '',
#     '\n': '',
#     '"': '\''
# }
#
# f = open("TEST.json", "r", encoding='utf-8')
# s = f.read()
# f.close()
# warnning = re.compile('codecs=".*?"', re.S)
# wrongs = re.findall(warnning, s)
# wrong: object
# corrects = []
# for wrong in wrongs:
#     for i in replace_dict3:
#         wrong = wrong.replace(i, replace_dict3[i])
#     corrects.append(wrong)
#
# for i in range(len(wrongs)):
#     s = s.replace(wrongs[i], corrects[i])
#
# print(s)

# 哈哈没想到吧，爷又弄好了

# ----------------重新遍历字典-----------------------

# f = open("streamingData.json", "r", encoding='utf-8')
# s = f.read()
# f.close()
# string = json.loads(s)
# formats = string['streamingData']['adaptiveFormats']
#
# def get_dict_allkeys(key, dict_a): # 查询字典a中键值，并将键值放入字典b
#     """
#     多维/嵌套字典数据无限遍历，获取json返回结果的所有key值集合
#     :param dict_a:
#     :return: key_list
#     """
#     if isinstance(dict_a, dict):  # 使用isinstance检测数据类型
#         for x in range(len(dict_a)):
#             temp_key = list(dict_a.keys())[x]
#             temp_value = dict_a[temp_key]
#             get_dict_allkeys(key, temp_value)  # 自我调用实现无限遍历
#     elif isinstance(dict_a, list):
#         for k in dict_a:
#             if isinstance(k, dict):
#                 for x in range(len(k)):
#                     temp_key = list(k.keys())[x]
#                     temp_value = k[temp_key]
#                     get_dict_allkeys(key, temp_value)
#
#
# # get_dict_allkeys('width', string)
# # get_dict_allkeys('lastModified', string)
#
#
# # info_list = {
# #     'itag': [], # 标签
# #     'mimeType': [], # 数据格式
# #     'bitrate': [], # 比特率
# #     'width': [], # 视频宽
# #     'height': [], # 视频高
# #     'lastModified': [], # 修改时间unix时间戳，毫秒级
# #     'fps': [], # 帧率
# #     'qualityLabel': [], # 逐帧扫描率，成像效果
# #     'approxDurationMs': [], # 时常
# #     'audioSampleRate': [], # 若没有则为去音视频
# #     'averageBitrate': [], # 平均比特率
# # }
#
# show2user = formats
# for item in show2user:
#     del item['url']
# for i in range(len(show2user)):
#     print(str(i) + str(show2user[i]) + '\n')
#
# # get_dict_allkeys('width', formats, info_list)
# # get_dict_allkeys('fps', formats, info_list)


# ------------下载-----------------------
# down_list = input('which to download:(0-%d，多个用空格分割)')
# print(type(down_list))
# f = open("streamingData.json", "r", encoding='utf-8')
# s = f.read()
# string = json.loads(s)
# # print(type(string['streamingData']['adaptiveFormats'][0]))
# cipher = re.compile('&url=(.*)')
# print(string['streamingData']['adaptiveFormats'][0])
# a = re.findall(cipher, string['streamingData']['adaptiveFormats'][0]['signatureCipher'])
# print(a)

# ---------------unicode-------------------

# replace_list = {
#     r'\\\"': '',
#     r'\\u0026': '&',
#     r'\u0026': '&',
#     r'\\"': "'",
#     r'\"': r"'",
#     r'\\': '',
#     r'\/': '/',
#     r'\u003c': '<',
#     r'\u003e': '>',
# }
#
# --------------初始化cfg文件夹--------------------

# path = './123/'
#
# def mkdir(path):
#     import os
#
#     isExists = os.path.exists(path)
#     if not isExists:
#         os.makedirs(path)
#
# mkdir(path)
#
# f = open("./123/123.text", 'w', encoding='utf-8')
# f.write("123")

# ----------------------调用idm----------------------

import os

path = 'C:\\Program Files (x86)\\Internet Download Manager\\'
IDM = 'idman'
os.chdir(path)
DownPath = 'C:\\Users\\10941\\Desktop\\'
DownUrl = 'https://w.wallhaven.cc/full/wy/wallhaven-wyz5ex.jpg'
FileName = '123.jpg'
command = ' '.join([IDM, '/d', DownUrl, '/p', DownPath, '/f', FileName, '/q', '/s'])
os.system(command)
