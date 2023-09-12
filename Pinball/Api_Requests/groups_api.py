import requests
import json
import pandas as pd

# api token
# 21eu4djBC3xg81s1gZYsyIIIOfw2JOsQuIeHO3tvjWp3rl1F9IQv7KwxICBD

url = "https://opdb.org/api/export/groups"

parameters = {
    "api_token": "21eu4djBC3xg81s1gZYsyIIIOfw2JOsQuIeHO3tvjWp3rl1F9IQv7KwxICBD"
}

response = requests.get(url, params = parameters)

print(response.status_code)

# print(response.json())


data = response.json()
print(len(data))

df = pd.json_normalize(data)
# print(df)

df.to_csv("group_data.csv")