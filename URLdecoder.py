# -*- coding: utf-8 -*-
# @Time : 2020/8/30 18:37
# @Author : KevinHoo
# @Site : 
# @File : URLdecoder.py
# @Software: PyCharm 
# @Email : hu.rui0530@gmail.com


decode_list = {
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



def seperatorOff(a):
    print('converting url...')
    for key in decode_list:
        a = a.replace(decode_list[key], key)
    return a


def splice(list, index, num):
    for i in range(num):
        list[index + i] = ''
    while '' in list:
        list.remove('')

    return list

class Gv:
    def HF(a:list):
        a.reverse()

    def A2(a:list, b):
        splice(a, 0, b)

    def ch(a:list, b):
        c = a[0]
        a[0] = a[b % len(a)]
        a[b % len(a)] = c

def Hv(s):
    print('decrypting signature...')
    a = []
    for item in s:
        a.append(item)
    Gv.A2(a, 1)
    Gv.ch(a, 39)
    Gv.A2(a, 3)
    return ''.join(a)


def decode(s):
    return Hv(s)

if __name__ == '__main__':
    print(decode(
        'OqAOq0QJ8wRQIhAJwynfDBELz-k39lHkkCQv=bAcSVgvhSjbGSYP2xpYqDAiBQ8OVaJwGXVulEPGq-v-PKxWqG6AxEANyhaalPQ5SPIg=='))
#        q0QJ8wRQIhAJwynfDBELz-k39lHkkCQv=bAcqVgvhSjbGSYP2xpYqDAiBQ8OVaJwGXVulEPGq-v-PKxWqG6AxEANyhaalPQ5SPIg==

