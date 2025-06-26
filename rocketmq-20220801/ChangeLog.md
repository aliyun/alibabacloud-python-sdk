2025-06-26 Version: 3.1.2
- Update API CreateDisasterRecoveryPlan: add request parameters body.instances.$.consumerGroupId.
- Update API GetDisasterRecoveryPlan: add response parameters Body.data.instances.$.consumerGroupId.
- Update API ListDisasterRecoveryPlans: add response parameters Body.data.list.$.instances.$.consumerGroupId.
- Update API UpdateDisasterRecoveryPlan: add request parameters body.instances.$.consumerGroupId.


2025-06-26 Version: 3.1.2
- Update API CreateDisasterRecoveryPlan: add request parameters body.instances.$.consumerGroupId.
- Update API GetDisasterRecoveryPlan: add response parameters Body.data.instances.$.consumerGroupId.
- Update API ListDisasterRecoveryPlans: add response parameters Body.data.list.$.instances.$.consumerGroupId.
- Update API UpdateDisasterRecoveryPlan: add request parameters body.instances.$.consumerGroupId.


2025-05-28 Version: 3.1.1
- Update API CreateConsumerGroup: add request parameters body.consumeRetryPolicy.fixedIntervalRetryTime.
- Update API GetConsumerGroup: add response parameters Body.data.consumeRetryPolicy.fixedIntervalRetryTime.
- Update API UpdateConsumerGroup: add request parameters body.consumeRetryPolicy.fixedIntervalRetryTime.


2025-04-15 Version: 3.1.0
- Support API CreateDisasterRecoveryPlan.
- Support API DeleteDisasterRecoveryItem.
- Support API GetDisasterRecoveryItem.
- Support API GetDisasterRecoveryPlan.
- Support API ListDisasterRecoveryCheckpoints.
- Support API ListDisasterRecoveryItems.
- Support API ListDisasterRecoveryPlans.
- Support API SyncDisasterRecoveryCheckpoint.
- Support API UpdateDisasterRecoveryItem.
- Support API UpdateDisasterRecoveryPlan.
- Update API ListConsumerGroupSubscriptions: add request parameters topicName.
- Update API ListConsumerGroupSubscriptions: add request The number of query or body parameters has changed from zero to many.


2025-02-19 Version: 3.0.0
- Support API GetInstanceAcl.
- Support API GetInstanceIpWhitelist.
- Update API AddDisasterRecoveryItem: update param body.
- Update API CreateInstance: update param body.
- Update API CreateInstanceAcl: update param body.
- Update API DeleteInstanceIpWhitelist: add param ipWhitelists.
- Update API DeleteInstanceIpWhitelist: update param ipWhitelist.
- Update API GetConsumerGroup: update param consumerGroupId.
- Update API GetConsumerGroup: update response param.
- Update API GetConsumerGroupLag: add param topicName.
- Update API GetInstanceAccount: update response param.
- Update API GetTrace: update response param.
- Update API ListInstanceAccount: update param pageNumber.
- Update API ListInstanceAccount: update param pageSize.
- Update API ListInstanceAcl: update param pageNumber.
- Update API ListInstanceAcl: update param pageSize.
- Update API ListInstanceIpWhitelist: update param pageNumber.
- Update API ListInstanceIpWhitelist: update param pageSize.
- Update API UpdateInstanceAccount: update param username.
- Update API UpdateInstanceAcl: update param body.


2024-12-31 Version: 2.1.0
- Support API DeleteDisasterRecoveryPlan.
- Support API ListMetricMeta.
- Support API StartDisasterRecoveryItem.
- Support API StopDisasterRecoveryItem.
- Update API GetConsumerGroupLag: update response param.


2024-12-31 Version: 2.1.0
- Support API DeleteDisasterRecoveryPlan.
- Support API ListMetricMeta.
- Support API StartDisasterRecoveryItem.
- Support API StopDisasterRecoveryItem.
- Update API GetConsumerGroupLag: update response param.


