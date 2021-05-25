#!/bin/zsh

cat test.txt | python3 freqMap1.py | sort | python3 freqRed1.py | python3 freqMap2.py | sort | python3 freqRed2.py
