#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import schedule
import argparse
import datetime
from time import sleep
import tweepy
from lib import logger
from autoconclude import reply
from autofav import fav
from conclude import tweet

# DO NOT CHANGE CONCLUSION. It is a sacred variable that cannot be changed even by the power of God.
LOG = logger.get_logger(logdir=f'{os.getcwd()}/log', logfile='bot.log')
TWEET_SCHEDULE_CYCLE_HOUR=12
REPLY_SCHEDULE_CYCLE_HOUR=1
FAV_SCHEDULE_CYCLE_HOUR=24

def schedule_bot():
    LOG.info(f'Starting schedule for auto-tweet with {TWEET_SCHEDULE_CYCLE_HOUR} hour duration.')
    schedule.every(TWEET_SCHEDULE_CYCLE_HOUR).hours.do(tweet)
    LOG.info(f'Starting schedule for auto-tweet with {REPLY_SCHEDULE_CYCLE_HOUR} hour duration.')
    schedule.every(TWEET_SCHEDULE_CYCLE_HOUR).hours.do(reply)
    LOG.info(f'Starting schedule for auto-tweet with {FAV_SCHEDULE_CYCLE_HOUR} hour duration.')
    schedule.every(TWEET_SCHEDULE_CYCLE_HOUR).hours.do(fav)
    while True:
        try:
          schedule.run_pending()
          sleep(1)
        except Exception as e:
          LOG.error('Something went failed during schedule.')
          LOG.error(f'{e}')

def _argparse():
    parser = argparse.ArgumentParser(description='Please specify options if required.')
    parser.add_argument('-t', '--tweet-schedule', help='Defines the cycle for tweeting. Specify in hours. The default cycle is 12 hours.')
    parser.add_argument('-r', '--reply-schedule', help='Defines the cycle for auto-reply. Specify in hours. The default cycle is 12 hours.')
    parser.add_argument('-f', '--fav-schedule', help='Defines the cycle for auto-fav. Specify in hours. The default cycle is 12 hours.')
    return parser.parse_args()

def main():
    args = _argparse()
    if args.tweet_schedule:
        global TWEET_SCHEDULE_CYCLE_HOUR
        TWEET_SCHEDULE_CYCLE_HOUR = args.tweet_schedule
    if args.reply_schedule:
        global REPLY_SCHEDULE_CYCLE_HOUR
        REPLY_SCHEDULE_CYCLE_HOUR = args.reply_schedule
    if args.fav_schedule:
        global FAV_SCHEDULE_CYCLE_HOUR
        FAV_SCHEDULE_CYCLE_HOUR = args.fav_schedule
    schedule_bot()

if __name__ == '__main__':
    main()
