#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import schedule
import argparse
import datetime
from time import sleep
import tweepy
from lib import logger
from lib.config import TweetConfigLoader

# DO NOT CHANGE CONCLUSION. It is a sacred variable that cannot be changed even by the power of God.
KINNIKUN="kinnikun0917"
LOG = logger.get_logger(logdir=f'{os.getcwd()}/log', logfile='autofav.log')
SCHEDULE_CYCLE_HOUR=24
FAV_CRITERIA_HOUR=24

def fav():
    LOG.info("Let's look into Kinnikun's tweet...")
    try:
        config=TweetConfigLoader()
        auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
        auth.set_access_token(config.access_token, config.access_token_secret)
        api = tweepy.API(auth)
        timeline_kinnnikun = api.user_timeline(screen_name=KINNIKUN)
        time_now =  datetime.datetime.now(datetime.timezone.utc)
        for kinniku_tweet in timeline_kinnnikun:
            tweet_datetime = datetime.datetime.strptime(kinniku_tweet._json['created_at'], '%a %b %d %H:%M:%S %z %Y')
            if time_now < tweet_datetime + datetime.timedelta(hours=FAV_CRITERIA_HOUR):
                LOG.info(f"Tweet id: {kinniku_tweet._json['id']}")
                LOG.info(f"He says...: {kinniku_tweet._json['text']}")
                try:
                  api.create_favorite(id=kinniku_tweet._json['id'])
                  LOG.info('So cool! Favorite!')
                except Exception as e:
                    LOG.error('Something went failed during favorite...')
                    LOG.error(f'{e}')
    except Exception as e:
        LOG.error('Something went failed during favorite...')
        LOG.error(f'{e}')

def schedule_bot():
    LOG.info('Starting Schedule...')
    schedule.every(SCHEDULE_CYCLE_HOUR).hours.do(tweet)
    while True:
        try:
          schedule.run_pending()
          sleep(3600 * SCHEDULE_CYCLE_HOUR)
        except Exception as e:
          LOG.error('Something went failed during schedule.')
          LOG.error(f'{e}')

def _argparse():
    parser = argparse.ArgumentParser(description='Please specify options if required.')
    parser.add_argument('-s', '--schedule', help='Defines the cycle for Tweeting. Specify in hours. The default cycle is 12 hours.')
    return parser.parse_args()

def main():
    args = _argparse()
    if args.schedule:
        global SCHEDULE_CYCLE_HOUR
        SCHEDULE_CYCLE_HOUR = args.schedule
    LOG.info(f'Bot started with {SCHEDULE_CYCLE_HOUR}-hour cycles.')
    fav()

if __name__ == '__main__':
    main()
