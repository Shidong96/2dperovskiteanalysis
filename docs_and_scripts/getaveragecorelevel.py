#!/usr/bin/env python
import os, sys
import math
import numpy as np
os.popen("grep 1s OUTCAR > corevals")
infile = open('corevals', 'r')
elenums = os.popen("sed -n 7p POSCAR").readline().split()
#print elenums
numC = int(elenums[0])
numI = int(elenums[2])
numN = int(elenums[3])
if len(elenums)==5:
	numPb = int(elenums[4])
else:
	numPb = int(elenums[4])+int(elenums[5])

corelevelI = 0
corelevelPb = 0

for i in xrange(0, numC):
	infile.readline()
for i in xrange(0, numI):
	corelevelI += float(infile.readline().split()[2])
corelevelI = float(corelevelI/numI)
print "corelevelI:"
print corelevelI

for i in xrange(0, numN):
        infile.readline()
for i in xrange(0, numPb):
        corelevelPb += float(infile.readline().split()[2])
corelevelPb = float(corelevelPb/numPb)
print "corelevelPb:"
print corelevelPb

infile.close()
os.popen("rm corevals")
























#infile = open('POSCAR_1','r')
#outfile = open('POSCAR_0','w')
#string = infile.readline()
#outfile.write(string)
#for i in xrange(0,3):
#        outfile.write(infile.readline())
#string = infile.readline()
#outfile.write(string)
#cellc=0
#cellc=float(string.split()[2])
#outfile.write(infile.readline())
#elementnum = []
#elementnum1 = []
#sumnumber = 0
#string = infile.readline()
#elementnum = string.split()
#for i in xrange(0, len(elementnum)):
#        sumnumber += int(elementnum[i])
#elementnum1.append(int(elementnum[0])-1)
#elementnum1.append(int(elementnum[1])-6)
#elementnum1.append(int(elementnum[2])-3)
#elementnum1.append(int(elementnum[3])-1)
#elementnum1.append(int(elementnum[4])-1)
#for a in elementnum1:
#        outfile.write('  '+str(a))
#outfile.write('\n')
#outfile.write(infile.readline())
#strings = []
#cstrings = []
#sortedcstrings = []
#for i in xrange(0, sumnumber):
#        strings.append(infile.readline())
#for i in xrange(1,int(elementnum[4])+1):
#        cstrings.append([i,float(strings[-i].split()[2])])
#sortedcstrings = sorted(cstrings, key = lambda c:c[1])
#"slice_perov.py" 
