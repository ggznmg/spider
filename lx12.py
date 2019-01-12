# 实现百度搜索关键字"胡旺是个好人"，将结果存入本地
import urllib.request
import urllib.parse
url="http://baidu.com/"
headers={'Referer': 'https://www.baidu.com/',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
parameter={"wd":"%E8%83%A1%E6%97%BA"}
datas = urllib.parse.urlencode(parameter,encoding='utf-8')
url=url+"/s?"+datas
data = urllib.request.Request(url,method="GET")
response = urllib.request.urlopen(url=data)
test=response.read().decode('utf8')
with open('/home/gz/Desktop/zy2.txt',mode='w',encoding='utf8')as f:
    f.write(test)