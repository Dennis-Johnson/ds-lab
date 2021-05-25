#!/bin/zsh

python3 parse_csv.py ../datasets/heart_disease_data.csv | python3 map.py | sort | python3 reduce.py
