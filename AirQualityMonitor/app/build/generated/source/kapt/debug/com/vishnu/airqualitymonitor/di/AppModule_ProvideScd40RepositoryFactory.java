// Generated by Dagger (https://dagger.dev).
package com.vishnu.airqualitymonitor.di;

import com.vishnu.airqualitymonitor.repository.Scd40Repository;
import dagger.internal.DaggerGenerated;
import dagger.internal.Factory;
import dagger.internal.Preconditions;
import dagger.internal.QualifierMetadata;
import dagger.internal.ScopeMetadata;

@ScopeMetadata("javax.inject.Singleton")
@QualifierMetadata
@DaggerGenerated
@SuppressWarnings({
    "unchecked",
    "rawtypes"
})
public final class AppModule_ProvideScd40RepositoryFactory implements Factory<Scd40Repository> {
  @Override
  public Scd40Repository get() {
    return provideScd40Repository();
  }

  public static AppModule_ProvideScd40RepositoryFactory create() {
    return InstanceHolder.INSTANCE;
  }

  public static Scd40Repository provideScd40Repository() {
    return Preconditions.checkNotNullFromProvides(AppModule.INSTANCE.provideScd40Repository());
  }

  private static final class InstanceHolder {
    private static final AppModule_ProvideScd40RepositoryFactory INSTANCE = new AppModule_ProvideScd40RepositoryFactory();
  }
}