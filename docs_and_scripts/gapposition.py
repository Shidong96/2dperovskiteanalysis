import os,sys
import math

file = open('OUTCAR', 'r')
vbm = -1000
cbm = 1000
while True:
	string = file.readline()
	if len(string.split()) != 0 and string.split()[0] == 'E-fermi':
		print "E-fermi", string.split()[2]
	if len(string.split()) == 6 and string.split()[0] == 'k-point':
		kpoint = string
		file.readline()
		energy = file.readline()
		while len(energy.split()) == 3:
			if energy.split()[2] != '0.00000' and float(energy.split()[1]) > vbm:
				vbm = float(energy.split()[1])
				coorvbm = kpoint.split()[3:6] 
			if energy.split()[2] == '0.00000' and float(energy.split()[1]) < cbm:
				cbm = float(energy.split()[1])
				coorcbm = kpoint.split()[3:6]
				break
			energy = file.readline()
	if string == '':
		print vbm, coorvbm
		print cbm, coorcbm
		print "bandgap is:", cbm-vbm
		break
