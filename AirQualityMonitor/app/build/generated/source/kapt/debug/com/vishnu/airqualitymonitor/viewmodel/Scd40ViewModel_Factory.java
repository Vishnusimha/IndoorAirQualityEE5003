// Generated by Dagger (https://dagger.dev).
package com.vishnu.airqualitymonitor.viewmodel;

import com.vishnu.airqualitymonitor.repository.Scd40Repository;
import dagger.internal.DaggerGenerated;
import dagger.internal.Factory;
import dagger.internal.QualifierMetadata;
import dagger.internal.ScopeMetadata;
import javax.inject.Provider;

@ScopeMetadata
@QualifierMetadata
@DaggerGenerated
@SuppressWarnings({
    "unchecked",
    "rawtypes"
})
public final class Scd40ViewModel_Factory implements Factory<Scd40ViewModel> {
  private final Provider<Scd40Repository> repositoryProvider;

  public Scd40ViewModel_Factory(Provider<Scd40Repository> repositoryProvider) {
    this.repositoryProvider = repositoryProvider;
  }

  @Override
  public Scd40ViewModel get() {
    return newInstance(repositoryProvider.get());
  }

  public static Scd40ViewModel_Factory create(Provider<Scd40Repository> repositoryProvider) {
    return new Scd40ViewModel_Factory(repositoryProvider);
  }

  public static Scd40ViewModel newInstance(Scd40Repository repository) {
    return new Scd40ViewModel(repository);
  }
}