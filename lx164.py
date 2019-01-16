from lxml import etree
import requests

headers={
'Referer': 'http://www.hetaodaxue.com/xyxw.htm',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
response=requests.get('http://www.hetaodaxue.com/xyxw.htm',headers=headers)
response.encoding='utf8'
# print(response)
tree=etree.HTML(response.text)
# print(tree)
# result = etree.tostring(tree)
# print(result)
# print(result.decode('utf-8'))
res = tree.xpath('//div[@class="right_list_news"]/div/ul/li/a')
for a in res:
    print(a.xpath('./@href')[0])
    print(a.xpath('./text()')[0])

for i in range(1,108):
    response=requests.get('http://www.hetaodaxue.com/xyxw/{}.htm'.format(i),headers=headers)
    response.encoding='utf8'
    # print(response)
    tree=etree.HTML(response.text)
    # print(tree)
    # result = etree.tostring(tree)
    # print(result)
    # print(result.decode('utf-8'))
    res = tree.xpath('//div[@class="right_list_news"]/div/ul/li/a')
    for a in res:
        print(a.xpath('./@href')[0])
        print(a.xpath('./text()')[0])

    


