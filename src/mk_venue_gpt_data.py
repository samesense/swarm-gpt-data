'''Add venue caterories to raw venue dl'''
import sys

import pandas as pd

category_tsv, venue_csv, checkin_csv, out_csv = sys.argv[1:]
cats = pd.read_csv(category_tsv, delimiter="\t").rename(columns={"fsq_id": "id"})
cols = [
    "id",
    "name",
    "address",
    "postalCode",
    "cc",
    "city",
    "state",
    "country",
    "formattedAddress",
    "latitude",
    "longitude",
    "crossStreet",
    "neighborhood",
]
dat = pd.read_csv(venue_csv, on_bad_lines = 'warn')[cols].rename(columns={'name':'venue_name'})
df = pd.merge(dat, cats, on="id", how="left").rename(columns={'id':'venue_id'})

cols = ['id', 'created', 'venue', 'timeZoneOffset', 'shout',]
dat = pd.read_csv(checkin_csv, on_bad_lines = 'warn')[cols].rename(columns={'venue':'venue_id'})
df = pd.merge(dat, df, on="venue_id", how="left")
df.to_csv(out_csv, index=False)
