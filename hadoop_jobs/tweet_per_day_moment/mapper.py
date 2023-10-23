#!/usr/bin/env python
import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin)

for row in reader:
    date_str = row[1]
    date_str = date_str.rsplit(' ', 2)[0] + ' ' + date_str.rsplit(' ', 2)[2]  # remove timezone
    date_obj = datetime.strptime(date_str, '%a %b %d %H:%M:%S %Y')
    hour = date_obj.hour

    if 6 <= hour < 12:
        time_of_day = 'morning'
    elif 12 <= hour < 17:
        time_of_day = 'afternoon'
    elif 17 <= hour < 21:
        time_of_day = 'evening'
    else:
        time_of_day = 'night'

    print('%s\t%s\t%s' % (date_obj.strftime('%a %b %d'), time_of_day, 1))
