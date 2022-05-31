#!/usr/bin/env python
import os,sys
import math
from pymatgen.io.vaspio import Poscar

class generate():
    def __init__(self,path):
        if path == None:path = os.getcwd()
    def get_structure(self):
        os.system('rm POTCAR')
        #print Poscar.from_file('CONTCAR')
        a = Poscar.from_file('POSCAR')
        elements = a.site_symbols
        print elements
        #os.system('rm POTCAR')
        for i in xrange(0,len(elements)):
                print elements[i]
                if (elements[i] == 'Pb'):
                        os.system('cat /home/xgzhao/usr/psudopotential/paw_pbe/Pb/POTCAR >> POTCAR')
                else:
                        os.system('cat /home/xgzhao/usr/psudopotential/paw_pbe/{0}/POTCAR >> POTCAR'.format(elements[i]))
        #print a

###
if __name__ == '__main__':
        G= generate('.')
        G.get_structure()

