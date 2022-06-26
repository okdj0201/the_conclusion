#!/bin/bash
ps -ef | grep schedule_bot | grep -v grep | awk '{print $2}' | xargs kill -9

