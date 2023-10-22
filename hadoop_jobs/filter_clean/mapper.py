#!/usr/bin/env python
import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    if row[1] and row[4]:  # assuming 'date' is the first column and 'text' is the fourth column
        print('%s\t%s\t%s' % (row[1], row[3], row[4]))  # output 'date', 'user', and 'text'

