2025-04-23 Version: 3.0.13
- Update API ListAggregateConfigRuleEvaluationResults: add response parameters Body.EvaluationResults.EvaluationResultList.$.EvaluationId.
- Update API ListAggregateConfigRuleEvaluationResults: add response parameters Body.EvaluationResults.EvaluationResultList.$.LastNonCompliantRecordTimestamp.
- Update API ListAggregateResourceEvaluationResults: add response parameters Body.EvaluationResults.EvaluationResultList.$.EvaluationId.
- Update API ListAggregateResourceEvaluationResults: add response parameters Body.EvaluationResults.EvaluationResultList.$.LastNonCompliantRecordTimestamp.
- Update API ListConfigRuleEvaluationResults: add response parameters Body.EvaluationResults.EvaluationResultList.$.EvaluationId.
- Update API ListConfigRuleEvaluationResults: add response parameters Body.EvaluationResults.EvaluationResultList.$.LastNonCompliantRecordTimestamp.
- Update API ListResourceEvaluationResults: add response parameters Body.EvaluationResults.EvaluationResultList.$.EvaluationId.
- Update API ListResourceEvaluationResults: add response parameters Body.EvaluationResults.EvaluationResultList.$.LastNonCompliantRecordTimestamp.


2025-04-03 Version: 3.0.12
- Update API CreateAggregateConfigRule: add request parameters ResourceNameScope.
- Update API CreateConfigRule: add request parameters ResourceNameScope.
- Update API GetAggregateConfigRule: add response parameters Body.ConfigRule.ResourceNameScope.
- Update API GetConfigRule: add response parameters Body.ConfigRule.ResourceNameScope.
- Update API ListManagedRules: add request parameters FilterType.
- Update API UpdateAggregateConfigRule: add request parameters ResourceNameScope.
- Update API UpdateAggregator: add request parameters FolderId.
- Update API UpdateConfigRule: add request parameters ResourceNameScope.


2025-01-21 Version: 3.0.11
- Update API CreateAggregateCompliancePack: add param Tag.
- Update API CreateAggregateConfigRule: add param Tag.
- Update API CreateAggregator: add param Tag.
- Update API CreateCompliancePack: add param Tag.
- Update API GetAggregateCompliancePack: add param Tag.
- Update API GetAggregateCompliancePack: update response param.
- Update API GetAggregator: add param Tag.
- Update API GetAggregator: update response param.
- Update API GetCompliancePack: add param Tag.
- Update API GetCompliancePack: update response param.
- Update API ListAggregateCompliancePacks: add param Tag.
- Update API ListAggregateCompliancePacks: update response param.
- Update API ListAggregateConfigRules: add param Tag.
- Update API ListAggregators: add param Tag.
- Update API ListAggregators: update response param.
- Update API ListCompliancePacks: add param Tag.
- Update API ListCompliancePacks: update response param.
- Update API UpdateAggregateCompliancePack: add param Tag.
- Update API UpdateAggregateConfigRule: add param Tag.
- Update API UpdateAggregator: add param Tag.
- Update API UpdateCompliancePack: add param Tag.


2025-01-20 Version: 3.0.10
- Update API EvaluatePreConfigRules: add param ResourceTypeFormat.
- Update API EvaluatePreConfigRules: update param EnableManagedRules.


