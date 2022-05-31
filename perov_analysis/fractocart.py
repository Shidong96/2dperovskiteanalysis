#!/usr/bin/env python
import numpy as np
import os
import sys
"""
fractional to cartesian
"""
infile = open(sys.argv[1], 'r')
outfile = open('poscar', 'w')
outfile.write(infile.readline())
outfile.write(infile.readline())

string = infile.readline()
outfile.write(string)
a = float(string.split()[0])
string = infile.readline()
outfile.write(string)
b = float(string.split()[1])
string = infile.readline()
outfile.write(string)
c = float(string.split()[2])
outfile.write(infile.readline())

number = 0
string = infile.readline()
outfile.write(string)
for N in string.split():
    number += int(N)
infile.readline()
outfile.write('Cartesian\n')
count = 0
for i in range(0,number):
        string = infile.readline()
        temp = string.split()
        temp[0] = float(temp[0])
        temp[1] = float(temp[1])
        temp[2] = float(temp[2])

        if temp[0] > 0.95:
            temp[0] = temp[0]-1
            count = count +1
        if temp[1] > 0.95:
            temp[1] = temp[1]-1
        if temp[2] < 0.05:
            temp[2] = temp[2]+1

        temp[0] = temp[0]*a
        temp[1] = temp[1]*b
        temp[2] = temp[2]*c
        newstring = '  '+"{0:20}".format(temp[0])+"{0:20}".format(temp[1])+"{0:20}".format(temp[2])+'\n'
        outfile.write(newstring)
print count
infile.close()
outfile.close()
