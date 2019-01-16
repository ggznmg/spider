import requests
from lxml import etree
import threading
import urllib.parse
import pymongo
import time
headers={
'Referer': 'http://www.hetaodaxue.com/xyxw.htm',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
def get_lianjie(url):
    start = time.time()
    for i in url:
        response=requests.get(i,headers=headers)
        response.encoding='utf8'
        tree=etree.HTML(response.text)
        res = tree.xpath('//div[@class="right_list_news"]/div/ul/li/a')
        for a in res:
            addr=a.xpath('./@href')[0]
            print(a.xpath('./@href')[0])
            get_biaoti(tree,addr) 
        end = time.time()
        print("爬虫完毕",end - start)   

def get_biaoti(tree,addr):
    res = tree.xpath('//div[@class="right_list_news"]/div/ul/li/a')
    for a in res:
        name=a.xpath('./text()')[0]
        print(a.xpath('./text()')[0])
        lock.acquire()  # 锁住mongo
        write_local(addr,name)
        lock.release() # 打开mongo
        
def write_local(addr,name):
   
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["dddd"]
    mycol = mydb["hetao"]
    mycol.insert_one({'name':name,'add':addr})
    myclient.close() #!!!!!!!!!!!


if __name__ == "__main__":
    list1=[]
    for i in range(108,1,-1):
        if i == 108:
            url = 'http://www.hetaodaxue.com/xyxw.htm'
            #get_lianjie(url)
        else:
            url = 'http://www.hetaodaxue.com/xyxw/{}.htm'.format(i)
            #get_lianjie(url)
        list1.append(url)
     
    #url_list = [i for i in range(1,24)]
    
    lock = threading.Lock() # 创建线程锁
    print(list1)
    thread_1 = threading.Thread(target=get_lianjie,args=(list1[:36],))
   
    thread_2 = threading.Thread(target=get_lianjie,args=(list1[36:72],))

    thread_3 = threading.Thread(target=get_lianjie,args=(list1[72:],))

    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_1.join()
    thread_2.join()
    thread_3.join()