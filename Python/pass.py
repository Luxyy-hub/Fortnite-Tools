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

# Set up the request body for the battle pass purchase
purchase_data = {
    "currency": "VBUCKS",
    "items": [
        {
            "item_id": "BID_Tier100",
            "quantity": 1
        }
    ]
}

# Make the purchase request
purchase_response = requests.post("https://fortniteapi.com/v2/game/v2.4.0/offerings", headers=headers, json=purchase_data)

# Check the response status code to make sure the purchase was successful
if purchase_response.status_code == 200:
    print("Battle Pass successfully purchased!")
else:
    print("Error purchasing Battle Pass:", purchase_response.status_code, purchase_response.text)
