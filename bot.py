# coding: utf-8
# Exceptions are silently passed because I truly don't give a shout :D

import tweepy
import ConfigParser

cnf = ConfigParser.ConfigParser()
cnf.read(filenames='/root/twitbot/config.ini')

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
with open(name='/root/twitbot/followed.log', mode='a') as followed:
    for result in search_result:
        if not result.retweeted:
            if 'RT' in result.text:
                try:
                    api.retweet(result.id)
                    operations['RT'] += 1
                except:
                    pass
            if 'follow' in result.text.lower(): # and result.author.id.followed:
                try:
                    api.create_friendship(result.author.id)
                    operations['Followed'] += 1
                    followed.write('{0}:\t{1}\n'.format(result.author.id, 'followed'))
                except:
                    pass
    # Following cleaning (limit of 5000 following)
    if len(followed.read()) > 4000:
        lines = followed.read().split('\n')
        for line in lines:
            try:
                api.destroy_friendship(line.split(':')[0])
                operations['Unfollowed'] += 1
                followed.write('{0}:\t{1}\n'.format(line.split(':')[0], 'unfollowed'))
            except:
                pass

with open(name='/root/twitbot/operations.log', mode='a') as log:
    log.write('RT: {0}\t Followed: {1}\t Unfollowed: {2}'.format(operations['RT'],
                                                                 operations['Followed'],
                                                                 operations['Unfollowed']))



