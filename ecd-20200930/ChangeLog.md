2025-05-26 Version: 4.8.0
- Support API CreateTemplate.
- Support API DeleteTemplates.
- Support API DescribeTemplates.
- Support API ModifyTemplate.
- Support API ModifyTemplateBaseInfo.
- Update API AddUserToDesktopGroup: add request parameters UserGroupName.
- Update API CreateConfigGroup: add request parameters ConfigTimers.$.SegmentTimers.
- Update API CreateDesktopGroup: add request parameters UserGroupName.
- Update API CreateDesktops: add request parameters AppRuleId.
- Update API DescribeDesktopGroups: add response parameters Body.DesktopGroups.$.UserGroupName.
- Update API DescribeTimerGroup: add response parameters Body.Data.ConfigTimers.$.SegmentTimers.
- Update API DescribeUsersInGroup: add response parameters Body.UserGroupName.
- Update API ModifyTimerGroup: add request parameters ConfigTimers.$.SegmentTimers.
- Update API RemoveUserFromDesktopGroup: add request parameters UserGroupName.


2025-05-12 Version: 4.7.8
- Update API DescribeModificationPrice: add request parameters ResourceSpecs.


2025-04-28 Version: 4.7.7
- Update API CreateCloudDriveService: add request parameters ResellerOwnerUid.
- Update API CreateDesktopGroup: add request parameters ResellerOwnerUid.
- Update API CreateDesktops: add request parameters ResellerOwnerUid.
- Update API CreateNetworkPackage: add request parameters ResellerOwnerUid.
- Update API DeleteDesktopGroup: add request parameters ResellerOwnerUid.
- Update API DeleteDesktops: add request parameters ResellerOwnerUid.
- Update API DeleteNetworkPackages: add request parameters ResellerOwnerUid.
- Update API DescribeModificationPrice: add request parameters ResellerOwnerUid.
- Update API DescribePrice: add request parameters ResellerOwnerUid.
- Update API DescribeRefundPrice: add request parameters ResellerOwnerUid.
- Update API DescribeRenewalPrice: add request parameters ResellerOwnerUid.
- Update API ModifyDesktopChargeType: add request parameters ResellerOwnerUid.
- Update API ModifyDesktopSpec: add request parameters ResellerOwnerUid.
- Update API ModifyNetworkPackageBandwidth: add request parameters ResellerOwnerUid.
- Update API RenewDesktopGroup: add request parameters ResellerOwnerUid.
- Update API RenewDesktops: add request parameters ResellerOwnerUid.
- Update API RenewNetworkPackages: add request parameters ResellerOwnerUid.


2025-04-25 Version: 4.7.6
- Update API CreateCenterPolicy: add request parameters InternetPrinter.
- Update API CreateCenterPolicy: add request parameters SafeMenu.
- Update API CreateCenterPolicy: add request parameters DeviceRules.$.Platforms.
- Update API CreatePolicyGroup: add request parameters DeviceRules.$.Platforms.
- Update API DescribeCenterPolicyList: add response parameters Body.DescribePolicyGroups.$.InternetPrinter.
- Update API DescribeCenterPolicyList: add response parameters Body.DescribePolicyGroups.$.SafeMenu.
- Update API DescribeCenterPolicyList: add response parameters Body.DescribePolicyGroups.$.DeviceRules.$.Platforms.
- Update API DescribeImageModifiedRecords: add response parameters Body.ImageModifiedRecords.$.Reason.
- Update API DescribePolicyGroups: add response parameters Body.DescribePolicyGroups.$.InternetPrinter.
- Update API DescribePolicyGroups: add response parameters Body.DescribePolicyGroups.$.SafeMenu.
- Update API DescribePolicyGroups: add response parameters Body.DescribePolicyGroups.$.DeviceRules.$.Platforms.
- Update API ModifyCenterPolicy: add request parameters InternetPrinter.
- Update API ModifyCenterPolicy: add request parameters SafeMenu.
- Update API ModifyCenterPolicy: add request parameters DeviceRules.$.Platforms.
- Update API ModifyPolicyGroup: add request parameters DeviceRules.$.Platforms.


2025-04-25 Version: 4.7.5
- Generated python 2020-09-30 for ecd.

2025-04-19 Version: 4.7.4
- Update API DescribeClientEvents: add request parameters FillHardwareInfo.
- Update API DescribeClientEvents: add request parameters Language.
- Update API DescribeClientEvents: add response parameters Body.Events.$.TerminalInfo.


