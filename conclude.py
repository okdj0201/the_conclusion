#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import schedule
import argparse
from time import sleep
import tweepy
from lib import logger
from lib.config import TweetConfigLoader

# DO NOT CHANGE CONCLUSION. It is a sacred variable that cannot be changed even by the power of God.
CONCLUSION="しねない"
LOG = logger.get_logger(logdir=f'{os.getcwd()}/log', logfile='conclude.log')
SCHEDULE_CYCLE_HOUR=1

def tweet():
    LOG.info('Tweeting...')
    try:
        config=TweetConfigLoader()
        auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
        auth.set_access_token(config.access_token, config.access_token_secret)
        api = tweepy.API(auth)
        api.update_status(CONCLUSION)
        LOG.info('Tweeted!')
    except Exception as e:
        LOG.error('Something went failed during tweet.')
        LOG.error(f'{e}')

def schedule_bot():
    LOG.info('Starting Schedule...')
    schedule.every(SCHEDULE_CYCLE_HOUR).hours.do(tweet)
    while True:
        try:
          schedule.run_pending()
          sleep(1)
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
    schedule_bot()

if __name__ == '__main__':
    main()
