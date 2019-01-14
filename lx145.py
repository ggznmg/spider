import re
typ='Extra stings Hello 2134567 World_This is a Regex Demo Extra stings'
result = re.search('(Extra) stings Hello 2134567 (.*) is a Regex Demo Extra (.*)',typ ,re.S)

print(result.group(1,2,3))
# type="submit" id="su" value="百度一下" class="bg s_btn"></span><span class="tools"><span id="mHolder"><div id="mCon"><span>输入法</span></div><ul id="mMenu">