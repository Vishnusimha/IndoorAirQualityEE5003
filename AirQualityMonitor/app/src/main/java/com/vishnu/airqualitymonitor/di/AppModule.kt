package com.vishnu.airqualitymonitor.di

import com.vishnu.airqualitymonitor.repository.Scd40Repository
import com.vishnu.airqualitymonitor.repository.Scd40RepositoryImpl
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
object AppModule {

    @Provides
    @Singleton
    fun provideScd40Repository(): Scd40Repository {
        return Scd40RepositoryImpl()
    }
}