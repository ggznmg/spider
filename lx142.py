import re
content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content)) # 字符串的长度
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*?Demo$',content)
# result = re.match('H.*3 (\d\d\d\d).*',content)
result = re.match('H.*3 (\d{4}).*',content)
# result = re.match('Hello 123 4567 (World)_This is a Regex Demo',content)
result = re.match('Hello (\d{3}) 4567 (World)_This is a Regex Demo',content)
print(result.group(2))
print(result.group(1))
print(result.group(1,2))

# print(result.group()) # 返回匹配的内容
# print(result.span()) # 返回匹配的字符的范围长度