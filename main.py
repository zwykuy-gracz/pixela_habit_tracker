import requests
from datetime import datetime as dt

USERNAME = 'lucjan1'
TOKEN = 'ergzvsvklaovl'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20221009"

graph_config = {
    'id': 'graph1',
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'sora',
}

headers = {
    'X-USER-TOKEN': TOKEN,
}

today = dt(year=2022, month=10, day=9)
todays_progess = {
    "date": today.strftime("%Y%m%d"),
    "quantity": '4',
}

response = requests.put(url=pixel_update_endpoint, json=todays_progess, headers=headers)
# response = requests.post(url=pixel_creation_endpoint, json=todays_progess, headers=headers)
# response = requests.get(url=graph_endpoint, headers=headers)
print(response.text)

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)