2025-06-16 Version: 1.10.0
- Support API CreateEnterpriseAcceleratePolicy.
- Support API CreateEnterpriseAccelerateTarget.
- Support API DeleteEnterpriseAcceleratePolicy.
- Support API DeleteEnterpriseAccelerateTarget.
- Support API DeleteOtpConfig.
- Support API DisableEnterpriseAcceleratePolicy.
- Support API EnableEnterpriseAcceleratePolicy.
- Support API ImportEnterpriseAccelerateTargets.
- Support API ListEnterpriseAccelerateLogs.
- Support API ListEnterpriseAcceleratePolicies.
- Support API ListEnterpriseAccelerateTargets.
- Support API ModifyEnterpriseAcceleratePolicy.
- Update API CreatePrivateAccessPolicy: add request parameters TrustedProcessGroupIds.
- Update API CreatePrivateAccessPolicy: add request parameters TrustedProcessStatus.
- Update API CreatePrivateAccessPolicy: add request parameters TrustedSoftwareIds.
- Update API CreateWmBaseImage: add request parameters ImageControl.
- Update API CreateWmExtractTask: add request parameters IsClientEmbed.
- Update API GetPrivateAccessPolicy: add response parameters Body.Policy.TrustedProcessGroupIds.
- Update API GetPrivateAccessPolicy: add response parameters Body.Policy.TrustedProcessStatus.
- Update API GetPrivateAccessPolicy: add response parameters Body.Policy.TrustedSoftwareIds.
- Update API GetUserDevice: add response parameters Body.Device.MatchDeviceGroupIds.
- Update API ListPrivateAccessPolices: add response parameters Body.Polices.$.TrustedProcessGroupIds.
- Update API ListPrivateAccessPolices: add response parameters Body.Polices.$.TrustedProcessStatus.
- Update API ListPrivateAccessPolices: add response parameters Body.Polices.$.TrustedSoftwareIds.
- Update API ListUserDevices: add request parameters DeviceGroupId.
- Update API ListUserDevices: add response parameters Body.Devices.$.MatchDeviceGroupIds.
- Update API ListUserPrivateAccessPolicies: add response parameters Body.Polices.$.TrustedProcessGroupIds.
- Update API ListUserPrivateAccessPolicies: add response parameters Body.Polices.$.TrustedSoftwareIds.
- Update API UpdatePrivateAccessPolicy: add request parameters TrustedProcessGroupIds.
- Update API UpdatePrivateAccessPolicy: add request parameters TrustedProcessStatus.
- Update API UpdatePrivateAccessPolicy: add request parameters TrustedSoftwareIds.


2025-04-27 Version: 1.8.6
- Update API CreateApprovalProcess: add request parameters MatchSchemas.EndpointHardeningSchemaId.
- Update API CreateApprovalProcess: add request parameters MatchSchemas.SoftwareHardeningSchemaId.
- Update API CreateApprovalProcess: add response parameters Body.Process.EndpointHardeningPolicies.
- Update API CreateApprovalProcess: add response parameters Body.Process.SoftwareHardeningPolicies.
- Update API GetApprovalProcess: add response parameters Body.Process.EndpointHardeningPolicies.
- Update API GetApprovalProcess: add response parameters Body.Process.SoftwareHardeningPolicies.
- Update API ListApprovalProcesses: add response parameters Body.Processes.$.EndpointHardeningPolicies.
- Update API ListApprovalProcesses: add response parameters Body.Processes.$.SoftwareHardeningPolicies.
- Update API UpdateApprovalProcess: add request parameters MatchSchemas.EndpointHardeningSchemaId.
- Update API UpdateApprovalProcess: add request parameters MatchSchemas.SoftwareHardeningSchemaId.
- Update API UpdateApprovalProcess: add response parameters Body.Process.EndpointHardeningPolicies.
- Update API UpdateApprovalProcess: add response parameters Body.Process.SoftwareHardeningPolicies.


2025-04-23 Version: 1.8.5
- Update API GetUserDevice: add response parameters Body.Device.Workshop.
- Update API ListUserDevices: add request parameters Workshop.
- Update API ListUserDevices: add response parameters Body.Devices.$.Workshop.


