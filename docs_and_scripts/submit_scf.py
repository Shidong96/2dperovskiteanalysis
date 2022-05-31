#!/usr/bin/env python
import os,sys
import math
#import numpy as np
path = os.getcwd()
lists = sorted(os.listdir(path))
#lists = ['POSCAR_MA3Sb2I9_0D_dimer','POSCAR_MA3Sb2I9_layered_Cs','POSCAR_MA3Sb2I9_layer_Rb_monoclinic','POSCAR_MA3Sb2I9_C2c']
#lists = ['POSCAR_MA3Sb2I9_layered_Cs','POSCAR_MA3Sb2I9_layer_Rb_monoclinic','POSCAR_MA3Sb2I9_C2c']
#lists = ['POSCAR_MA3Sb2I9_0D_dimer']

counter =0
for i in range(0, len(lists)):
    #if os.path.isdir(lists[i]) and lists[i] != "POSCAR_MAPbI3_001_direct":
    if lists[i] == "POSCAR_MAPbI3_001_direct":
	os.chdir(path + "/" + str(lists[i]))
	#os.system('rm -r scf')
	#os.system('mkdir opt')
	#os.chdir('opt')
	#os.system('mv ../* ./')
	#os.chdir('..')
	#os.system('cp -r opt scf')
	os.chdir('scf')
	print os.getcwd()
	"""	
        #os.system('sed "20d" -i INCAR')
        #os.system('sed "19 aNPAR = 4" -i INCAR')
        os.system('sed "21d" -i INCAR')
        os.system('sed "20 aKSPACING = 0.30" -i INCAR')
        os.system('sed "29d" -i INCAR')
        #os.system('sed "22 aSYMPREC = 1e-3" -i INCAR')

	#os.system('./submit.sh')"""
	#os.system('rm  KPOINTS')
        os.system('cp CONTCAR POSCAR')
        os.system('diff POSCAR ../opt/CONTCAR')
        os.system('cp ../../INCAR_scf  ./INCAR')
        os.system('cp ../../KPOINTS  ./')
        #os.system('cp INCAR_4  ./INCAR')
        #os.system('cp ../vdw_kernel.bindat ./')
        #os.system('cp ../vasp_test.sh ./')
        os.system('cp ../../vasp.sh ./')
        #os.system('python get_unit_cell.py')
        #os.system('qsub vasp_test.sh')
        os.system('qsub vasp.sh')
	os.chdir(path)
	counter +=1
print counter
