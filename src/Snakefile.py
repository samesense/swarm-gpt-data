include: "Snakefile_const.py"
include: "Snakefile_venues.py"


rule all:
    input:
        INT / 'gpt_data.csv'
