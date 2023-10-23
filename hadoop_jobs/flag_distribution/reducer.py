#!/usr/bin/env python
import sys

current_flag = None
flag_count = 0

for line in sys.stdin:
    flag, count = line.strip().split('\t', 1)
    count = int(count)

    if current_flag == flag:
        flag_count += count
    else:
        if current_flag:
            print('%s\t%s' % (current_flag, flag_count))
        current_flag = flag
        flag_count = count

if current_flag == flag:
    print('%s\t%s' % (current_flag, flag_count))

