package com.vishnu.airqualitymonitor.data

data class SensorData(
    val createdAt: String,
    val entryId: String,
    val field1: String,
    val field2: String,
    val field3: String,
    val field4: String,
    val field5: String="null",
    val field6: String="null",
    val field7: String?
)
