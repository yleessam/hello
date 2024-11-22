import requests
jtbc_economy = requests.get("http://fs.jtbc.joins.com//RSS/economy.xml")
#print(jtbc_economy.text)

from bs4 import BeautifulSoup
economy_new_soup = BeautifulSoup(jtbc_economy.content, "xml")
link_list = economy_new_soup.select("item > link")

print(len(link_list),'건')

#print(link_list[1].text)


# news = requests.get(link_list[0].text)
# news_soup = BeautifulSoup(news.content, "html.parser")

# #title 추출
# title_el = news_soup.find("meta", {"name":"twitter:title"})
# title = title_el["content"]

# #description 추출
# desc_el = news_soup.find("meta", {"name":"twitter:description"})
# description = desc_el["content"]
# print(description)

news_list = []

#list 순회
for link in link_list:
    #print(link.text)
    news = requests.get(link.text)
    news_soup = BeautifulSoup(news.content, "html.parser")

    title_el = news_soup.find("meta", {"name":"twitter:title"})
    title = title_el["content"]

    #description 추출
    desc_el = news_soup.find("meta", {"name":"twitter:description"})
    description = desc_el["content"]

    news_list.append([title, description])
    #print(title,description)

import pandas as pd
df = pd.DataFrame(news_list, columns=["title", "description"])
print(df.head())
df.to_csv("jtbc_news.csv", index=False)