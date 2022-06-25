#!/bin/bash
ps -ef | grep conclude | grep -v grep | awk '{print $2}' | xargs kill -9

