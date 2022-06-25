#!/bin/bash
cd ..
python conclude.py > /dev/null 2>&1 &
python autoconclude.py > /dev/null 2>&1 &
