#!/usr/bin/env python
import os,sys
import math
#import numpy as np
path = os.getcwd()
lists = sorted(os.listdir(path))
#lists = ['opt_charge_0','opt_charge_1','opt_charge_-1']
#lists = ['K_i_ab_charge_1','K_i_ab_charge_neutral','K_i_ac_charge_1','K_i_ac_charge_neutral']
#lists = ['CuInCl','CuInBr','CuInI','CuGaCl','CuGaBr','CuGaI','AgInCl','AgInBr','AgInI','AgGaCl','AgGaBr','AgGaI']
#lists = ['POSCAR_MAI','POSCAR_MABr','POSCAR_MACl','POSCAR_SbI3']


for i in range(0, len(lists)):
    if os.path.isdir(lists[i]):
	os.chdir(path + "/" + str(lists[i]))
	#os.system('rm -r band')
	#os.system('rm -r relax_cellshape')
	#os.system('rm -r relax_ions')
	#os.system('cp -r opt scf')
	#os.chdir('scf')
	#os.chdir('opt')
	#os.system('mv ../* ./')
	print os.getcwd()
        #tmp = os.popen('grep "reached required accuracy - stopping structural energy minimisation" vasp.log').readline()
        #tmp = os.popen('grep "reached required accuracy - stopping structural energy minimisation" run.log').readline()
        tmp = os.popen('grep "reached required accuracy - stopping structural energy minimisation" OUTCAR').readline()
        #tmp = os.popen('grep "General timing and accounting informations for this job:" OUTCAR').readline()
        if tmp=="":
               print "very bad news"
        else:
               print "successfully"
	

	#os.system('cp ../../cbvb.x ./')
	#os.system('./cbvb.x')
	os.chdir(path)

