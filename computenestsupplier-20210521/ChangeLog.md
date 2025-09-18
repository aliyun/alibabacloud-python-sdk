2025-09-18 Version: 7.3.0
- Support API CreateOpsNotice.
- Support API GetOpsNotice.
- Support API ListOpsNotices.
- Update API GetService: add response parameters Body.ServiceLocaleConfigs.
- Update API ListServices: add response parameters Body.Services.$.ServiceLocaleConfigs.
- Update API UpdateService: add request parameters ServiceLocaleConfigs.


2025-09-09 Version: 7.2.0
- Support API DeleteAcrImageRepositories.
- Support API DeleteAcrImageTags.
- Support API GetNetworkAvailableZones.
- Support API GetServiceTemplateCriterionIssues.
- Support API ListArtifactBuildLogs.
- Support API ListServiceBuildLogs.
- Update API GetService: add response parameters Body.SecretKey.


2025-07-11 Version: 7.1.5
- Update API CreateArtifact: add request parameters ArtifactBuildProperty.EnableGpu.
- Update API UpdateArtifact: add request parameters ArtifactBuildProperty.EnableGpu.
- Update API UpdateArtifact: add request parameters ArtifactBuildProperty.SystemDiskSize.


2025-06-16 Version: 7.1.4
- Update API CreateArtifact: add request parameters ArtifactBuildProperty.SystemDiskSize.


2025-05-29 Version: 7.1.3
- Update API ListArtifacts: add response parameters Body.Artifacts.$.PermissionType.


2025-05-27 Version: 7.1.2
- Update API GetServiceProvisions: add response parameters Body.ServiceProvisions.$.CommodityProvisions.


2025-05-22 Version: 7.1.1
- Update API UpdateServiceInstanceAttribute: add request parameters LicenseData.ResponseInfo.


2025-05-08 Version: 7.1.0
- Support API ListServiceInstanceBill.
- Update API UpdateService: add request parameters BuildParameters.


2025-04-17 Version: 7.0.6
- Update API GetService: add response parameters Body.SupportContacts.
- Update API GetSupplierInformation: add response parameters Body.SupportContacts.
- Update API UpdateSupplierInformation: add request parameters SupportContacts.


2025-04-07 Version: 7.0.5
- Update API GetService: add response parameters Body.BuildParameters.


2025-04-01 Version: 7.0.4
- Generated python 2021-05-21 for ComputeNestSupplier.

2025-03-19 Version: 7.0.3
- Update API GetSupplierInformation: update response param.
- Update API ListAcrImageRepositories: update response param.


2025-03-12 Version: 7.0.2
- Generated python 2021-05-21 for ComputeNestSupplier.

2025-03-12 Version: 7.0.1
- Update API CreateArtifact: update param ArtifactBuildProperty.
- Update API ListServiceInstanceResources: update param NextToken.
- Update API UpdateArtifact: update param ArtifactBuildProperty.
- Update API UpgradeServiceInstance: update param ServiceInstanceId.


2025-03-05 Version: 7.0.0
- Update API ListServiceInstanceResources: delete param ResourceARN.


2025-03-03 Version: 6.3.0
- Support API CancelServiceRegistration.
- Support API CreateServiceTestCase.
- Support API CreateServiceTestTask.
- Support API CreateSupplierRegistration.
- Support API DeleteServiceTestCase.
- Support API GenerateDefaultServiceTestConfig.
- Support API GetServiceRegistration.
- Support API GetServiceTestTask.
- Support API GetSupplierInformation.
- Support API ListArtifactRisks.
- Support API ListResellers.
- Support API ListServiceInstanceDeployDetails.
- Support API ListServiceInstanceLogs.
- Support API ListServiceInstanceResources.
- Support API ListServiceInstanceUpgradeHistory.
- Support API ListServiceRegistrations.
- Support API ListServiceTestCases.
- Support API ListServiceTestTaskLogs.
- Support API ListServiceTestTasks.
- Support API ListSupplierRegistrations.
- Support API ListTagResources.
- Support API UpdateServiceTestCase.
- Support API UpdateSharedAccountPermission.
- Support API UpdateSupplierInformation.
- Support API WithdrawService.
- Update API GetArtifact: update response param.
- Update API ListArtifacts: update response param.
- Update API UpdateArtifact: add param PermissionType.
- Update API UpdateArtifact: update param ArtifactProperty.
- Update API UpdateArtifact: update param VersionName.


2025-01-02 Version: 6.1.0
- Support API GenerateServicePolicy.
- Support API GetServiceProvisions.
- Support API ListTagKeys.
- Support API ListTagValues.
- Support API TagResources.
- Support API UnTagResources.


2024-12-17 Version: 6.0.0
- Update API CreateArtifact: add param ClientToken.
- Update API CreateArtifact: update param ArtifactProperty.
- Update API DeleteArtifact: add param ClientToken.
- Update API ReleaseArtifact: add param ClientToken.
- Update API UpdateArtifact: add param ClientToken.
- Update API UpdateArtifact: update param ArtifactProperty.


2024-12-02 Version: 5.0.1
- Update API CreateArtifact: add param ArtifactBuildType.
- Update API CreateArtifact: update param ArtifactBuildProperty.
- Update API CreateArtifact: update response param.
- Update API GetArtifact: update response param.
- Update API ListArtifactVersions: update response param.
- Update API UpdateArtifact: update param ArtifactBuildProperty.
- Update API UpdateArtifact: update response param.


2024-12-02 Version: 5.0.0
- Update API GetService: update response param.
- Update API GetServiceInstance: update response param.


2024-11-26 Version: 4.1.0
- Support API RollbackServiceInstance.


