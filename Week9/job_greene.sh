#!/bin/bash -l
#SBATCH --time=96:00:00
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --output=error.%j.o
#SBATCH --error=error.%j.e
#SBATCH --mail-type=REQUEUE
#SBATCH --mem=20GB

source /scratch/work/courses/CHEM-GA-2671-2023fa/software/lammps-gcc-30Oct2022/setup_lammps.bash

mpirun lmp -var configfile ../Inputs/n360/kalj_n360_create.lmp -var id 1 -in ../Inputs/create_3d_binary.lmp

mpirun lmp -var configfile ../Inputs/n360/kalj_n360_T1.5.lmp -var id 1 -in ../Inputs/anneal_3d_binary.lmp

