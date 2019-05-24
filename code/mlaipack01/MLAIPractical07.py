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

# The default is 5 rows
print(dataframe.head(20))
print("-*-"*20)
print("Shape", dataframe.shape)
print("-*-"*20)
print(dataframe.dtypes)
print("-*-"*20)

pandas.set_option('precision',2)
print("description=\n", dataframe.describe)
print("-*-"*20)

class_counts = dataframe.groupby('class').size()
print(class_counts)
print("-*-"*20)

correlations = dataframe.corr(method="pearson")
print(correlations)
print("-#-"*20)
