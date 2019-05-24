#!/usr/bin/env /home/haozeke/.venvs/ictAI/bin/python

import os
import pandas

dirname = os.path.dirname(__file__)
ftmp = os.path.join(dirname,'data/indian-diabetes.data.csv')
hnames = [
    'preg',
    'plas',
    'pres',
    'skin',
    'test',
    'mass',
    'pedi',
    'age',
    'class'
]

dataframe = pandas.read_csv(ftmp, names=hnames)

print(dataframe.head(20))
print("-*-"*20)
print("Shape", dataframe.shape)
print("-*-"*20)
print(dataframe.dtypes)
print("-*-"*20)

print('\n')
class_counts = dataframe.groupby('class').size()
print(class_counts)
print("-#-"*20)
