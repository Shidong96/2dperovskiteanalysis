#!/usr/bin/env python
#coding=utf-8
import numpy as np
#import matplotlib.pyplot as plt
import os
import sys
import math

class slice():
	def __init__(self):
		self.path = os.getcwd()
	def sliceperov(self, inf,outf):	
		"""
		This script is used on fractional poscar files only
		"""
		infile = open(inf,'r')
		outfile = open(outf,'w')
		string = infile.readline()
		outfile.write(string)
		for i in xrange(0,3):
			outfile.write(infile.readline())
		string = infile.readline()
		outfile.write(string)
		cellc=0
		cellc=float(string.split()[2])
		outfile.write(infile.readline())
		elementnum = []		
		elementnum1 = []
		sumnumber = 0
		string = infile.readline()
		elementnum = string.split()
		for i in xrange(0, len(elementnum)):
			sumnumber += int(elementnum[i])
		elementnum1.append(int(elementnum[0])-1)
		elementnum1.append(int(elementnum[1])-6)
		elementnum1.append(int(elementnum[2])-3)
		elementnum1.append(int(elementnum[3])-1)
		elementnum1.append(int(elementnum[4])-1)
		for a in elementnum1:
			outfile.write('  '+str(a))
		outfile.write('\n')
		outfile.write(infile.readline())
		strings = []
		cstrings = []
		sortedcstrings = []
		for i in xrange(0, sumnumber):
			strings.append(infile.readline())
		for i in xrange(1,int(elementnum[4])+1):
			cstrings.append([i,float(strings[-i].split()[2])])
		sortedcstrings = sorted(cstrings, key = lambda c:c[1])
		midc = sortedcstrings[int(math.ceil(int(elementnum[4])/2+0.5))-1][1]
		#print 'midc'+str(midc)
		sigmac = midc - sortedcstrings[int(math.ceil(int(elementnum[4])/2+0.5))-2][1]
		#print 'signmac'+str(sigmac)
		rangemax = midc+float(1/cellc)
		rangemin = midc-float(5/cellc)
		#print 'rangemax'+str(rangemax)
		#print 'rangemin'+str(rangemin)
		dell = []
		for i in xrange(0, sumnumber):
		        if ((float(strings[i].split()[2])>rangemin)&(float(strings[i].split()[2])<rangemax)):
		                strings[i] = ''
		        elif (float(strings[i].split()[2])<rangemin):
		                temp = strings[i].split()
		                temp[2] = str(float(temp[2])+sigmac)
		                strings[i] = '  '+"  ".join(temp)+'\n'
		for a in strings:
		        outfile.write(a)
		infile.close()
		outfile.close()
	def fractocart(self,inf):
		"""
		fractional to cartesian
		"""
		infile = open(inf, 'r')
		outfile = open("poscar", 'w')
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
	def movetomid(self,outf):
		infile = open("poscar", 'r')
		outfile = open(outf, 'w')
		outfile.write(infile.readline())
		for i in xrange(0, 3):
		        outfile.write(infile.readline())
		string = infile.readline()
		outfile.write(string)
		cellcstr = string.split()[2]
		cellc = float(cellcstr)
		outfile.write(infile.readline())
		sumnumber = 0
		string = infile.readline()
		outfile.write(string)
		for i in string.split():
		        sumnumber += int(i)
		outfile.write(infile.readline())
		strings = []
		cstrings = []
		for i in xrange(0, sumnumber):
		        string = infile.readline()
		        strings.append(string)
		        cstrings.append(float(string.split()[2]))
		maxer = max(cstrings)
		miner = min(cstrings)
		oldmid = float(maxer+miner)/2
		newcellc = 30+maxer-miner
		delta = float(0.5*newcellc-oldmid)
		#print "cellc for 30A vacuum:"
		#print newcellc
		print "delta"
		print delta
		#if (maxer+10)> cellc:
		        #print "midpoint:"
			#print maxer+(cellc-(maxer-miner))/2-cellc
		#else:
		        #print "midpoint"
			#print maxer+(cellc-(maxer-miner))/2
		for i in xrange(0, sumnumber):
		        cstrings[i] = cstrings[i] + delta
		        temp = strings[i].split()
		        temp[2] = str(cstrings[i])
		        outfile.write('  '+"{0:20}".format(temp[0])+"{0:20}".format(temp[1])+"{0:20}".format(temp[2])+'\n')
		infile.close()
		outfile.close()
		
		file_data = ""
		with open(outf, "r") as f:
		    for line in f:
		        if cellcstr in line:
		                #print "yes"
		                line = line.replace(cellcstr,str(newcellc))
		        file_data += line
		with open(outf,"w") as f:
		    f.write(file_data)
		f.close()
a = slice()
infile = ""
outfile = ""
for i in 5,4,3,2,1:
	infile = "POSCAR_%r" %i
	outfile = "POSCAR_%r" %(i-1)
	a.sliceperov(infile,outfile)
for i in 4,3,2,1,0:
	file = "POSCAR_%r" %i	
	a.fractocart(file)
	a.movetomid(file)
	os.popen("rm poscar")
