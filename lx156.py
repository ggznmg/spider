import requests
from bs4 import BeautifulSoup
HTML = requests.get('https://book.douban.com/tag/%E6%95%A3%E6%96%87').text
soup = BeautifulSoup(HTML,'lxml')
res_img=soup.select('body img') 
#print(res_img)
res_a=soup.select('#subject_list .subject-list li .info a')
#print(res_a)
res_title=soup.select('#subject_list .subject-list  li .pub')
# print(res_title[0].text)
for img in res_img:    
    print(img.attrs['src'])
    print('---------------')
for a in res_a:    
    print(a.text[0])
    print('---------------')
for title in res_title:    
    print(title.text.strip().split(' / ')[0])
     