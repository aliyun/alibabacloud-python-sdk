2025-09-09 Version: 5.0.4
- Update API DescribeAlerts: add response parameters Body.Data.ResponseData.$.DetectionRuleId.
- Update API DescribeAlerts: add response parameters Body.Data.ResponseData.$.ProductId.
- Update API DescribeAlerts: add response parameters Body.Data.ResponseData.$.VendorId.
- Update API DescribeAlertsWithEntity: add response parameters Body.Data.ResponseData.$.DetectionRuleId.
- Update API DescribeAlertsWithEntity: add response parameters Body.Data.ResponseData.$.ProductId.
- Update API DescribeAlertsWithEntity: add response parameters Body.Data.ResponseData.$.VendorId.
- Update API DescribeAlertsWithEvent: add response parameters Body.Data.ResponseData.$.DetectionRuleId.
- Update API DescribeAlertsWithEvent: add response parameters Body.Data.ResponseData.$.ProductId.
- Update API DescribeAlertsWithEvent: add response parameters Body.Data.ResponseData.$.VendorId.
- Update API DescribeEventCountByThreatLevel: add response parameters Body.Data.InfoLevelEventNum.
- Update API DescribeEventCountByThreatLevel: add response parameters Body.Data.SeriousLevelEventNum.


2025-09-08 Version: 5.0.3
- Generated python 2022-06-16 for cloud-siem.

2025-06-18 Version: 5.0.2
- Update API ListEntities: add request parameters Tags.
- Update API ListEntities: add response parameters Body.Data.ResponseData.$.IsAsset.
- Update API ListEntities: add response parameters Body.Data.ResponseData.$.IsMalware.
- Update API ListEntities: add response parameters Body.Data.ResponseData.$.Tags.


2025-06-05 Version: 5.0.1
- Update API ListAutomateResponseConfigs: add request parameters ResponseRuleType.
- Update API ListAutomateResponseConfigs: add response parameters Body.Data.ResponseData.$.ResponseRuleType.


