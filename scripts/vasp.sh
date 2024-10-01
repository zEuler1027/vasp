#!/bin/bash
#SBATCH -p 64c512g
#SBATCH --ntasks-per-node=64
#SBATCH -J __cpu__
#SBATCH -n 64 

module load vasp/6.3.2-TS-Sol-Beef-intel-2021.4.0
module load intel

ulimit -l unlimited
ulimit -s unlimited

ROOTDIR=$(pwd)
for dir in "$ROOTDIR"/*/; do  
        echo "Entering $dir"  
        cd "$dir" || exit # 切换到目录，如果失败则退出  
	mpirun vasp_std
		#mpirun -np $SLURM_NPROCS $EXEC
	cd ..
done

scontrol show job $SLURM_JOBID
