#!/usr/bin/env python

from pymatgen.io.vaspio import Vasprun
import os
import sys

# get directory list
path = os.getcwd()
lists = sorted(os.listdir(path))

outfile = open("dir\tgap.txt", "w")
outfile.write("gap\tdirect\n")

for i in range(0, len(lists)):
    if(os.path.isdir(lists[i])): # folder
        print lists[i]
        os.chdir(path + "/" + lists[i])
        gap=0.0
        direct=0.0
        #filedir=sys.argv[1]
        run = Vasprun('./vasprun.xml', parse_projected_eigen=False)
        bands = run.get_band_structure()
        gap = bands.get_band_gap()['energy']
        direct = bands.get_direct_band_gap()

        outfile.write(lists[i])
        outfile.write("\t")
        outfile.write(str(gap))
        outfile.write("\t")
        outfile.write(str(direct))
        outfile.write("\t\n")
        os.chdir(path)

outfile.close()


