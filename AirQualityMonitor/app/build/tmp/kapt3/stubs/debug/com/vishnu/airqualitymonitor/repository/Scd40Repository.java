package com.vishnu.airqualitymonitor.repository;

import com.vishnu.airqualitymonitor.data.Scd40;

@kotlin.Metadata(mv = {1, 7, 1}, k = 1, d1 = {"\u0000\u001a\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000e\n\u0002\b\u0002\bf\u0018\u00002\u00020\u0001J\u0011\u0010\u0002\u001a\u00020\u0003H\u00a6@\u00f8\u0001\u0000\u00a2\u0006\u0002\u0010\u0004J\u0011\u0010\u0005\u001a\u00020\u0003H\u00a6@\u00f8\u0001\u0000\u00a2\u0006\u0002\u0010\u0004J\u0011\u0010\u0006\u001a\u00020\u0007H\u00a6@\u00f8\u0001\u0000\u00a2\u0006\u0002\u0010\u0004J\u0011\u0010\b\u001a\u00020\u0007H\u00a6@\u00f8\u0001\u0000\u00a2\u0006\u0002\u0010\u0004\u0082\u0002\u0004\n\u0002\b\u0019\u00a8\u0006\t"}, d2 = {"Lcom/vishnu/airqualitymonitor/repository/Scd40Repository;", "", "getLastScd40DataFromRaspberryPiServer", "Lcom/vishnu/airqualitymonitor/data/Scd40;", "(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;", "getScd40DataFromThingSpeak", "getScd40FullDataFromRaspberryPiServer", "", "getScd40FullDataFromThingSpeak", "app_debug"})
public abstract interface Scd40Repository {
    
    @org.jetbrains.annotations.Nullable
    public abstract java.lang.Object getScd40DataFromThingSpeak(@org.jetbrains.annotations.NotNull
    kotlin.coroutines.Continuation<? super com.vishnu.airqualitymonitor.data.Scd40> continuation);
    
    @org.jetbrains.annotations.Nullable
    public abstract java.lang.Object getScd40FullDataFromThingSpeak(@org.jetbrains.annotations.NotNull
    kotlin.coroutines.Continuation<? super java.lang.String> continuation);
    
    @org.jetbrains.annotations.Nullable
    public abstract java.lang.Object getLastScd40DataFromRaspberryPiServer(@org.jetbrains.annotations.NotNull
    kotlin.coroutines.Continuation<? super com.vishnu.airqualitymonitor.data.Scd40> continuation);
    
    @org.jetbrains.annotations.Nullable
    public abstract java.lang.Object getScd40FullDataFromRaspberryPiServer(@org.jetbrains.annotations.NotNull
    kotlin.coroutines.Continuation<? super java.lang.String> continuation);
}