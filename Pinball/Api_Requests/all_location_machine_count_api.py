
import requests
import json
import pandas as pd

url = "https://pinballmap.com/api/v1/regions/location_and_machine_counts"
response = requests.get(url)
data = response.json()
print(pd.json_normalize(data))