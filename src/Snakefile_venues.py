import csv

def load_venues():
    venues = {}
    with open(RAW / 'venues.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            id = row['id']
            venues[id] = True
    return venues

VENUES = ['5275501b11d23f6cc01041fa', '4f21bcb7a17c052b073720da'] #load_venues()

rule get_venue_info:
    output:
        INT / 'venue_json/{id}.json'
    shell:
        'python query_fsq.py {wildcards.id} {output}'

rule all_venues:
    input:
        expand(INT / 'venue_json/{id}.json', id=VENUES)
