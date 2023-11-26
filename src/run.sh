#!/usr/bin/env sh

snakemake -s Snakefile.py \
	-j1 \
	--rerun-triggers mtime \
	-p all_venues
