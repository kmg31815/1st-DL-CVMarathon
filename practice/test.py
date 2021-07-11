import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/NBA/index.html'
resp = requests.get(url)

soup = BeautifulSoup(resp.text, "lxml")
for d in soup.find_all(class_="title"):
    print(d.text.replace('\n', ''))
    try:
        r = BeautifulSoup(requests.get('https://www.ptt.cc'+d.find('a')['href']).text, "lxml")
#         print(r.find_all(class_='article-meta-value'))
        print('作者: ' + r.find_all(class_='article-meta-value')[0].text)
        print('時間: ' + r.find_all(class_='article-meta-value')[3].text+'\n')
        break
    except:
        continue