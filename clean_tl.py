# coding: utf-8
# Exceptions are silently passed because I truly don't give a shout :D

import tweepy
from tweepy import TweepError
import ConfigParser
import time
import sys


cnf = ConfigParser.ConfigParser()
#cnf.read(filenames='/root/twitbot/config.ini')
cnf.read(filenames='config.ini')

consumer_key = cnf.get(section='auth', option='consumer_key')
consumer_secret = cnf.get(section='auth', option='consumer_secret')
access_token = cnf.get(section='auth', option='access_token')
access_token_secret = cnf.get(section='auth', option='access_token_secret')
selfid = cnf.get(section='auth', option='selfid')

# Auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print api.rate_limit_status()

cleaned = 0
for friend_id in api.friends_ids(selfid):
    print api.get_user(friend_id).screen_name
    time.sleep(1)
    try:
        api.destroy_friendship(friend_id)
        cleaned += 1
        print '\t\tok'
    except TweepError as e:
        print e
        sys.exit()

print 'Unfollowed {0} accounts !'.format(cleaned)
