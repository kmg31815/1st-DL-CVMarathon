import requests
from bs4 import BeautifulSoup

input_keyword = "防彈少年團"  # 這裡可以自己定義有興趣的關鍵字

utf8_url = repr(input_keyword.encode('UTF-8')).upper()  # 編碼成UTF-8並轉成大寫字元
utf8_url = utf8_url.replace("\\X", "%")                 # 用 '%' 取代 '\X'
# print("%s: %s" % (input_keyword, utf8_url))
print("%s: %s" % (input_keyword, utf8_url[2:-1:1]))     # 擷取中間的編碼結果
# [2:-1:1] => 取第2個~最後一個，每次後推一個
print()

# 組成Wiki關鍵字搜尋的網址格式
root_keyword_link = '/wiki/' + utf8_url[2:-1:1]
print(root_keyword_link)
print()

headers = {
    'authority': 'zh.wikipedia.org',
    'method': 'GET',
    'path': '/wiki/' + root_keyword_link,
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': 'GeoIP=TW:NWT:New_Taipei:24.94:121.54:v4; zhwikimwuser-sessionId=bf6409fe2a9df6501c39; WMF-Last-Access=11-Jul-2021; WMF-Last-Access-Global=11-Jul-2021; zhwikiwmE-sessionTickLastTickTime=1625998688788; zhwikiwmE-sessionTickTickCount=1; zhwikiel-sessionId=1cad118585385b0bcb33',
    'referer': 'https://zh.wikipedia.org/zh-tw/%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = 'https://zh.wikipedia.org' + root_keyword_link  # 組合關鍵字查詢URL
resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'

html = BeautifulSoup(resp.text, "lxml")
content = html.find(name='div', attrs={'id':'mw-content-text'}).find_all(name='p')

#
# 解析回傳資料，並萃取文章內容
#
for paragraph in content:
    print(paragraph.get_text())