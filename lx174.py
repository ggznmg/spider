from selenium import webdriver
from selenium.webdriver import ActionChains # 行动链
browser= webdriver.Chrome()  # 绑定谷歌
url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url) # 打开url
# <iframe frameborder="0" id="iframeResult" style="height: 306px;"></iframe>
# switch_to.frame转换成iframe元素标签(xml)，iframeResult为其id
browser.switch_to.frame('iframeResult') 
# <div id="droppable" class="ui-droppable">请放置到这里！</div>
# 控制拖拽块
source=browser.find_element_by_css_selector('#draggable')
#<div id="draggable" class="ui-draggable" style="position: relative; left: 290px; top: 27px;">请拖拽我！</div>

# 控制目标块
target=browser.find_element_by_css_selector('#droppable')
actions=ActionChains(browser)  # 开启行动链
actions.drag_and_drop(source=source,target=target) # 将source 拖拽到target
actions.perform()