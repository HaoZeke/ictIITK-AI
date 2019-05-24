#!/usr/bin/env /home/haozeke/.venvs/ictAI/bin/python

import os.path as osp
import pandas

dirname = osp.dirname(__file__)
ftemp = osp.join(dirname,'data/indian-diabetes.data.csv')

hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pandas.read_csv(ftemp,names=hnames)
print("pandas Data: ", dataframe.shape)
print(dataframe)
print("\n\n")
print(type(dataframe))
