import os, sys
import math
import numpy as np
class getenergy(object):
	def __init__(self, path):
	    self.path = path
	def printE(self):
	    dir = []
            for i in 0,1,2,3,4,5:
		dir.append("POSCAR_BA2MA{}Pb{}I{}_001_direct".format(i,i+1,3*i+4))
	    #dir.append("POSCAR_PbI2")
	    #dir.append("POSCAR_H12C4IN")
	    #dir.append("POSCAR_H6CIN")
	    for a in dir:
	    	os.chdir("{}/{}/scf".format(self.path, a))
		
	        f = open('OUTCAR', 'r')
		while True:
			line = f.readline()
			if "energy  without entropy" in line:
				print "the energy without entropy of "+"{0:17}  ".format(a.split('_')[1]+':') + line.split()[3]
				break
			

            




currentpath = os.getcwd()
energy = getenergy(path = currentpath)
energy.printE()
