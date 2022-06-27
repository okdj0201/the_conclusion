#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import schedule
import argparse
import datetime
from time import sleep
import tweepy
from lib import logger
from lib.config import TweepyAPIWrapper

# DO NOT CHANGE CONCLUSION. It is a sacred variable that cannot be changed even by the power of God.
KINNIKUN="kinnikun0917"
LOG = logger.get_logger()
FAV_CRITERIA_HOUR=24

def fav():
    LOG.info("Let's look into Kinnikun's tweet...")
    try:
        api = TweepyAPIWrapper('~/.tweet_api.yml').get_api()
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

