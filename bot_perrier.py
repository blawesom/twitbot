# coding: utf-8

import tweepy
from tweepy import TweepError
import time, random
import datetime
import ConfigParser


def init_auth():
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

    return auth


def wait_rand_time():
    time.sleep((random.random()*10+5)*60)
    return


def check_time():
    if datetime.datetime.now().hour is in range(8,20):
        return True
    return False


if __name__ == "__main__":
    """ This bot tweets a stand ard text every 5 to 15 minutes.
        It will not post anything outside 'normal' human hours.
        Challenge ends the 29th of may.
    """

    texttweet = "#SmashPerrier #Prems"

    auth = init_auth()
    api = tweepy.API(auth)

    while datetime.date.today() < datetime.date(2017, 5, 29):
        if check_time:
            wait_rand_time()
            api.tweet(texttweet)
            print "I posted at {} !".format(datetime.datetime.now())

    print('Win')
