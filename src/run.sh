#!/usr/bin/env sh

snakemake -s Snakefile \
	-j1 \
	--rerun-triggers mtime \
	--rerun-incomplete \
	-p all
