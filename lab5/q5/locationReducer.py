"""
locationReducer.py

similar to wordcount aggregator from q1 (/q1/reducer.py)
"""

import sys

current_country = None

total_confirmed = 0
total_deaths = 0
total_recovered = 0

for i, line in enumerate(sys.stdin):
    
    # parse input from map.py, piped from stdin
    country, confirmed, deaths, recovered = line.strip().split('\t')

    try:
        confirmed = int(confirmed)
        deaths    = int(deaths)
        recovered = int(recovered)
    
    except ValueError:
        print("Line {}: ValueError encountered".format(i))
        continue

    if current_country == country:
        total_confirmed += confirmed
        total_deaths += deaths
        total_recovered += recovered

    else: 
        if current_country:
            print("{}\t{}\t{}\t{}".format(current_country, total_confirmed, total_deaths, total_recovered))
        current_country = country
        total_confirmed = confirmed
        total_deaths = deaths
        total_recovered = recovered

if current_country == country:
    print("{}\t{}\t{}\t{}".format(current_country, total_confirmed, total_deaths, total_recovered))
    
