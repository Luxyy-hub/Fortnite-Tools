// coded by Luxy(the real one, fuck daniel) 
// player feedback request fixed by Mr-zanzibar
// Discord : SuperCharger#2023 ,Don.Zanzibar#3562
#include <iostream>
#include <cpprest/http_client.h>

using namespace web;
using namespace web::http;
using namespace web::http::client;

int main() {
    // Set up authentication
    const std::string access_token = "YOUR_ACCESS_TOKEN";
    const http_headers headers { U("Authorization"), U("Bearer " + access_token) };

    // Set up the request body for the player feedback
    const json::value feedback_data {
        { "Category", "Cheating" },
        { "Subject", "Suspected Cheating" },
        { "Body", "I suspect this player is cheating because..." },
        { "PlayerId", "" }
    };

    // Make the player feedback request
    http_client client { U("https://fortnite-public-service-prod11.ol.epicgames.com") };
    uri_builder builder { U("/fortnite/api/game/v2/profile/{account_id}/client/PlayerFeedback") };
    const pplx::task<http_response> response = client.request(methods::POST, builder.to_string(), headers, feedback_data);

    // Check the response status code to make sure the request was successful
    response.then([](const http_response& response) {
        if (response.status_code() == 200) {
            std::cout << "Player successfully reported!" << std::endl;
        } else {
            std::cout << "Error reporting player: " << response.status_code() << " " << response.reason_phrase() << std::endl;
        }
    }).wait();

    return 0;
}
