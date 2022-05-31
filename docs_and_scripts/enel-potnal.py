#!/usr/bin/python

from pymatgen.io.vaspio import Vasprun
import os

path = os.getcwd()

def get_pot():
  from pymatgen.io.vaspio import Locpot
  locpot =  Locpot.from_file('LOCPOT')
  #yy = locpot.get_average_along_axis(2)[-1]
  zz = locpot.get_average_along_axis(2)
  yy = zz[0]
  print yy

os.chdir(path)
get_pot()