2025-04-10 Version: 4.7.3
- Update API DescribeOfficeSites: add response parameters Body.OfficeSites.$.IsLdap.
- Update API DescribeOfficeSites: add response parameters Body.OfficeSites.$.LdapUrl.
- Update API DescribeSnapshots: add request parameters OsType.
- Update API DescribeSnapshots: add response parameters Body.Snapshots.$.DiskStatus.
- Update API DescribeSnapshots: add response parameters Body.Snapshots.$.OsType.


2025-04-09 Version: 4.7.2
- Update API CreateImage: add request parameters DataSnapshotIds.
- Update API DescribeDesktopGroups: add response parameters Body.DesktopGroups.$.IsLdap.
- Update API DescribeDesktops: add response parameters Body.Desktops.$.IsLdap.
- Update API DescribeUsersInGroup: add response parameters Body.EndUsers.$.DisplayNameNew.
- Update API DescribeUsersInGroup: add response parameters Body.EndUsers.$.UserPrincipalName.
- Update API ListDirectoryUsers: add response parameters Body.Users.$.DisplayNameNew.
- Update API ListDirectoryUsers: add response parameters Body.Users.$.UserPrincipalName.
- Update API ListOfficeSiteUsers: add response parameters Body.Users.$.DisplayNameNew.
- Update API ListOfficeSiteUsers: add response parameters Body.Users.$.UserPrincipalName.
- Update API RebuildDesktops: add request parameters AfterStatus.


2025-03-27 Version: 4.7.1
- Update API CreateConfigGroup: add request parameters ConfigTimers.$.NotificationTime.
- Update API DescribeTimerGroup: add response parameters Body.Data.ConfigTimers.$.NotificationTime.
- Update API ModifyTimerGroup: add request parameters ConfigTimers.$.NotificationTime.


2025-03-26 Version: 4.7.0
- Support API CloneCenterPolicy.
- Support API CreateCenterPolicy.
- Support API DeleteCenterPolicy.
- Support API DescribeCenterPolicyList.
- Support API DescribeResourceByCenterPolicyId.
- Support API ModifyCenterPolicy.
- Support API ModifyResourceCenterPolicy.


2025-03-25 Version: 4.6.4
- Update API AddUserToDesktopGroup: add param UserOuPath.
- Update API AddUserToDesktopGroup: update param EndUserIds.
- Update API CreateDesktopGroup: add param UserOuPath.
- Update API DescribeDesktopGroups: update response param.
- Update API DescribeUsersInGroup: update response param.
- Update API RemoveUserFromDesktopGroup: add param UserOuPath.
- Update API RemoveUserFromDesktopGroup: update param EndUserIds.


2025-03-18 Version: 4.6.3
- Update API DescribeDesktops: update response param.
- Update API DescribePolicyGroups: update response param.
- Update API RebootDesktops: add param OsUpdate.
- Update API StopDesktops: add param OsUpdate.


2025-03-17 Version: 4.6.2
- Update API CreateDesktops: add param ExtendInfo.


2025-03-13 Version: 4.6.1
- Update API DescribeDesktops: update response param.


2025-03-04 Version: 4.6.0
- Support API CreateBandwidthResourcePackages.
- Update API DescribeDesktopsInGroup: add param CustomEndTimePeriod.
- Update API DescribeDesktopsInGroup: add param CustomStartTimePeriod.
- Update API DescribePolicyGroups: add param PageNumber.
- Update API DescribePolicyGroups: add param PageSize.
- Update API DescribePolicyGroups: update response param.
- Update API ModifyDiskSpec: add param ResellerOwnerUid.
- Update API RenewNetworkPackages: add param AutoRenew.


2025-02-25 Version: 4.5.0
- Support API ModifyOfficeSiteDnsInfo.
- Update API CreatePolicyGroup: update param DomainResolveRule.
- Update API DescribeDesktopTypes: add param GpuMemory.
- Update API DescribeDesktopTypes: update param DesktopTypeIdList.
- Update API DescribeDesktops: update response param.
- Update API ModifyPolicyGroup: update param DomainResolveRule.


