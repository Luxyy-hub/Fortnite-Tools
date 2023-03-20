import okhttp3.MediaType.Companion.toMediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONObject

// Set up authentication
val api_key = ""
val authorization_token = ""

// Set up the request headers
val headers = mapOf(
    "Authorization" to "Bearer $api_key",
    "Content-Type" to "application/json"
).toHeaders()

// Set up the request body for the level grant
val grant_data = JSONObject().apply {
    put("quantity", 10)
}

// Make the level grant request
val client = OkHttpClient()
val request = Request.Builder()
    .url("https://fortniteapi.com/v2/game/v2.4.0/items/GrantLevel")
    .headers(headers)
    .post(grant_data.toString().toRequestBody("application/json".toMediaType()))
    .build()
val grant_response = client.newCall(request).execute()

// Check the response status code to make sure the grant was successful
if (grant_response.code == 200) {
    println("Levels granted successfully!")
} else {
    println("Error granting levels: ${grant_response.code} ${grant_response.body?.string()}")
}
