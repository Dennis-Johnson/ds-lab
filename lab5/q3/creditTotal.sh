#!/bin/zsh

cat ../datasets/german_credit.csv | python3 map.py | sort | python3 reduce.py
