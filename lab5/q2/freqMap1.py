#!/usr/bin/env python
'''
A basic mapper function/program that
takes whatever is passed on stdin and
outputs tuples of all the words formatted
as (word, 1)
'''
import sys

for line in sys.stdin:

    # create tuples of all words in line
    L = [ (word.strip().lower(), 1 ) for word in line.strip().split() ]

    for word in line.strip().split():
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for freqRed1.py
        #
        # tab-delimited; the trivial word count is 1
        print( '%s\t1' % (word) )

