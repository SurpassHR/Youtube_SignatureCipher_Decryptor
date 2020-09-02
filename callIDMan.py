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
    FileName = '123.mp4'
    command = ' '.join([IDM, '/d', DownUrl, '/p', DownPath, '/f', FileName, '/q'])
    # autoDowncmd = ' '.join([IDM, '/s'])
    os.system(command)

    return True

FileName = '123.jpg'
DownUrl = 'https://r8---sn-juh-h4hz.googlevideo.com/videoplayback?expire=1599048727&ei=tzdPX5GBB4re4gLGip_oAQ&ip=60.246.31.156&id=o-AJwnNuWKfNUzLAC2aeDQxtjkwsOZtxmLrJlxDBdX3olC&itag=248&aitags=133,134,135,136,137,160,242,243,244,247,248,271,278,313,394&source=youtube&requiressl=yes&mh=Lh&mm=31,29&mn=sn-juh-h4hz,sn-i3belnlz&ms=au,rdu&mv=m&mvi=8&pl=20&gcr=mo&initcwndbps=1090000&vprv=1&mime=video/webm&gir=yes&clen=46676610&dur=295.336&lmt=1583110965238265&mt=1599027040&fvip=2&keepalive=yes&beids=9466587&c=WEB&txp=5531432&sparams=expire,ei,ip,id,aitags,source,requiressl,gcr,vprv,mime,gir,clen,dur,lmt&lsparams=mh,mm,mn,ms,mv,mvi,pl,initcwndbps&lsig=AG3C_xAwRAIgZuywWERYUr1VT_iZAxgLxcTzQDho0tSIVjF-c17pQHwCIGul-1GV72xyUUFfWgXL4fY3UE35Cqsj-7kH6LCG0XYY&sig=AOq0QJ8wRAIgRQyVP5542aR3QBu2KkSzrr0h9JmwKWz8D99Bad3-kf8CIAyR2Im2rCmdfWysDtcyb7DsgD4qPswg9bfxwF9Cgurd'
DownPath = './'
call(DownUrl, DownPath, FileName)