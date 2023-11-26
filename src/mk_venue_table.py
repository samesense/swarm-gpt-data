"""Mk csv for one json file"""
import json
import sys


def is_invalid(venue_json):
    with open(venue_json) as f:
        for line in f:
            if "invalid venue" in line:
                return True
    return False


def write_tab(venue_json, out_tab):
    with open(venue_json) as f, open(out_tab, "w") as fout:
        print("fsq_id\tCategories", file=fout)
        data = json.load(f)
        venue_id = data["fsq_id"]
        cats = []
        for category in data["categories"]:
            cat_name = category["name"]
            cats.append(cat_name)
        cats = ";".join(cats)
        print(f"{venue_id}\t{cats}", file=fout)


venue_id, venue_json, out_tab = sys.argv[1:]
if is_invalid(venue_json):
    with open(out_tab, "w") as fout:
        print("fsq_id\tCategories", file=fout)
        print(f"{venue_id}\t", file=fout)
else:
    write_tab(venue_json, out_tab)
