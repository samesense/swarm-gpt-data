'''Get venue info given fsq_id'''
import requests
import sys

fsq_id, out_json = sys.argv[1:]
with open('key') as f:
    key = f.readline().strip()

url = f"https://api.foursquare.com/v3/places/{fsq_id}"

headers = {
    "accept": "application/json",
    "Authorization":key
}

response = requests.get(url, headers=headers)
with open(out_json, "w") as json_file:
    print(response.text, file=json_file)
