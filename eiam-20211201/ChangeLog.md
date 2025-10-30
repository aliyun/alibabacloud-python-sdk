2025-10-30 Version: 2.4.0
- Support API AddCustomPrivacyPoliciesToBrand.
- Support API CreateCustomPrivacyPolicy.
- Support API DeleteCustomPrivacyPolicy.
- Support API DisableCustomPrivacyPolicy.
- Support API EnableCustomPrivacyPolicy.
- Support API GetCustomPrivacyPolicy.
- Support API ListCustomPrivacyPolicies.
- Support API ListCustomPrivacyPoliciesForBrand.
- Support API RemoveCustomPrivacyPoliciesFromBrand.
- Support API UpdateCustomPrivacyPolicy.


2025-10-20 Version: 2.3.0
- Support API CreateBrand.
- Support API DeleteBrand.
- Support API DisableBrand.
- Support API EnableBrand.
- Support API GetBrand.
- Support API GetLoginRedirectApplicationForBrand.
- Support API ListBrands.
- Support API SetLoginRedirectApplicationForBrand.
- Support API UpdateBrand.
- Support API UpdateDomainBrand.


2025-10-15 Version: 2.2.0
- Support API AddApplicationAccountToUser.
- Support API CreateApplicationFederatedCredential.
- Support API CreateApplicationToken.
- Support API CreateFederatedCredentialProvider.
- Support API CreateNetworkZone.
- Support API DeleteApplicationFederatedCredential.
- Support API DeleteApplicationToken.
- Support API DeleteFederatedCredentialProvider.
- Support API DeleteNetworkZone.
- Support API DisableApplicationFederatedCredential.
- Support API DisableApplicationToken.
- Support API DisableFederatedCredentialProvider.
- Support API DisableIdentityProviderAuthn.
- Support API EnableApplicationFederatedCredential.
- Support API EnableApplicationToken.
- Support API EnableFederatedCredentialProvider.
- Support API EnableIdentityProviderAuthn.
- Support API GetApplicationFederatedCredential.
- Support API GetApplicationTemplate.
- Support API GetFederatedCredentialProvider.
- Support API GetNetworkZone.
- Support API ListApplicationAccounts.
- Support API ListApplicationAccountsForUser.
- Support API ListApplicationFederatedCredentials.
- Support API ListApplicationFederatedCredentialsForProvider.
- Support API ListApplicationSupportedProvisionProtocolTypes.
- Support API ListApplicationTokens.
- Support API ListApplicationsForGroup.
- Support API ListApplicationsForNetworkAccessEndpoint.
- Support API ListApplicationsForNetworkZone.
- Support API ListConditionalAccessPoliciesForApplication.
- Support API ListConditionalAccessPoliciesForUser.
- Support API ListFederatedCredentialProviders.
- Support API ListIdentityProvidersForNetworkAccessEndpoint.
- Support API ListNetworkZones.
- Support API ObtainApplicationToken.
- Support API RemoveApplicationAccountFromUser.
- Support API UpdateApplicationFederatedCredential.
- Support API UpdateApplicationFederatedCredentialDescription.
- Support API UpdateApplicationInfo.
- Support API UpdateApplicationTokenExpirationTime.
- Support API UpdateDomainIcpNumber.
- Support API UpdateFederatedCredentialProvider.
- Support API UpdateFederatedCredentialProviderDescription.
- Support API UpdateNetworkZone.
- Support API UpdateNetworkZoneDescription.
- Update API GetDomain: add response parameters Body.Domain.BrandId.
- Update API ListDomains: add request parameters BrandId.
- Update API ListDomains: add response parameters Body.Domains.$.BrandId.


2025-08-25 Version: 2.1.0
- Support API UpdateApplicationClientSecretExpirationTime.