2025-01-15 Version: 3.0.9
- Update API ActiveAggregateConfigRules: add param CompliancePackId.
- Update API ActiveAggregateConfigRules: update param ConfigRuleIds.
- Update API ActiveConfigRules: add param CompliancePackId.
- Update API ActiveConfigRules: update param ConfigRuleIds.
- Update API CreateAggregateConfigRule: add param ExtendContent.
- Update API CreateConfigRule: add param ExtendContent.
- Update API CreateConfigRule: add param Tag.
- Update API DeactiveAggregateConfigRules: add param CompliancePackId.
- Update API DeactiveAggregateConfigRules: update param ConfigRuleIds.
- Update API DeactiveConfigRules: add param CompliancePackId.
- Update API DeactiveConfigRules: update param ConfigRuleIds.
- Update API GetAggregateConfigRule: add param Tag.
- Update API GetAggregateConfigRule: update response param.
- Update API GetAggregator: update response param.
- Update API GetConfigRule: add param Tag.
- Update API GetConfigRule: update response param.
- Update API GetIntegratedServiceStatus: update response param.
- Update API ListAggregateConfigRules: add param CompliancePackId.
- Update API ListAggregateConfigRules: update param Keyword.
- Update API ListConfigRules: add param CompliancePackId.
- Update API ListConfigRules: add param Tag.
- Update API ListConfigRules: update param Keyword.
- Update API ListIntegratedService: update response param.
- Update API UpdateConfigRule: add param ExtendContent.
- Update API UpdateConfigRule: add param Tag.
- Update API UpdateIntegratedServiceStatus: add param AggregatorDeliveryDataType.


2024-08-29 Version: 3.0.8
- Update API ListAggregateDiscoveredResources: add param EndUpdateTimestamp.
- Update API ListAggregateDiscoveredResources: add param ExcludeResourceTypes.
- Update API ListAggregateDiscoveredResources: add param StartUpdateTimestamp.
- Update API ListAggregateDiscoveredResources: update response param.
- Update API ListDiscoveredResources: add param EndUpdateTimestamp.
- Update API ListDiscoveredResources: add param ExcludeResourceTypes.
- Update API ListDiscoveredResources: add param StartUpdateTimestamp.
- Update API ListDiscoveredResources: update param MaxResults.
- Update API ListDiscoveredResources: update response param.


2024-08-07 Version: 3.0.7
- Generated python 2020-09-07 for Config.

2024-08-07 Version: 3.0.7
- Generated python 2020-09-07 for Config.

2024-08-01 Version: 3.0.6
- Update API CreateAggregateConfigDeliveryChannel: add param CompliantSnapshot.
- Update API CreateAggregateConfigRule: update param ExcludeTagsScope.
- Update API CreateAggregateConfigRule: update param TagsScope.
- Update API CreateConfigDeliveryChannel: add param CompliantSnapshot.
- Update API GetAggregateConfigDeliveryChannel: update response param.
- Update API GetConfigDeliveryChannel: update response param.
- Update API ListAggregateConfigDeliveryChannels: update response param.
- Update API ListConfigDeliveryChannels: update response param.
- Update API UpdateAggregateConfigDeliveryChannel: add param CompliantSnapshot.
- Update API UpdateConfigDeliveryChannel: add param CompliantSnapshot.


