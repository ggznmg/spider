import requests
import re
url="http://zyk.bjhd.gov.cn/zwdt/hdyw/"
headers={ 
        'Referer':'http://zyk.bjhd.gov.cn/zwdt/hdyw/',          
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; LCTE; rv:11.0) like Gecko'
    }
response=requests.get(url)
response.encoding='utf-8'
# r=respose.text
HTML=response.text
# compile预编译 适用于文本过长
regex=re.compile('.*?if\(!strLink\){document\.write\(\'<a href="\.(.*shtml)".*\'\)}')
result=regex.findall(HTML)
print(result)

url = ['http://zyk.bjhd.gov.cn/zwdt/hdyw' + i for i in result]
print(url)
print()
for j in url:
    print(j)






# with open('/home/gz/Desktop/zy3.txt',mode='w',encoding='utf8')as f:
    # f.write(r)




