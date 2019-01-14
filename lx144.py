import re
content = '''Hello 1234567 World_This 
is a Regex Demo'''
result = re.match('^He.*?(\d+).*?Demo$',content)
print(result) # 这里匹配是因为. 是不能匹配换行符的
result = re.match('^He.*?(\d+).*?Demo$',content,re.S)
print(result.group(1))