2024-12-26 Version: 2.0.0
- Support API AddDisasterRecoveryItem.
- Update API CreateConsumerGroup: update param body.
- Update API CreateInstance: update param body.
- Update API CreateTopic: update param body.
- Update API GetConsumerGroupLag: update response param.
- Update API GetInstance: update response param.
- Update API GetInstanceAccount: update response param.
- Update API GetTopic: update response param.
- Update API GetTrace: update response param.
- Update API ListConsumerGroups: update param pageNumber.
- Update API ListConsumerGroups: update param pageSize.
- Update API ListConsumerGroups: update response param.
- Update API ListInstances: add param storageSecretKey.
- Update API ListTopics: update response param.
- Update API UpdateConsumerGroup: update param body.
- Update API UpdateTopic: update param body.


2024-09-25 Version: 1.5.1
- Update API GetTrace: update param instanceId.
- Update API GetTrace: update param topicName.
- Update API GetTrace: update param messageId.
- Update API ListTraces: update param instanceId.
- Update API ListTraces: update param topicName.
- Update API ListTraces: update param endTime.
- Update API ListTraces: update param pageNumber.
- Update API ListTraces: update param pageSize.
- Update API ListTraces: update param queryType.
- Update API ListTraces: update param startTime.


2024-09-09 Version: 1.5.0
- Support API CreateInstanceAccount.
- Support API CreateInstanceAcl.
- Support API CreateInstanceIpWhitelist.
- Support API DeleteConsumerGroupSubscription.
- Support API DeleteInstanceAccount.
- Support API DeleteInstanceAcl.
- Support API DeleteInstanceIpWhitelist.
- Support API GetConsumerGroupLag.
- Support API GetConsumerGroupSubscription.
- Support API GetConsumerStack.
- Support API GetInstanceAccount.
- Support API GetMessageDetail.
- Support API GetTrace.
- Support API ListInstanceAccount.
- Support API ListInstanceAcl.
- Support API ListInstanceIpWhitelist.
- Support API ListMessages.
- Support API ListTagResources.
- Support API ListTraces.
- Support API TagResources.
- Support API UntagResources.
- Support API UpdateInstanceAccount.
- Support API UpdateInstanceAcl.
- Support API VerifyConsumeMessage.
- Support API VerifySendMessage.
- Update API ListConsumerGroupSubscriptions: update param consumerGroupId.
- Update API ListTopicSubscriptions: update param topicName.


2024-07-25 Version: 1.4.5
- Update API ListInstances: add param seriesCodes.


2024-07-03 Version: 1.4.4
- Update API CreateInstance: update param body.


2024-07-03 Version: 1.4.4
- Update API CreateInstance: update param body.


2024-05-31 Version: 1.4.3
- Update API ListInstances: update param pageNumber.
- Update API ListInstances: update param pageSize.


2024-05-28 Version: 1.4.2
- Update API GetInstance: update response param.
- Update API ListConsumerGroupSubscriptions: update response param.
- Update API ListTopicSubscriptions: update response param.


2024-03-29 Version: 1.4.1
- Update API GetInstance: update response param.
- Update API UpdateInstance: update param body.


2024-03-28 Version: 1.4.0
- Support API ListAvailableZones.
- Support API ListConsumerConnections.
- Support API ListRegions.
- Support API ListTopicSubscriptions.
- Update API ListTopics: update param pageNumber.
- Update API ListTopics: update param pageSize.


2024-02-27 Version: 1.3.0
- Support API ListAvailableZones.
- Support API ListConsumerConnections.
- Support API ListRegions.
- Support API ListTopicSubscriptions.


2024-02-21 Version: 1.2.0
- Support API ListAvailableZones.
- Support API ListRegions.


2023-10-09 Version: 1.1.2
- Generated python 2022-08-01 for RocketMQ.

2023-10-09 Version: 1.1.1
- Generated python 2022-08-01 for RocketMQ.

2023-09-28 Version: 1.1.0
- Generated python 2022-08-01 for RocketMQ.

2023-05-08 Version: 1.0.5
- Optimize some APIs.

2023-02-08 Version: 1.0.4
- Support Dead Letter.
- Support ResourceGroup.

2023-01-11 Version: 1.0.3
- Delete consumerGroupId from topic and group api.
- Support for Dead Letter.

2022-12-16 Version: 1.0.2
- Add CreateInstance api.
- Optimize GetInstance and UpdateInstance params and results.

2022-09-13 Version: 1.0.1
- Remove ResourceGroupId from api.

2022-08-04 Version: 1.0.0
- Init RocketMQ v5 OpenAPI.

