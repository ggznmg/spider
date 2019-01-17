from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

browser = webdriver.Chrome()
browser.get("https://book.douban.com/tag/%E6%95%A3%E6%96%87")
# imgs=browser.find_elements_by_xpath('//div[#content]')
# elem = driver.find_element_by_css_selector("#q")
# print(elem)
# elem.clear()
# elem.send_keys("内衣")
# # elem.send_keys(Keys.RETURN)
# # search = driver.find_element_by_css_selector("#q")
# browser.save_screenshot('text.png')
# browser.close()
# from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://book.douban.com/tag/%E6%97%A5%E6%9C%AC%E6%96%87%E5%AD%A6')
imgs = driver.find_elements_by_xpath(
    '//*[@id="subject_list"]/ul/li/div[1]/a/img')

titles = driver.find_elements_by_xpath(
    '//*[@id="subject_list"]/ul/li/div[2]/h2/a')

auths = driver.find_elements_by_xpath(
    '//*[@id="subject_list"]/ul/li/div[2]/div[1]')
for img, title, auth in zip(imgs, titles, auths):
    print(title.get_attribute('title'), img.get_attribute(
        'src'), auth.text.split(' / ')[0])