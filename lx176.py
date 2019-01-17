import requests
from  selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
import pymongo
# from selenium.webdriver import  ActionChains
# from selenium.webdriver.common.alert import Alert

# def get_lianjie(url):
def get_lianjie():    
    driver = webdriver.Chrome()
    driver.get("https://www.taobao.com/")
    elem = driver.find_element_by_css_selector("#q")
    # print(elem)
    # elem.clear()
    elem.send_keys("美食")
    elem.send_keys(Keys.ENTER) # 模拟按下回车

    for i in range(100):
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        prices=driver.find_elements_by_xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div/div[2]/div[1]/div[1]/strong')
        names=driver.find_elements_by_xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div/div[2]/div[2]/a')
        for price ,name in zip(prices,names):
            #print(price.text)
            pri=price.text
            #print(name.text)
            na=name.text
            write_local(pri,na)
        
        sure = driver.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[2]/span[3]')  
        sure.send_keys(Keys.ENTER)
    
       # write_local(price,name)

def write_local(price,name):
     myclient = pymongo.MongoClient("mongodb://localhost:27017/")
     mydb = myclient["zy17"]
     mycol = mydb["taobaomeishi"]
     mycol.insert_one({'name':name,'price':price})
     myclient.close() #!!!!!!!!!!!

if __name__ == "__main__":
    get_lianjie()
        # list1=[]
        # for i in range(1,4):
        # if i == 1:
        #     url = 'http://op.hanhande.net/shtml/meitu.shtml'
        #     # get_lianjie(url)
        # else:
        #     url='http://op.hanhande.net/shtml/op_wz/list_2602_{}.shtml'.format(i)      
        #     # get_lianjie(url)
        # list1.append(i)   
