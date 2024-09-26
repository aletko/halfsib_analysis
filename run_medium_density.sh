#! /bin/bash

module load snakemake
module load matplotlib
module load PLINK

snakemake --cores all --configfile medium_density.yaml -s run.smk