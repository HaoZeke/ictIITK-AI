#!/usr/bin/env /home/haozeke/.venvs/ictAI/bin/python

import os
import numpy

dirname = os.path.dirname(__file__)
filetmp = os.path.join(dirname,'data/indian-diabetes.data.csv')
raw_data=open(filetmp, 'r')

data=numpy.loadtxt(raw_data, delimiter=",")

print("Numpy loadtxt: ",data.shape)
raw_data.close()

# print("\n\n\n")
# for l in data:
#     print(l)
