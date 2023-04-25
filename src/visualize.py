#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)


import time
import matplotlib.pyplot as plt

data_lang = {}
with open('reduced.lang','r') as f:
        for line in f:
            if not line:
                continue
            values = line.split()
            if len(values) != 2:
                continue
            key, value = line.strip().split()
            data_lang[key] = int(value)

sorted_data1 = sorted(data_lang.items(), key=lambda x: x[1])[:10]
keys1 = [x[0] for x in sorted_data1]
values1 = [x[1] for x in sorted_data1]

plt.bar(keys1, values1)
plt.xlabel('languages')
plt.ylabel('count')
plt.title('Top 10 languages of twitter tweets tweeted')
plt.savefig('figure1.png')
plt.clf()
