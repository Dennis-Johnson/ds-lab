#!/bin/zsh

python3 parse_csv.py ../datasets/heart_disease_data.csv | python3 mapper.py | sort | python3 reducer.py
