#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')

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

with open('reduced.country') as f:
    data2 = f.read()
    data = json.loads(data2)
    data_key = data[str(args.key)]
    print("data_key=", data_key)
    lang_nums = [v for v in data_key.values()]
    countries = [k for k in data_key.keys()]
print("countries=", countries)
sorted_data = sorted(data_key.items(), key=lambda x: x[1])
sorted_data1 = sorted_data[-10:]
print("sorted_data1=", sorted_data1)
keys1 = [x[0] for x in sorted_data1]
values1 = [x[1] for x in sorted_data1]
print("values1=", values1)
import numpy as np
fig = plt.figure()
n = len(keys1)
ind = np.arange(n)
plt.bar(ind, values1)
plt.xticks(ind, keys1)
plt.xlabel('Country')
plt.ylabel('# of Tweets')
plt.title('#Coronavirus in Korean by Country')
plt.savefig('figure4.png')


