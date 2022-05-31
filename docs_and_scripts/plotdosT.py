#!/usr/bin/env python
#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import os,sys
sys.setrecursionlimit(20000000)
import math
from matplotlib.font_manager import FontProperties

class PlotPDOS():
    def __init__(self):
        self.path = os.getcwd();

    # 得到晶胞基矢和倒异基矢
    def getLatticeVector(self):
        infile = open(self.path + "/CONTCAR")
        string = infile.readline() # comment line

        string = infile.readline()
        latticeConstant = float(string)
        
        a=[] # lattice vector
        for i in range(0, 3):
            string = infile.readline()
            temp = np.array([float(s0)*latticeConstant for s0 in string.split()])
            if (a == []):
                a = temp
            else:
                a = np.vstack([a, temp])

        volume = a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + \
            a[0][2]*a[1][0]*a[2][1] - a[0][0]*a[1][2]*a[2][1] - \
            a[0][1]*a[1][0]*a[2][2] - a[0][2]*a[1][1]*a[2][0]
        
        b = np.zeros((3,3))
        for i in range(0,3):
            if (i == 0):
                j = 1
                k = 2
            elif (i == 1):
                j = 2
                k = 0
            else:
                j = 0
                k = 1
            c = np.zeros(3)
            c[0] = a[j][1]*a[k][2] - a[j][2]*a[k][1]
            c[1] = a[j][2]*a[k][0] - a[j][0]*a[k][2]
            c[2] = a[j][0]*a[k][1] - a[j][1]*a[k][0]
            for j in range(0, 3):
                b[i][j] = 2*math.pi*c[j]/volume
       
        return a, b, volume

    # get element information from CONTCAR
    def getElementinfo(self):
        s = "sed -n 6p " + self.path + "/CONTCAR"
        elements = os.popen(s).readline().split()
        s = "sed -n 7p " + self.path + "/CONTCAR"
        string = os.popen(s).readline()
        elementNumbers = [int(s0) for s0 in string.split()]
        
        totalAtomNumbers = 0
        for i in range(0, len(elementNumbers)):
            totalAtomNumbers += elementNumbers[i]

        return elements, elementNumbers, totalAtomNumbers
        
    # get dos from DOSCAR
    def getDOS(self):
        infile = open(self.path + "/DOSCAR")

        # skip comment lines
        for i in range(0,5):
            string = infile.readline()
        
        string = infile.readline()
        points = int(string.split()[2])
        efermi = float(string.split()[3])

        # read total DOS
        energy = []
        totalDOS = []
        cumulativeDOS = []
        for i in range(0, points):
            string = infile.readline()
            temp = [float(s0) for s0 in string.split()]
            if (energy == []):
                energy = np.array([temp[0]-efermi])
                totalDOS = np.array([temp[1]])
                cumulativeDOS = np.array([temp[2]])
            else:
                energy = np.hstack([energy, temp[0]-efermi])
                totalDOS = np.hstack([totalDOS, temp[1]])
                cumulativeDOS = np.array([cumulativeDOS, temp[2]])

        # read PDOS
        elements, elementNumbers, totalAtomNumbers = self.getElementinfo()

        atomPDOS = [0]*totalAtomNumbers # np.zeros(totalAtomNumbers)
        for i in range(0, totalAtomNumbers):
            print "read:" , i+1, "atoms"
            infile.readline() # skip

            pdos = []
            s = []
            p = []
            d = []
            for j in range(0, points):
                string = infile.readline()
                temp = [float(s0) for s0 in string.split()]
		if len(temp) > 4:
			porbital = range(2,5)
			dorbital = range(5,10)
		else:
			porbital = range(2,3)
			dorbital = range(3,4)
                # s
                if (s == []):
                    s = np.array(temp[1])
                else:
                    s = np.hstack([s, temp[1]])
                # p
                v = 0
                for k in porbital:
                    v += temp[k]
                if (p == []):
                    p = np.array([v])
                else:
                    p = np.hstack([p, v])
                # d
                v = 0
                for k in dorbital:
                    v += temp[k]
                if (d == []):
                    d = np.array([v])
                else:
                    d = np.hstack([d, v])
                
            pdos = np.array([s, p, d])
            atomPDOS[i] = pdos
            
        # pdos of element
        elementPDOS = [0]*len(elementNumbers)
        counter = 0
        for i in range(0, len(elementNumbers)):
            temp = 0
            for j in range(0, elementNumbers[i]):
                temp += atomPDOS[counter]
                counter += 1
            elementPDOS[i] = temp
        
        return energy, totalDOS, cumulativeDOS, atomPDOS, elementPDOS, elements

    # plot element pdos
    def plotElementPDOS(self):

	showf = False
	bdf   = 'pdosmod'
	if len(sys.argv) == 2 and ( str(sys.argv[1]) == 'T' or str(sys.argv[1]) == 't'):
        	showf = True
	elif len(sys.argv) >= 2:
        	bdf = str(sys.argv[1])

        linestyle = ["--", "-", ":", "-."]
        obrt=['s','p','d']
        c = ["r", "g", "b", "c", "m", "orangered"]

        energy, totalDOS, cumulativeDOS, atomPDOS, elementPDOS, elements = self.getDOS()
        a, b, volume = self.getLatticeVector()
        # 除以体积
        totalDOS = totalDOS/volume

        plt.figure(figsize=(8,20))

        #plt.plot(energy, totalDOS, "-", color="k",linewidth=1.5, label="total")

        plt.axhline(y=0, linestyle="--", color="r")

        # I
	for j in 2,4:
		for i in range(0,3):
  		      plt.plot( elementPDOS[j][i]/volume, energy, linestyle[j-1],linewidth=2, color=c[i], label=elements[j]+"-"+obrt[i])
	
        plt.ylabel("$\mathregular{Energy\ (eV)}$", fontsize=16).set_fontweight("bold")
        plt.xlabel(r"$\mathregular{PDOS\ (states/eV/\AA^{3})}$", fontsize=16).set_fontweight("bold")
        plt.ylim(-2,3)
        plt.xlim(0.0,0.002)
        plt.xticks(fontsize=18)
        plt.yticks(fontsize=18)
        plt.tick_params(labelsize=18)
	plt.legend(loc='upper center', bbox_to_anchor=(0.70,0.99),ncol=1,fontsize = '50', frameon=False)
        #plt.legend(loc=2, prop=(FontProperties(weight="bold", size=12)), ncol=4, frameon=False)
        plt.tight_layout()
	if showf:
		plt.show()
	else:
	        plt.savefig(bdf+".png", dpi=600)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
p = PlotPDOS()
p.plotElementPDOS()

