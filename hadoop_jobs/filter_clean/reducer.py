#!/usr/bin/env python
import sys

row_key = 1 #needed to write back to Hbase

# Process each line from the input
for line in sys.stdin:
    # Print the line as it is + id for hbase
    print('{},{}'.format(row_key, line.strip()))
    row_key += 1
