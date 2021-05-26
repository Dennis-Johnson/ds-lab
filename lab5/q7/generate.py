'''
generate.py

generates 100 pseudo-random natural numbers
'''

import random


for _ in range(100):
    # map generated number from range [0, 1] to [0, 100]
    num = int(random.random() * 100)
    print(num, end=' ')

