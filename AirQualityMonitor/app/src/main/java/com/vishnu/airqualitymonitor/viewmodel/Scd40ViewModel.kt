package com.vishnu.airqualitymonitor.viewmodel

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.vishnu.airqualitymonitor.data.Scd40
import com.vishnu.airqualitymonitor.repository.Scd40Repository
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import javax.inject.Inject


@HiltViewModel
class Scd40ViewModel @Inject constructor(private val repository: Scd40Repository) : ViewModel() {
    //    ThingSpeak
    private val _scd40DataThingSpeakCloud = MutableStateFlow<Scd40?>(null)
    val scd40DataThingSpeakCloud: Flow<Scd40?> get() = _scd40DataThingSpeakCloud.asStateFlow()

    fun fetchScd40DataFromThingSpeakCloud() {
        viewModelScope.launch(Dispatchers.IO) {
            val scd40DataThingSpeakCloud = repository.getScd40DataFromThingSpeak()
            withContext(Dispatchers.Main) {
                _scd40DataThingSpeakCloud.value = scd40DataThingSpeakCloud
            }
        }
    }

    //Full ThingSpeak cloud data
    private val _scd40FullJsonThingSpeakCloudData = MutableStateFlow<String?>(null)
    val scd40FullJsonThingSpeakCloudData: Flow<String?> get() = _scd40FullJsonThingSpeakCloudData.asStateFlow()

    fun fetchFullScd40JsonDataFromThingSpeakCloud() {
        viewModelScope.launch(Dispatchers.IO) {
            val scd40FullDataThingSpeakCloud = repository.getScd40FullDataFromThingSpeak()
            withContext(Dispatchers.Main) {
                _scd40FullJsonThingSpeakCloudData.value = scd40FullDataThingSpeakCloud
            }
        }
    }

    //Local RPI data
    private val _scd40LastRPIData = MutableStateFlow<Scd40?>(null)
    val scd40LastRPIData: Flow<Scd40?> get() = _scd40LastRPIData.asStateFlow()

    fun fetchScd40DataFromRaspberryPiServer() {
        viewModelScope.launch(Dispatchers.IO) {
            val scd40Data = repository.getLastScd40DataFromRaspberryPiServer()
            withContext(Dispatchers.Main) {
                _scd40LastRPIData.value = scd40Data
            }
        }
    }

    //Local RPI data
    private val _scd40FullJsonRPIData = MutableStateFlow<String?>(null)
    val scd40FullJsonRPIData: Flow<String?> get() = _scd40FullJsonRPIData.asStateFlow()

    fun fetchFullScd40JsonDataFromRaspberryPiServer() {
        viewModelScope.launch(Dispatchers.IO) {
            val scd40JsonData = repository.getScd40FullDataFromRaspberryPiServer()
            withContext(Dispatchers.Main) {
                _scd40FullJsonRPIData.value = scd40JsonData
            }
        }
    }
}