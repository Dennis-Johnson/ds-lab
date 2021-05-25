#!/bin/zsh

python3 parse_csv.py ../datasets/covid_19_data.csv | python3 freqMap1.py | sort | python3 freqRed1.py | python3 freqMap2.py | sort | python3 freqRed2.py
