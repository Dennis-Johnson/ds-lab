#!/bin/zsh

cat test.txt | python3 map.py | sort | python3 reduce.py
