#!/usr/bin/env python 

import os, sys
import math
import numpy as np
import matplotlib.pyplot as plt


class PlotBand(object):
    def __init__(self, path):
        self.path = path;
    def get_lattice(self):
        cell = [[0.0,0.0,0.0], [0.0,0.0,0.0], [0.0,0.0,0.0]]
        #elements = []
        elementnum = []
        coord = []
        infile = open(self.path + '/' + 'CONTCAR', 'r')
        while 1:
                string = infile.readline()
                #elements = string.split()
                #print elements

                if not string:
                        break
                else:
                        string = infile.readline()
                        for i in xrange(0,3):
                            string = infile.readline()
                            for j in xrange(0,len(string.split())):
                                if (len(string.split())==3):
                                        cell[i][j]=float(string.split()[j])
                        #string = infile.readline()
                        #elements = string.split()
                        #string = infile.readline()
                        #elementnum = [int(s0) for s0 in string.split()]
                        #print elementnum 
                        #string = infile.readline()
                        #print string
                        #for kk in xrange(0,len(elementnum)):
                             #for mm in xrange(0,int(elementnum[kk])):
                                #temp = ['0',0.0,0.0,0.0]
                                #string = infile.readline()
                                #temp[0] = elements[kk]
                                #tmp = [float(s0) for s0 in string.split()]
                                #for jj in xrange(0,3):
                                    #temp[jj+1] = tmp[jj]
                                #if (coord == []):
                                        #coord = np.array([temp])
                                #else:
                                        #coord = np.vstack([coord, temp])
                break
        return cell
    def crossp(self, va, vb):
        crossp =  np.array([0.,0.,0.])
        crossp[0] = va[1]*vb[2] - va[2]*vb[1]
        crossp[1] = va[2]*vb[0] - va[0]*vb[2]
        crossp[2] = va[0]*vb[1] - va[1]*vb[0]
        #print crossp[0], crossp[1], crossp[2]
        return crossp
    def volume(self):
        cell  = self.get_lattice()
        #print cell
        cell = np.array(cell)
        volume = sum(cell[0,:] * (self.crossp(cell[1,:], cell[2,:]))) 
        #print volume
        return volume, cell
    def recipvector(self):
        volume, cell = self.volume()
        cell = np.array(cell)
        recipvector = [None, None, None]
        recipvector = np.array(recipvector)
        recipvector[0] = self.crossp(cell[1,:], cell[2,:])/volume
        #recipvector[0] = self.crossp(cell[1,:], cell[2,:])/volume*2*math.pi
        recipvector[1] = self.crossp(cell[2,:], cell[0,:])/volume
        recipvector[2] = self.crossp(cell[0,:], cell[1,:])/volume
        
        #print recipvector
        return recipvector

    def convert_kpoint_cartesian(self, kpoint):
        recipvector = self.recipvector()
        #print recipvector
        distance = []
        tmp = 0
        distance.append(tmp)
        counter = 0
        for i in xrange(1, len(kpoint)):
            #f[i] =  re.sub(',', ' ', f[i])
            #f[i-1] =  re.sub(',', ' ', f[i-1])
            temp1 =  kpoint[i]
            temp2 =  kpoint[i-1]
            dx =  (temp1[0] - temp2[0])*recipvector[0][0] + (temp1[1] - temp2[1])*recipvector[1][0] + (temp1[2] - temp2[2])*recipvector[2][0]
            dy =  (temp1[0] - temp2[0])*recipvector[0][1] + (temp1[1] - temp2[1])*recipvector[1][1] + (temp1[2] - temp2[2])*recipvector[2][1]
            dz =  (temp1[0] - temp2[0])*recipvector[0][2] + (temp1[1] - temp2[1])*recipvector[1][2] + (temp1[2] - temp2[2])*recipvector[2][2]
            delta = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2) + math.pow(dz, 2))
            #print delta
            tmp += delta
            #distance.append(tmp*multiple)
            distance.append(tmp)
            counter += 1
        #print distance, len(distance)
        #print counter
        return distance

    def getEfermi(self):
        s = "grep 'E-fermi' " + 'scf' + '/' + 'OUTCAR'
        #s = "grep 'E-fermi' " + '/home/dongwen/Desktop/workplace_2017/lead_free_329/wuzhou_download/test_MA_direction/opt_vdw/POSCAR_MA3Sb2I9_p3m1_110_direct/scf_band' + '/' + 'OUTCAR'
        string = os.popen(s).readline()
        Efermi = float(string.split()[2])
        return Efermi

    # get band from EIGENVAL
    # kpoints: n*3 array
    # bands: nbands*nkpoints array
    def getBand(self):

        Efermi = self.getEfermi()

        infile = open(self.path + "/EIGENVAL")
        # comment lines
        for i in range(0, 5):
            infile.readline()
        # get total number of kpints and bands
        string = infile.readline()
        totalKpoints = int(string.split()[1])
        totalBands = int(string.split()[2])

        # read bands
        bands = []
        kpoints = []
        counter = 0
        maxer=-100.0
        xbar=0.0
        for i in range(0, totalKpoints):
            infile.readline() # blank line

            # get kpoint coordinate
            string = infile.readline()
            kp = np.array([float(s0) for s0 in string.split()[:3]])
            if (kpoints == []):
                kpoints = kp
            else:
                kpoints = np.vstack([kpoints, kp])

            # get band value
            bk = [] # bands of a kpoint
            for j in range(0, totalBands):
                string = infile.readline()
                temp = np.array(float(string.split()[1]) - Efermi)
                if temp<=0 and temp>=maxer:
                        maxer=temp
                if (bk == []):
                    bk = temp
                else:
                    bk = np.hstack([bk, temp])
            # bk->bands
            xbar=0.0 - maxer
            if (bands == []):
                bands = bk
            else:
                bands = np.vstack([bands, bk])
            counter += 1

        if (counter != totalKpoints):
            print "error! read number of kpoints", counter

        #print  kpoints, len(kpoints)
        #print   bands, len(bands)
        #print  kpoints, bands, xbar
        return kpoints,  bands, xbar

    def getHighSymmetryPoints(self):
        #print self.path
        infile = open(self.path + "/" + "KPOINTS")
        infile.readline() # comment line
        string = infile.readline()
        nhspoints = int(string)

        infile.readline() # skip
        string = infile.readline()

        # kpoints and kpointsName
        hspoints = []
        hspointsName = []
        if (string.startswith("rec")):

            while(string):
                string = infile.readline()
                if (string != ""):
                    temp = np.array([float(s0) for s0 in string.split()[:3]])
                    name = string.split()[-1]
                    if (name == "\Gamma" or name == "\gamma"):
                        name = "$\Gamma$"
                    name = np.array([name])

                    if (hspoints == []):
                        hspoints = temp
                        hspointsName = name
                    else:
                        if (hspointsName[-1] != name):
                            hspoints = np.vstack([hspoints, temp])
                            hspointsName = np.hstack([hspointsName, name])

        print hspointsName, nhspoints
        return hspointsName, nhspoints

    def plotband(self):
        kpoints, bands, xbar = self.getBand()
        distances = self.convert_kpoint_cartesian(kpoint = kpoints)
        
        # plot bands
        for i in range(0, bands.shape[0]):
            bands[i] =bands[i]+ xbar
            plt.plot(distances, bands[i], "b")

        # plot high symmerty lines
        hspointsName, hspointsDistance, hspoints = self.getHighSymmetryPoints()

        for i in range(0, len(hspointsDistance)):
            plt.axvline(x = hspointsDistance[i], color="k")

        plt.axhline(y = 0, linestyle="--") # fermi line

        plt.xticks(hspointsDistance, hspointsName)

        plt.ylim(-4,8)
        plt.xlim(distances[0], distances[-1])
        plt.ylabel('Energy (eV)', fontsize = 18)
        plt.tight_layout()
        plt.savefig("band_new.png", dpi=300)
