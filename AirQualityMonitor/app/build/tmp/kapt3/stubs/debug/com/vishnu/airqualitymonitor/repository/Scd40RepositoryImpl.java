package com.vishnu.airqualitymonitor.repository;

import android.util.Log;
import com.vishnu.airqualitymonitor.data.Scd40;
import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import org.json.JSONArray;
import org.json.JSONObject;
import java.io.IOException;

@kotlin.Metadata(mv = {1, 7, 1}, k = 1, d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u000b\n\u0002\u0018\u0002\n\u0002\b\u0005\b\u0007\u0018\u00002\u00020\u0001B\u0005\u00a2\u0006\u0002\u0010\u0002J\u0011\u0010\u0017\u001a\u00020\u0018H\u0096@\u00f8\u0001\u0000\u00a2\u0006\u0002\u0010\u0019J\u0011\u0010\u001a\u001a\u00020\u0018H\u0096@\u00f8\u0001\u0000\u00a2\u0006\u0002\u0010\u0019J\u0011\u0010\u001b\u001a\u00020\u0006H\u0096@\u00f8\u0001\u0000\u00a2\u0006\u0002\u0010\u0019J\u0011\u0010\u001c\u001a\u00020\u0006H\u0096@\u00f8\u0001\u0000\u00a2\u0006\u0002\u0010\u0019R\u000e\u0010\u0003\u001a\u00020\u0004X\u0082\u0004\u00a2\u0006\u0002\n\u0000R\u001a\u0010\u0005\u001a\u00020\u0006X\u0086\u000e\u00a2\u0006\u000e\n\u0000\u001a\u0004\b\u0007\u0010\b\"\u0004\b\t\u0010\nR\u001a\u0010\u000b\u001a\u00020\fX\u0086\u000e\u00a2\u0006\u000e\n\u0000\u001a\u0004\b\r\u0010\u000e\"\u0004\b\u000f\u0010\u0010R\u001a\u0010\u0011\u001a\u00020\fX\u0086\u000e\u00a2\u0006\u000e\n\u0000\u001a\u0004\b\u0012\u0010\u000e\"\u0004\b\u0013\u0010\u0010R\u001a\u0010\u0014\u001a\u00020\fX\u0086\u000e\u00a2\u0006\u000e\n\u0000\u001a\u0004\b\u0015\u0010\u000e\"\u0004\b\u0016\u0010\u0010\u0082\u0002\u0004\n\u0002\b\u0019\u00a8\u0006\u001d"}, d2 = {"Lcom/vishnu/airqualitymonitor/repository/Scd40RepositoryImpl;", "Lcom/vishnu/airqualitymonitor/repository/Scd40Repository;", "()V", "client", "Lokhttp3/OkHttpClient;", "field1Value", "", "getField1Value", "()Ljava/lang/String;", "setField1Value", "(Ljava/lang/String;)V", "field2Value", "", "getField2Value", "()I", "setField2Value", "(I)V", "field3Value", "getField3Value", "setField3Value", "field4Value", "getField4Value", "setField4Value", "getLastScd40DataFromRaspberryPiServer", "Lcom/vishnu/airqualitymonitor/data/Scd40;", "(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;", "getScd40DataFromThingSpeak", "getScd40FullDataFromRaspberryPiServer", "getScd40FullDataFromThingSpeak", "app_debug"})
public final class Scd40RepositoryImpl implements com.vishnu.airqualitymonitor.repository.Scd40Repository {
    @org.jetbrains.annotations.NotNull
    private java.lang.String field1Value = "";
    private int field2Value = 0;
    private int field3Value = 0;
    private int field4Value = 0;
    private final okhttp3.OkHttpClient client = null;
    
    public Scd40RepositoryImpl() {
        super();
    }
    
    @org.jetbrains.annotations.NotNull
    public final java.lang.String getField1Value() {
        return null;
    }
    
    public final void setField1Value(@org.jetbrains.annotations.NotNull
    java.lang.String p0) {
    }
    
    public final int getField2Value() {
        return 0;
    }
    
    public final void setField2Value(int p0) {
    }
    
    public final int getField3Value() {
        return 0;
    }
    
    public final void setField3Value(int p0) {
    }
    
    public final int getField4Value() {
        return 0;
    }
    
    public final void setField4Value(int p0) {
    }
    
    @org.jetbrains.annotations.Nullable
    @java.lang.Override
    public java.lang.Object getScd40DataFromThingSpeak(@org.jetbrains.annotations.NotNull
    kotlin.coroutines.Continuation<? super com.vishnu.airqualitymonitor.data.Scd40> continuation) {
        return null;
    }
    
    @org.jetbrains.annotations.Nullable
    @java.lang.Override
    public java.lang.Object getScd40FullDataFromThingSpeak(@org.jetbrains.annotations.NotNull
    kotlin.coroutines.Continuation<? super java.lang.String> continuation) {
        return null;
    }
    
    @org.jetbrains.annotations.Nullable
    @java.lang.Override
    public java.lang.Object getLastScd40DataFromRaspberryPiServer(@org.jetbrains.annotations.NotNull
    kotlin.coroutines.Continuation<? super com.vishnu.airqualitymonitor.data.Scd40> continuation) {
        return null;
    }
    
    @org.jetbrains.annotations.Nullable
    @java.lang.Override
    public java.lang.Object getScd40FullDataFromRaspberryPiServer(@org.jetbrains.annotations.NotNull
    kotlin.coroutines.Continuation<? super java.lang.String> continuation) {
        return null;
    }
}