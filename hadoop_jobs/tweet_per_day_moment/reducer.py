#!/usr/bin/env python
import sys

current_date = None
current_moment = None
tweet_count = 0

for line in sys.stdin:
    date, moment, count = line.strip().split('\t')
    count = int(count)

    if current_date == date and current_moment == moment:
        tweet_count += count
    else:
        if current_date and current_moment:
            print('%s\t%s\t%s' % (current_date, current_moment, tweet_count))
        current_date = date
        current_moment = moment
        tweet_count = count

if current_date == date and current_moment == moment:
    print('%s\t%s\t%s' % (current_date, current_moment, tweet_count))
