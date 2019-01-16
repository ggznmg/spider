from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html">first item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
print(html)
result = etree.tostring(html)
print(result)
print(result.decode('utf-8'))
result = html.xpath('//div/ul/li/a')
print(result)
res = html.xpath('//div/ul/li/a/@href')
print(res)
# from lxml import etree
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//*')
# print(result)