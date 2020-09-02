# -*- coding: utf-8 -*-
# @Time : 2020/9/2 13:35
# @Author : KevinHoo
# @Site : 
# @File : URLdecoder.py.py
# @Software: PyCharm 
# @Email : hu.rui0530@gmail.com


decode_dict = {
    ' ': '%20',
    '"': '%22',
    '#': '%23',
    '%': '%25',
    '&': '%26',
    '(': '%28',
    ')': '%29',
    '+': '%2B',
    ',': '%2C',
    '/': '%2F',
    ':': '%3A',
    ';': '%3B',
    '<': '%3C',
    '=': '%3D',
    '>': '%3E',
    '?': '%3F',
    '@': '%40',
    '\\': '%5C',
    '|': '%7C',
}


# 百分号解码
def seperatorOff(a):
    print('converting url...')
    for key in decode_dict:
        a = a.replace(decode_dict[key], key)
    return a


def splice(list, index, num):
    for i in range(num):
        list[index + i] = ''
    while '' in list:
        list.remove('')

    return list


class Fv:
    def i7(a:list, b):
        c = a[0]
        a[0] = a[b % len(a)]
        a[b % len(a)] = c

    def D3(a:list, b):
        splice(a, 0, b)

    def Hm(a:list, num:int):
        a.reverse()

def Gv(s):
    a = []
    for item in s:
        a.append(item)
    Fv.Hm(a, 30)
    Fv.i7(a, 69)
    Fv.Hm(a, 3)
    Fv.i7(a, 20)
    Fv.Hm(a, 52)
    Fv.i7(a, 32)
    Fv.D3(a, 3)
    return ''.join(a)


def decode(s):
    return Gv(s)


if __name__ == '__main__':
    # sigcipher = ""
    # sigcipher = seperatorOff(sigcipher)
    # s = ""
    # s = decode(s)
    print(seperatorOff('https://r2---sn-jxnj5-cjoe.googlevideo.com/videoplayback%3Fexpire%3D1599061097%26ei%3DCWhPX_uJKs-uW__QpIgI%26ip%3D13.69.158.161%26id%3Do-AMptcNa7sVQHQBiiBb6KPrXw0T9-FZFvMtv6lY-9GIEZ%26itag%3D18%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DLh%26mm%3D31%252C29%26mn%3Dsn-jxnj5-cjoe%252Csn-4g5e6nzl%26ms%3Dau%252Crdu%26mv%3Du%26mvi%3D2%26pl%3D23%26gcr%3Die%26vprv%3D1%26mime%3Dvideo%252Fmp4%26gir%3Dyes%26clen%3D17793698%26ratebypass%3Dyes%26dur%3D295.404%26lmt%3D1583110775970339%26mt%3D1599039073%26fvip%3D2%26c%3DWEB%26txp%3D5531432%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cgir%252Cclen%252Cratebypass%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%26lsig%3DAG3C_xAwRQIgXEnR8OzzFXGWYiKu9kokr7HfLvOQ1OQk5hSmTSk7UcICIQCtyWBGRuEDV1gnxRWg2ZYXt5ru0ES-QfzK4deMU6pFDA%253D%253D'))