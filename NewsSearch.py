import requests
import json
import pandas as pd
from newspaper import Article
import config


request_strings = ['gay', "don't say gay"]

#iterate trough strings


def news_query(strings_lst,url = "https://bing-news-search1.p.rapidapi.com/news/search" ):

    # url = "https://bing-news-search1.p.rapidapi.com/news/search"
    for s in strings_lst:
        querystring = {"q":s,"freshness":"Day","textFormat":"Raw","safeSearch":"Off"}

        headers = {
            'x-bingapis-sdk': "true",
            'x-search-location': "Florida",
            'x-rapidapi-host': "bing-news-search1.p.rapidapi.com",
            'x-rapidapi-key': config.api_key
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        # return response.json()
        #print("QUERY:"+s, response.text)
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=4)

def news_parse():
    #json_data = news_query(request_strings)
    # for item in json_data:
    #     for data_item in item['data']:
    #         print data_item['url'], data_item['value']
    #df = pd.read_json('data.json')
    with open('data.json', encoding='utf-8') as json_data:
        data = json.load(json_data)
    df = pd.DataFrame(data['value'])
    print(df[['url']])
    print(df[['url']].head(1))
    for index, row in df[['url']].head(1).iterrows():
        print(row['url'])
        url=row['url']
        article = Article(url)
        article.download()
        article.html
        article.parse()
        print("/n")
        print(article.text)

news_parse()

#news_query(request_strings)

#url = "https://www.hollywoodreporter.com/news/general-news/gabrielle-union-dont-say-gay-bill-at-disney-premiere-1235113450/"
#url = "https://www.tampabay.com/news/environment/2022/03/17/south-hillsboroughs-taps-could-be-bolstered-by-reclaimed-water/"
# url = "https://www.usatoday.com/videos/entertainment/2022/03/31/oscar-isaac-dont-say-gay-bill-sickening/7226474001/"
# article = Article(url)
# article.download()
# article.html
# article.parse()
# print("/n")
# print(article.text)