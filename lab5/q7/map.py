'''
map.py

formats input from STDIN to
tuples that are later counted by reduce.py
'''


import sys

for line in sys.stdin:
    nums = line.strip().split()
    

    for num in nums:
        try:
            num = int(num)
        except ValueError:
            #skip and continue quietly
            continue

        if num % 2 == 0: 
            print(num, '\teven')
        else:
            print(num, '\todd')



