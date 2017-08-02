#coding=utf-8
# Author:Bob
# Version:1.1
# for Rust
import os
import time
import re
import codecs
from urllib import request
from bs4 import BeautifulSoup


import spider
import warnings
warnings.filterwarnings("ignore")

Web = 'https://kaisery.github.io/trpl-zh-cn/'
Local ='./rust'

def win_name_check(str_name):
    name = str_name.replace('/','')
    name = name.replace('\\','')
    name = name.replace('*','')
    name = name.replace('?','')
    name = name.replace('/','')
    name = name.replace(':','')
    name = name.replace('<','')
    name = name.replace('>','')
    name = name.replace('|','')
    return name

def get_href(bs_str):
    global Web
    global Local
    bs_t = BeautifulSoup(str(bs_str))
    list_t = bs_t.select('li')
    #sub_list = bs_t.select('li')
    #print(len(list_t))
    if(len(list_t)==1):
        tag_t = bs_t.a
        print(tag_t.get_text(),end=":\t")
        print(tag_t['href'],end='')
        #request.urlretrieve(Web+tag_t['href'],Local+'/'+tag_t['href'])
        name = win_name_check(tag_t.get_text())
        print('\n'+Web+tag_t['href'])
        print(Local+'/'+name+".html")
        request.urlretrieve(Web+tag_t['href'],Local+'/'+name+".html")
    else:
        cnt=0
        for i in list_t:
            cnt=cnt+1
            if(cnt==1):
                continue
            print(" ",end='\t')
            get_href(i)
            print("")
        print("")
    return 0
    
if __name__=='__main__':
    print(time.ctime(time.time()))
    try:
        os.mkdir(Local)
    except:
        print("exist dir")
    a = spider.htmlpage(Web)
    bs = BeautifulSoup(a.page)
    print("-------------------")
    for i in bs.select('.chapter > li'):
        #print(i)
        get_href(i)
        print("\n")
    
    
