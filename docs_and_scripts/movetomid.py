#!/usr/bin/env python
#coding=utf-8

infile = open("POSCAR", 'r')
outfile = open("poscar.vasp", 'w')
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
with open("poscar.vasp", "r") as f:
    for line in f:
        if cellcstr in line:
                #print "yes"
                line = line.replace(cellcstr,str(newcellc))
        file_data += line
with open("poscar.vasp","w") as f:
    f.write(file_data)
f.close()

