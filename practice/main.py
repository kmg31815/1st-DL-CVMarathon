import requests
from bs4 import BeautifulSoup

url = 'https://movies.yahoo.com.tw/movie_comingsoon.html'
resp = requests.get(url)
resp.encoding = 'utf-8'

soup = BeautifulSoup(resp.text, 'lxml')
html = soup.find("ul", attrs={'class':'release_list'})
movie_items = html.find_all("li")

for p in movie_items:
    movies = p.find("div", attrs={'class': 'release_info'}).find("div", attrs={'class': 'release_movie_name'}).find("a")
    date = p.find("div", attrs={'class': 'release_info'}).find("div", attrs={'class': 'release_movie_time'}).text
    print("Movie:" + movies["data-ga"][24:].replace("']", "") + "\n" + date)
