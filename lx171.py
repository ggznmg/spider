from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

# response = requests.get('http://www.taobao.com')
# print(response)


driver = webdriver.Chrome()
driver.get("https://www.taobao.com/")
elem = driver.find_element_by_css_selector("#q")
print(elem)
elem.clear()
elem.send_keys("美食")
# elem.send_keys(Keys.RETURN)
# search = driver.find_element_by_css_selector("#q")

browser.save_screenshot('text.png')
browser.close()

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait



# import re
# browser=webdriver.Chrome() # 下载的chrome.exe的文件位置

# try:
#     browser.get('http://www.baidu.com') # 传入url
#     input=browser.find_element_by_id('kw') # 找到元素id为kw 实际上kw就是百度的输入框id
#     input.send_keys('Python')  # 输入python
#     input.send_keys(Keys.ENTER) # 模拟按下回车
#     wait = WebDriverWait(browser,10) # 等待浏览器10秒加载
#     wait.until(EC.presence_of_element_located((By.ID,'content_left'))) # 等待id为content_left的元素加载出来
#     print(browser.current_url) # 打印ur
#     print(browser.get_cookies()) # 打印cookies
#     print(type(browser.page_source)) # 打印源代码
# #     print(browser.page_source)# 打印源代码
# #     doc = pq(browser.page_source)
#     regex=re.compile(r'<title>(.*?)</title>')
#     rest=regex.findall(browser.page_source)
#     print(rest)
# finally:
#     print('ok')
#     browser.close() # 关闭浏览器