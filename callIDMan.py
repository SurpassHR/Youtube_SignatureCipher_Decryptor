# -*- coding: utf-8 -*-
# @Time : 2020/8/31 14:51
# @Author : KevinHoo
# @Site : 
# @File : callIDMan.py
# @Software: PyCharm 
# @Email : hu.rui0530@gmail.com

import os


def call(DownUrl, DownPath, FileName):
    """
    :param DownUrl: 下载链接
    :param DownPath: 保存位置
    :param FileName: 文件名
    :return:
    """
    path = 'C:\\Program Files (x86)\\Internet Download Manager\\'
    IDM = 'idman'
    os.chdir(path)
    FileName = '123.jpg'
    command = ' '.join([IDM, '/d', DownUrl, '/p', DownPath, '/f', FileName, '/q'])
    # autoDowncmd = ' '.join([IDM, '/s'])
    os.system(command)
    return True
