#!/usr/bin/env python
import sys
import happybase

# Connect to HBase
connection = happybase.Connection('localhost')
table = connection.table('processed_tweets')

for line in sys.stdin:
    # Split the line into columns
    id, date, user, text = line.strip().split(',')

    # Insert the data into HBase
    table.put(id, {'cf:date': date, 'cf:user': user, 'cf:text': text})
