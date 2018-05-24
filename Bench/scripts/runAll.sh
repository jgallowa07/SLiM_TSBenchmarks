#!/bin/bash

SEED=27467

for N in 1000 10000 
do
	for size in 1000 10000
	do	
		
		PED_OUTPUT_FILE_NAME=ped_output.N$N"."size$size".out"
		PED_TIME_FILE_NAME=ped_timimg.N$N"."size$size".out"
		NEUT_OUTPUT_FILE_NAME=neut_output.N$N"."size$size".out"
		NEUT_TIME_FILE_NAME=neut_timimg.N$N"."size$size".out"
		PEDNM_OUTPUT_FILE_NAME=pedNM_output.N$N"."size$size".out"
		PEDNM_TIME_FILE_NAME=pedNM_timimg.N$N"."size$size".out"
		REL_OUTPUT_FILE_NAME=rel_output.N$N"."size$size".out"
		REL_TIME_FILE_NAME=rel_timimg.N$N"."size$size".out"


		#Neutral Mutations
		/usr/local/Cellar/gnu-time/1.9/bin/gtime --format='%E / %S / %U / %M' \
		  --output="../ComparisonTimes/RealTimes/$NEUT_TIME_FILE_NAME" ../../../SLiM/bin/slim \
		  -s $SEED -d n_ind=$N -d size_rho=$size ../BenchRecipes/benchmarks_neutral.slim &> ../Output/Reals/$NEUT_OUTPUT_FILE_NAME

		#Neutral Mutations Release SLiM
		/usr/local/Cellar/gnu-time/1.9/bin/gtime --format='%E / %S / %U / %M' \
		  --output="../ComparisonTimes/RealTimes/$REL_TIME_FILE_NAME" ../../../SLiM2_6/bin/slim \
		  -s $SEED -d n_ind=$N -d size_rho=$size ../BenchRecipes/benchmarks_neutral.slim &> ../Output/Reals/$REL_OUTPUT_FILE_NAME

		#Pedigree Recording With Mutations
		/usr/local/Cellar/gnu-time/1.9/bin/gtime --format='%E / %S / %U / %M' \
		  --output="../ComparisonTimes/RealTimes/$PED_TIME_FILE_NAME" ../../../SLiM/bin/slim \
		  -s $SEED -d n_ind=$N -d size_rho=$size ../BenchRecipes/benchmarks_pedigree.slim &> ../Output/Reals/$PED_OUTPUT_FILE_NAME

		#Pedigree Recording W/O Mutations
		/usr/local/Cellar/gnu-time/1.9/bin/gtime --format='%E / %S / %U / %M' \
		  --output="../ComparisonTimes/RealTimes/$PEDNM_TIME_FILE_NAME" ../../../SLiM/bin/slim \
		  -s $SEED -d n_ind=$N -d size_rho=$size ../BenchRecipes/benchmarks_pedigree_nm.slim &> ../Output/Reals/$PEDNM_OUTPUT_FILE_NAME

	done
done




