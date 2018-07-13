#! /usr/bin/python3
# newsapi.og api key :  2ffba65c92de4a4aa4cc27dc05442ca9

from  newsapi import NewsApiClient

newapi = NewsApiClient(api_key='2ffba65c92de4a4aa4cc27dc05442ca9')

headlines = newapi.get_everything(
			q= 'bitcoin',
			sources ='bbc-news, cnn, the-verge',
		#	country = 'us',
			language ='en',
		#	from = '2018-06-01',
#			category = 'business'
#			sort_by = 'relevancy'
)

articles = headlines['articles']

#for news in articles:
#	print(news)


print(articles[0]['url'])
