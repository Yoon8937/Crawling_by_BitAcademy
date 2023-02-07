from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import re #정규표현식



# dining_url = "https://www.diningcode.com/list.dc"
dining_url = "https://www.diningcode.com/list.dc?query=%EC%84%9C%EC%9A%B8"
chrome_options = webdriver.ChromeOptions()

#크롬 Webdriver객체 생성
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wd.get(dining_url)
time.sleep(1)
html = wd.page_source
soup = BeautifulSoup(html,'html.parser')


stores = soup.select('div.InfoHeader>h2') #div에서 자식 <h2를 뽑아냄
scores = soup.select('div.Rate>p.Score') #div 이름이 class인것에서 <p태그에서 score인것을 추출
userScores = soup.select('div.Rate>p.UserScore')
# print(stores)
# for i in stores:
#     print(i)


store_list = list()
for index, store in enumerate(stores):
    store_dict = dict()
    print(store.text)
    # store_dict["store_name"] = re.sub(r'[^\uAC00-\uD7A3\s]','',store.text)# ^ 제외한 (정규식) 즉 한글을 제외한 ㅓ것을 모두 빈""대체
    # print("After : ",store.text)
    print("===================================================================")
    # store_dict["store"] = scores[index].select_one("span").text
    # userScore = re.sub('<p.*?>.*?/>|</p>','',str(userScores[index]))
    # print('userScore', userScore)
    # store_dict["userScore"] = re.sub('\(\W*\)','',str(userScore)).strip()
    # scorer = re.findall('\(([^)]+)', userScore)
    # store_dict["scorer"] = scorer[0]
    # store_list.append(store_dict)

    # store_dict = dict()
    # store_dict["store_name"] = re.sub(r'[^\uAC00-\uD7A3\s]','',store.text)
    # store_dict["score"] = scores[index].select_one('span').text
    # userScore=re.sub('<p.*?>.*?/>|</p>',"",str(userScores[index]))
    # print('userScore', userScore)
    # store_dict["userScore"] = re.sub('\(\w*\)',"", str(userScore)).strip()
    # scorer = re.findall('\(([^)]+)', userScore)
    # store_dict["scorer"]= scorer[0]
    # store_list.append(store_dict)
#
# for store in store_list:
#     print(store)



# import pymongo
# conn = pymongo.MongoClient()#연결
# db = conn.bitDB #bitDB 데이터베이스 이름
# Stores = db.Stores
#
# db.Stores.insert_many(store_list)





























