'''
# maxReducer.py
'''

import sys

mostFreqConfirmed = None
mostFreqDeaths    = None
mostFreqConfirmed = None
currentMaxConfirmed = -1
currentMaxDeaths    = -1
currentMaxRecovered = -1

for line in sys.stdin:
    country, confirmed, deaths, recovered = line.strip().split('\t')
    
    confirmed = int(confirmed)
    deaths    = int(deaths)
    recovered = int(recovered)

    if confirmed > currentMaxConfirmed:
          currentMaxConfirmed = confirmed
          mostFreqConfirmed = country
    if deaths > currentMaxDeaths:
          currentMaxDeaths = deaths
          mostFreqDeaths = country
    if recovered > currentMaxRecovered:
          currentMaxRecovered = recovered
          mostFreqRecovered = country

# output mostFreq country(s) for all 3 stats
print( 'Most confirmed cases: %s\t%s' % (mostFreqConfirmed, currentMaxConfirmed))
print( 'Most deaths         : %s\t%s' % (mostFreqDeaths, currentMaxDeaths   ))
print( 'Most recovered cases: %s\t%s' % (mostFreqRecovered, currentMaxRecovered))
