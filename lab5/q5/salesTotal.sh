#!/bin/zsh

cat example.txt | python3 map_test.py | sort | python3 reduce_test.py
