# # 使用requests库爬取ImageNet库中的图片存入本地
# # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808
import requests
headers = {    
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
reponse = requests.get('http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808')
add=reponse.text.split('\r\n')
for i in add:

    try:
        response = requests.get(i,headers=headers,timeout=1,allow_redirects=False) 
        print(i)
        with open('/home/gz/Desktop/{}'.format(i.split('/')[-1]),mode='wb',) as f:  
            f.write(response.content)   
    except Exception as e:
        print(e)   
    
