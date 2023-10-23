#!/usr/bin/env python
import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    print('text\t%s' % len(row[4]))

