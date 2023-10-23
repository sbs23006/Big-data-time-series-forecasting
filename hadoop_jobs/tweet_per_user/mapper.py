#!/usr/bin/env python
import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    print('%s\t%s' % (row[3], 1))  # user is the fourth column

