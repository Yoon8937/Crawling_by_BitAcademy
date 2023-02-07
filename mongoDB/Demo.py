from bs4 import BeautifulSoup
import urllib.request

# http://gimgane.co.kr/board/index.php?board=map_01&sca=all&type=list&select=&search=&page=2

stores = []
for page in range(1,27):
    kimGaNe_url = 'http://gimgane.co.kr/board/index.php?board=map_01&sca=all&type=list&select=&search=&page={0}'.format(page)
    html = urllib.request.urlopen(kimGaNe_url)
    soupKimgane = BeautifulSoup(html, "html.parser")
    tag_tbody = soupKimgane.find("tbody")
    # print(tag_tbody)
    # print("=====================================================================")

    for store in tag_tbody.find_all('tr'):
        # print(store)
        store_info = dict()
        store_td = store.find_all('td')
        # print(store_td)
        # print("================================================================")
#
# 1.매장명 2.매장주소 3.전화번호
        store_name = store_td[0].string
        store_info["매장명"] = store_td[0].string

        store_address = store_td[1].string
        store_info["매장주소"] = store_td[1].string

        store_num = store_td[2].string
        store_info["매장번호"] = store_td[2].string
        stores.append(store_info)

for i in stores:
    print(i)























