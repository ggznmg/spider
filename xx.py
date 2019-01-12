import urllib.request
import urllib.parse
url="http://www.17k.com/chapter/2933095/36699279.html"
headers={'Referer': 'http://www.17k.com/chapter/2933095/36699279.html',
          'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
data = urllib.request.Request(url,method="GET")
# data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
# print(data)
response = urllib.request.urlopen(url=data)
test=response.read().decode('utf8')
with open('/home/gz/Desktop/zy1.txt',mode='w',encoding='utf8')as f:
    f.write(test)
# print(response.read().decode('utf8'))