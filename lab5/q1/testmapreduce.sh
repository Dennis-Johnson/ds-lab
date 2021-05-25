#!/bin/zsh

cat test.txt | python3 mapper.py | sort | python3 reducer.py
