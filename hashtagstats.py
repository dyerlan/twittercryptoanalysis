#Twitter hashtag stats 

import sys 
from collections import defaultdict
import json

def get_hashtags(tweet):
    entities = tweet.get('entities', {})
    hashtags = entities.get('hashtags', [])
    return [tag['text'].lower() for tag in hashtags]


def usage():
    print("Usage:")
    print("python {} <filename.jsonl>".format(sys.argv[0]))


