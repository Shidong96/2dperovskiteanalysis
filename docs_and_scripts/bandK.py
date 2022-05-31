#!/usr/bin/env python 
from pymatgen.symmetry.bandstructure import HighSymmKpath
from pymatgen.io.vaspio import Poscar
import os
__all__=['read_pscar','high_symmetry_path']
class constrctkpts():
        def __init__(self,path=None,file='POSCAR',points=30):

                if path == None: path = os.getcwd()
                self.hkpline=""""""
                self.read_pscar(path,file)
                self.high_symmetry_path(points)

        def read_pscar(self,path=None,file='POSCAR'):
                '''Readin the structure from POSCAR/CONTCAR'''
                a = Poscar.from_file(path+'/'+file)
                self.structure = a.structure

        def high_symmetry_path(self,points=30):
                '''Get the high symmetric paths'''
                structure = self.structure
                latstr    = HighSymmKpath(structure)
                kpath     = latstr.kpath['path']
                kpoint    = latstr.kpath['kpoints']
                kplines   = []
                title   = ("""k-points along high symmetry lines\
                          \n"""+str(points)+"""\nLine-mode\n"""+\
                          """rec""")
                print title
                for i in xrange(len(kpath)):
                        for k in xrange(len(kpath[i])):
                                if (i == 0 and k ==0) or (i == len(kpath) -1 and k ==len(kpath[i]) -1):
                                        print "".join(["{0:10.4f}".format(m) \
                                        for m in kpoint[kpath[i][k]]]),  '! '+str(kpath[i][k])
                                else:
                                        for j in xrange(0,2):print "".join(["{0:10.4f}".format(m) \
                                        for m in kpoint[kpath[i][k]]]),  '! '+str(kpath[i][k])


if __name__ == '__main__':
        constrctkpts(file='CONTCAR',points=30)

