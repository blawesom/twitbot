# coding: utf-8

import twitter
import time, random
import datetime, sys
import ConfigParser


def init_auth():
    #path = '/root/twitbot/'
    path = ''
    cnf = ConfigParser.ConfigParser()
    cnf.read(filenames='{0}config.ini'.format(path))

    con_key = cnf.get(section='auth', option='consumer_key')
    con_secret = cnf.get(section='auth', option='consumer_secret')
    token_key = cnf.get(section='auth', option='access_token')
    token_secret = cnf.get(section='auth', option='access_token_secret')

    # Auth
    auth = twitter.Api(consumer_key=con_key,
                          consumer_secret=con_secret,
                          access_token_key=token_key,
                          access_token_secret=token_secret)

    return auth


def wait_rand_time():
    wait_time = (random.random()*10)*60
    print "Waiting {} min".format(wait_time/60)
    time.sleep(wait_time)
    return


def check_time():
    if datetime.datetime.now().hour in range(8,20):
        return True
    return False


if __name__ == "__main__":
    """ This bot tweets a stand ard text every 5 to 15 minutes.
        It will not post anything outside 'normal' human hours.
        Challenge ends the 29th of may.
    """

    texttweet = "#SmashPerrier #Prems"
    post_count = 0
    api = init_auth()
    print(api.VerifyCredentials())

    while datetime.date.today() < datetime.date(2017, 5, 29):
        if check_time:
            wait_rand_time()
            try:
                api.PostUpdate(texttweet)
                print "I posted at {} !".format(datetime.datetime.now())
                post_count = +1
            except:
                pass
    print('Win avec {} tweets !'.format(post_count))
