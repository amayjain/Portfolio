import requests
import json
import pandas as pd
from pinball_regions_api import regions

url_main = "https://pinballmap.com"
url_api = "/api/v1/locations"
url = url_main + url_api


# baseline
response = requests.get(url, params = {"region": regions[0]})
print(response.status_code)
data = response.json()


# json_str = json.dumps(data, indent=3)
# print(json_str)

df = pd.json_normalize(data, "locations")

# attach all other regions and their machines
for i in range(1, len(regions)):
    resp = requests.get(url, params = {"region": regions[i]})
    data_ = resp.json()
    df = pd.concat([df, pd.json_normalize(data_, "locations")])

df.to_csv("locations_machines_attributes.csv")