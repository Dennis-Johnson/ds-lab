"""mapper.py"""

import sys

for line in sys.stdin:

    # remove trailing whitespace and then spilt
    words = line.strip().split()

    for word in words:
        print("{}\t{}".format(word, 1))