2025-08-12 Version: 2.0.2
- Update API CreateApplicationClientSecret: add request parameters ExpirationTime.
- Update API GetApplicationSsoConfig: add response parameters Body.ApplicationSsoConfig.OidcSsoConfig.AllowedPublicClient.
- Update API ListApplicationClientSecrets: add response parameters Body.ApplicationClientSecrets.$.ExpirationTime.
- Update API ObtainApplicationClientSecret: add response parameters Body.ApplicationClientSecret.ExpirationTime.
- Update API SetApplicationSsoConfig: add request parameters OidcSsoConfig.AllowedPublicClient.


2025-08-06 Version: 2.0.1
- Update API GetApplicationProvisioningConfig: add response parameters Body.ApplicationProvisioningConfig.NetworkAccessEndpointId.
- Update API SetApplicationProvisioningConfig: add request parameters NetworkAccessEndpointId.


2025-07-30 Version: 2.0.0
- Update API CreateIdentityProvider: add request parameters ClientToken.
- Update API CreateIdentityProvider: add request parameters DingtalkAppConfig.EncryptKey.
- Update API CreateIdentityProvider: add request parameters DingtalkAppConfig.VerificationToken.
- Update API CreateUser: add request parameters ClientToken.
- Update API GetApplication: add response parameters Body.Application.CustomSubjectStatus.
- Update API GetIdentityProvider: add response parameters Body.IdentityProviderDetail.DingtalkAppConfig.EncryptKey.
- Update API GetIdentityProvider: add response parameters Body.IdentityProviderDetail.DingtalkAppConfig.VerificationToken.
- Update API ListApplications: delete response parameters Body.Applications.$.M2MClientStatus.
- Update API ListApplications: delete response parameters Body.Applications.$.ResourceServerIdentifier.
- Update API ListApplications: delete response parameters Body.Applications.$.ResourceServerStatus.
- Update API UpdateConditionalAccessPolicy: add request parameters ClientToken.
- Update API UpdateConditionalAccessPolicyDescription: add request parameters ClientToken.
- Update API UpdateIdentityProvider: add request parameters ClientToken.
- Update API UpdateIdentityProvider: add request parameters DingtalkAppConfig.EncryptKey.
- Update API UpdateIdentityProvider: add request parameters DingtalkAppConfig.VerificationToken.


2025-03-21 Version: 1.9.2
- Generated python 2021-12-01 for Eiam.

2025-03-20 Version: 1.9.1
- Update API CreateIdentityProvider: update param UdPullConfig.
- Update API CreateInstance: update response param.
- Update API GetIdentityProviderUdPullConfiguration: update response param.
- Update API SetIdentityProviderUdPullConfiguration: add param PeriodicSyncConfig.


2025-03-20 Version: 1.9.0
- Support API CreateConditionalAccessPolicy.
- Support API DeleteConditionalAccessPolicy.
- Support API DisableConditionalAccessPolicy.
- Support API EnableConditionalAccessPolicy.
- Support API GetConditionalAccessPolicy.
- Support API ListConditionalAccessPolicies.
- Support API ListConditionalAccessPoliciesForNetworkZone.
- Support API UpdateConditionalAccessPolicy.
- Support API UpdateConditionalAccessPolicyDescription.
- Update API CreateDomain: update response param.
- Update API CreateDomainProxyToken: update response param.
- Update API CreateNetworkAccessEndpoint: update response param.


2025-02-14 Version: 1.8.1
- Update API GetApplication: update response param.
- Update API ListApplications: add param M2MClientStatus.
- Update API ListApplications: add param ResourceServerStatus.
- Update API ListApplications: add param SsoType.
- Update API ListApplications: update response param.
- Update API ListIdentityProviders: update response param.


2025-01-15 Version: 1.8.0
- Support API GetInstanceLicense.
- Update API CreateIdentityProvider: update param LarkConfig.
- Update API GetIdentityProvider: update response param.
- Update API ListIdentityProviders: update response param.
- Update API UpdateIdentityProvider: update param LarkConfig.


2025-01-09 Version: 1.7.0
- Support API GetInstanceLicense.


