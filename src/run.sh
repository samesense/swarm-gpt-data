#!/usr/bin/env sh

snakemake -s Snakefile.py \
	--use-conda \
	-j1 \
	--rerun-triggers mtime \
	--rerun-incomplete \
	-n all
