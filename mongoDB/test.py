# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import re #정규표현식
# html_page = '<html><body>test</body></html>'
# print(type(html_page))
# html_tag =re.compile('<.*?>')
# text = re.sub(html_tag, '', html_page)
#
# print(text)



url = 'https://n.news.naver.com/mnews/article/009/0005084584?sid=101'
chrome_options = webdriver.ChromeOptions()

wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wd.get(url)

wd.get(url)
time.sleep(1)
html = wd.page_source
soup = BeautifulSoup(html, 'html.parser')
date_tag = soup.select_one("div#ct> div.media_end_head.go_trans > div.media_end_head_info.nv_notrans > div.media_end_head_info_datestamp > div > span")

date_tag = str(date_tag)
html_tag =re.compile('<.*?>')
text = re.sub(html_tag, '', date_tag)
print(text)









