#!/usr/bin/env python
"""reducer.py"""

import sys

#Variable Declaration
total_sum = 0
count = 0


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    value, occurrence = line.split("\t")

    # convert count (currently a string) to int
    try:
         value = int(value)
         occurrence = int(occurrence)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # Calculate Total Sum
    total_sum += value * occurrence

    # Calculate Total Count
    count += occurrence

# Calculate the average 
average = float(total_sum) / count
# Print Output 
print("Average\t%s" % (average))

