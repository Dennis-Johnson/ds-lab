'''
reduce.py

count number of even and odd numbers 
from output of map.py

input -> (num   even | odd)
'''

import sys

even_count = 0
odd_count  = 0

for line in sys.stdin:
    num, parity = line.strip().split('\t', 1)
    
    if parity == 'even':
        even_count += 1
    elif parity == 'odd':
        odd_count +=1 

print("Counted {} even numbers".format(even_count))
print("Counted {} odd  numbers".format(odd_count))