2024-11-12 Version: 4.0.1
- Update API GetService: update response param.


2024-11-07 Version: 4.0.0
- Delete API ListServiceCategories.
- Update API CreateArtifact: add param ArtifactBuildProperty.
- Update API CreateArtifact: update param ArtifactProperty.
- Update API CreateArtifact: update response param.
- Update API GetArtifact: update response param.
- Update API ListAcrImageRepositories: update response param.
- Update API ListArtifactVersions: add param Filters.
- Update API ListArtifactVersions: update response param.
- Update API UpdateArtifact: add param ArtifactBuildProperty.
- Update API UpdateArtifact: update param ArtifactProperty.
- Update API UpdateArtifact: update response param.


2024-10-25 Version: 2.8.0
- Support API LaunchService.
- Support API PreLaunchService.
- Update API CreateService: add param ComplianceMetadata.
- Update API CreateService: add param DryRun.
- Update API CreateService: update param ServiceInfo.
- Update API CreateService: update response param.
- Update API GetService: add param ServiceInstanceId.
- Update API GetService: add param ServiceName.
- Update API GetService: update param ServiceId.
- Update API GetService: update response param.
- Update API UpdateService: add param ComplianceMetadata.
- Update API UpdateService: add param DryRun.
- Update API UpdateService: update param Commodity.
- Update API UpdateService: update param ServiceInfo.
- Update API UpdateService: update param UpdateOption.
- Update API UpdateService: update response param.
- Update API UpdateServiceInstanceAttribute: add param Reason.


2024-10-22 Version: 2.7.0
- Support API LaunchService.
- Support API PreLaunchService.
- Update API CreateService: add param DryRun.
- Update API CreateService: update param ServiceInfo.
- Update API CreateService: update response param.
- Update API GetService: update response param.
- Update API UpdateService: add param DryRun.
- Update API UpdateService: update param Commodity.
- Update API UpdateService: update param ServiceInfo.
- Update API UpdateService: update param UpdateOption.
- Update API UpdateService: update response param.
- Update API UpdateServiceInstanceAttribute: add param Reason.


2024-07-30 Version: 2.6.1
- Update API UpdateService: update param UpdateOption.


2024-07-22 Version: 2.6.0
- Support API ListServiceSharedAccounts.
- Support API RemoveServiceSharedAccounts.


2024-07-22 Version: 2.5.0
- Support API ApproveServiceUsage.
- Support API CreateServiceUsage.
- Support API ListServiceCategories.
- Support API RejectServiceUsage.


2024-07-18 Version: 2.4.4
- Update API GetServiceInstance: update response param.


2024-07-15 Version: 2.4.3
- Update API UpdateService: add param Commodity.
- Update API UpdateServiceInstanceAttribute: add param LicenseData.


2024-06-28 Version: 2.4.2
- Update API GetUploadCredentials: add param Visibility.


2024-06-20 Version: 2.4.1
- Update API UpdateService: add param ApprovalType.
- Update API UpdateService: add param ShareType.


2024-06-18 Version: 2.4.0
- Support API RestartServiceInstance.
- Support API StartServiceInstance.
- Support API StopServiceInstance.
- Update API GetService: update param ServiceVersion.


2024-05-30 Version: 3.0.0
- Support API AddServiceSharedAccounts.
- Support API GetServiceTemplateParameterConstraints.
- Support API UpdateServiceInstanceAttribute.
- Support API UpdateServiceInstanceSpec.
- Support API UpgradeServiceInstance.
- Update API CreateService: add param BuildParameters.
- Update API CreateService: add param Resellable.
- Update API CreateService: update param ServiceInfo.
- Update API CreateServiceInstance: add param EndTime.
- Update API GetService: update response param.
- Update API GetServiceEstimateCost: add param Commodity.
- Update API GetServiceEstimateCost: update response param.
- Update API GetServiceInstance: update response param.
- Update API ListArtifactVersions: add param MaxResults.
- Update API ListArtifactVersions: delete param MaxResult.
- Update API ListServiceInstances: update response param.
- Update API ListServiceUsages: add param SupplierRole.
- Update API ListServiceUsages: update response param.
- Update API ListServices: update response param.
- Update API UpdateService: add param Resellable.
- Update API UpdateService: add param UpdateOption.
- Update API UpdateService: update param ServiceInfo.


2023-09-08 Version: 2.3.2
- Generated python 2021-05-21 for ComputeNestSupplier.

2023-08-31 Version: 2.3.1
- Generated python 2021-05-21 for ComputeNestSupplier.

2023-08-31 Version: 2.3.0
- Generated python 2021-05-21 for ComputeNestSupplier.

2023-08-18 Version: 2.2.0
- Generated python 2021-05-21 for ComputeNestSupplier.

2023-08-12 Version: 2.1.1
- Generated python 2021-05-21 for ComputeNestSupplier.

2023-08-10 Version: 2.1.0
- Add 3 API CreateServiceInstance, DeleteServiceInstances, ContinueDeployServiceInstance.

2023-05-23 Version: 1.2.3
- Add UpdateService GetService DeleteService.

2023-05-16 Version: 1.2.2
- Add UpdateService GetService DeleteService.

2023-05-16 Version: 1.2.1
- Add response Permission.

2023-04-28 Version: 1.2.0
- Add API ListServices and CreateService.

2023-02-06 Version: 1.1.2
- Public ListServiceUsages  OpenApi.

2021-08-31 Version: 1.1.1
- Support ComputeNest Operation.

2021-08-31 Version: 1.1.0
- Support ComputeNest Operation.

2021-08-25 Version: 1.0.0
- The first version of ComputeNestSupplier SDK.

