const fetch = require('node-fetch');

// Set up the authentication
const api_key = "YOUR_API_KEY_HERE";

// Set up the request headers
const headers = {
  "Authorization": "Bearer " + api_key,
  "Content-Type": "application/json"
};

// Make the request to get the store data
fetch("https://fortniteapi.com/v2/shop/br", { headers })
  .then(response => response.json())
  .then(store_data => {
    const available_banners = store_data.data.featured.filter(item => item.type === 'Banner');

    // Buy the first banner in the available list
    if (available_banners.length > 0) {
      const banner_to_buy = available_banners[0];
      const buy_data = {
        "item": {
          "item_id": banner_to_buy.itemId,
          "item_category": banner_to_buy.itemCategory,
          "item_rarity": banner_to_buy.itemRarity,
          "item_type": banner_to_buy.itemType
        },
        "currency": "MtxCurrency",
        "quantity": 1
      };

      fetch("https://fortniteapi.com/v2/shop/br/buy", {
        method: 'POST',
        headers,
        body: JSON.stringify(buy_data)
      })
      .then(buy_response => {
        if (buy_response.status === 200) {
          console.log("Successfully purchased banner:", banner_to_buy.name);
        } else {
          console.log("Error purchasing banner:", buy_response.status, buy_response.statusText);
        }
      });
    } else {
      console.log("No banners available to purchase");
    }
  });
