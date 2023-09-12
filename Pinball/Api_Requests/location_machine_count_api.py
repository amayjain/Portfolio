from pinball_regions_api import *


# test_region = regions[1]

# url_main = "https://pinballmap.com"
# url_api = "/api/v1/regions/location_and_machine_counts"
# url = url_main + url_api

# parameters = {"region_name": test_region}

# response = requests.get(url, params = parameters)
# print(response.status_code)
# data = response.json()

# # print(data)

# df = pd.json_normalize(data)

# print(df)

df = pd.DataFrame(data = {'regions': regions})

def get_loc(region):
    url = "https://pinballmap.com/api/v1/regions/location_and_machine_counts"
    parameters = {"region_name": region}
    response = requests.get(url, params = parameters)
    data = response.json()
    return pd.json_normalize(data)['num_locations']

def get_mac(region):
    url = "https://pinballmap.com/api/v1/regions/location_and_machine_counts"
    parameters = {"region_name": region}
    response = requests.get(url, params = parameters)
    data = response.json()
    return pd.json_normalize(data)['num_lmxes']

df['#_locations'] = df['regions'].apply(get_loc)
df['#_machines'] = df['regions'].apply(get_mac)

df.to_csv("region_location_machine_counts.csv")