2025-05-27 Version: 5.0.0
- Support API ListEntities.
- Delete API AddUser.
- Delete API BatchJobSubmit.
- Delete API DeleteUser.
- Delete API DescribeAttackTimeLine.
- Delete API DescribeCsImportedProdStatusByUser.
- Delete API DescribeJobStatus.
- Delete API DescribeLogStore.
- Delete API DoQuickField.
- Delete API DoSelfDelegate.
- Delete API GetHistograms.
- Delete API GetLogs.
- Delete API GetQuickQuery.
- Delete API ListOperation.
- Delete API ListQuickQuery.
- Delete API ListUserProdLogs.
- Delete API ListUsersByProd.
- Delete API SaveQuickQuery.
- Delete API ShowQuickAnalysis.
- Delete API SubmitJobs.
- Update API DescribeAlerts: add request parameters AlertName.
- Update API DescribeAlerts: add request parameters AlertType.
- Update API DescribeAlerts: add request parameters AssetId.
- Update API DescribeAlerts: add request parameters AssetName.
- Update API DescribeAlerts: add request parameters EntityId.
- Update API DescribeAlerts: add request parameters EntityName.
- Update API DescribeAlerts: add request parameters LabelType.
- Update API DescribeAlerts: add response parameters Body.Data.ResponseData.$.EntityList.
- Update API DescribeAlerts: add response parameters Body.Data.ResponseData.$.ExtendContent.
- Update API DescribeAlerts: add response parameters Body.Data.ResponseData.$.SubUserName.
- Update API DescribeAlertsCount: add request parameters QueryType.
- Update API DescribeAlertsCount: add response parameters Body.Data.CountMap.
- Update API DescribeAlertsWithEntity: add request parameters EndTime.
- Update API DescribeAlertsWithEntity: add request parameters EntityUuid.
- Update API DescribeAlertsWithEntity: add request parameters StartTime.
- Update API DescribeAlertsWithEntity: add response parameters Body.Data.ResponseData.$.EntityList.
- Update API DescribeAlertsWithEntity: add response parameters Body.Data.ResponseData.$.SubUserName.
- Update API DescribeAlertsWithEvent: add request parameters AlertName.
- Update API DescribeAlertsWithEvent: add request parameters AlertType.
- Update API DescribeAlertsWithEvent: add request parameters AssetId.
- Update API DescribeAlertsWithEvent: add request parameters AssetName.
- Update API DescribeAlertsWithEvent: add request parameters EndTime.
- Update API DescribeAlertsWithEvent: add request parameters EntityId.
- Update API DescribeAlertsWithEvent: add request parameters EntityName.
- Update API DescribeAlertsWithEvent: add request parameters StartTime.
- Update API DescribeAlertsWithEvent: add response parameters Body.Data.ResponseData.$.ExtendContent.
- Update API DescribeAlertsWithEvent: add response parameters Body.Data.ResponseData.$.SubUserName.
- Update API DescribeCloudSiemAssets: add request parameters AssetName.
- Update API DescribeCloudSiemAssets: add request parameters AssetUuid.
- Update API DescribeCloudSiemEventDetail: add response parameters Body.Data.AttckStages.
- Update API DescribeCloudSiemEventDetail: add response parameters Body.Data.IncidentType.
- Update API DescribeCloudSiemEventDetail: add response parameters Body.Data.RuleId.
- Update API DescribeCloudSiemEvents: add request parameters EntityUuid.
- Update API DescribeCloudSiemEvents: add response parameters Body.Data.ResponseData.$.AttckStages.
- Update API DescribeCloudSiemEvents: add response parameters Body.Data.ResponseData.$.IncidentType.
- Update API DescribeCloudSiemEvents: add response parameters Body.Data.ResponseData.$.RuleId.
- Update API DescribeDisposeAndPlaybook: add request parameters EntityUuid.
- Update API DescribeDisposeAndPlaybook: add response parameters Body.Data.ResponseData.$.EntityType.
- Update API DescribeDisposeAndPlaybook: add response parameters Body.Data.ResponseData.$.PlaybookList.$.Available.
- Update API DescribeDisposeAndPlaybook: add response parameters Body.Data.ResponseData.$.PlaybookList.$.Uuid.
- Update API ListCustomizeRuleTestResult: add request parameters DetectionRuleId.
- Update API ListCustomizeRuleTestResult: add request parameters EndTime.
- Update API ListCustomizeRuleTestResult: add request parameters StartTime.
- Update API ListCustomizeRuleTestResult: add request parameters VerifyType.
- Update API ListCustomizeRuleTestResult: add response parameters Body.Data.PageInfo.VerifiedCount.
- Update API ListCustomizeRuleTestResult: add response parameters Body.Data.ResponseData.$.VerifyType.
- Update API ListDisposeStrategy: add request parameters IncidentUuid.
- Update API ListDisposeStrategy: add response parameters Body.Data.ResponseData.$.TaskUrl.
- Update API PostEventDisposeAndWhiteruleList: add request parameters ThreatLevel.


2024-08-13 Version: 4.0.1
- Update API DescribeProdCount: update param RoleType.
- Update API DescribeProdCount: update response param.
- Update API ListAccountsByLog: update param CloudCode.
- Update API ListImportedLogsByProd: update param CloudCode.


2024-08-07 Version: 4.0.0
- Delete API BatchJobCheck.
- Delete API DeleteQuickQuery.
- Delete API DescribeCustomizeRule.
- Update API BindAccount: add param RoleFor.
- Update API BindAccount: add param RoleType.
- Update API DeleteBindAccount: add param RoleFor.
- Update API DeleteBindAccount: add param RoleType.
- Update API DescribeImportedLogCount: add param RoleFor.
- Update API DescribeImportedLogCount: add param RoleType.
- Update API DescribeProdCount: add param RoleFor.
- Update API DescribeProdCount: add param RoleType.
- Update API ListAccountAccessId: add param RoleFor.
- Update API ListAccountAccessId: add param RoleType.
- Update API ListBindAccount: add param RoleFor.
- Update API ListBindAccount: add param RoleType.
- Update API ModifyBindAccount: add param RoleFor.
- Update API ModifyBindAccount: add param RoleType.
- Update API SubmitImportLogTasks: add param RoleFor.
- Update API SubmitImportLogTasks: add param RoleType.


