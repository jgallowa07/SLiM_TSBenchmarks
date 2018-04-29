#!/bin/bash

SEED=27467
N=10
size=10

TIME_MEM_FILE_N=neutral_time_arg.N$N"."size$size".out"
TIME_MEM_FILE_I=initial_pedigree_time_arg.N$N"."size$size".out"
TIME_MEM_FILE_U=unordered_map_time_arg.N$N"."size$size".out"

(time ../../bin_initial/slim -s $SEED -d n_ind=$N -d size_rho=$size ../BenchRecipes/benchmarks_neutral.slim &> ../slurm_runs/$TIME_MEM_FILE_N) \
	&> ../Optimizations/$TIME_MEM_FILE_N