###
#band =  PlotBand(path = '.')
n = 0 
kpoint_sum = []
band_sum  = []
hspointsName_sum  = []
xbar = []
nhspoints = 0
for i in xrange(1,4):
    p = 'nonscf_' + str(i)
    band =  PlotBand(path = p)
    kpoints, bands, xbar  = band.getBand()
    print xbar
    if kpoint_sum == []:
        kpoint_sum = kpoints
        #band_sum =  np.transpose(bands) 
        #band_sum =  bands + xbar
        band_sum =  bands
    else:
        kpoint_sum = np.vstack([kpoint_sum, kpoints])
        #band_sum = np.vstack([band_sum,  bands + xbar])
        band_sum = np.vstack([band_sum,  bands])
    hspointsName, nhspoints = band.getHighSymmetryPoints()
    if i ==1: 
        hspointsName_sum = hspointsName
    else:
        hspointsName_sum = np.hstack([hspointsName_sum, hspointsName[1:]])
    nhspoints = nhspoints
    #print hspointsName_sum
    #xbar.append(str(xbar))
###### read the indirect gap and direct band gap  ######
#print kpoint_sum, len(kpoint_sum)
#print band_sum, len(band_sum)
Maxer = -100
Miner = 100
counter_vbm = 0
counter_cbm = 0
E_counts_vbm = 0
E_counts_cbm = 0
for k in xrange(0, len(kpoint_sum)):
    for m in xrange(0, len(band_sum[k])):
        if band_sum[k][m] < 0 and band_sum[k][m] > Maxer:
            Maxer = band_sum[k][m]
            counter_vbm = k
            E_counts_vbm = m
        elif band_sum[k][m] > 0 and band_sum[k][m] < Miner:
            Miner = band_sum[k][m]
            counter_cbm = k
            E_counts_cbm = m