2025-02-11 Version: 4.4.0
- Support API BindConfigGroup.
- Support API CreateConfigGroup.
- Support API DeleteConfigGroup.
- Support API DescribeConfigGroup.
- Support API DescribeTimerGroup.
- Support API ModifyConfigGroup.
- Support API ModifyTimerGroup.
- Support API UnbindConfigGroup.
- Update API CreateDesktopGroup: add param DataDiskCategory.
- Update API CreateDesktopGroup: add param DataDiskPerLevel.
- Update API CreateDesktopGroup: add param DataDiskSize.
- Update API CreateDesktopGroup: add param DefaultLanguage.
- Update API CreateDesktopGroup: add param DesktopType.
- Update API CreateDesktopGroup: add param ExclusiveType.
- Update API CreateDesktopGroup: add param GroupAmount.
- Update API CreateDesktopGroup: add param Hostname.
- Update API CreateDesktopGroup: add param ImageId.
- Update API CreateDesktopGroup: add param MultiResource.
- Update API CreateDesktopGroup: add param SessionType.
- Update API CreateDesktopGroup: add param SnapshotPolicyId.
- Update API CreateDesktopGroup: add param SystemDiskCategory.
- Update API CreateDesktopGroup: add param SystemDiskPerLevel.
- Update API CreateDesktopGroup: add param SystemDiskSize.
- Update API CreateDesktopGroup: add param TimerGroupId.
- Update API CreateDesktopGroup: update param BundleId.
- Update API CreateDesktopGroup: update response param.
- Update API CreateDesktops: add param SavingPlanId.
- Update API DescribeAclEntries: add param OfficeSiteId.
- Update API DescribeDesktopGroups: add param DesktopGroupIds.
- Update API DescribeDesktopGroups: add param MultiResource.
- Update API DescribeDesktopTypes: add param SupportMinSessionCount.
- Update API DescribeDesktopTypes: add param ZoneId.
- Update API DescribeDesktopTypes: update response param.
- Update API DescribeDesktops: add param MultiResource.
- Update API DescribeOfficeSites: update response param.
- Update API DescribePolicyGroups: add param ExternalPolicyGroupIds.
- Update API DescribePolicyGroups: update response param.
- Update API DescribeRecordings: add param StandardEndTime.
- Update API DescribeRecordings: add param StandardStartTime.


2025-01-24 Version: 4.3.0
- Support API BindConfigGroup.
- Support API CreateConfigGroup.
- Support API DeleteConfigGroup.
- Support API DescribeConfigGroup.
- Support API DescribeTimerGroup.
- Support API ModifyConfigGroup.
- Support API ModifyTimerGroup.
- Support API UnbindConfigGroup.
- Update API CreateDesktopGroup: add param DataDiskCategory.
- Update API CreateDesktopGroup: add param DataDiskPerLevel.
- Update API CreateDesktopGroup: add param DataDiskSize.
- Update API CreateDesktopGroup: add param DefaultLanguage.
- Update API CreateDesktopGroup: add param DesktopType.
- Update API CreateDesktopGroup: add param ExclusiveType.
- Update API CreateDesktopGroup: add param GroupAmount.
- Update API CreateDesktopGroup: add param Hostname.
- Update API CreateDesktopGroup: add param ImageId.
- Update API CreateDesktopGroup: add param MultiResource.
- Update API CreateDesktopGroup: add param SessionType.
- Update API CreateDesktopGroup: add param SnapshotPolicyId.
- Update API CreateDesktopGroup: add param SystemDiskCategory.
- Update API CreateDesktopGroup: add param SystemDiskPerLevel.
- Update API CreateDesktopGroup: add param SystemDiskSize.
- Update API CreateDesktopGroup: add param TimerGroupId.
- Update API CreateDesktopGroup: update param BundleId.
- Update API CreateDesktopGroup: update response param.
- Update API DescribeAclEntries: add param OfficeSiteId.
- Update API DescribeDesktopGroups: add param DesktopGroupIds.
- Update API DescribeDesktopGroups: add param MultiResource.
- Update API DescribeDesktopTypes: add param SupportMinSessionCount.
- Update API DescribeDesktopTypes: add param ZoneId.
- Update API DescribeDesktopTypes: update response param.
- Update API DescribeDesktops: add param MultiResource.
- Update API DescribeOfficeSites: update response param.
- Update API DescribePolicyGroups: add param ExternalPolicyGroupIds.
- Update API DescribePolicyGroups: update response param.
- Update API DescribeRecordings: add param StandardEndTime.
- Update API DescribeRecordings: add param StandardStartTime.


2025-01-15 Version: 4.2.3
- Update API ApplyAutoSnapshotPolicy: update param DesktopId.
- Update API DescribeBundles: update response param.
- Update API DescribeSnapshots: update response param.


