#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from logging import FileHandler
from logging import Formatter
from logging import NOTSET
from logging import StreamHandler

import sys
import os

FORMAT = "[%(asctime)s] [%(levelname)s][%(module)s][%(funcName)s]: %(message)s"

def get_logger(logdir=False, logfile=False, loglevel='INFO'):
    logger = logging.getLogger(__name__)
    if logdir and logfile:
        file_handler = _get_file_handler(logdir,
                                        logfile,
                                        loglevel)
        logger.addHandler(file_handler)
    logging.basicConfig(level=NOTSET, format=FORMAT)
    return logger

def _get_file_handler(logdir, logfile, loglevel):
    if not os.path.isdir(logdir):
        os.makedirs(logdir, exist_ok=True)
    file_handler = FileHandler(f"{logdir}/{logfile}")
    file_handler.setLevel(loglevel)
    file_handler.setFormatter(
        Formatter(FORMAT)
    )
    return file_handler