2024-12-17 Version: 1.6.1
- Update API CreateIdentityProvider: add param LogoUrl.
- Update API GetIdentityProvider: update response param.
- Update API ListIdentityProviders: update response param.
- Update API ListSynchronizationJobs: add param Filters.
- Update API ListSynchronizationJobs: update response param.
- Update API RunSynchronizationJob: add param Description.
- Update API RunSynchronizationJob: add param PasswordInitialization.
- Update API RunSynchronizationJob: add param SynchronizationScopeConfig.
- Update API RunSynchronizationJob: add param UserIdentityTypes.
- Update API RunSynchronizationJob: update param TargetId.
- Update API RunSynchronizationJob: update response param.
- Update API UpdateIdentityProvider: add param LogoUrl.


2024-12-17 Version: 1.6.1
- Update API CreateIdentityProvider: add param LogoUrl.
- Update API GetIdentityProvider: update response param.
- Update API ListIdentityProviders: update response param.
- Update API ListSynchronizationJobs: add param Filters.
- Update API ListSynchronizationJobs: update response param.
- Update API RunSynchronizationJob: add param Description.
- Update API RunSynchronizationJob: add param PasswordInitialization.
- Update API RunSynchronizationJob: add param SynchronizationScopeConfig.
- Update API RunSynchronizationJob: add param UserIdentityTypes.
- Update API RunSynchronizationJob: update param TargetId.
- Update API RunSynchronizationJob: update response param.
- Update API UpdateIdentityProvider: add param LogoUrl.


2024-12-16 Version: 1.6.0
- Support API CreateIdentityProvider.
- Support API DeleteIdentityProvider.
- Support API DisableIdentityProviderUdPull.
- Support API EnableIdentityProviderUdPull.
- Support API GetIdentityProvider.
- Support API GetIdentityProviderUdPullConfiguration.
- Support API ListIdentityProviders.
- Support API SetIdentityProviderUdPullConfiguration.
- Support API UpdateIdentityProvider.
- Update API GetApplicationSsoConfig: update response param.
- Update API SetApplicationSsoConfig: add param ClientToken.
- Update API SetApplicationSsoConfig: update param SamlSsoConfig.


2024-11-06 Version: 1.5.2
- Update API GetPasswordExpirationConfiguration: update response param.
- Update API SetPasswordExpirationConfiguration: add param EffectiveAuthenticationSourceIds.


2024-11-01 Version: 1.5.1
- Generated python 2021-12-01 for Eiam.

2024-10-24 Version: 1.5.0
- Support API DeleteOrganizationalUnitChildren.
- Update API CreateOrganizationalUnit: update param OrganizationalUnitName.
- Update API GetApplication: update response param.
- Update API GetApplicationSsoConfig: update response param.
- Update API SetApplicationSsoConfig: update param SamlSsoConfig.
- Update API UpdateOrganizationalUnit: update param OrganizationalUnitName.


2024-07-30 Version: 1.4.0
- Support API GetSynchronizationJob.
- Support API ListSynchronizationJobs.
- Support API RunSynchronizationJob.


2024-05-29 Version: 1.3.3
- Update API GetApplicationProvisioningScope: update param ApplicationId.
- Update API GetApplicationProvisioningScope: update param InstanceId.
- Update API GetApplicationProvisioningScope: update response param.
- Update API GetDomain: update param DomainId.
- Update API ListGroupsForUser: update response param.
- Update API ListUsersForGroup: update response param.
- Update API SetApplicationProvisioningScope: add param GroupIds.
- Update API SetApplicationProvisioningScope: update param ApplicationId.
- Update API SetApplicationProvisioningScope: update param InstanceId.
- Update API SetApplicationProvisioningScope: update response param.


2024-03-12 Version: 1.3.2
- Update API GetUser: update response param.
- Update API ListApplications: update response param.


2023-12-21 Version: 1.3.1
- Generated python 2021-12-01 for Eiam.

2023-12-20 Version: 1.3.0
- Generated python 2021-12-01 for Eiam.

2023-09-13 Version: 1.2.0
- Generated python 2021-12-01 for Eiam.

2023-08-10 Version: 1.1.0
- Generated python 2021-12-01 for Eiam.