2024-04-26 Version: 3.0.6
- Update API CloseDelivery: add param RoleFor.
- Update API CloseDelivery: add param RoleType.
- Update API DeleteAutomateResponseConfig: add param RoleFor.
- Update API DeleteAutomateResponseConfig: add param RoleType.
- Update API DeleteCustomizeRule: add param RoleFor.
- Update API DeleteCustomizeRule: add param RoleType.
- Update API DeleteWhiteRuleList: add param RoleFor.
- Update API DeleteWhiteRuleList: add param RoleType.
- Update API DescribeAggregateFunction: add param RoleFor.
- Update API DescribeAggregateFunction: add param RoleType.
- Update API DescribeAlertScene: add param RoleFor.
- Update API DescribeAlertScene: add param RoleType.
- Update API DescribeAlertSceneByEvent: add param RoleFor.
- Update API DescribeAlertSceneByEvent: add param RoleType.
- Update API DescribeAlertSource: add param RoleFor.
- Update API DescribeAlertSource: add param RoleType.
- Update API DescribeAlertSourceWithEvent: add param RoleFor.
- Update API DescribeAlertSourceWithEvent: add param RoleType.
- Update API DescribeAlertType: add param RoleFor.
- Update API DescribeAlertType: add param RoleType.
- Update API DescribeAlertType: add param RuleType.
- Update API DescribeAlerts: add param RoleFor.
- Update API DescribeAlerts: add param RoleType.
- Update API DescribeAlertsCount: add param RoleFor.
- Update API DescribeAlertsCount: add param RoleType.
- Update API DescribeAlertsWithEntity: add param RoleFor.
- Update API DescribeAlertsWithEntity: add param RoleType.
- Update API DescribeAlertsWithEvent: add param RoleFor.
- Update API DescribeAlertsWithEvent: add param RoleType.
- Update API DescribeAlertsWithEvent: update response param.
- Update API DescribeAttackTimeLine: add param RoleFor.
- Update API DescribeAttackTimeLine: add param RoleType.
- Update API DescribeAutomateResponseConfigCounter: add param RoleFor.
- Update API DescribeAutomateResponseConfigCounter: add param RoleType.
- Update API DescribeAutomateResponseConfigFeature: add param RoleFor.
- Update API DescribeAutomateResponseConfigFeature: add param RoleType.
- Update API DescribeAutomateResponseConfigPlayBooks: add param RoleFor.
- Update API DescribeAutomateResponseConfigPlayBooks: add param RoleType.
- Update API DescribeCloudSiemAssets: add param RoleFor.
- Update API DescribeCloudSiemAssets: add param RoleType.
- Update API DescribeCloudSiemAssetsCounter: add param RoleFor.
- Update API DescribeCloudSiemAssetsCounter: add param RoleType.
- Update API DescribeCloudSiemEventDetail: add param RoleFor.
- Update API DescribeCloudSiemEventDetail: add param RoleType.
- Update API DescribeCloudSiemEvents: add param RoleFor.
- Update API DescribeCloudSiemEvents: add param RoleType.
- Update API DescribeCloudSiemEvents: update response param.
- Update API DescribeCustomizeRuleCount: add param RoleFor.
- Update API DescribeCustomizeRuleCount: add param RoleType.
- Update API DescribeCustomizeRuleCount: update response param.
- Update API DescribeCustomizeRuleTest: add param RoleFor.
- Update API DescribeCustomizeRuleTest: add param RoleType.
- Update API DescribeCustomizeRuleTestHistogram: add param RoleFor.
- Update API DescribeCustomizeRuleTestHistogram: add param RoleType.
- Update API DescribeDisposeAndPlaybook: add param RoleFor.
- Update API DescribeDisposeAndPlaybook: add param RoleType.
- Update API DescribeDisposeStrategyPlaybook: add param RoleFor.
- Update API DescribeDisposeStrategyPlaybook: add param RoleType.
- Update API DescribeEntityInfo: add param RoleFor.
- Update API DescribeEntityInfo: add param RoleType.
- Update API DescribeEventCountByThreatLevel: add param EndTime.
- Update API DescribeEventCountByThreatLevel: add param RoleFor.
- Update API DescribeEventCountByThreatLevel: add param RoleType.
- Update API DescribeEventCountByThreatLevel: add param StartTime.
- Update API DescribeEventDispose: add param RoleFor.
- Update API DescribeEventDispose: add param RoleType.
- Update API DescribeLogFields: add param RoleFor.
- Update API DescribeLogFields: add param RoleType.
- Update API DescribeLogSource: add param RoleFor.
- Update API DescribeLogSource: add param RoleType.
- Update API DescribeLogType: add param RoleFor.
- Update API DescribeLogType: add param RoleType.
- Update API DescribeOperators: add param RoleFor.
- Update API DescribeOperators: add param RoleType.
- Update API DescribeScopeUsers: add param RoleFor.
- Update API DescribeScopeUsers: add param RoleType.
- Update API DescribeScopeUsers: update response param.
- Update API DescribeStorage: add param RoleFor.
- Update API DescribeStorage: add param RoleType.
- Update API DescribeUserBuyStatus: update param SubUserId.
- Update API DescribeUserBuyStatus: update response param.
- Update API DescribeWafScope: add param RoleFor.
- Update API DescribeWafScope: add param RoleType.
- Update API DescribeWhiteRuleList: add param RoleFor.
- Update API DescribeWhiteRuleList: add param RoleType.
- Update API EnableAccessForCloudSiem: add param AutoSubmit.
- Update API EnableAccessForCloudSiem: add param RoleFor.
- Update API EnableAccessForCloudSiem: add param RoleType.
- Update API GetCapacity: add param RoleFor.
- Update API GetCapacity: add param RoleType.
- Update API GetStorage: add param RoleFor.
- Update API GetStorage: add param RoleType.
- Update API ListAccountsByLog: add param RoleFor.
- Update API ListAccountsByLog: add param RoleType.
- Update API ListAccountsByLog: update param CloudCode.
- Update API ListAccountsByLog: update param LogCodes.
- Update API ListAllProds: add param RoleFor.
- Update API ListAllProds: add param RoleType.
- Update API ListAutomateResponseConfigs: add param RoleFor.
- Update API ListAutomateResponseConfigs: add param RoleType.
- Update API ListAutomateResponseConfigs: update response param.
- Update API ListCloudSiemCustomizeRules: add param Order.
- Update API ListCloudSiemCustomizeRules: add param OrderField.
- Update API ListCloudSiemCustomizeRules: add param RoleFor.
- Update API ListCloudSiemCustomizeRules: add param RoleType.
- Update API ListCloudSiemCustomizeRules: update response param.
- Update API ListCloudSiemPredefinedRules: add param AttCk.
- Update API ListCloudSiemPredefinedRules: add param EventTransferType.
- Update API ListCloudSiemPredefinedRules: add param LogSource.
- Update API ListCloudSiemPredefinedRules: add param Order.
- Update API ListCloudSiemPredefinedRules: add param OrderField.
- Update API ListCloudSiemPredefinedRules: add param RoleFor.
- Update API ListCloudSiemPredefinedRules: add param RoleType.
- Update API ListCloudSiemPredefinedRules: update response param.
- Update API ListCustomizeRuleTestResult: add param RoleFor.
- Update API ListCustomizeRuleTestResult: add param RoleType.
- Update API ListDelivery: add param RoleFor.
- Update API ListDelivery: add param RoleType.
- Update API ListDisposeStrategy: add param RoleFor.
- Update API ListDisposeStrategy: add param RoleType.
- Update API ListImportedLogsByProd: add param RoleFor.
- Update API ListImportedLogsByProd: add param RoleType.
- Update API ListImportedLogsByProd: update param CloudCode.
- Update API ListImportedLogsByProd: update response param.
- Update API ListUserProdLogs: add param RoleFor.
- Update API ListUserProdLogs: add param RoleType.
- Update API ListUserProdLogs: update response param.
- Update API ListUsersByProd: add param RoleFor.
- Update API ListUsersByProd: add param RoleType.
- Update API ListUsersByProd: update response param.
- Update API OpenDelivery: add param RoleFor.
- Update API OpenDelivery: add param RoleType.
- Update API PostAutomateResponseConfig: add param RoleFor.
- Update API PostAutomateResponseConfig: add param RoleType.
- Update API PostCustomizeRule: add param AttCk.
- Update API PostCustomizeRule: add param RoleFor.
- Update API PostCustomizeRule: add param RoleType.
- Update API PostCustomizeRule: update response param.
- Update API PostCustomizeRuleTest: add param RoleFor.
- Update API PostCustomizeRuleTest: add param RoleType.
- Update API PostEventDisposeAndWhiteruleList: add param RoleFor.
- Update API PostEventDisposeAndWhiteruleList: add param RoleType.
- Update API PostEventWhiteruleList: add param RoleFor.
- Update API PostEventWhiteruleList: add param RoleType.
- Update API PostFinishCustomizeRuleTest: add param RoleFor.
- Update API PostFinishCustomizeRuleTest: add param RoleType.
- Update API PostRuleStatusChange: add param RoleFor.
- Update API PostRuleStatusChange: add param RoleType.
- Update API RestoreCapacity: add param RoleFor.
- Update API RestoreCapacity: add param RoleType.
- Update API SetStorage: add param RoleFor.
- Update API SetStorage: add param RoleType.
- Update API UpdateAutomateResponseConfigStatus: add param RoleFor.
- Update API UpdateAutomateResponseConfigStatus: add param RoleType.
- Update API UpdateWhiteRuleList: add param RoleFor.
- Update API UpdateWhiteRuleList: add param RoleType.


