#!/bin/zsh

python3 generate.py | python3 map.py | sort | python3 reduce.py
