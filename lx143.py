import re
tpe='"submit" id="su" value="百度一下" class="bg s_btn"></span><span class="tools"><span id="mHolder"><div id="mCon"><span>输入法</span></div><ul id="mMenu">'
content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello.*?(\d+).*Demo$',content) 
# result = re.match('"submit" id="su" value="(百度一下)" class="bg s_btn"></span><span class="tools"><span id="mHolder"><div id="mCon"><span>(输入法)</span></div><ul id="mMenu">',tpe) 
# result = re.match('"submit" id="su" value="(\w{4})" class="bg s_btn"></span><span class="tools"><span id="mHolder"><div id="mCon"><span>(\w{3})</span></div><ul id="mMenu">',tpe) 
result = re.match('.*value="(\w{4}) .*<span>(\w{3})</.*',tpe) 
print(result)
print(result.group(1,2))