2024-06-19 Version: 3.0.5
- Update API CreateAggregateCompliancePack: add param ExcludeRegionIdsScope.
- Update API CreateAggregateCompliancePack: add param ExcludeResourceGroupIdsScope.
- Update API CreateAggregateCompliancePack: add param ExcludeTagsScope.
- Update API CreateAggregateCompliancePack: add param ResourceIdsScope.
- Update API CreateAggregateCompliancePack: add param TagsScope.
- Update API CreateAggregateConfigRule: add param AccountIdsScope.
- Update API CreateAggregateConfigRule: add param ExcludeRegionIdsScope.
- Update API CreateAggregateConfigRule: add param ExcludeResourceGroupIdsScope.
- Update API CreateAggregateConfigRule: add param ExcludeTagsScope.
- Update API CreateAggregateConfigRule: add param ResourceIdsScope.
- Update API CreateAggregateConfigRule: add param TagsScope.
- Update API CreateAggregateConfigRule: update param ClientToken.
- Update API CreateAggregateConfigRule: update param Description.
- Update API CreateAggregateConfigRule: update param ExcludeResourceIdsScope.
- Update API CreateAggregateConfigRule: update param InputParameters.
- Update API CreateAggregateConfigRule: update param MaximumExecutionFrequency.
- Update API CreateAggregateConfigRule: update param RegionIdsScope.
- Update API CreateAggregateConfigRule: update param ResourceGroupIdsScope.
- Update API CreateAggregateConfigRule: update param TagKeyLogicScope.
- Update API CreateAggregateConfigRule: update param TagKeyScope.
- Update API CreateAggregateConfigRule: update param TagValueScope.
- Update API CreateAggregateConfigRule: update response param.
- Update API CreateCompliancePack: add param ExcludeRegionIdsScope.
- Update API CreateCompliancePack: add param ExcludeResourceGroupIdsScope.
- Update API CreateCompliancePack: add param ExcludeTagsScope.
- Update API CreateCompliancePack: add param ResourceIdsScope.
- Update API CreateCompliancePack: add param TagsScope.
- Update API CreateConfigRule: add param ExcludeRegionIdsScope.
- Update API CreateConfigRule: add param ExcludeResourceGroupIdsScope.
- Update API CreateConfigRule: add param ExcludeTagsScope.
- Update API CreateConfigRule: add param ResourceIdsScope.
- Update API CreateConfigRule: add param TagsScope.
- Update API GetAggregateCompliancePack: update response param.
- Update API GetAggregateConfigRule: update response param.
- Update API GetCompliancePack: update response param.
- Update API GetConfigRule: update response param.
- Update API UpdateAggregateCompliancePack: add param ExcludeRegionIdsScope.
- Update API UpdateAggregateCompliancePack: add param ExcludeResourceGroupIdsScope.
- Update API UpdateAggregateCompliancePack: add param ExcludeTagsScope.
- Update API UpdateAggregateCompliancePack: add param ResourceIdsScope.
- Update API UpdateAggregateCompliancePack: add param TagsScope.
- Update API UpdateAggregateCompliancePack: update param ClientToken.
- Update API UpdateAggregateCompliancePack: update param ConfigRules.
- Update API UpdateAggregateCompliancePack: update param Description.
- Update API UpdateAggregateCompliancePack: update param ExcludeResourceIdsScope.
- Update API UpdateAggregateCompliancePack: update param RegionIdsScope.
- Update API UpdateAggregateCompliancePack: update param ResourceGroupIdsScope.
- Update API UpdateAggregateCompliancePack: update param RiskLevel.
- Update API UpdateAggregateCompliancePack: update param TagKeyScope.
- Update API UpdateAggregateCompliancePack: update param TagValueScope.
- Update API UpdateAggregateCompliancePack: update response param.
- Update API UpdateAggregateConfigRule: add param AccountIdsScope.
- Update API UpdateAggregateConfigRule: add param ExcludeRegionIdsScope.
- Update API UpdateAggregateConfigRule: add param ExcludeResourceGroupIdsScope.
- Update API UpdateAggregateConfigRule: add param ExcludeTagsScope.
- Update API UpdateAggregateConfigRule: add param ResourceIdsScope.
- Update API UpdateAggregateConfigRule: add param TagsScope.
- Update API UpdateAggregateConfigRule: update param ClientToken.
- Update API UpdateAggregateConfigRule: update param ConfigRuleTriggerTypes.
- Update API UpdateAggregateConfigRule: update param Description.
- Update API UpdateAggregateConfigRule: update param ExcludeResourceIdsScope.
- Update API UpdateAggregateConfigRule: update param InputParameters.
- Update API UpdateAggregateConfigRule: update param MaximumExecutionFrequency.
- Update API UpdateAggregateConfigRule: update param RegionIdsScope.
- Update API UpdateAggregateConfigRule: update param ResourceGroupIdsScope.
- Update API UpdateAggregateConfigRule: update param ResourceTypesScope.
- Update API UpdateAggregateConfigRule: update param RiskLevel.
- Update API UpdateAggregateConfigRule: update param TagKeyLogicScope.
- Update API UpdateAggregateConfigRule: update param TagKeyScope.
- Update API UpdateAggregateConfigRule: update param TagValueScope.
- Update API UpdateAggregateConfigRule: update response param.
- Update API UpdateCompliancePack: add param ExcludeRegionIdsScope.
- Update API UpdateCompliancePack: add param ExcludeResourceGroupIdsScope.
- Update API UpdateCompliancePack: add param ExcludeTagsScope.
- Update API UpdateCompliancePack: add param ResourceIdsScope.
- Update API UpdateCompliancePack: add param TagsScope.
- Update API UpdateCompliancePack: update param ClientToken.
- Update API UpdateCompliancePack: update param ConfigRules.
- Update API UpdateCompliancePack: update param Description.
- Update API UpdateCompliancePack: update param ExcludeResourceIdsScope.
- Update API UpdateCompliancePack: update param RegionIdsScope.
- Update API UpdateCompliancePack: update param ResourceGroupIdsScope.
- Update API UpdateCompliancePack: update param RiskLevel.
- Update API UpdateCompliancePack: update param TagKeyScope.
- Update API UpdateCompliancePack: update param TagValueScope.
- Update API UpdateCompliancePack: update response param.
- Update API UpdateConfigRule: add param ExcludeRegionIdsScope.
- Update API UpdateConfigRule: add param ExcludeResourceGroupIdsScope.
- Update API UpdateConfigRule: add param ExcludeTagsScope.
- Update API UpdateConfigRule: add param ResourceIdsScope.
- Update API UpdateConfigRule: add param TagsScope.
- Update API UpdateConfigRule: update param ClientToken.
- Update API UpdateConfigRule: update param ConfigRuleTriggerTypes.
- Update API UpdateConfigRule: update param Description.
- Update API UpdateConfigRule: update param ExcludeResourceIdsScope.
- Update API UpdateConfigRule: update param InputParameters.
- Update API UpdateConfigRule: update param MaximumExecutionFrequency.
- Update API UpdateConfigRule: update param RegionIdsScope.
- Update API UpdateConfigRule: update param ResourceGroupIdsScope.
- Update API UpdateConfigRule: update param ResourceTypesScope.
- Update API UpdateConfigRule: update param RiskLevel.
- Update API UpdateConfigRule: update param TagKeyLogicScope.
- Update API UpdateConfigRule: update param TagKeyScope.
- Update API UpdateConfigRule: update param TagValueScope.
- Update API UpdateConfigRule: update response param.


