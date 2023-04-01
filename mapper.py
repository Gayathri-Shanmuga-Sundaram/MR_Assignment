#!/usr/bin/env python
"""mapper.py"""

import sys

# Input from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Split the line into integers
    values = line.split()
    # Iterate over all values and output them as (value, 1) pairs
    for value in values:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        print("%s\t%s" % (value, 1))