2024-04-17 Version: 3.0.5
- Update API CloseDelivery: add param RoleFor.
- Update API CloseDelivery: add param RoleType.
- Update API DeleteAutomateResponseConfig: add param RoleFor.
- Update API DeleteAutomateResponseConfig: add param RoleType.
- Update API DeleteCustomizeRule: add param RoleFor.
- Update API DeleteCustomizeRule: add param RoleType.
- Update API DeleteWhiteRuleList: add param RoleFor.
- Update API DeleteWhiteRuleList: add param RoleType.
- Update API DescribeAggregateFunction: add param RoleFor.
- Update API DescribeAggregateFunction: add param RoleType.
- Update API DescribeAlertScene: add param RoleFor.
- Update API DescribeAlertScene: add param RoleType.
- Update API DescribeAlertSceneByEvent: add param RoleFor.
- Update API DescribeAlertSceneByEvent: add param RoleType.
- Update API DescribeAlertSource: add param RoleFor.
- Update API DescribeAlertSource: add param RoleType.
- Update API DescribeAlertSourceWithEvent: add param RoleFor.
- Update API DescribeAlertSourceWithEvent: add param RoleType.
- Update API DescribeAlertType: add param RoleFor.
- Update API DescribeAlertType: add param RoleType.
- Update API DescribeAlertType: add param RuleType.
- Update API DescribeAlerts: add param RoleFor.
- Update API DescribeAlerts: add param RoleType.
- Update API DescribeAlertsCount: add param RoleFor.
- Update API DescribeAlertsCount: add param RoleType.
- Update API DescribeAlertsWithEntity: add param RoleFor.
- Update API DescribeAlertsWithEntity: add param RoleType.
- Update API DescribeAlertsWithEvent: add param RoleFor.
- Update API DescribeAlertsWithEvent: add param RoleType.
- Update API DescribeAlertsWithEvent: update response param.
- Update API DescribeAttackTimeLine: add param RoleFor.
- Update API DescribeAttackTimeLine: add param RoleType.
- Update API DescribeAutomateResponseConfigCounter: add param RoleFor.
- Update API DescribeAutomateResponseConfigCounter: add param RoleType.
- Update API DescribeAutomateResponseConfigFeature: add param RoleFor.
- Update API DescribeAutomateResponseConfigFeature: add param RoleType.
- Update API DescribeAutomateResponseConfigPlayBooks: add param RoleFor.
- Update API DescribeAutomateResponseConfigPlayBooks: add param RoleType.
- Update API DescribeCloudSiemAssets: add param RoleFor.
- Update API DescribeCloudSiemAssets: add param RoleType.
- Update API DescribeCloudSiemAssetsCounter: add param RoleFor.
- Update API DescribeCloudSiemAssetsCounter: add param RoleType.
- Update API DescribeCloudSiemEventDetail: add param RoleFor.
- Update API DescribeCloudSiemEventDetail: add param RoleType.
- Update API DescribeCloudSiemEvents: add param RoleFor.
- Update API DescribeCloudSiemEvents: add param RoleType.
- Update API DescribeCloudSiemEvents: update response param.
- Update API DescribeCustomizeRuleCount: add param RoleFor.
- Update API DescribeCustomizeRuleCount: add param RoleType.
- Update API DescribeCustomizeRuleCount: update response param.
- Update API DescribeCustomizeRuleTest: add param RoleFor.
- Update API DescribeCustomizeRuleTest: add param RoleType.
- Update API DescribeCustomizeRuleTestHistogram: add param RoleFor.
- Update API DescribeCustomizeRuleTestHistogram: add param RoleType.
- Update API DescribeDisposeAndPlaybook: add param RoleFor.
- Update API DescribeDisposeAndPlaybook: add param RoleType.
- Update API DescribeDisposeStrategyPlaybook: add param RoleFor.
- Update API DescribeDisposeStrategyPlaybook: add param RoleType.
- Update API DescribeEntityInfo: add param RoleFor.
- Update API DescribeEntityInfo: add param RoleType.
- Update API DescribeEventCountByThreatLevel: add param EndTime.
- Update API DescribeEventCountByThreatLevel: add param RoleFor.
- Update API DescribeEventCountByThreatLevel: add param RoleType.
- Update API DescribeEventCountByThreatLevel: add param StartTime.
- Update API DescribeEventDispose: add param RoleFor.
- Update API DescribeEventDispose: add param RoleType.
- Update API DescribeLogFields: add param RoleFor.
- Update API DescribeLogFields: add param RoleType.
- Update API DescribeLogSource: add param RoleFor.
- Update API DescribeLogSource: add param RoleType.
- Update API DescribeLogType: add param RoleFor.
- Update API DescribeLogType: add param RoleType.
- Update API DescribeOperators: add param RoleFor.
- Update API DescribeOperators: add param RoleType.
- Update API DescribeScopeUsers: add param RoleFor.
- Update API DescribeScopeUsers: add param RoleType.
- Update API DescribeScopeUsers: update response param.
- Update API DescribeStorage: add param RoleFor.
- Update API DescribeStorage: add param RoleType.
- Update API DescribeUserBuyStatus: update param SubUserId.
- Update API DescribeUserBuyStatus: update response param.
- Update API DescribeWafScope: add param RoleFor.
- Update API DescribeWafScope: add param RoleType.
- Update API DescribeWhiteRuleList: add param RoleFor.
- Update API DescribeWhiteRuleList: add param RoleType.
- Update API EnableAccessForCloudSiem: add param AutoSubmit.
- Update API EnableAccessForCloudSiem: add param RoleFor.
- Update API EnableAccessForCloudSiem: add param RoleType.
- Update API GetCapacity: add param RoleFor.
- Update API GetCapacity: add param RoleType.
- Update API GetStorage: add param RoleFor.
- Update API GetStorage: add param RoleType.
- Update API ListAccountsByLog: add param RoleFor.
- Update API ListAccountsByLog: add param RoleType.
- Update API ListAccountsByLog: update param CloudCode.
- Update API ListAccountsByLog: update param LogCodes.
- Update API ListAllProds: add param RoleFor.
- Update API ListAllProds: add param RoleType.
- Update API ListAutomateResponseConfigs: add param RoleFor.
- Update API ListAutomateResponseConfigs: add param RoleType.
- Update API ListAutomateResponseConfigs: update response param.
- Update API ListCloudSiemCustomizeRules: add param Order.
- Update API ListCloudSiemCustomizeRules: add param OrderField.
- Update API ListCloudSiemCustomizeRules: add param RoleFor.
- Update API ListCloudSiemCustomizeRules: add param RoleType.
- Update API ListCloudSiemCustomizeRules: update response param.
- Update API ListCloudSiemPredefinedRules: add param AttCk.
- Update API ListCloudSiemPredefinedRules: add param EventTransferType.
- Update API ListCloudSiemPredefinedRules: add param LogSource.
- Update API ListCloudSiemPredefinedRules: add param Order.
- Update API ListCloudSiemPredefinedRules: add param OrderField.
- Update API ListCloudSiemPredefinedRules: add param RoleFor.
- Update API ListCloudSiemPredefinedRules: add param RoleType.
- Update API ListCloudSiemPredefinedRules: update response param.
- Update API ListCustomizeRuleTestResult: add param RoleFor.
- Update API ListCustomizeRuleTestResult: add param RoleType.
- Update API ListDelivery: add param RoleFor.
- Update API ListDelivery: add param RoleType.
- Update API ListDisposeStrategy: add param RoleFor.
- Update API ListDisposeStrategy: add param RoleType.
- Update API ListImportedLogsByProd: add param RoleFor.
- Update API ListImportedLogsByProd: add param RoleType.
- Update API ListImportedLogsByProd: update param CloudCode.
- Update API ListImportedLogsByProd: update response param.
- Update API OpenDelivery: add param RoleFor.
- Update API OpenDelivery: add param RoleType.
- Update API PostAutomateResponseConfig: add param RoleFor.
- Update API PostAutomateResponseConfig: add param RoleType.
- Update API PostCustomizeRule: add param AttCk.
- Update API PostCustomizeRule: add param RoleFor.
- Update API PostCustomizeRule: add param RoleType.
- Update API PostCustomizeRule: update response param.
- Update API PostCustomizeRuleTest: add param RoleFor.
- Update API PostCustomizeRuleTest: add param RoleType.
- Update API PostEventDisposeAndWhiteruleList: add param RoleFor.
- Update API PostEventDisposeAndWhiteruleList: add param RoleType.
- Update API PostEventWhiteruleList: add param RoleFor.
- Update API PostEventWhiteruleList: add param RoleType.
- Update API PostFinishCustomizeRuleTest: add param RoleFor.
- Update API PostFinishCustomizeRuleTest: add param RoleType.
- Update API PostRuleStatusChange: add param RoleFor.
- Update API PostRuleStatusChange: add param RoleType.
- Update API RestoreCapacity: add param RoleFor.
- Update API RestoreCapacity: add param RoleType.
- Update API SetStorage: add param RoleFor.
- Update API SetStorage: add param RoleType.
- Update API UpdateAutomateResponseConfigStatus: add param RoleFor.
- Update API UpdateAutomateResponseConfigStatus: add param RoleType.
- Update API UpdateWhiteRuleList: add param RoleFor.
- Update API UpdateWhiteRuleList: add param RoleType.


2024-03-27 Version: 3.0.4
- Update API BatchJobCheck: update response param.
- Update API DescribeCloudSiemEventDetail: update response param.


2024-02-22 Version: 3.0.3
- Update API DescribeCloudSiemEventDetail: update response param.


2024-01-18 Version: 3.0.2
- Generated python 2022-06-16 for cloud-siem.

2023-12-14 Version: 3.0.1
- Generated python 2022-06-16 for cloud-siem.

2023-12-14 Version: 3.0.0
- Generated python 2022-06-16 for cloud-siem.

2023-12-11 Version: 2.3.0
- Generated python 2022-06-16 for cloud-siem.

2023-11-21 Version: 2.2.0
- Generated python 2022-06-16 for cloud-siem.

2023-11-15 Version: 2.1.0
- Generated python 2022-06-16 for cloud-siem.

2023-11-02 Version: 2.0.0
- Generated python 2022-06-16 for cloud-siem.

2023-03-06 Version: 1.0.0
- Get the capicity which cloud siem user used until yesterday.

