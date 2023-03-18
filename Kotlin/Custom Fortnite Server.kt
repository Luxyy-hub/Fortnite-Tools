import java.net.HttpURLConnection
import java.net.URL
import java.util.*

fun startCustomMatch(accessToken: String, matchParams: Map<String, Any>) {
    val url = URL("https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/matchmakingservice/ticket/player")
    val connection = url.openConnection() as HttpURLConnection
    connection.requestMethod = "POST"
    connection.setRequestProperty("Authorization", "bearer $accessToken")
    connection.setRequestProperty("Content-Type", "application/json")
    connection.doOutput = true
    val jsonInputString = """${toJson(matchParams)}"""
    val outputStream = connection.outputStream
    outputStream.write(jsonInputString.toByteArray(Charsets.UTF_8))
    outputStream.flush()
    outputStream.close()

    val responseCode = connection.responseCode
    val responseMessage = connection.responseMessage
    val responseBody = connection.inputStream.use { it.reader().use { reader -> reader.readText() } }

    if (responseCode == HttpURLConnection.HTTP_OK) {
        println("The custom match has been started successfully!")
    } else {
        println("An error occurred while starting the custom match: $responseCode $responseMessage $responseBody")
    }
}

fun main() {
    // Get access to Epic Games development program and access token
    // Specify desired game settings
    val matchParams: MutableMap<String, Any> = HashMap()
    matchParams["queue_id"] = "Playlist_DefaultSolo"
    matchParams["game_mode"] = "br"
    matchParams["game_type"] = "default"
    matchParams["team_size"] = 1
    matchParams["region"] = "EU"
    val customAttributes: MutableMap<String, String> = HashMap()
    customAttributes["gameplay_stats"] = "false"
    customAttributes["gameplay_replay"] = "false"
    customAttributes["spectator_count"] = "0"
    customAttributes["team_account_ids"] = "[]"
    matchParams["custom_attributes"] = customAttributes

    val accessToken = "your_access_token"

    startCustomMatch(accessToken, matchParams)
}

fun toJson(map: Map<String, Any>): String {
    val sb = StringBuilder()
    sb.append("{")
    for ((key, value) in map) {
        sb.append("\"$key\":")
        when (value) {
            is Map<*, *> -> sb.append(toJson(value as Map<String, Any>))
            is String -> sb.append("\"$value\"")
            else -> sb.append(value)
        }
        sb.append(",")
    }
    sb.deleteCharAt(sb.length - 1)
    sb.append("}")
    return sb.toString()
}
