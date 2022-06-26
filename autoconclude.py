#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import argparse
import datetime
import schedule
from time import sleep
import tweepy
from lib import logger
from lib.config import TweetConfigLoader

REPLY="しねない"
REPLY_CRITERIA_HOUR=1
SCHEDULE_CYCLE_HOUR=1
LOG = logger.get_logger(logdir=f'{os.getcwd()}/log', logfile='autoconclude.log')

def autoreply():
    try:
        LOG.info('Autoreply...')
        config=TweetConfigLoader()
        auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
        auth.set_access_token(config.access_token, config.access_token_secret)
        api = tweepy.API(auth)
        mentions = api.mentions_timeline()
        time_now =  datetime.datetime.now(datetime.timezone.utc)
        for mention in api.mentions_timeline():
            tweet_datetime = datetime.datetime.strptime(mention._json['created_at'], '%a %b %d %H:%M:%S %z %Y')
            if time_now < tweet_datetime + datetime.timedelta(hours=REPLY_CRITERIA_HOUR):
                 LOG.info(f'Generating autoreply to {mention._json["user"]["name"]}, Tweeted {mention._json["text"]}')
                 api.update_status(status=f'@{mention._json["user"]["screen_name"]} {REPLY}', in_reply_to_status_id=mention._json['id'])
    except Exception as e:
        LOG.error('Error during autoreply.')
        LOG.error(f'{e}')

def schedule_auto_reply():
    schedule.every(SCHEDULE_CYCLE_HOUR).hours.do(autoreply)
    while True:
        try:
          schedule.run_pending()
          sleep(1)
        except Exception as e:
          LOG.error('Something went failed during schedule.')
          LOG.error(f'{e}')

def _argparse():
    parser = argparse.ArgumentParser(description='Please specify options if required.')
    parser.add_argument('-s', '--schedule', help='Defines the cycle for Tweeting. Specify in hours. The default cycle is 1 hours.')
    parser.add_argument('-r', '--reply', help='Defines how many hours ago replies should be responded to. Specify in hours. Default is 1 hour.')
    return parser.parse_args()


def main():
    args = _argparse()
    if args.schedule:
        global SCHEDULE_CYCLE_HOUR
        SCHEDULE_CYCLE_HOUR = args.schedule
    if args.reply:
        global REPLY_CRITERIA_HOUR
        REPLY_CRITERIA_HOUR = args.reply
    LOG.info(f'Bot started with {SCHEDULE_CYCLE_HOUR}-hour cycles. Replies will send {REPLY_CRITERIA_HOUR} hour mentions.')
    schedule_auto_reply()

if __name__ == '__main__':
    main()
