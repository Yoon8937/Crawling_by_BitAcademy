import pymongo
# html전체를 가져옴.
# <tb> 전체표에서 가져옴


from bs4 import BeautifulSoup
import urllib.request

stores = [] #결과를 저장할 리스트
encText = urllib.parse.quote("서울")
# print(encText)

for page in range(1,17):
    Hollys_url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&gugun=&store=&sido='%(page)
    Hollys_url += encText
    # print(Hollys_url)
    html = urllib.request.urlopen(Hollys_url)
    soupHollys = BeautifulSoup(html, "html.parser")
    # print(soupHollys)
    tag_tbody = soupHollys.find("tbody")
    # print(tag_tbody)

    for store in tag_tbody.find_all('tr'):
        store_info = dict()# 개별 매장 정보를 사전 형태로 저장
        store_td = store.find_all('td')
        print(type(store_td), store_td)
        print("==================================================================================")
        store_name = store_td[1].string
        store_info["store_name"] = store_td[1].string

        store_sido = store_td[0].string
        store_info["store_sido"] = store_td[0].string

        store_address = store_td[3].string; store_info["store_address"] = store_td[3].string
        store_phone = store_td[5].string; store_info["store_phone"] = store_td[5].string
        # print('매장명', store_name, '시도구', store_sido, '주소', store_address, '전화번호', store_phone)
        stores.append(store_info)

for store in stores:
    print(store)


# import mongoDB
# conn = pymongo.MongoClient()#연결
# db = conn.bitDB #bitDB 데이터베이스 이름
# Holly = db.Holly
#
# db.Holly.insert_many(stores)

