#print Maxer, Miner
#print counter_vbm, counter_cbm, E_counts_vbm, E_counts_cbm
print "VBM kpoint is ", kpoint_sum[counter_vbm]
print "CBM kpoint is ", kpoint_sum[counter_cbm]
print "Band gap is ", Miner - Maxer
#print "Direct gap is ", band_sum[counter_vbm][E_counts_vbm+1] - band_sum[counter_vbm][E_counts_vbm] 
print "Direct gap is ", band_sum[counter_cbm][E_counts_cbm] - band_sum[counter_cbm][E_counts_cbm-1] 
####

#print hspointsName_sum
tmp =  PlotBand(path = 'band_1')
#hspointsName, nhspoints = tmp.getHighSymmetryPoints()
distance = tmp.convert_kpoint_cartesian(kpoint = kpoint_sum)
hspointsDistance = np.array(distance[0]) # origin point

for i in range(1, len(hspointsName_sum)):
    index = nhspoints*i - 1
    hspointsDistance = np.hstack([hspointsDistance, distance[index]])

# plot bands
shifts = 0.055969
band_sum = np.transpose(band_sum)
for i in range(0, band_sum.shape[0]):
    #band_sum[i] = band_sum[i]
    plt.plot(distance, band_sum[i] + shifts, "b")

# plot high symmerty lines
for i in range(0, len(hspointsDistance)):
    plt.axvline(x = hspointsDistance[i], color="k")

plt.axhline(y = 0, linestyle="--") # fermi line

plt.xticks(hspointsDistance, hspointsName_sum)

plt.ylim(-4,8)
plt.xlim(distance[0], distance[-1])
plt.ylabel('Energy (eV)', fontsize = 18)
plt.tight_layout()
plt.savefig("band_merge_p3m1_110.png", dpi=300)



#band.plotband()