2025-04-16 Version: 1.8.4
- Update API UpdatePrivateAccessApplication: add request parameters L7ProxyDomainPrivate.


2024-11-13 Version: 1.9.0
- Support API ListUserApplications.
- Support API ListUserPrivateAccessPolicies.


2024-10-30 Version: 1.8.2
- Generated python 2023-01-20 for csas.

2024-10-29 Version: 1.8.1
- Update API CreatePrivateAccessApplication: add param BrowserAccessStatus.
- Update API CreatePrivateAccessApplication: add param L7ProxyDomainAutomaticPrefix.
- Update API CreatePrivateAccessApplication: add param L7ProxyDomainCustom.
- Update API CreatePrivateAccessApplication: update param Protocol.
- Update API CreateWmEmbedTask: add param CsvControl.
- Update API CreateWmExtractTask: add param CsvControl.
- Update API GetPrivateAccessApplication: update response param.
- Update API ListPrivateAccessApplications: add param AccessModes.
- Update API ListPrivateAccessApplications: update response param.
- Update API UpdatePrivateAccessApplication: add param L7ProxyDomainAutomaticPrefix.
- Update API UpdatePrivateAccessApplication: add param L7ProxyDomainCustom.
- Update API UpdatePrivateAccessApplication: add param L7ProxyDomainPrivate.
- Update API UpdatePrivateAccessApplication: update param Protocol.


2024-07-03 Version: 1.8.0
- Support API ListNacUserCert.
- Support API UpdateNacUserCertStatus.


2024-06-20 Version: 1.7.0
- Support API CreateWmBaseImage.
- Support API CreateWmEmbedTask.
- Support API CreateWmExtractTask.
- Support API CreateWmInfoMapping.
- Support API GetWmEmbedTask.
- Support API GetWmExtractTask.
- Support API LookupWmInfoMapping.


2024-06-18 Version: 1.6.1
- Update API CreatePrivateAccessPolicy: add param DeviceAttributeAction.
- Update API GetPrivateAccessPolicy: update response param.
- Update API ListPrivateAccessPolices: update response param.
- Update API UpdatePrivateAccessPolicy: add param DeviceAttributeAction.


2024-06-11 Version: 1.6.0
- Support API DeleteUserDevices.
- Support API ExportUserDevices.


2024-06-06 Version: 1.5.0
- Support API RevokeUserSession.


2024-05-17 Version: 1.4.1
- Update API ListUserDevices: add param InnerIp.


2024-04-25 Version: 1.4.0
- Support API CreateClientUser.
- Support API CreateIdpDepartment.
- Support API DeleteClientUser.
- Support API DeleteIdpDepartment.
- Support API GetActiveIdpConfig.
- Support API GetClientUser.
- Support API GetIdpConfig.
- Support API ListClientUsers.
- Support API ListIdpConfigs.
- Support API ListIdpDepartments.
- Support API UpdateClientUser.
- Support API UpdateClientUserPassword.
- Support API UpdateClientUserStatus.
- Support API UpdateIdpDepartment.


2024-04-15 Version: 1.3.0
- Support API ListPopTrafficStatistics.
- Support API ListUsers.
- Support API UpdateUsersStatus.
- Update API CreatePrivateAccessPolicy: add param DeviceAttributeId.
- Update API CreatePrivateAccessPolicy: update param CustomUserAttributes.
- Update API GetPrivateAccessPolicy: update response param.
- Update API ListPrivateAccessPolices: add param ApplicationName.
- Update API ListPrivateAccessPolices: add param TagName.
- Update API ListPrivateAccessPolices: update response param.
- Update API UpdatePrivateAccessPolicy: add param DeviceAttributeId.


2023-11-15 Version: 1.2.1
- Generated python 2023-01-20 for csas.

2023-09-14 Version: 1.2.0
- Generated python 2023-01-20 for csas.

2023-08-30 Version: 1.1.2
- Generated python 2023-01-20 for csas.

2023-08-24 Version: 1.1.1
- Generated python 2023-01-20 for csas.

2023-08-16 Version: 1.1.0
- Generated python 2023-01-20 for csas.

2023-06-12 Version: 1.0.1
- Supported recommand serialization format flat.

2023-03-24 Version: 1.0.0
- Supported PrivateAccess and userGroup OPEN API .

