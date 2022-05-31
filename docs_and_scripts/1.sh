for i in 0 1 2 3 4 5 
do
cd POSCAR_PEA2MA$i*
mkdir opt/
mkdir scf/
mv POSCAR_PEA2MA$i* opt/
cp ../vasp_circ.pbs opt/
cp ../vdw_kernel.bindat opt/
cp ../vdw_kernel.bindat scf/
cp ../INCAR_SCF scf/
cp ../INCAR_1 opt
cp ../INCAR_2 opt
cp ../INCAR_3 opt
cp ../getPOTCAR.py opt
cp ../KPOINTS opt
cp ../KPOINTS scf

cd opt/
cp POSCAR_PEA2MA$i* POSCAR
chmod 664 POSCAR
python getPOTCAR.py
cd ..
cd scf/
cp INCAR_SCF INCAR
cd ..
cd opt
qsub vasp_circ.pbs
cd ..

cd ..
done
