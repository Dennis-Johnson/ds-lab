#!/bin/zsh

cat ../datasets/covid_19_data.csv | python3 map.py | sort | python3 locationReducer.py | python3 maxReducer.py
