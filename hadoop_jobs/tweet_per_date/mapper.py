#!/usr/bin/env python
import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    print('%s\t%s' % (row[1], 1))  # date is the second column

