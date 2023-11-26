import csv

def load_venues():
    venues = {}
    with open(RAW / 'venues.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            id = row['id']
            venues[id] = True
    return venues

VENUES = list(load_venues())[:1000]

rule get_venue_info:
    output:
        INT / 'venue_json/{id}.json'
    shell:
        'python query_fsq.py {wildcards.id} {output}'

rule format_venue_info:
    input:
        INT / 'venue_json/{id}.json'
    output:
        INT / 'tmp/venue_tab/{id}.tsv'
    shell:
        'python mk_venue_table.py {wildcards.id} {input} {output}'

rule cat_venues:
    input:
        expand(INT / 'tmp/venue_tab/{id}.tsv', id=VENUES)
    output:
        INT / 'tmp/venues.tsv'
    params:
        dir = INT / 'tmp/venue_tab'
    shell:
        'python cat_tables.py {params.dir} {output}'

rule gpt_venues:
    input:
        INT / 'tmp/venues.tsv',
        RAW / 'venues.csv',
    output:
        INT / 'venues.csv'
    shell:
        'python mk_venue_gpt_data.py {input} {output}'
