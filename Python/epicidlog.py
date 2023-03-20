import requests

# Set up authentication
api_key = ""
authorization_token = ""

# Set up the request headers
headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json"
}

# Set up the request body with the account ID
account_id = "YOUR_EPIC_ACCOUNT_ID_HERE"
login_data = {
    "accountId": account_id
}

# Make the login request
login_response = requests.post("https://fortniteapi.com/v2/auth/login", headers=headers, json=login_data)

# Check the response status code to make sure the login was successful
if login_response.status_code == 200:
    print("Successfully logged in to account with ID:", account_id)
else:
    print("Error logging in:", login_response.status_code, login_response.text)
