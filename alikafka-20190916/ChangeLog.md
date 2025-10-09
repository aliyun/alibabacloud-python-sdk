2025-10-09 Version: 2.13.1
- Update API GetConsumerProgress: add response parameters Body.ConsumerProgress.TopicList.$.OffsetList.$.Accumulate.


2025-08-18 Version: 2.13.0
- Support API FailoverTest.


2025-08-06 Version: 2.12.2
- Update API GetInstanceList: add response parameters Body.InstanceList.$.ConfluentInstanceComponents.


2025-07-24 Version: 2.12.1
- Update API GetInstanceList: add response parameters Body.InstanceList.$.RecommendedPartitionCount.


2025-07-15 Version: 2.12.0
- Support API GetRiskList.


2025-05-27 Version: 2.11.0
- Support API ListRebalanceInfo.


2025-04-23 Version: 2.10.2
- Update API GetConsumerProgress: add response parameters Body.ConsumerProgress.state.


2025-04-09 Version: 2.10.1
- Update API GetAllowedIpList: add response parameters Body.AllowedList.InternetList.$.BlackIPList.
- Update API GetAllowedIpList: add response parameters Body.AllowedList.InternetList.$.BlackIPMap.
- Update API GetAllowedIpList: add response parameters Body.AllowedList.InternetList.$.SecurityGroupId.
- Update API GetAllowedIpList: add response parameters Body.AllowedList.InternetList.$.UserDefinedSharedSecurityGroup.
- Update API GetAllowedIpList: add response parameters Body.AllowedList.VpcList.$.BlackIPList.
- Update API GetAllowedIpList: add response parameters Body.AllowedList.VpcList.$.BlackIPMap.
- Update API GetAllowedIpList: add response parameters Body.AllowedList.VpcList.$.SecurityGroupId.
- Update API GetAllowedIpList: add response parameters Body.AllowedList.VpcList.$.UserDefinedSharedSecurityGroup.


2025-02-12 Version: 2.10.0
- Support API DescribeAclResourceName.


2025-01-06 Version: 2.9.0
- Support API CreatePostPayInstance.
- Support API CreatePrePayInstance.
- Update API ConvertPostPayOrder: add param PaidType.
- Update API EnableAutoTopicCreation: add param UpdatePartition.
- Update API EnableAutoTopicCreation: update param Operate.
- Update API GetConsumerList: update response param.
- Update API GetConsumerProgress: update response param.
- Update API GetInstanceList: update response param.
- Update API UpgradePrePayOrder: update param DiskSize.


2024-11-25 Version: 2.8.1
- Update API GetInstanceList: update response param.


2024-11-15 Version: 2.8.0
- Support API GetKafkaClientIp.
- Update API GetInstanceList: update response param.


2024-08-02 Version: 2.7.2
- Update API GetConsumerProgress: add param HideLastTimestamp.
- Update API UpgradePrePayOrder: update response param.


2024-07-30 Version: 2.7.1
- Update API GetConsumerProgress: add param HideLastTimestamp.


2024-05-16 Version: 2.7.0
- Support API CreateScheduledScalingRule.
- Support API DeleteScheduledScalingRule.
- Support API GetAutoScalingConfiguration.
- Support API ModifyScheduledScalingRule.
- Update API CreatePrePayOrder: update param ConfluentConfig.
- Update API CreatePrePayOrder: update param DeployType.
- Update API CreatePrePayOrder: update param DiskSize.
- Update API CreatePrePayOrder: update param DiskType.
- Update API GetTopicList: update response param.


2024-04-23 Version: 2.6.6
- Update API CreatePostPayOrder: update param DiskSize.
- Update API CreatePostPayOrder: update param DiskType.
- Update API CreatePrePayOrder: update param ConfluentConfig.
- Update API GetInstanceList: add param Series.
- Update API GetInstanceList: update response param.
- Update API UpgradePrePayOrder: update param ConfluentConfig.


2024-04-11 Version: 2.6.5
- Update API CreatePostPayOrder: add param PaidType.
- Update API CreatePostPayOrder: add param ServerlessConfig.
- Update API CreatePostPayOrder: update param DiskSize.
- Update API CreatePostPayOrder: update param DiskType.
- Update API GetInstanceList: update response param.


2024-04-03 Version: 2.6.4
- Update API CreateAcl: add param AclOperationTypes.
- Update API CreateAcl: add param AclPermissionType.
- Update API CreateAcl: add param Host.
- Update API CreateAcl: update param AclOperationType.
- Update API CreateSaslUser: add param Mechanism.
- Update API DeleteAcl: add param AclOperationTypes.
- Update API DeleteAcl: add param AclPermissionType.
- Update API DeleteAcl: add param Host.
- Update API DeleteAcl: update param AclOperationType.
- Update API DeleteSaslUser: add param Mechanism.
- Update API DescribeAcls: add param AclOperationType.
- Update API DescribeAcls: add param AclPermissionType.
- Update API DescribeAcls: add param Host.
- Update API DescribeAcls: update response param.
- Update API DescribeSaslUsers: update response param.
- Update API GetConsumerProgress: update response param.


2024-03-25 Version: 2.6.2
- Update API GetInstanceList: update response param.


2024-03-20 Version: 2.6.1
- Update API CreatePrePayOrder: add param Duration.
- Update API CreatePrePayOrder: add param PaidType.
- Update API CreatePrePayOrder: update param DeployType.
- Update API CreatePrePayOrder: update param DiskSize.
- Update API CreatePrePayOrder: update param DiskType.
- Update API GetConsumerList: add param CurrentPage.
- Update API GetConsumerList: add param PageSize.
- Update API GetConsumerList: update response param.
- Update API UpgradePrePayOrder: update param DiskSize.
- Update API UpgradePrePayOrder: update param PaidType.


