// Made by Luxy, https://github.com/Luxyy-hub, Discord: SuperCharger#2023

const axios = require('axios');

const apiKey = "";
const authorizationToken = "";

const purchaseData = {
    currency: "USD",
    items: [
        {
            item_id: "monthlySubscription",
            quantity: 1
        }
    ],
    payment_token: "<insert payment token here>",
    subscription_id: "<insert subscription id here>"
};

const config = {
    headers: {
        "Authorization": `Bearer ${authorizationToken}`,
        "Content-Type": "application/json"
    }
};

axios.post("https://payments.fortnite.com/v1/tokens/purchase", purchaseData, config)
    .then(response => {
        console.log("Fortnite Crew subscription successfully purchased!");
    })
    .catch(error => {
        console.log(`Error purchasing Fortnite Crew subscription: ${error.response.status} ${error.response.data}`);
    });
