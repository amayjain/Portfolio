import requests
import json
import pandas as pd

# Example
# url = "https://pinballmap.com/api/v1/machines"

# apis = {"/api/v1/locations.json": 'Fetch locations for all regions',
# "/api/v1/regions": "Fetch all regions",
# "/api/v1/regions/location_and_machine_counts": "Get location and machine counts",
# "/api/v1/location_machine_xrefs/top_n_machines": "Show the top N machines on location"}

url_main = "https://pinballmap.com"
url_api = "/api/v1/regions"
url = url_main + url_api

response = requests.get(url)
# print(response.status_code)
data = response.json()

# json_str = json.dumps(data, indent=3)
# print(json_str)

# to find regions
# url_api = "/api/v1/regions"
df = pd.json_normalize(data, "regions")
regions = list(df["name"])
