import requests

url = "https://pontos.ri.se/api/vessel_ids"
headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2wiOiIiLCJjb3VudHJ5IjoiU0UiLCJleHAiOjE3MzQxMjk0NjcsImlhdCI6MTczMTQ5OTcyMSwiaXNzIjoicG9udG9zLWh1YiIsIm9yZ2FuaXNhdGlvbl90eXBlIjoidW5pdmVyc2l0eSIsInB1cnBvc2UiOiJyZXNlYXJjaCIsInJvbGUiOiJ3ZWJfdXNlciIsInN1YiI6Il9fdG9rZW5fXyJ9.8WUTLR8_g1iDjk264ElCfWVQ2XBrV6ZqKeCpVN-Nrvs"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Data fetched successfully!")
    data = response.json()
    print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
