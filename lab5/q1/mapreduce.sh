#!/bin/zsh

cat input.txt | python3 mapper.py | sort | python3 reducer.py
