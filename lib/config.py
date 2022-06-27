#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import yaml
from . import logger
import tweepy
log = logger.get_logger(loglevel='INFO')


class TweepyAPIWrapper:
    """Load Configuration and get api with twepy."""

    def __init__(self, file_path=None):
        # Load config from environment variable
        self.load_env()
        # Load config from Configuration file when environment variable is not defined.
        if self._is_any_conf_empty() and file_path:
            self.load_config(file_path)
        # Raise exception if environment variable / config file do not have enough information.
        if self._is_any_conf_empty():
            msg=f'''
                 Either Environment Variable or Config File is wrong. 
                 Currently following value is missing.
                 api_key : {self.api_key}
                 api_secret : {self.api_secret}
                 access_token : {self.access_token}
                 access_token_secret : {self.access_token_secret}
                 bearer_token: {self.bearer_token}
                 1. Specify environment variable
                    e.g.)
                    export API_KEY="<Please obtain API key from twitter api>"
                    export API_SECRET="<Please obtain API secret from twitter api>"
                    export ACCESS_TOKEN="<Please obtain Access Token from twitter api>"
                    export ACCESS_TOKEN_SECRET="<Please obtain Access token secret from twitter api>"
                    export BEARER_TOKEN="<Please obtain Bearer Token secret from twitter api>
                 2. Write your config file with following format. 
                    Currently you need to define following contents to {file_path}
                    ```
                    api_key: "<Please obtain API key from twitter api>"
                    api_secret: "<Please obtain API secret from twitter api>"
                    access_token: "<Please obtain Access Token from twitter api>"
                    access_token_secret: "<Please obtain Access Token secret from twitter api>"
                    bearer_token: "<Please obtain Bearer Token secret from twitter api>"
                    ```
                 '''
            raise ValueError(msg)


    def load_env(self):
        log.info('Load Config from environment variable.')
        self.api_key = os.getenv('API_KEY')
        self.api_secret = os.getenv('API_SECRET')
        self.access_token = os.getenv('ACCESS_TOKEN')
        self.access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
        self.bearer_token=os.getenv('BEARER_TOKEN')

    def _is_any_conf_empty(self):
        return any([not self.api_key, not self.api_secret, not self.access_token, not self.access_token_secret, not self.bearer_token])
   
    def load_config(self, file_path):
        log.info('Load Config from configuration file. {}'.format(file_path))
        ab_path = os.path.expanduser(file_path)
        if not os.path.exists(ab_path):
            return
        with open(ab_path) as f:
            config=yaml.safe_load(f)
            self.api_key = config.get('api_key',{})
            self.api_secret = config.get('api_secret',{})
            self.access_token = config.get('access_token',{})
            self.access_token_secret = config.get('access_token_secret',{})
            self.bearer_token = config.get('bearer_token')

    def get_api(self):
        auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return tweepy.API(auth)
