#!/usr/bin/env python3

import sys, math, scipy.interpolate

''' Inputs two sets of points (from two curves), interpolate one of
they in the points of the other and returns the difference between
interpolated (first curve) and real points (second curve). The
diference samples are output through the stdout.

USAGE EXAMPLE:

./interplate.py data_file_1.dat data_file_2.dat > data_file_3.dat

# Note: the domain of data_file_2 must be included in the domain of data_file_1.
'''

# First curve
x = [0.0] # X coordinates
y = [0.0] # Y coordinates

f = open(sys.argv[1])
line = f.readline()
while (line != ""):
    if "#" != line[0]:
        splitted_line = line.split()
        x.append(float(splitted_line[0]))
        y.append(float(splitted_line[1]))
    line = f.readline()

f.close()

# Create the interpolate function
y_interp = scipy.interpolate.interp1d(x,y)

# Evaluate the first curve at the x coordinates of the second one

f = open(sys.argv[2])
line = f.readline()
while (line != ""):
    if "#" != line[0]:
        splitted_line = line.split()
        x = float(splitted_line[0])
        y = float(splitted_line[1])
        if not math.isnan(y_interp(x)):
            print(x, '\t', y-y_interp(x)) # print x, y-y_interp(x) # print (x, '\t', y-y_interp(x))
    line = f.readline()

f.close()
