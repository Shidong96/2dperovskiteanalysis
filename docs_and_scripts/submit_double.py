#!/usr/bin/env python
import os,sys
import math
#import numpy as np
path = os.getcwd()
lists = sorted(os.listdir(path))
#lists = ['POSCAR_MA3Sb2I9_0D_dimer','POSCAR_MA3Sb2I9_layered_Cs','POSCAR_MA3Sb2I9_layer_Rb_monoclinic','POSCAR_MA3Sb2I9_C2c']
#lists = ['POSCAR_Cs2Sb2I6Cl3_I1_1_I4_2_direct','POSCAR_Cs2Sb2I6Cl3_I1_2_I4_1_direct','POSCAR_Cs2Sb2I6Cl3_I1_3_direct','POSCAR_Cs2Sb2I6Cl3_I4_3_direct','POSCAR_Cs2Sb2I8Cl_I1_direct','POSCAR_Cs2Sb2I8Cl_I4_direct']

for i in range(0, len(lists)):
    if os.path.isdir(lists[i]) and lists[i] != "POSCAR_MAPbI3_001_direct":
	os.chdir(path + "/" + str(lists[i]))
	#os.system('rm -r band')
	#os.system('rm -r relax_cellshape')
	#os.system('rm -r relax_ions')
	#os.system('rm -r hse')
	#os.system('cp -r scf hse')
	#os.chdir('hse')
	#os.system('mv ../* ./')
	print os.getcwd()
	

	#os.system('cp CONTCAR POSCAR')
        #os.system('sed "22 aSYMPREC = 1e-3" -i INCAR')
        #os.system('cp ../../INCAR_hse ./INCAR')
        #os.system('cp ../../vasp.pbs ./')
        #os.system('cp IBZKPT KPOINTS')
        #os.system('grep ENMAX POTCAR > tmp.dat')
        #inputf = open("tmp.dat",'r')
        #lines = os.popen('wc -l tmp.dat').readline().split()[0]
        #print lines
        #ENMAX = []
        #for i in xrange(0,int(lines)):
        #        line = inputf.readline().split()[2]
        #        #print line
        #        ENMAX.append(float(line.strip(';')))
        #print np.array(ENMAX).max()
        #tmp = np.array(ENMAX).max()
        #print float(tmp)*1.3
        #os.system('sed "1d" -i INCAR')
        #os.system('sed "1 iENCUT= {0}" -i INCAR'.format(tmp*1.3))
        #os.system('rm -r tmp.dat')
        #os.system('rm -r KPOINTS')



	os.system('cp ../KPOINTS ./')
	os.system('cp ../vasp.sh ./')
	os.system('cp ../dwyang ./')
	os.system('cp ../INCAR* ./')
	#os.system('cp ../KPOINTS ./')
	os.system('cp ../vdw_kernel.bindat ./')
	#os.system('qsub vasp.sh')
	#os.system('./submit.sh')
	os.chdir(path)

