#!/usr/bin/env python
import sys
import csv
import string
import nltk
from nltk.corpus import stopwords

# Download the stopwords from NLTK
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

reader = csv.reader(sys.stdin)

# remove empty rows with user and text 
# remove not needed columns
# remove punctuation from the text
# remove stopwords

for row in reader:
    if row[1] and row[4]:
        # Remove punctuation from 'text'
        text = row[4].translate(str.maketrans('', '', string.punctuation))
        # Remove stopwords
        text = ' '.join(word for word in text.split() if word not in stop_words)
        print('%s,%s,%s' % (row[1], row[3], text))  # output 'date', 'user', and 'text'
