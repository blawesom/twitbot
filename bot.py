# coding: utf-8

import tweepy
from tweepy import TweepError
import ConfigParser

#path = '/root/twitbot/'
path = ''
cnf = ConfigParser.ConfigParser()
cnf.read(filenames='{0}config.ini'.format(path))

consumer_key = cnf.get(section='auth', option='consumer_key')
consumer_secret = cnf.get(section='auth', option='consumer_secret')
access_token = cnf.get(section='auth', option='access_token')
access_token_secret = cnf.get(section='auth', option='access_token_secret')

# Auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

search_result = api.search(q='concours&gagner', count=200)

operations = {'RT': 0, 'Followed': 0, 'Unfollowed': 0}
with open(name='{0}followed.log'.format(path), mode='a') as followed:
    for i, result in enumerate(search_result):
        print 'tweet n°{0}'.format(i+1)
        if not result.retweeted:
            try:
                api.retweet(result.id)
                operations['RT'] += 1
                if 'follow' in result.text.lower():
                    api.create_friendship(result.author.id)
                    operations['Followed'] += 1
                    followed.write('{0}:\t{1}\n'.format(result.author.screen_name, 'followed'))
            except TweepError as e:
                with open(name='{0}error.log'.format(path), mode='a') as log:
                    log.write('{0}\n'.format(e.message[0]['message']))

    # # Following cleaning (limit of 5000 following)
    # if len(followed.read()) > 4000:
    #     lines = followed.read().split('\n')
    #     for line in lines:
    #         try:
    #             api.destroy_friendship(line.split(':')[0])
    #             operations['Unfollowed'] += 1
    #             followed.write('{0}:\t{1}\n'.format(line.split(':')[0], 'unfollowed'))
    #         except:
    #             pass

with open(name='{0}operations.log'.format(path), mode='a') as log:
    log.write('RT: {0}\t Followed: {1}\t Unfollowed: {2}\n'.format(operations['RT'],
                                                                 operations['Followed'],
                                                                 operations['Unfollowed']))



