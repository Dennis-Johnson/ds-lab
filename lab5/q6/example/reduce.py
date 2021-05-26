'''
reduce.py

sum output from map.py
to get resultant estimation of PI
'''

import sys 

sum = 0 

for line in sys.stdin: 
      # parse the input from map.py 
      word, count = line.strip().split('\t', 1) 

      try: 
          count = float(count) 

      except ValueError: 

          # count was not a number, so silently 
          # ignore/discard this line 

          print( "--skipping (%s, %s)" % ( str(word), str(count) ) ) 
          continue 

      sum += count 

# output the last word if needed! 
print( '%1.10f\t0' % sum ) 
