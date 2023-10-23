#!/usr/bin/env python
import sys

current_date = None
tweet_count = 0

for line in sys.stdin:
    date, count = line.strip().split('\t', 1)
    count = int(count)

    if current_date == date:
        tweet_count += count
    else:
        if current_date:
            print('%s\t%s' % (current_date, tweet_count))
        current_date = date
        tweet_count = count

if current_date == date:
    print('%s\t%s' % (current_date, tweet_count))

