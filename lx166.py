import requests
from lxml import etree
import threading
import urllib.parse
import pymongo
import time

headers={
'Referer':'http://op.hanhande.net/shtml/meitu.shtml',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

def get_lianjie(url):
    start = time.time()
    for i in url:
        response=requests.get(url,headers=headers)
        response.encoding='gbk'
        tree=etree.HTML(response.text)
        res = tree.xpath('//ul[@class="spic pic1"]/li/a')
        for a in res:
                addr=a.xpath('./@href')[0]
                print(a.xpath('./@href')[0])
                name=a.xpath('./@title')[0]
                print(a.xpath('./@title')[0])
                write_local(addr,name)
        
def write_local(addr,name):
     myclient = pymongo.MongoClient("mongodb://localhost:27017/")
     mydb = myclient["zy1"]
     mycol = mydb["hzw"]
     mycol.insert_one({'name':name,'add':addr})
     myclient.close() #!!!!!!!!!!!

if __name__ == "__main__":
    list1=[]
    for i in range(25,1,-1):
        if i == 1:
             url = 'http://op.hanhande.net/shtml/meitu.shtml'
             get_lianjie(url)
        else:
              url='http://op.hanhande.net/shtml/op_wz/list_2602_{}.shtml'.format(i)      
              get_lianjie(url)
        list1.append(url)   
    #url_list = [i for i in range(1,24)]
    
     lock = threading.Lock() # 创建线程锁
     print(list1)

     thread_1 = threading.Thread(target=get_lianjie,args=(list1[:8],))
    thread_2 = threading.Thread(target=get_lianjie,args=(list1[8:16],))
     thread_3 = threading.Thread(target=get_lianjie,args=(list1[16:],))

     thread_1.start()
     thread_2.start()
     thread_3.start()

     thread_1.join()
     thread_2.join()
     thread_3.join()        
