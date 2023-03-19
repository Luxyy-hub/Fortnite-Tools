import requests

# Set up the authentication
api_key = "YOUR_API_KEY_HERE"

# Set up the request headers
headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json"
}

# Make the request to get the store data
store_response = requests.get("https://fortniteapi.com/v2/shop/br", headers=headers)

# Parse the response to get the available banners
store_data = store_response.json()
available_banners = []
for item in store_data['data']['featured']:
    if item['type'] == 'Banner':
        available_banners.append(item)

# Buy the first banner in the available list
if len(available_banners) > 0:
    banner_to_buy = available_banners[0]
    buy_data = {
        "item": {
            "item_id": banner_to_buy['itemId'],
            "item_category": banner_to_buy['itemCategory'],
            "item_rarity": banner_to_buy['itemRarity'],
            "item_type": banner_to_buy['itemType']
        },
        "currency": "MtxCurrency",
        "quantity": 1
    }
    buy_response = requests.post("https://fortniteapi.com/v2/shop/br/buy", headers=headers, json=buy_data)
    if buy_response.status_code == 200:
        print("Successfully purchased banner:", banner_to_buy['name'])
    else:
        print("Error purchasing banner:", buy_response.status_code, buy_response.text)
else:
    print("No banners available to purchase")
