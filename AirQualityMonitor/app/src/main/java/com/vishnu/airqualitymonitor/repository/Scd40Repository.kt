package com.vishnu.airqualitymonitor.repository

import com.vishnu.airqualitymonitor.data.Scd40

interface Scd40Repository {
    suspend fun getScd40DataFromThingSpeak(): Scd40
    suspend fun getScd40FullDataFromThingSpeak(): String

    suspend fun getLastScd40DataFromRaspberryPiServer(): Scd40
    suspend fun getScd40FullDataFromRaspberryPiServer(): String
}