##  requests 생성
import requests
from bs4 import BeautifulSoup

url = 'https://www.melon.com/chart/index.htm'
header = {'User-Agent': 'Mozila/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
#print(response.text)
#print(soup)

##lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
titles = soup.select("div.ellipsis.rank01 a")
singers = soup.select("div.ellipsis.rank02")

titles_list = [ title.text for title in titles]
#print(titles_list)

singer_list=[]
singer_list = [ singer.find('a').text for singer in singers]
# for singer in singers:
#     singer_list.append( singer.find('a').text )

##print(singer_list)

rank=10
for r in range(rank):
    print(str(r+1) + '위: ' + titles_list[r] + ' - ' + singer_list[r])