import okhttp3.OkHttpClient
import okhttp3.Request
import org.json.JSONObject

fun main() {
    val url = "https://fortniteapi.com/v2/cosmetics/br"
    val apiKey = "YOUR_API_KEY"

    val client = OkHttpClient()
    val request = Request.Builder()
        .url(url)
        .addHeader("Authorization", apiKey)
        .addHeader("Content-Type", "application/json")
        .build()

    val response = client.newCall(request).execute()

    if (response.code() == 200) {
        val responseData = response.body()?.string()
        val jsonObject = JSONObject(responseData)

        val dataArray = jsonObject.getJSONArray("data")
        for (i in 0 until dataArray.length()) {
            val item = dataArray.getJSONObject(i)
            if (item.getJSONObject("type").getString("value") == "outfit") {
                println("Name: ${item.getString("name")}")
                println("Rarity: ${item.getJSONObject("rarity").getString("value")}")
                println()
            }
        }
    } else {
        println("Error: ${response.code()} ${response.body()?.string()}")
    }
}
