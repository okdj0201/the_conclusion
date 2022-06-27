#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import argparse
import datetime
import schedule
from time import sleep
import tweepy
from lib import logger
from lib.config import TweepyAPIWrapper

REPLY="しねない"
REPLY_CRITERIA_HOUR=1
LOG = logger.get_logger()

def reply():
    try:
        LOG.info('Autoreply...')
        api = TweepyAPIWrapper('~/.tweet_api.yml').get_api()
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

