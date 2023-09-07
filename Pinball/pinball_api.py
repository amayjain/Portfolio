import requests
import json
import pandas as pd

# api token
# 21eu4djBC3xg81s1gZYsyIIIOfw2JOsQuIeHO3tvjWp3rl1F9IQv7KwxICBD

names = ['Sorcerer', 'Black Knight', 
         'Space Shuttle', 'Firepower', 
         'Pinbot', 'Fun House', 
         'Whirlwind']

url = "https://opdb.org/api/export"

parameters = {
    "api_token": "21eu4djBC3xg81s1gZYsyIIIOfw2JOsQuIeHO3tvjWp3rl1F9IQv7KwxICBD"
}

response = requests.get(url, params = parameters)

print(response.status_code)

# print(response.json())


data = response.json()
print(len(data))

df1 = pd.json_normalize(data)
df2 = pd.json_normalize(data, 'images')
df = pd.concat([df1,df2], axis = 1)





df.to_csv("all_data.csv")


