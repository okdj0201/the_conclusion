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
LOG = logger.get_logger()

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

