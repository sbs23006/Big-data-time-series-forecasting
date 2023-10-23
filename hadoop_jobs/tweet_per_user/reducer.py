#!/usr/bin/env python
import sys

current_user = None
tweet_count = 0

for line in sys.stdin:
    user, count = line.strip().split('\t', 1)
    count = int(count)

    if current_user == user:
        tweet_count += count
    else:
        if current_user:
            print('%s\t%s' % (current_user, tweet_count))
        current_user = user
        tweet_count = count

if current_user == user:
    print('%s\t%s' % (current_user, tweet_count))