2025-01-11 Version: 4.2.2
- Update API CreateDesktops: update param BundleId.
- Update API DescribeClientEvents: update response param.


2024-12-19 Version: 4.2.1
- Update API DescribeNASFileSystems: update response param.
- Update API DescribePolicyGroups: update response param.


2024-12-16 Version: 4.2.0
- Support API DescribeModificationPrice.
- Support API DescribeRefundPrice.
- Support API DescribeRenewalPrice.
- Support API RenewDesktopGroup.
- Update API CreateADConnectorOfficeSite: add param VSwitchId.
- Update API CreateADConnectorOfficeSite: update param CenId.
- Update API CreateADConnectorOfficeSite: update param CidrBlock.
- Update API CreateAutoSnapshotPolicy: update param PolicyName.
- Update API CreateDesktopGroup: add param PromotionId.
- Update API CreateDesktops: add param DesktopAttachment.
- Update API CreateDesktops: add param ResourceGroupId.
- Update API CreateDesktops: add param TimerGroupId.
- Update API CreateDesktops: update param Tag.
- Update API CreatePolicyGroup: add param WyAssistant.
- Update API CreatePolicyGroup: update param AuthorizeAccessPolicyRule.
- Update API DescribeCloudDriveGroups: update response param.
- Update API DescribeDesktopSessions: add param EndUserIdFilter.
- Update API DescribeDesktopSessions: update param OfficeSiteId.
- Update API DescribeDesktopTypes: add param DesktopTypeIdList.
- Update API DescribeDesktopTypes: add param OrderBy.
- Update API DescribeDesktopTypes: add param Scope.
- Update API DescribeDesktopTypes: add param SortType.
- Update API DescribeDesktopTypes: update response param.
- Update API DescribeDesktops: add param PageNumber.
- Update API DescribeDesktops: add param PageSize.
- Update API DescribeDesktops: update response param.
- Update API DescribeInvocations: add param IncludeInvokeDesktops.
- Update API DescribeInvocations: update response param.
- Update API DescribeKmsKeys: update response param.
- Update API DescribeOfficeSites: update response param.
- Update API DescribePolicyGroups: update response param.
- Update API DescribePrice: add param Duration.
- Update API DescribePrice: add param RootDiskCategory.
- Update API DescribePrice: add param UserDiskCategory.
- Update API DescribePrice: delete param BundleModels.
- Update API DescribePrice: delete param EduCdsEnable.
- Update API DescribePrice: delete param EduCdsSize.
- Update API DescribePrice: delete param EduCommittedTime.
- Update API DescribePrice: delete param EduDesktopBundleId.
- Update API DescribePrice: delete param EduDesktopNum.
- Update API DescribePrice: delete param EduRoomClassify.
- Update API DescribePrice: delete param EduStudentBundleId.
- Update API DescribePrice: delete param EduStudentNum.
- Update API DescribePrice: delete param EduTeacherBundleId.
- Update API DescribePrice: delete param EduTeacherNum.
- Update API DescribePrice: delete param HardwareVersion.
- Update API DescribePrice: delete param NetworkType.
- Update API DescribePrice: delete param PackageSize.
- Update API DescribePrice: delete param RootDiskPerformanceLevel.
- Update API DescribePrice: delete param SpPeriodInfo.
- Update API DescribePrice: delete param SpPrice.
- Update API DescribePrice: delete param SpType.
- Update API DescribePrice: delete param UserDiskPerformanceLevel.
- Update API DescribePrice: update param GroupDesktopCount.
- Update API DescribePrice: update param RootDiskSizeGib.
- Update API DescribePrice: update param UserDiskSizeGib.
- Update API GetConnectionTicket: update response param.
- Update API ListDirectoryUsers: add param AssignedInfo.
- Update API ListDirectoryUsers: add param IncludeAssignedUser.
- Update API ListDirectoryUsers: add param SortType.
- Update API ListDirectoryUsers: update response param.
- Update API ListOfficeSiteUsers: add param AssignedInfo.
- Update API ListOfficeSiteUsers: add param IncludeAssignedUser.
- Update API ListOfficeSiteUsers: add param SortType.
- Update API ListOfficeSiteUsers: update response param.
- Update API ModifyCloudDrivePermission: add param NoDownloadNoUploadEndUserIds.
- Update API ModifyDesktopSpec: update param UserDiskSizeGib.
- Update API ModifyPolicyGroup: add param WyAssistant.
- Update API ModifyPolicyGroup: update param AuthorizeAccessPolicyRule.
- Update API ModifyPolicyGroup: update param RevokeAccessPolicyRule.
- Update API RunCommand: update param DesktopId.
- Update API UploadImage: add param SystemDiskSize.


