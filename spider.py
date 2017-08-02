#coding=utf-8
import time
import re
import codecs
import os
from urllib import request
from bs4 import BeautifulSoup

class htmlpage:
    headers={
       'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
       'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
        'Connection': 'keep-alive'
    }
    protocol="http"
    
    def __init__(self,url,decode='utf-8'):
        self.url=url
        self.decode=decode

        try:
            self.__req=request.Request(self.url,headers=self.headers)
        except ValueError:
            print("incorrect url:%s"%self.url)
            exit()
        try:
            self.web=request.urlopen(self.__req)

        except :
            print("failure to connect to url:%s"%self.url)
            exit()
        
        self.__setProtocol__(str(self.web.geturl()))
        self.page=self.web.read()
        self.page=self.page.decode(self.decode)

    def __setProtocol__(self,url):
        if(url.find("https")==0):
            self.protocol="https"

    def __del__(self):
        print("quit:%s"%self.url)

class local_res:
    def __init__(self,urllist):
        self.urllist=urllist
        self.path=local

    def save_as(local):
        self.path=local
        self.cnt=0
        for i in self.urllist:
            print(i)
            request.urlretrieve(i[0],local+str(cnt)+'.'+i[1])
            cnt=cnt+1


if __name__=='__main__':
    print(time.ctime(time.time()))
    url=input("url:")
    ac=htmlpage(url)

    #m_re=r'(src="|url\()(http://.+\.(jpg|png|gif|jpeg))("|\?|\))'
    m_re=r'(//\S+?\.(gif|png|jpg|jpeg))'
    file=codecs.open("111.txt",'w','utf-8')
    file.write(str(ac.page))
    file.close()
    #imgre=re.compile(m_re,re.I)
    imgs=re.findall(m_re,ac.page,re.I)
    print("picture list:")
    #local_res()
    #res_save()
    #local="F:\\workspace-python\\data\\"
    local='./data_pic'
    try:
        os.mkdir(local)
    except:
        print("exist dir")
    cnt=0
    imgs=list(set(imgs))
    for i in imgs:
        print(i)
        request.urlretrieve('http:'+i[0],local+'/'+str(cnt)+'.'+i[1])
        cnt=cnt+1
    print("\ntotal number:")
    print(len(imgs))
    ursl=input("url:")
    #imgs.aixifan.com/cms/2017_07_26/1501075572622.jpg
    #request.urlretrieve("http://video.acfun.cn/010040020400005953936000010000100000000000-0000-0000-0182-BBB500000000.mp4?customer_id=5859fdaee4b0eaf5dd325b91&start=0.0&auth_key=1498726471-1010014850719126ef92bcfcc467d7611a8d8005d0d6rmp479c3225faf5074cc92d85c1f999ec5a7-ACFUN-7edbf1650729bbad7a135d73b27eb34c",local+'v.mp4')
    #request.urlretrieve("http://i0.hdslb.com/bfs/archive/17759bd2d61eb97e992642f79a15ddabd015d0dc.png",'sss.png')
