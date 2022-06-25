#!/bin/bash
ps -ef | grep autoconclude | grep -v grep | awk '{print $2}' | xargs kill -9

