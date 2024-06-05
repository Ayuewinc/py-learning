import requests
import re
from bs4 import BeautifulSoup
import pandas


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

def crawler_bs(resp):
    soup = BeautifulSoup(resp.content, 'lxml')
    #通过CSS选择器从页面中提取包含电影标题/评分的span标签
    titles = soup.select('div.info > div.hd > a > span:nth-child(1)')
    ratings = soup.select('div.info > div.bd > div > span.rating_num')
#   通过html选择器从页面中提取包含电影标题/评分的span标签
#   titles = soup.find_all('span', {'class' : 'title'})
#   ratings = soup.find_all('span', {'class' : 'rating_num'})
    """ for element in ratings_content:
        ratings.append(element.string) """
    return zip(titles, ratings)

def crawler_re(resp):
    title_pattern = re.compile(r'<span class="title">([^&].*?)</span>')
    rating_pattern = re.compile(r'<span class="rating_num".*?>(.*?)</span>')
    titles = title_pattern.findall(resp.text)
    ratings = rating_pattern.findall(resp.text)
    return zip(titles, ratings)

def data2xlsx(table_header, table_data):
    # table_header, table_data are list
    dataframe = pandas.DataFrame(dict(zip(table_header, table_data)))
    dataframe.to_excel("./douban250.xlsx", encoding='gbk', index=False)


for i in range(0, 1):
    url = f'https://movie.douban.com/top250?start={i * 25}'
    resp = requests.get(url, headers=headers)
#    titles_ratings = crawler_re(resp)
    """
    titles_ratings = crawler_bs(resp)
    for title, rating in titles_ratings:
        print(title.text)
        print(rating.text)
    """
    titles_ratings = crawler_re(resp)
    table_header = {'title', 'rating'}
    table_titles, table_ratings = zip(*titles_ratings)
    table_data = {table_titles, table_ratings}
    data2xlsx(table_header, table_data)
