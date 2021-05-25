'''
map.py
input: expects covid_19_data.csv

Columns are:
    SNo	ObservationDate	Province/State	Country/Region	LastUpdate	Confirmed	Deaths	Recovered

output: (Country/Region, Confirmed, Deaths, Recovered)
'''
import fileinput

for i, line in enumerate(fileinput.input()):
    
    if i == 0: 
        continue #skip the row of column names

    data = line.strip().split(",")
    
    if len(data) != 8:
        continue #ignore this line
    
    country = data[3]
    cases_confirmed = data[5]
    cases_deaths    = data[6]
    cases_recovered = data[7]
    print ("{}\t{}\t{}\t{}".format(country, cases_confirmed, cases_deaths, cases_recovered))

