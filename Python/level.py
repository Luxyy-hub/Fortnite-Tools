import requests
import json

# Set up authentication
api_key = ""
authorization_token = ""

# Set up the request headers
headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json"
}

# Set up the request body for the level grant
grant_data = {
    "quantity": 10
}

# Make the level grant request
grant_response = requests.post("https://fortniteapi.com/v2/game/v2.4.0/items/GrantLevel", headers=headers, json=grant_data)

# Check the response status code to make sure the grant was successful
if grant_response.status_code == 200:
    print("Levels granted successfully!")
else:
    print("Error granting levels:", grant_response.status_code, grant_response.text)
