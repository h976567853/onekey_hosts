#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import urllib.request
import re
import zipfile
import os
import time
from urllib.request import urlretrieve
               
#获取页面HTML内容
def getcontent(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }

    request = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

#正则匹配获取host下载链接
def geturl():
    url1 = 'https://iiio.io/download/'
    pattern1 = re.compile('<a href="(.*?)/">(.*?)/</a>',re.S)
    pages = re.findall(pattern1,getcontent(url1))
    pagenum=pages[-3][1]

    url2=url1+pagenum
    pattern2 = re.compile(u'<a href="Windows(.*?).zip">Windows系列跟苹果系列.zip</a>  ',re.S)
    str = re.findall(pattern2,getcontent(url2))
    result=url2+'/Windows'+str[0]+'.zip'
    print('\n已经获取hosts,版本:'+pagenum)
    time.sleep(0.5)
    return result

    #下载host文件
def gethosts(url):
    urlretrieve(url,'temp.zip')
    f = zipfile.ZipFile('temp.zip')  
    f.extractall(pwd=b'0920')
    print('\n解压缩完成')

#设置host    
def sethosts():   
    os.system('copy /y "hosts" "C:\Windows\System32\drivers\etc\hosts"')
    time.sleep(0.5)
    os.system('C:\windows\system32\ipconfig /flushdns')

gethosts(geturl())
sethosts()
print('\nhost已经更新完成')
#删除临时文件
os.remove('temp.zip')
os.remove('hosts')

input ("\nPlease Press Enter To Exit")