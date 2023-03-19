import requests

# Set up authentication
access_token = "YOUR_ACCESS_TOKEN"
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Set up the request body for the player feedback
feedback_data = {
    "Category": "Cheating",
    "Subject": "Suspected Cheating",
    "Body": "I suspect this player is cheating because...",
    "PlayerId": ""
}

# Make the player feedback request
response = requests.post("https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{account_id}/client/PlayerFeedback", headers=headers, json=feedback_data)

# Check the response status code to make sure the request was successful
if response.status_code == 200:
    print("Player successfully reported!")
else:
    print("Error reporting player:", response.status_code, response.text)
