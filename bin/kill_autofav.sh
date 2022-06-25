#!/bin/bash
ps -ef | grep autofav | grep -v grep | awk '{print $2}' | xargs kill -9