2024-06-12 Version: 3.0.4
- Update API GenerateAggregateResourceInventory: add param ResourceDeleted.
- Update API GenerateAggregateResourceInventory: update response param.
- Update API GenerateResourceInventory: add param ResourceDeleted.
- Update API GenerateResourceInventory: update response param.
- Update API GetAggregateDiscoveredResource: add param ComplianceOption.
- Update API GetAggregateDiscoveredResource: update param ResourceOwnerId.
- Update API GetAggregateDiscoveredResource: update response param.
- Update API GetAggregateResourceComplianceByConfigRule: update param ComplianceType.
- Update API GetAggregateResourceComplianceByConfigRule: update response param.
- Update API GetDiscoveredResource: add param ComplianceOption.
- Update API GetDiscoveredResource: update param Region.
- Update API GetDiscoveredResource: update response param.
- Update API GetResourceComplianceGroupByRegion: update param ConfigRuleIds.
- Update API GetResourceComplianceGroupByRegion: update response param.
- Update API ListAggregateConfigRuleEvaluationResults: update param CompliancePackId.
- Update API ListAggregateConfigRuleEvaluationResults: update param ComplianceType.
- Update API ListAggregateConfigRuleEvaluationResults: update param ConfigRuleId.
- Update API ListAggregateConfigRuleEvaluationResults: update param MaxResults.
- Update API ListAggregateConfigRuleEvaluationResults: update param NextToken.
- Update API ListAggregateConfigRuleEvaluationResults: update param ResourceOwnerId.
- Update API ListAggregateConfigRuleEvaluationResults: update response param.
- Update API ListAggregateRemediationExecutions: update param ConfigRuleId.
- Update API ListAggregateRemediationExecutions: update param ExecutionStatus.
- Update API ListAggregateRemediationExecutions: update param MaxResults.
- Update API ListAggregateRemediationExecutions: update param NextToken.
- Update API ListConfigRuleEvaluationResults: update param CompliancePackId.
- Update API ListConfigRuleEvaluationResults: update param ComplianceType.
- Update API ListConfigRuleEvaluationResults: update param ConfigRuleId.
- Update API ListConfigRuleEvaluationResults: update param MaxResults.
- Update API ListConfigRuleEvaluationResults: update param NextToken.
- Update API ListConfigRuleEvaluationResults: update response param.
- Update API ListRemediationExecutions: update param ConfigRuleId.
- Update API ListRemediationExecutions: update param ExecutionStatus.
- Update API ListRemediationExecutions: update param MaxResults.
- Update API ListRemediationExecutions: update param NextToken.
- Update API ListRemediationExecutions: update response param.


