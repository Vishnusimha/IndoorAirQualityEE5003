package com.vishnu.airqualitymonitor.repository

import android.util.Log
import com.vishnu.airqualitymonitor.data.Scd40
import okhttp3.Call
import okhttp3.Callback
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.Response
import org.json.JSONArray
import org.json.JSONObject
import java.io.IOException

class Scd40RepositoryImpl : Scd40Repository {
    var field1Value = ""
    var field2Value = 0
    var field3Value = 0
    var field4Value = 0

    private val client = OkHttpClient()

    override suspend fun getScd40DataFromThingSpeak(): Scd40 {
        val url =
            "https://api.thingspeak.com/channels/2170317/feeds.json?api_key=ZX4O2GQUNBUWP5WG&results=1"
        val request = Request.Builder()
            .url(url)
            .get()
            .build()

        client.newCall(request).enqueue(object : Callback {
            override fun onFailure(call: Call, e: IOException) {
                Log.e("JSONRequest", "Failed to make request: ${e.message}")
            }

            override fun onResponse(call: Call, response: Response) {
                val json = response.body?.string()?.let { JSONObject(it) }
                Log.d("JSONResponse", json.toString())
                // Handle the JSON data as needed
                // Get the "feeds" array from the JSON response
                val feedsArray = json?.getJSONArray("feeds")

                if (feedsArray != null) {
                    if (feedsArray.length() > 0) {
                        // Get the latest entry from the "feeds" array
                        val latestEntry = feedsArray.getJSONObject(0)

                        // Extract the values of "field1", "field2", "field3", and "field4"
                        field1Value = latestEntry.optString("field1", "")
                        field2Value = latestEntry.optDouble("field2", 0.0).toInt()
                        field3Value = latestEntry.optDouble("field3", 0.0).toInt()
                        field4Value = latestEntry.optInt("field4", 0)

                        // Do something with the extracted values
                        Log.d("Field1", field1Value)
                        Log.d("Field2", field2Value.toString())
                        Log.d("Field3", field3Value.toString())
                        Log.d("Field4", field4Value.toString())
                    } else {
                        Log.e("JSONResponse", "No data available")
                    }
                }
            }
        })
        return Scd40(field1Value, field2Value, field3Value, field4Value)
    }

    override suspend fun getScd40FullDataFromThingSpeak(): String {
        val url = "https://api.thingspeak.com/channels/2170317/feeds.json?api_key=ZX4O2GQUNBUWP5WG"
        val request = Request.Builder()
            .url(url)
            .get()
            .build()

        var feedsJsonString = ""

        try {
            val response = client.newCall(request).execute()
            val jsonData = response.body?.string()

            if (response.isSuccessful && jsonData != null) {
                val json = JSONObject(jsonData)
                val feedsArray = json.optJSONArray("feeds")

                if (feedsArray != null) {
                    feedsJsonString = feedsArray.toString()
                    println("feedsJsonString: $feedsJsonString")
                }
            } else {
                Log.e("JSONRequest", "Failed to get JSON data: ${response.code}")
            }
        } catch (e: IOException) {
            Log.e("JSONRequest", "Failed to make request: ${e.message}")
        }

        return feedsJsonString
    }

    override suspend fun getLastScd40DataFromRaspberryPiServer(): Scd40 {
        val url = "http://192.168.1.43:8000/json"
        val request = Request.Builder()
            .url(url)
            .get()
            .build()

        try {
            val response = client.newCall(request).execute()
            val jsonData = response.body?.string()

            if (response.isSuccessful && jsonData != null) {
                // Parse the JSON array
                val jsonArray = JSONArray(jsonData)

                // Check if the JSON array is not empty
                if (jsonArray.length() > 0) {
                    // Get the latest entry (last object in the array)
                    val latestEntry = jsonArray.getJSONObject(jsonArray.length() - 1)

                    // Extract the values of field1, field2, field3, and field4
                    val field1Value = latestEntry.getString("field1")
                    val field2Value = latestEntry.getString("field2").toDouble().toInt()
                    val field3Value = latestEntry.getString("field3").toDouble().toInt()
                    val field4Value = latestEntry.getString("field4").toDouble().toInt()

                    // Do something with the extracted values
                    Log.i("CSVRequest", "Field1: $field1Value")
                    Log.i("CSVRequest", "Field2: $field2Value")
                    Log.i("CSVRequest", "Field3: $field3Value")
                    Log.i("CSVRequest", "Field4: $field4Value")

                    // Create and return the Scd40 object with the extracted values
                    return Scd40(field1Value, field2Value, field3Value, field4Value)
                } else {
                    Log.i("CSVRequest", "JSON array is empty")
                }
            } else {
                Log.e("CSVRequest", "Failed to get JSON data: ${response.code}")
            }
        } catch (e: IOException) {
            Log.e("CSVRequest", "Failed to make CSV request: ${e.message}")
            Log.i("CSVRequest", "Failed")
        }

        // Return the initial values (empty Scd40 object)
        return Scd40("", 0, 0, 0)
    }

    override suspend fun getScd40FullDataFromRaspberryPiServer(): String {
        val url = "http://192.168.1.43:8000/json"
        val request = Request.Builder()
            .url(url)
            .get()
            .build()

        try {
            val response = client.newCall(request).execute()
            val jsonData = response.body?.string()

            if (response.isSuccessful && jsonData != null) {
                // Return the full JSON data as it is
                return jsonData
            } else {
                Log.e("CSVRequest", "Failed to get JSON data: ${response.code}")
            }
        } catch (e: IOException) {
            Log.e("CSVRequest", "Failed to make CSV request: ${e.message}")
            Log.i("CSVRequest", "Failed")
        }

        // Return an empty JSON string if the request failed
        return ""
    }
}