2024-07-23 Version: 4.1.2
- Update API DescribeCloudDriveGroups: update response param.


2024-07-22 Version: 4.1.1
- Update API CancelAutoSnapshotPolicy: update param PolicyId.
- Update API CreateDesktops: add param SnapshotPolicyId.
- Update API DescribeAutoSnapshotPolicy: update param MaxResults.


2024-07-21 Version: 4.1.0
- Support API DownloadCdsFile.


2024-07-19 Version: 4.0.2
- Update API CreatePolicyGroup: add param DeviceRedirects.
- Update API CreatePolicyGroup: add param DeviceRules.
- Update API DescribeBundles: add param GpuDriverType.
- Update API DescribeDesktopTypes: add param GpuDriverType.
- Update API DescribePolicyGroups: update response param.
- Update API ModifyPolicyGroup: add param DeviceRedirects.
- Update API ModifyPolicyGroup: add param DeviceRules.


2024-07-10 Version: 4.0.1
- Update API DescribeOfficeSites: add param SecurityProtection.
- Update API DescribeOfficeSites: update response param.


2024-07-09 Version: 4.0.0
- Support API SetDesktopMaintenance.
- Update API AddDesktopOversoldUserGroup: add param Tag.
- Update API CreateADConnectorOfficeSite: add param BackupDCHostname.
- Update API CreateADConnectorOfficeSite: add param BackupDns.
- Update API CreateDesktopGroup: add param Tag.
- Update API CreatePolicyGroup: add param MaxReconnectTime.
- Update API DescribeDesktopGroups: add param Tag.
- Update API DescribeDesktopGroups: update response param.
- Update API DescribeDesktopSessions: add param CheckOsSession.
- Update API DescribeDesktopSessions: add param SubPayType.
- Update API DescribeDesktopSessions: update response param.
- Update API DescribeDesktops: add param FillResourceGroup.
- Update API DescribeDesktops: add param GpuInstanceGroupId.
- Update API DescribeDesktops: add param QosRuleId.
- Update API DescribeDesktops: add param ResourceGroupId.
- Update API DescribeDesktops: add param SubPayType.
- Update API DescribeDesktops: update response param.
- Update API DescribeDirectories: update response param.
- Update API DescribeOfficeSites: update response param.
- Update API DescribePolicyGroups: update response param.
- Update API DescribePrice: update param BundleModels.
- Update API ExportDesktopGroupInfo: add param Tag.
- Update API ListTagResources: update param Tag.
- Update API ModifyADConnectorOfficeSite: add param BackupDCHostname.
- Update API ModifyADConnectorOfficeSite: add param BackupDns.
- Update API ModifyAutoSnapshotPolicy: update response param.
- Update API ModifyDesktopSpec: add param ResourceSpecs.
- Update API ModifyDesktopSpec: add param ResourceType.
- Update API ModifyDesktopSpec: update param DesktopId.
- Update API ModifyDesktopSpec: update response param.
- Update API ModifyPolicyGroup: add param MaxReconnectTime.
- Update API RebuildDesktops: add param Language.
- Update API RenewDesktops: add param AutoRenew.


2024-05-07 Version: 3.6.3
- Update API DescribeDesktopInfo: update response param.


2024-05-07 Version: 3.6.3
- Update API DescribeDesktopInfo: update response param.


2024-04-29 Version: 3.6.2
- Update API CreateCloudDriveService: update response param.
- Update API CreateDesktops: add param MonthDesktopSetting.
- Update API DescribeDesktopOversoldGroup: update response param.
- Update API DescribeDesktopOversoldUser: update param ClientToken.
- Update API DescribeOfficeSites: update response param.
- Update API RenewDesktops: add param ResourceType.


2024-04-19 Version: 3.6.1
- Update API CreateCloudDriveService: update response param.
- Update API DescribeDesktopOversoldGroup: update response param.
- Update API DescribeDesktopOversoldUser: update param ClientToken.


