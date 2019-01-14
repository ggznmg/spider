import re
content = 'Extra stings Hello 2134567 World_This is a Regex Demo Extra stings'
result = re.sub('\d+','hahah',content)
print(result)