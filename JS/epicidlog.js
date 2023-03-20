const fetch = require('node-fetch');

// Set up authentication
const api_key = "";
const authorization_token = "";

// Set up the request headers
const headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json"
}

// Set up the request body with the account ID
const account_id = "YOUR_EPIC_ACCOUNT_ID_HERE";
const login_data = {
    "accountId": account_id
};

// Make the login request
fetch("https://fortniteapi.com/v2/auth/login", {
    method: "POST",
    headers: headers,
    body: JSON.stringify(login_data)
})
.then(response => {
    // Check the response status code to make sure the login was successful
    if (response.status === 200) {
        console.log("Successfully logged in to account with ID:", account_id);
    } else {
        console.log("Error logging in:", response.status, response.statusText);
    }
})
.catch(error => console.log("Error:", error));
