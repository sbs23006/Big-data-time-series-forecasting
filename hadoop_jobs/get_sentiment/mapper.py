#!/usr/bin/env python

import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

for line in sys.stdin:
    columns = line.strip().split(',')
    
    if len(columns) == 4:
        text = columns[3]
        sentiment_scores = analyzer.polarity_scores(text)
        sentiment = sentiment_scores['compound']
        sentiment_classification = "positive" if sentiment_scores['compound'] >= 0.05 else "negative" if sentiment_scores['compound'] <= -0.05 else "neutral"
        print(f"{line.strip()},{sentiment},{sentiment_classification}")
