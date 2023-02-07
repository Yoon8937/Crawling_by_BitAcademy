from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import re #정규표현식

naverNews_url = "https://news.naver.com/main/list.naver?mode=LS2D&sid2=258&sid1=101&mid=shm&date=20230206&page=1"
chrome_options = webdriver.ChromeOptions()


wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wd.get(naverNews_url)
time.sleep(1)
html = wd.page_source
soup = BeautifulSoup(html,'html.parser')
# tag_tbody = soup.find("tbody")
# print(tag_tbody)
# stores = soup.select('li')
# stores = soup.select('li > dl > dt')
# stores = soup.select('li ')
stores = soup.select('li > dl')
# stores = soup.select('li > dl > dt')

# print(stores)

def getArticleScript(article_script_url):
    wd.get(article_script_url)
    time.sleep(1)
    html = wd.page_source
    soup = BeautifulSoup(html, 'html.parser')
    tmp = soup.select("div#dic_area")
    # print('tmp :', "type :",type(tmp),tmp)
    tag = re.compile('<.*?>')
    script = ""
    for i in tmp:
        i = str(i)
        txt = re.sub(tag, '', i).strip()
        new_txt = txt.replace("\n", "")
        script = new_txt
    return script
        # print(new_txt)
        # script += txt.strip() + " "
        # print("본문 :",len(txt),type(txt),txt,"끝끝끝")
    # print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")


def getArticleDate(article_script_url):
    wd.get(article_script_url)
    html = wd.page_source
    soup = BeautifulSoup(html, 'html.parser')
    date_tag = soup.select_one(
        "div#ct> div.media_end_head.go_trans > div.media_end_head_info.nv_notrans > div.media_end_head_info_datestamp > div > span")
    date_tag = str(date_tag)
    html_tag = re.compile('<.*?>')
    script_date = re.sub(html_tag, '', date_tag)
    return script_date











def getTitleMethod(article):
    ansStr = ""
    tag = re.compile('<.*?>')
    for i in article:
        i = str(i)
        txt = re.sub(tag, '', i).strip()
        if txt == "":
            continue
        ansStr = txt
    return ansStr


for index,article in enumerate(stores):
    # print(index, article)

    # print("!!기사제목과 링크!! : ",article.find_all('a'))
    # print("!!기사제목과 링크!! : ",article.find_all('a'))

    # print('article : ',article)
    # method(article.select('a'))
    raw_html = article.find_all('a')
    title = getTitleMethod(raw_html)



    #완료
    print("제목 : ",title)
    print("!!링크!! : ",article.find('a')['href'])
    print("언론사 : ",article.find_all(attrs={'class': re.compile('^writing')})[0].string )
    # print("몇 분전 : ",article.find_all(attrs={'class': re.compile('^date is_new')})[0].string )

    article_script_url = article.find('a')['href']
    article_script = getArticleScript(article_script_url)
    print('본론 :',article_script)
    script_date = getArticleDate(article_script_url)
    print("작성 날짜 :",script_date)









































