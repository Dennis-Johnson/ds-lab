#!/usr/bin/env python

'''
freqRed1.py
'''

import sys

lastWord = None
_sum = 0

for line in sys.stdin:
      word, count = line.strip().split('\t', 1)
      count = int(count)

      if lastWord==None:
          lastWord = word
          _sum = count
          continue

      if word == lastWord:
          _sum += count
      
      else:
          print( "%s\t%d" % ( lastWord, _sum ) )
          _sum = count
          lastWord = word

# output last word
if lastWord == word:
    print( '%s\t%s' % (lastWord, _sum ) )

