import requests
import os
from datetime import datetime
USERNAME = "azan"
TOKEN = os.enviorn["TOKEN"]
ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

# user_parmas = {
#     "token":TOKEN,
#     "username":USERNAME,
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }
# response = requests.post(url=pixela_endpoint,json=user_parmas)
# print(response.text)

# graph_config = {
#     "id":ID,
#     "name":"Cycling Graph",
#     "unit":"Km",
#     "type":"float",
#     "color":"ajisai"
# }

today = datetime(year=2024,month=9,day=5)

# pixel_post_config = {
#     "date":tomorrow.strftime("%Y%m%d"),
#     "quantity":"21.65",
# }

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{today.strftime('%Y%m%d')}"

headers = {
    "X-USER-TOKEN":TOKEN
}
response = requests.post(url=delete_pixel_endpoint,headers=headers)
print(response.text)
