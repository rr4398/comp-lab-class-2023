#!/bin/bash
#SBATCH --job-name=Week5
#SBATCH --nodes=1
#SBATCH --tasks-per-node=20
#SBATCH --mem=8GB
#SBATCH --time=04:00:00
##SBATCH --gres=gpu:1 ## To ask for a gpu, remove #, don’t need right now
module purge
#module load gromacs/openmpi/intel/2020.4
module load gromacs/openmpi/intel/2018.3
#mpirun gmx_mpi pdb2gmx -f 1AKI_clean.pdb -o 1AKI_processed.gro -water spce
#mpirun gmx_mpi editconf -f 1AKI_processed.gro -o 1AKI_newbox.gro -c -d 1.0 -bt cubic
#mpirun gmx_mpi solvate -cp 1AKI_newbox.gro -cs spc216.gro -o 1AKI_solv.gro -p topol.top
#mpirun gmx_mpi grompp -f ions.mdp -c 1AKI_solv.gro -p topol.top -o ions.tpr
#mpirun -np 20 gmx_mpi grompp -f adp_T300.mdp -c adp.gro -p adp.top -o adp_T300.tpr
#mpirun gmx_mpi mdrun -v -deffnm adp_T300
gmx grompp -f adp_T300.mdp -c adp.gro -p adp.top -o adp_T300.tpr
gmx mdrun -v -deffnm adp_T300
