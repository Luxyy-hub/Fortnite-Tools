const fetch = require('node-fetch');

// Set up authentication
const api_key = "";
const authorization_token = "";

// Set up the request headers
const headers = {
  "Authorization": "Bearer " + api_key,
  "Content-Type": "application/json"
};

// Set up the request body for the battle pass purchase
const purchase_data = {
  "currency": "VBUCKS",
  "items": [
    {
      "item_id": "BID_Tier100",
      "quantity": 1
    }
  ]
};

// Make the purchase request
fetch("https://fortniteapi.com/v2/game/v2.4.0/offerings", {
  method: 'POST',
  headers,
  body: JSON.stringify(purchase_data)
})
.then(purchase_response => {
  // Check the response status code to make sure the purchase was successful
  if (purchase_response.status === 200) {
    console.log("Battle Pass successfully purchased!");
  } else {
    console.log("Error purchasing Battle Pass:", purchase_response.status, purchase_response.statusText);
  }
});
