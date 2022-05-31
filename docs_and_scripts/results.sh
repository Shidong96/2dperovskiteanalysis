mkdir BANDPICS
mkdir LOCPOTZ
for i in 0 1 2 3 4 5
do
cd $i/band
./cbvb.x
./pyband.py
cp BandStructure.png ../../BANDPICS/Bandpic_$i.png
cd ../scf
grep TOTEN OUTCAR|tail -1
./getaveragecorelevel.py
./getmidpotential.py LOCPOT Z
cp LOCPOT_Z ../../LOCPOTZ/LOCPOT_Z$i
cd ../../
done
