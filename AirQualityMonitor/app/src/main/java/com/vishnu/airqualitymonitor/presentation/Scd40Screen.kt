package com.vishnu.airqualitymonitor.presentation

import android.util.Log
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.wrapContentSize
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.Surface
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.vishnu.airqualitymonitor.data.SensorData
import com.vishnu.airqualitymonitor.ui.theme.BabyBlue
import com.vishnu.airqualitymonitor.ui.theme.PurpleGrey80
import com.vishnu.airqualitymonitor.ui.theme.SeafoamGreen
import com.vishnu.airqualitymonitor.viewmodel.Scd40ViewModel
import org.json.JSONArray

@Composable
fun Scd40Screen(viewModel: Scd40ViewModel) {
    val scd40DataThingSpeakCloudState =
        viewModel.scd40DataThingSpeakCloud.collectAsState(initial = null)
    val scd40FullJsonThingSpeakCloudDataState =
        viewModel.scd40FullJsonThingSpeakCloudData.collectAsState(initial = null)

    val scd40LastRPIDataState = viewModel.scd40LastRPIData.collectAsState(initial = null)
    val scd40FullJsonRPIDataState = viewModel.scd40FullJsonRPIData.collectAsState(initial = null)

    @Composable
    fun SensorDataRow(sensorData: SensorData, color: Color) {
        // Compose your row here using the data from sensorData
        Card(
            modifier = Modifier
                .fillMaxWidth()
                .padding(8.dp),
            shape = RoundedCornerShape(8.dp),
        ) {
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .background(color)
                    .padding(8.dp)
            ) {
                Text(text = "No: ${sensorData.entryId}")
                Text(text = "Created At: ${sensorData.createdAt}")
                Text(text = "Temperature: ${sensorData.field2}")
                Text(text = "Humidity: ${sensorData.field3}")
                Text(text = "CO2: ${sensorData.field4}")
                if (sensorData.field5 != "null" && sensorData.field6 != "null") {
                    Text(text = "Temperature DHT11: ${sensorData.field5}")
                    Text(text = "Humidity DHT11: ${sensorData.field5}")
                }
                if(sensorData.field7 != "null"){
                    Text(text = "Was Ventilation required ? : ${sensorData.field7}")
                }
            }
        }

    }

    // Function to manually parse the JSON data into a list of SensorData objects
    fun parseSensorDataList(jsonData: String): List<SensorData> {
        val sensorDataList = mutableListOf<SensorData>()

        try {
            val jsonArray = JSONArray(jsonData)
            for (i in 0 until jsonArray.length()) {
                val jsonObject = jsonArray.getJSONObject(i)
                var sensorData = SensorData("null","null","null","null","null","null","null","null","null")
                if(jsonObject.has("field5") && jsonObject.has("field6") && jsonObject.has("field7")){
                    Log.i("HELLO", "EMPTYYYyyyyy")
                  sensorData = SensorData(
                        createdAt = jsonObject.getString("created_at"),
                        entryId = jsonObject.getString("entry_id"),
                        field1 = jsonObject.getString("field1"),
                        field2 = jsonObject.getString("field2"),
                        field3 = jsonObject.getString("field3"),
                        field4 = jsonObject.getString("field4"),
                        field5 = jsonObject.getString("field5"),
                        field6 = jsonObject.getString("field6"),
                        field7 = jsonObject.getString("field7"),
                    )
                } else if(jsonObject.has("field7")){
                    sensorData = SensorData(
                        createdAt = jsonObject.getString("created_at"),
                        entryId = jsonObject.getString("entry_id"),
                        field1 = jsonObject.getString("field1"),
                        field2 = jsonObject.getString("field2"),
                        field3 = jsonObject.getString("field3"),
                        field4 = jsonObject.getString("field4"),
                        field5 = "null",
                        field6 = "null",
                        field7 = jsonObject.getString("field7"),
                    )
                }else{
                    sensorData = SensorData(
                        createdAt = jsonObject.getString("created_at"),
                        entryId = jsonObject.getString("entry_id"),
                        field1 = jsonObject.getString("field1"),
                        field2 = jsonObject.getString("field2"),
                        field3 = jsonObject.getString("field3"),
                        field4 = jsonObject.getString("field4"),
                        field5 = "null",
                        field6 = "null",
                        field7 = "null",
                    )
                }
                sensorDataList.add(sensorData)
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }

        return sensorDataList
    }

    Surface(
        elevation = 2.dp,
        color = Color.White,
        shape = androidx.compose.material.MaterialTheme.shapes.small
    ) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(2.dp)
        ) {
            Text(
                text = "Air Quality Data",
                color = SeafoamGreen,
                style = MaterialTheme.typography.bodyMedium.copy(
                    fontSize = 30.sp,
                    fontWeight = FontWeight.Bold,
                    textAlign = TextAlign.Center
                ),
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(8.dp)
            )

            Text(
                text = "ThingSpeak Cloud Data",
                style = MaterialTheme.typography.labelSmall.copy(
                    textAlign = TextAlign.Center
                ),
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(8.dp)
            )
//            ThingSpeak latest data
            Column(modifier = Modifier.padding(8.dp)) {
                scd40DataThingSpeakCloudState.value?.let { scd40DataThingSpeakCloudState ->
                    Text(
                        text = "Time: ${scd40DataThingSpeakCloudState.time} ",
                        style = MaterialTheme.typography.bodyMedium
                    )
                    Text(
                        text = "Temperature: ${scd40DataThingSpeakCloudState.temperature} ",
                        style = MaterialTheme.typography.bodyMedium
                    )
                    Text(
                        text = "Humidity: ${scd40DataThingSpeakCloudState.humidity}",
                        style = MaterialTheme.typography.bodyMedium
                    )
                    Text(
                        text = "CO2: ${scd40DataThingSpeakCloudState.CO2}",
                        style = MaterialTheme.typography.bodyMedium
                    )
                }
            }
            Spacer(modifier = Modifier.height(4.dp))

            Button(modifier = Modifier
                .padding(8.dp)
                .align(Alignment.CenterHorizontally)
                .wrapContentSize(),
                onClick = { viewModel.fetchScd40DataFromThingSpeakCloud() }) {
                Text(text = "Latest Values (ThingSpeak)")
            }
            Button(
                modifier = Modifier
                    .padding(8.dp)
                    .align(Alignment.CenterHorizontally)
                    .wrapContentSize(),
                onClick = { viewModel.fetchFullScd40JsonDataFromThingSpeakCloud() }) {
                Text(text = "Full Data (ThingSpeak)")
            }
            Text(
                text = "Raspberry Pi Server Data",
                style = MaterialTheme.typography.labelSmall.copy(
                    textAlign = TextAlign.Center
                ),
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(8.dp)
            )
            Button(modifier = Modifier
                .padding(8.dp)
                .align(Alignment.CenterHorizontally)
                .wrapContentSize(),
                onClick = { viewModel.fetchScd40DataFromRaspberryPiServer() }) {
                Text(text = "Latest Values (Raspberry Pi Server)")
            }

            Spacer(modifier = Modifier.height(4.dp))

            Button(
                modifier = Modifier
                    .padding(8.dp)
                    .align(Alignment.CenterHorizontally)
                    .wrapContentSize(),
                onClick = { viewModel.fetchFullScd40JsonDataFromRaspberryPiServer() }) {
                Text(text = "Full Data (Raspberry Pi Server)")
            }

//            RPI latest Data
            Column(modifier = Modifier.padding(8.dp)) {
                scd40LastRPIDataState.value?.let { scd40Data ->
                    Text(
                        text = "Time: ${scd40Data.time} ",
                        style = MaterialTheme.typography.bodyMedium
                    )
                    Text(
                        text = "Temperature: ${scd40Data.temperature} ",
                        style = MaterialTheme.typography.bodyMedium
                    )
                    Text(
                        text = "Humidity: ${scd40Data.humidity}",
                        style = MaterialTheme.typography.bodyMedium
                    )
                    Text(
                        text = "CO2: ${scd40Data.CO2}",
                        style = MaterialTheme.typography.bodyMedium
                    )
                }
            }

            Spacer(modifier = Modifier.height(4.dp))
//            RPI full Json Data
            Column(modifier = Modifier.padding(8.dp)) {
                scd40FullJsonRPIDataState.value?.let { scd40FullJsonRPIDataState ->
                    // Displaying the JSON data in a RecyclerView
                    Text(
                        text = "RPI full Json Data",
                        style = MaterialTheme.typography.labelSmall
                    )
                    LazyColumn {
                        // Parsing JSON data into a list of SensorData objects
                        val sensorDataList = parseSensorDataList(scd40FullJsonRPIDataState)

                        items(sensorDataList.reversed()) { sensorData ->
                            SensorDataRow(sensorData, BabyBlue)
//                            Divider()
                        }
                    }
                }
            }

            Spacer(modifier = Modifier.height(4.dp))
//            ThingSpeak full json data
            Column(modifier = Modifier.padding(0.dp)) {
                scd40FullJsonThingSpeakCloudDataState.value?.let { scd40FullJsonThingSpeakCloudDataState ->
                    // Displaying the JSON data in a RecyclerView
                    Text(
                        text = "ThingSpeak full json data",
                        style = MaterialTheme.typography.labelSmall
                    )
                    LazyColumn {
                        // Parsing the JSON data into a list of SensorData objects
                        val sensorDataList =
                            parseSensorDataList(scd40FullJsonThingSpeakCloudDataState)

                        items(sensorDataList.reversed()) { sensorData ->
                            SensorDataRow(sensorData, PurpleGrey80)
                            // Divider()
                        }
                    }
                }
            }
        }
    }
}
