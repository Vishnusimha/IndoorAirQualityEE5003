package com.vishnu.airqualitymonitor.viewmodel;

import androidx.lifecycle.ViewModel;
import com.vishnu.airqualitymonitor.data.Scd40;
import com.vishnu.airqualitymonitor.repository.Scd40Repository;
import dagger.hilt.android.lifecycle.HiltViewModel;
import kotlinx.coroutines.Dispatchers;
import kotlinx.coroutines.flow.Flow;
import javax.inject.Inject;

@dagger.hilt.android.lifecycle.HiltViewModel
@kotlin.Metadata(mv = {1, 7, 1}, k = 1, d1 = {"\u00004\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\t\n\u0002\u0010\u0002\n\u0002\b\u0004\b\u0007\u0018\u00002\u00020\u0001B\u000f\b\u0007\u0012\u0006\u0010\u0002\u001a\u00020\u0003\u00a2\u0006\u0002\u0010\u0004J\u0006\u0010\u0016\u001a\u00020\u0017J\u0006\u0010\u0018\u001a\u00020\u0017J\u0006\u0010\u0019\u001a\u00020\u0017J\u0006\u0010\u001a\u001a\u00020\u0017R\u0016\u0010\u0005\u001a\n\u0012\u0006\u0012\u0004\u0018\u00010\u00070\u0006X\u0082\u0004\u00a2\u0006\u0002\n\u0000R\u0016\u0010\b\u001a\n\u0012\u0006\u0012\u0004\u0018\u00010\t0\u0006X\u0082\u0004\u00a2\u0006\u0002\n\u0000R\u0016\u0010\n\u001a\n\u0012\u0006\u0012\u0004\u0018\u00010\t0\u0006X\u0082\u0004\u00a2\u0006\u0002\n\u0000R\u0016\u0010\u000b\u001a\n\u0012\u0006\u0012\u0004\u0018\u00010\u00070\u0006X\u0082\u0004\u00a2\u0006\u0002\n\u0000R\u000e\u0010\u0002\u001a\u00020\u0003X\u0082\u0004\u00a2\u0006\u0002\n\u0000R\u0019\u0010\f\u001a\n\u0012\u0006\u0012\u0004\u0018\u00010\u00070\r8F\u00a2\u0006\u0006\u001a\u0004\b\u000e\u0010\u000fR\u0019\u0010\u0010\u001a\n\u0012\u0006\u0012\u0004\u0018\u00010\t0\r8F\u00a2\u0006\u0006\u001a\u0004\b\u0011\u0010\u000fR\u0019\u0010\u0012\u001a\n\u0012\u0006\u0012\u0004\u0018\u00010\t0\r8F\u00a2\u0006\u0006\u001a\u0004\b\u0013\u0010\u000fR\u0019\u0010\u0014\u001a\n\u0012\u0006\u0012\u0004\u0018\u00010\u00070\r8F\u00a2\u0006\u0006\u001a\u0004\b\u0015\u0010\u000f\u00a8\u0006\u001b"}, d2 = {"Lcom/vishnu/airqualitymonitor/viewmodel/Scd40ViewModel;", "Landroidx/lifecycle/ViewModel;", "repository", "Lcom/vishnu/airqualitymonitor/repository/Scd40Repository;", "(Lcom/vishnu/airqualitymonitor/repository/Scd40Repository;)V", "_scd40DataThingSpeakCloud", "Lkotlinx/coroutines/flow/MutableStateFlow;", "Lcom/vishnu/airqualitymonitor/data/Scd40;", "_scd40FullJsonRPIData", "", "_scd40FullJsonThingSpeakCloudData", "_scd40LastRPIData", "scd40DataThingSpeakCloud", "Lkotlinx/coroutines/flow/Flow;", "getScd40DataThingSpeakCloud", "()Lkotlinx/coroutines/flow/Flow;", "scd40FullJsonRPIData", "getScd40FullJsonRPIData", "scd40FullJsonThingSpeakCloudData", "getScd40FullJsonThingSpeakCloudData", "scd40LastRPIData", "getScd40LastRPIData", "fetchFullScd40JsonDataFromRaspberryPiServer", "", "fetchFullScd40JsonDataFromThingSpeakCloud", "fetchScd40DataFromRaspberryPiServer", "fetchScd40DataFromThingSpeakCloud", "app_debug"})
public final class Scd40ViewModel extends androidx.lifecycle.ViewModel {
    private final com.vishnu.airqualitymonitor.repository.Scd40Repository repository = null;
    private final kotlinx.coroutines.flow.MutableStateFlow<com.vishnu.airqualitymonitor.data.Scd40> _scd40DataThingSpeakCloud = null;
    private final kotlinx.coroutines.flow.MutableStateFlow<java.lang.String> _scd40FullJsonThingSpeakCloudData = null;
    private final kotlinx.coroutines.flow.MutableStateFlow<com.vishnu.airqualitymonitor.data.Scd40> _scd40LastRPIData = null;
    private final kotlinx.coroutines.flow.MutableStateFlow<java.lang.String> _scd40FullJsonRPIData = null;
    
    @javax.inject.Inject
    public Scd40ViewModel(@org.jetbrains.annotations.NotNull
    com.vishnu.airqualitymonitor.repository.Scd40Repository repository) {
        super();
    }
    
    @org.jetbrains.annotations.NotNull
    public final kotlinx.coroutines.flow.Flow<com.vishnu.airqualitymonitor.data.Scd40> getScd40DataThingSpeakCloud() {
        return null;
    }
    
    public final void fetchScd40DataFromThingSpeakCloud() {
    }
    
    @org.jetbrains.annotations.NotNull
    public final kotlinx.coroutines.flow.Flow<java.lang.String> getScd40FullJsonThingSpeakCloudData() {
        return null;
    }
    
    public final void fetchFullScd40JsonDataFromThingSpeakCloud() {
    }
    
    @org.jetbrains.annotations.NotNull
    public final kotlinx.coroutines.flow.Flow<com.vishnu.airqualitymonitor.data.Scd40> getScd40LastRPIData() {
        return null;
    }
    
    public final void fetchScd40DataFromRaspberryPiServer() {
    }
    
    @org.jetbrains.annotations.NotNull
    public final kotlinx.coroutines.flow.Flow<java.lang.String> getScd40FullJsonRPIData() {
        return null;
    }
    
    public final void fetchFullScd40JsonDataFromRaspberryPiServer() {
    }
}