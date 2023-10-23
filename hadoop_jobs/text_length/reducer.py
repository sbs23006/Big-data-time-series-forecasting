#!/usr/bin/env python
import sys

count = 0
total_length = 0

for line in sys.stdin:
    _, length = line.strip().split('\t', 1)
    length = int(length)

    count += 1
    total_length += length

print('Average text length: %s' % (total_length / count))

