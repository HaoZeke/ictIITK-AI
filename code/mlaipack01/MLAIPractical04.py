#!/usr/bin/env /home/haozeke/.venvs/ictAI/bin/python

import numpy
import urllib.request as ur

webPath = ur.urlopen("https://goo.gl/QnHW4g")
dataset = numpy.genfromtxt(webPath,delimiter=",")
for l in dataset:
    print(l)
print("URL Data Shape: ", dataset.shape)
