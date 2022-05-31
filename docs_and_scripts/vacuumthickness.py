import numpy as np
import os
import sys
class getvacuum(object):
        def __init__(self, path):
            self.path = path
        def printvacuum(self):
            dir = []
            for i in 0,1,2,3,4,5:
                dir.append("POSCAR_PEA2MA{}Pb{}I{}".format(i,i+1,3*i+4))
            #dir.append("POSCAR_PbI2")
            #dir.append("POSCAR_H12C4IN")
            #dir.append("POSCAR_H6CIN")
            for a in dir:
                os.chdir("{}/{}/opt".format(self.path, a))
		file = open('CONTCAR', 'r')
		for i in range(1,5):
		    string = file.readline()
		c = float(file.readline().split()[2])
		file.readline()
		number = 0
		for N in file.readline().split():
		    number += int(N)
		file.readline()
		max = float(file.readline().split()[2])
		min = float(file.readline().split()[2])
		if max < min :
			temp = max
			max = min
			min = temp
		n = 1
		while n <= (number-2):
			coordc = float(file.readline().split()[2])
			if max<coordc:
				max = coordc
			if min>coordc:
				min = coordc
			n += 1
		print("The vacuum thickness of {} is: ".format(a.split('_')[1])+str((1+min-max)*c)+"A")


currentpath = os.getcwd()
vacuum = getvacuum(path = currentpath)
vacuum.printvacuum()




