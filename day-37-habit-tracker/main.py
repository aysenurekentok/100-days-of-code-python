import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "heartbeatxprecious"
TOKEN = "dskj87843wcu"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "graph1"

graph_config = {
    "id": graph_id,
    "name": "Reading Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

create_pixel_endpoint = f"{graph_endpoint}/{graph_id}"

today = datetime.now()
date = today.strftime("%Y%m%d")

graph_config2 = {
    "date": date,
    "quantity": "65"
}

# response = requests.post(url=create_pixel_endpoint, json=graph_config2, headers=headers)
# print(response.text)

update_endpoint = f"{create_pixel_endpoint}/{date}"

update_parameters = {
    "quantity": "30"
}

# response = requests.put(url=update_endpoint, json=update_parameters, headers=headers)
# print(response.text)

delete_endpoint = f"{update_endpoint}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