2024-06-12 Version: 3.0.4
- Update API GenerateAggregateResourceInventory: add param ResourceDeleted.
- Update API GenerateAggregateResourceInventory: update response param.
- Update API GenerateResourceInventory: add param ResourceDeleted.
- Update API GenerateResourceInventory: update response param.
- Update API GetAggregateDiscoveredResource: add param ComplianceOption.
- Update API GetAggregateDiscoveredResource: update param ResourceOwnerId.
- Update API GetAggregateDiscoveredResource: update response param.
- Update API GetAggregateResourceComplianceByConfigRule: update param ComplianceType.
- Update API GetAggregateResourceComplianceByConfigRule: update response param.
- Update API GetDiscoveredResource: add param ComplianceOption.
- Update API GetDiscoveredResource: update param Region.
- Update API GetDiscoveredResource: update response param.
- Update API GetResourceComplianceGroupByRegion: update param ConfigRuleIds.
- Update API GetResourceComplianceGroupByRegion: update response param.
- Update API ListAggregateConfigRuleEvaluationResults: update param CompliancePackId.
- Update API ListAggregateConfigRuleEvaluationResults: update param ComplianceType.
- Update API ListAggregateConfigRuleEvaluationResults: update param ConfigRuleId.
- Update API ListAggregateConfigRuleEvaluationResults: update param MaxResults.
- Update API ListAggregateConfigRuleEvaluationResults: update param NextToken.
- Update API ListAggregateConfigRuleEvaluationResults: update param ResourceOwnerId.
- Update API ListAggregateConfigRuleEvaluationResults: update response param.
- Update API ListAggregateRemediationExecutions: update param ConfigRuleId.
- Update API ListAggregateRemediationExecutions: update param ExecutionStatus.
- Update API ListAggregateRemediationExecutions: update param MaxResults.
- Update API ListAggregateRemediationExecutions: update param NextToken.
- Update API ListConfigRuleEvaluationResults: update param CompliancePackId.
- Update API ListConfigRuleEvaluationResults: update param ComplianceType.
- Update API ListConfigRuleEvaluationResults: update param ConfigRuleId.
- Update API ListConfigRuleEvaluationResults: update param MaxResults.
- Update API ListConfigRuleEvaluationResults: update param NextToken.
- Update API ListConfigRuleEvaluationResults: update response param.
- Update API ListRemediationExecutions: update param ConfigRuleId.
- Update API ListRemediationExecutions: update param ExecutionStatus.
- Update API ListRemediationExecutions: update param MaxResults.
- Update API ListRemediationExecutions: update param NextToken.
- Update API ListRemediationExecutions: update response param.


