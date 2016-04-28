# coding: utf-8

import tweepy
import ConfigParser

cnf = ConfigParser.ConfigParser()
cnf.read(filenames='config.ini')

consumer_key = cnf.get(section='auth', option='consumer_key')
consumer_secret = cnf.get(section='auth', option='consumer_secret')
access_token = cnf.get(section='auth', option='access_token')
access_token_secret = cnf.get(section='auth', option='access_token_secret')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

search_result = api.search(q='concours&gagner', count=20)

for result in search_result:
    if not result.retweeted:
        if 'RT' in result.text:
            try:
                api.retweet(result.id)
            except:
                pass
        if 'follow' in result.text.lower():
            try:
                api.create_friendship(result.author.id)
            except:
                pass


