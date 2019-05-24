#!/usr/bin/env /home/haozeke/.venvs/ictAI/bin/python

import pandas as pd
import urllib.request as req

hnames = [
    'sepal-length',
    'sepal-width',
    'petal-length',
    'petal-width',
    'class',
]

webPath=req.urlopen("https://goo.gl/QnHW4g")
dataframe = pd.read_csv(webPath, names=hnames)
print(dataframe.shape)
print(dataframe)
print(dataframe.columns)
