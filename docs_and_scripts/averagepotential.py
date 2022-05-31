#!/usr/bin/env python
import os
import sys
#import numpy as np
import math
import string
import datetime
import time

infile = open('POSCAR', 'r')
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
for i in range(0,number):
	string = infile.readline()
	temp = string.split()
	temp[0] = float(temp[0])*a
	temp[1] = float(temp[1])*b
	temp[2] = float(temp[2])*c
	newstring = '  '+"{0:20}".format(temp[0])+"{0:20}".format(temp[1])+"{0:20}".format(temp[2])+'\n'
	outfile.write(newstring)
infile.close()
outfile.close()


infile = open('poscar', 'r')
for i in xrange(0, 3):
        infile.readline()
string = infile.readline()
cellc = float(string.split()[2])
infile.readline()
sumnumber = 0
infile.readline()
string = infile.readline()
for i in string.split():
        sumnumber += int(i)
infile.readline()
strings = []
cstrings = []
for i in xrange(0, sumnumber):
        string = infile.readline()
        strings.append(string)
        cstrings.append(float(string.split()[2]))
maxer = max(cstrings)
miner = min(cstrings)
#print maxer,miner

infile = open("LOCPOT_Z",'r')
string = infile.readline()
potentials = []
while 1:
        string = infile.readline()
        if string == '':
                break
        potentials.append((string.split()[0],string.split()[1]))
sortedpotentials = sorted(potentials, key = lambda s:s[1], reverse = True)
#print sortedpotentials[0]
npot=0
totalpot=0.000
for i in potentials:
    if (float(i[0])<miner) or (float(i[0])>maxer):
        npot=npot+1
        totalpot=totalpot+float(i[1])
averagepot = totalpot/npot
#print npot
print averagepot

