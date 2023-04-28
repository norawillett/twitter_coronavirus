#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--keys', nargs='+', required=True)
args = parser.parse_args()

import os
import glob
import json
from collections import Counter, defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from datetime import datetime

# Initialize a dictionary to hold the data for each key
data = defaultdict(lambda: defaultdict(list))

# Load the data for each key
for path in glob.glob('outputs/geoTwitter*.country'):
    with open(path) as f:
        tmp = json.load(f)
        filename = os.path.basename(path)
        date = filename[10:18]
        for key in args.keys:
            if key in tmp:
                data[key][date].append(sum(tmp[key].values()))

# Plot the data for each key
fig, ax = plt.subplots()
for key in args.keys:
    dates = sorted(data[key].keys())
    values = [sum(data[key][date]) for date in dates]
    days = [datetime.strptime(date, '%y-%m-%d') for date in dates]
    ax.plot(days, values, label=key)

# Customize the plot
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d'))
ax.set_xlabel('Date')
ax.set_ylabel('Number of Tweets')
ax.legend()

# Save the plot to a file
tags = [key[1:] for key in args.keys]
plt.savefig('_'.join(tags) + '.png')
