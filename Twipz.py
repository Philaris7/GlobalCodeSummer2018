#! /usr/bin/python3

import tweepy
#consumer key(api key) : YGSd5euOeA2zXIy4WzphidDwF
#consumer secret(api secret) : 8o26Xg8qn7cXLh7mOh52q9Kur61HHGixePPboLxylddFmiWzDh
#acces token : 1184027455-oO3fKZiSo51eCayAXSE3zhalAUbFqkznZs8CcKM
#access token secret : Ww2lGf79g0UyfN3qxjUAK5LUL6nsDRPY8rFvCKFljPN8z

api_key = 'YGSd5euOeA2zXIy4WzphidDwF'
secret_key = '8o26Xg8qn7cXLh7mOh52q9Kur61HHGixePPboLxylddFmiWzDh'
acc_token = '1184027455-oO3fKZiSo51eCayAXSE3zhalAUbFqkznZs8CcKM'
acc_secret = 'Ww2lGf79g0UyfN3qxjUAK5LUL6nsDRPY8rFvCKFljPN8z'


auth = tweepy.OAuthHandler(api_key, secret_key)
auth.set_access_token(acc_token, acc_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

#for tweet in public_tweets:
#	print(tweet.text, sep="\n")

user = api.get_user('ABP_Aris')

print('User name: ', user.screen_name)


for f in user.friends():
	print(f.screen_name)


for f in tweepy.Cursor(api.followers).items():
	print(f.screen_name)


#for status in tweepy.Cursor(api.user_timeline).items():
    # process status here
#    print(status)
