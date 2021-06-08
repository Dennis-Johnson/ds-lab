'''
# reduce.py
Find maximum population entry for each conutry
Input: The output from map.py on stdin
'''

import sys

currentMaxPop = -1
currentCountry = None

for i, line in enumerate(sys.stdin):
    if i > 80:
        break
    
    # Try to read a single line of input, continue otherwise
    try:
        country, population = line.strip().split("\t", 1)
    except Exception as e:
        continue
    
    # Try to parse a number, continue otherwise
    try:
        population = int(population)
    except ValueError as valErr:
        continue

    if currentCountry == country:
        if population > currentMaxPop:
            currentMaxPop = population
    
    else: 
        if currentCountry:
            print("Max Population in {}:\t{}".format(currentCountry, currentMaxPop))
        currentCountry = country
        currentMaxPop = population


if currentCountry == country:
    print("Max Population for {}:\t{}".format(currentCountry, currentMaxPop))
