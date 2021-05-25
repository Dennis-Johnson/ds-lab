'''
map.py
input: path to german_credit dataset
output: tuple (creditability, creditAmt) for each line
'''
import fileinput 

for i, line in enumerate(fileinput.input()):
    data = line.strip().split(',')

    if i == 0: 
        continue #Skip col header line
     
    creditability, creditAmt, DurationInMonths = data
    print("{}\t{}".format(creditability, creditAmt))


