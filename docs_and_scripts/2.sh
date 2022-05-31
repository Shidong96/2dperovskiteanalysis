for i in 2 3 4 5 
do
cd POSCAR_BA2MA$i*
cd scf
cp ../../vasp.pbs ./
qsub vasp.pbs
cd ../../
done
