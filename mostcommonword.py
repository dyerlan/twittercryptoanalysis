#Print the most common word
#To Run: python moscommonword.py <file.jsonl>

import sys
import json
from collections import Counter
import re
from nltk.corpus import stopwords
import string


punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']