2024-04-15 Version: 3.6.0
- Support API DescribeRecordings.
- Update API CreateDesktopOversoldGroup: add param IdleDisconnectDuration.
- Update API CreateDesktopOversoldGroup: add param KeepDuration.
- Update API DescribeDesktopSessions: add param DesktopId.
- Update API DescribeDesktopSessions: add param DesktopName.
- Update API DescribeDesktopSessions: update response param.
- Update API ModifyDesktopOversoldGroup: add param IdleDisconnectDuration.
- Update API ModifyDesktopOversoldGroup: add param KeepDuration.


2024-03-25 Version: 3.5.3
- Update API AddDevices: update response param.
- Update API DescribeFotaPendingDesktops: update param TaskUid.
- Update API UpdateFotaTask: update param UserStatus.


2024-03-15 Version: 3.5.2
- Generated python 2020-09-30 for ecd.

2024-03-15 Version: 3.5.1
- Generated python 2020-09-30 for ecd.

2024-03-14 Version: 3.5.0
- Support API DescribeDesktopGroupSessions.
- Update API ResetDesktops: add param DesktopGroupIds.
- Update API ResetDesktops: add param ResetScope.


2024-03-13 Version: 3.4.1
- Update API ResetDesktops: add param DesktopGroupIds.
- Update API ResetDesktops: add param ResetScope.


2024-03-12 Version: 3.4.0
- Support API DisconnectDesktopSessions.
- Support API UnbindUserDesktop.
- Update API CreateAutoSnapshotPolicy: update response param.
- Update API CreateCloudDriveService: add param AutoPay.
- Update API CreateCloudDriveService: add param AutoRenew.
- Update API CreateCloudDriveService: add param CdsChargeType.
- Update API CreateCloudDriveService: add param Period.
- Update API CreateCloudDriveService: add param PeriodUnit.
- Update API CreateCloudDriveService: add param UserCount.
- Update API CreateCloudDriveService: update param Name.
- Update API CreateCloudDriveService: update response param.
- Update API CreateSnapshot: update response param.
- Update API RebuildDesktops: update response param.
- Update API SetDesktopGroupTimer: update response param.
- Update API SetDesktopGroupTimerStatus: update response param.


2024-02-26 Version: 3.3.0
- Support API DisconnectDesktopSessions.
- Support API UnbindUserDesktop.
- Update API CreateAutoSnapshotPolicy: update response param.
- Update API CreateSnapshot: update response param.
- Update API RebuildDesktops: update response param.
- Update API SetDesktopGroupTimer: update response param.
- Update API SetDesktopGroupTimerStatus: update response param.


2024-02-22 Version: 3.2.0
- Support API DisconnectDesktopSessions.
- Update API CreateAutoSnapshotPolicy: update response param.
- Update API CreateSnapshot: update response param.
- Update API RebuildDesktops: update response param.
- Update API SetDesktopGroupTimer: update response param.
- Update API SetDesktopGroupTimerStatus: update response param.


2024-02-22 Version: 3.1.0
- Support API DisconnectDesktopSessions.
- Update API CreateAutoSnapshotPolicy: update response param.
- Update API CreateSnapshot: update response param.
- Update API RebuildDesktops: update response param.
- Update API SetDesktopGroupTimer: update response param.
- Update API SetDesktopGroupTimerStatus: update response param.


2024-01-26 Version: 3.0.1
- Update API CreatePolicyGroupadd RecordingUserNotify param.
add RecordingUserNotifyMessage param.
add WatermarkAntiCam param.
add WatermarkPower param.
- Update API DescribePolicyGroupsupdate response param.
- Update API ModifyPolicyGroupadd RecordingUserNotify param.
add RecordingUserNotifyMessage param.
add WatermarkAntiCam param.
add WatermarkPower param.


2024-01-15 Version: 3.0.0
- Generated python 2020-09-30 for ecd.

2023-08-01 Version: 2.0.16
- ADD DomianResolve.

2023-04-21 Version: 2.0.15
- Support desktop group auto scale.

2022-10-28 Version: 2.0.14
- Support desktop group auto scale.

2022-09-16 Version: 2.0.13
- Support remote coordinate control.

2022-09-05 Version: 2.0.11
- PolicyGroup support appContentProtection and recordContent.

2022-07-12 Version: 2.0.7
- Upgrade sdk to same version.

2021-08-03 Version: 2.0.1
- Generated python 2020-09-30 for ecd.

2021-03-09 Version: 1.0.1
- Test.

2021-03-08 Version: 2.0.0
- Generated python 2020-09-30 for ecd.

2020-11-16 Version: 1.0.0
- Generated python 2020-09-30 for ecd.