2024-03-15 Version: 2.6.0
- Support API EnableAutoGroupCreation.
- Support API EnableAutoTopicCreation.
- Support API GetTopicSubscribeStatus.
- Support API ReopenInstance.
- Support API StopInstance.
- Update API CreateAcl: update param AclResourceType.
- Update API CreatePrePayOrder: add param ConfluentConfig.
- Update API DeleteAcl: update param AclOperationType.
- Update API DeleteAcl: update param AclResourceType.
- Update API DescribeAcls: update param AclResourceType.
- Update API GetInstanceList: update response param.
- Update API StartInstance: add param VSwitchIds.
- Update API UpdateConsumerOffset: update param Time.
- Update API UpgradePostPayOrder: add param ServerlessConfig.
- Update API UpgradePostPayOrder: update param DiskSize.
- Update API UpgradePrePayOrder: add param ConfluentConfig.
- Update API UpgradePrePayOrder: add param PaidType.


2024-03-13 Version: 2.5.0
- Support API EnableAutoGroupCreation.
- Support API EnableAutoTopicCreation.
- Support API GetTopicSubscribeStatus.
- Update API CreateAcl: update param AclResourceType.
- Update API CreatePrePayOrder: add param ConfluentConfig.
- Update API DeleteAcl: update param AclOperationType.
- Update API DeleteAcl: update param AclResourceType.
- Update API DescribeAcls: update param AclResourceType.
- Update API GetInstanceList: update response param.
- Update API StartInstance: add param VSwitchIds.
- Update API UpgradePostPayOrder: add param ServerlessConfig.
- Update API UpgradePostPayOrder: update param DiskSize.
- Update API UpgradePrePayOrder: add param ConfluentConfig.
- Update API UpgradePrePayOrder: add param PaidType.


2024-03-01 Version: 2.4.0
- Support API EnableAutoGroupCreation.
- Support API EnableAutoTopicCreation.
- Support API GetTopicSubscribeStatus.
- Update API CreateAcl: update param AclResourceType.
- Update API CreatePrePayOrder: add param ConfluentConfig.
- Update API DeleteAcl: update param AclOperationType.
- Update API DeleteAcl: update param AclResourceType.
- Update API DescribeAcls: update param AclResourceType.
- Update API GetInstanceList: update response param.
- Update API StartInstance: add param VSwitchIds.
- Update API UpgradePostPayOrder: add param ServerlessConfig.
- Update API UpgradePostPayOrder: update param DiskSize.
- Update API UpgradePrePayOrder: add param ConfluentConfig.
- Update API UpgradePrePayOrder: add param PaidType.


2024-02-27 Version: 2.3.0
- Support API GetTopicSubscribeStatus.
- Update API CreateAcl: update param AclResourceType.
- Update API CreatePrePayOrder: add param ConfluentConfig.
- Update API DeleteAcl: update param AclOperationType.
- Update API DeleteAcl: update param AclResourceType.
- Update API DescribeAcls: update param AclResourceType.
- Update API GetInstanceList: update response param.
- Update API StartInstance: add param VSwitchIds.
- Update API UpgradePostPayOrder: add param ServerlessConfig.
- Update API UpgradePostPayOrder: update param DiskSize.
- Update API UpgradePrePayOrder: add param ConfluentConfig.
- Update API UpgradePrePayOrder: add param PaidType.


2024-02-27 Version: 2.2.0
- Support API GetTopicSubscribeStatus.
- Update API CreateAcl: update param AclResourceType.
- Update API DeleteAcl: update param AclOperationType.
- Update API DeleteAcl: update param AclResourceType.
- Update API DescribeAcls: update param AclResourceType.
- Update API UpgradePostPayOrder: add param ServerlessConfig.
- Update API UpgradePostPayOrder: update param DiskSize.


2024-02-26 Version: 2.1.1
- Update API CreateAcl: update param AclResourceType.
- Update API DeleteAcl: update param AclOperationType.
- Update API DeleteAcl: update param AclResourceType.
- Update API DescribeAcls: update param AclResourceType.
- Update API UpgradePostPayOrder: add param ServerlessConfig.
- Update API UpgradePostPayOrder: update param DiskSize.


2024-01-18 Version: 2.1.0
- Generated python 2019-09-16 for alikafka.

2023-10-09 Version: 2.0.12
- Generated python 2019-09-16 for alikafka.

2023-04-25 Version: 2.0.11
- Add UpdateConsumerOffset api.

2022-12-07 Version: 2.0.10
- Update Endpoint .

2022-11-18 Version: 2.0.9
- Add GetQuotaTip api.

2022-09-05 Version: 2.0.8
- Create and update order support to buy partition.

2022-08-31 Version: 2.0.7
- Create and update order support to buy partition.

2022-08-02 Version: 2.0.5
- TagResources add instanceId param.
- Add topic count, group count, partition count.

2022-07-27 Version: 2.0.4
- Supported new features.

2022-07-26 Version: 2.0.3
- TagResources add instanceId param.

2022-03-23 Version: 2.0.2
- Add GetAllInstanceId.

2022-02-16 Version: 2.0.1
- Support domain.
- Some params added.

2021-08-09 Version: 1.0.3
- Generated python 2019-09-16 for alikafka.

2021-08-09 Version: 0.0.1
- Add PartitionNum and other absent fields of GetTopicList API.

2021-03-17 Version: 1.0.2
- Generated python 2019-09-16 for alikafka.

2020-12-29 Version: 1.0.1
- AMP Version Change.

2020-12-28 Version: 1.0.0
- AMP Version Change.

