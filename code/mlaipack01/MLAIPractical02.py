#!/usr/bin/env /home/haozeke/.venvs/ictAI/bin/python

import csv

# This should not be required in any sane language
import os
dirname = os.path.dirname(__file__)
ftemp = os.path.join(dirname,'data/indian-diabetes.data.csv')

# Seriously, why no relative paths?
filename=open(ftemp, 'r')
reader=csv.reader(filename, delimiter=',') # Surely that should be the default? It's a CSV!
lines=list(reader)
print("\n\nNo. of rows: ",len(lines), "\n\n")
print(lines)
for l in lines:
    print(l)