2024-01-29 Version: 3.0.3
- Update API CreateAggregateCompliancePackupdate ClientToken param.
update CompliancePackTemplateId param.
update ConfigRules param.
update Description param.
update ExcludeResourceIdsScope param.
update RegionIdsScope param.
update ResourceGroupIdsScope param.
update RiskLevel param.
update TagKeyScope param.
update TagValueScope param.
update response param.
- Update API CreateAggregatoradd FolderId param.
update AggregatorAccounts param.
update AggregatorName param.
update AggregatorType param.
update ClientToken param.
update Description param.
update response param.
- Update API CreateCompliancePackupdate ClientToken param.
update CompliancePackTemplateId param.
update ConfigRules param.
update Description param.
update ExcludeResourceIdsScope param.
update RegionIdsScope param.
update ResourceGroupIdsScope param.
update RiskLevel param.
update TagKeyScope param.
update TagValueScope param.
update response param.
- Update API CreateConfigRuleupdate ClientToken param.
update Description param.
update ExcludeResourceIdsScope param.
update InputParameters param.
update MaximumExecutionFrequency param.
update RegionIdsScope param.
update ResourceGroupIdsScope param.
update RiskLevel param.
update TagKeyLogicScope param.
update TagKeyScope param.
update TagValueScope param.
update response param.
- Update API GetAggregatorupdate AggregatorId param.
update response param.
- Update API GetConfigRuleupdate response param.
- Update API GetRemediationTemplateupdate TemplateIdentifier param.
update response param.
- Update API GetResourceComplianceByConfigRuleupdate ComplianceType param.
update response param.
- Update API ListAggregatorsupdate MaxResults param.
update NextToken param.
update response param.
- Update API ListConfigRulesupdate ComplianceType param.
update ConfigRuleName param.
update ConfigRuleState param.
update PageNumber param.
update PageSize param.
update RiskLevel param.
update response param.
- Update API PutEvaluationsupdate DeleteMode param.
update Evaluations param.
update response param.


2023-12-13 Version: 3.0.2
- Generated python 2020-09-07 for Config.

2023-11-06 Version: 3.0.1
- Generated python 2020-09-07 for Config.

2023-09-01 Version: 3.0.0
- Generated python 2020-09-07 for Config.

2023-08-21 Version: 2.4.0
- Generated python 2020-09-07 for Config.

2023-08-09 Version: 2.3.0
- Generated python 2020-09-07 for Config.

2023-07-25 Version: 2.2.9
- Fix some problems.

2023-04-26 Version: 2.2.8
- Publish resource relations api.

2023-04-12 Version: 2.2.7
- Fix resourceOwnerId param.

2022-12-27 Version: 2.2.3
- Open Integrated Api.

2022-11-29 Version: 2.2.2
- Support ListRemediationExecutions.

2022-11-02 Version: 2.2.1
- Fix ListManagedRules bugs.

2022-08-12 Version: 2.1.9
- Fix ListManagedRules bugs.

2022-08-12 Version: 2.1.7
- Fix ListManagedRules bugs.

2022-07-21 Version: 2.1.5
- Support PreConfigRule.

2022-06-22 Version: 2.1.3
- Fix bugs.

2022-05-31 Version: 2.1.2
- Support aggregator delivery.

2022-02-23 Version: 2.1.1
- Support remediation.

2022-01-12 Version: 2.0.9
- Support folder for rule.

2021-12-28 Version: 2.0.7
- Support managed rule query.

2021-12-23 Version: 2.0.6
- Fix array params.

2021-12-21 Version: 2.0.5
- Fix array params.

2021-12-13 Version: 2.0.3
- Support query resourceType.

2021-11-20 Version: 2.0.2
- Support custom compliance pack.

2021-09-29 Version: 2.0.1
- Support custom compliance pack.

2021-09-23 Version: 2.0.0
- Add config integrated service batch query interface.

2021-08-25 Version: 1.0.0
- AMP version.

