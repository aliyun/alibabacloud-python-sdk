2025-08-05 Version: 7.0.0
- Update API ListEventStreamings: delete response parameters Body.Data.EventStreamings.$.RunOptions.RetryStrategy.MaximumEventAgeInSeconds.
- Update API ListEventStreamings: delete response parameters Body.Data.EventStreamings.$.RunOptions.RetryStrategy.MaximumRetryAttempts.


2025-06-19 Version: 6.2.2
- Update API DiscoverEventSource: add response parameters Body.Data.SourceMySQLDiscovery.EstimatedRows.
- Update API DiscoverEventSource: add response parameters Body.Data.SourceMySQLDiscovery.ExpireLogsDays.
- Update API DiscoverEventSource: add response parameters Body.Data.SourceMySQLDiscovery.WaitTimeout.


2025-06-18 Version: 6.2.1
- Update API CreateEventStreaming: add request parameters RunOptions.BusinessOption.
- Update API CreateEventStreaming: add request parameters Sink.SinkDorisParameters.
- Update API GetEventStreaming: add response parameters Body.Data.RunOptions.BusinessOption.
- Update API GetEventStreaming: add response parameters Body.Data.Sink.SinkDorisParameters.
- Update API ListEventStreamings: add response parameters Body.Data.EventStreamings.$.RunOptions.BusinessOption.
- Update API ListEventStreamings: add response parameters Body.Data.EventStreamings.$.Sink.SinkDorisParameters.
- Update API UpdateEventStreaming: add request parameters RunOptions.BusinessOption.
- Update API UpdateEventStreaming: add request parameters Sink.SinkDorisParameters.


2025-05-27 Version: 6.2.0
- Support API DiscoverEventSource.
- Support API TestEventSourceConfig.


2025-05-27 Version: 6.1.2
- Generated python 2020-04-01 for eventbridge.

2025-05-27 Version: 6.1.1
- Update API CreateEventStreaming: add request parameters RunOptions.Throttling.
- Update API CreateRule: add request parameters EventTargets.$.DeadLetterQueue.Network.
- Update API CreateRule: add request parameters EventTargets.$.DeadLetterQueue.SecurityGroupId.
- Update API CreateRule: add request parameters EventTargets.$.DeadLetterQueue.VSwitchIds.
- Update API CreateRule: add request parameters EventTargets.$.DeadLetterQueue.VpcId.
- Update API GetEventStreaming: add response parameters Body.Data.RunOptions.Throttling.
- Update API GetRule: add response parameters Body.Data.Targets.$.DeadLetterQueue.Network.
- Update API GetRule: add response parameters Body.Data.Targets.$.DeadLetterQueue.SecurityGroupId.
- Update API GetRule: add response parameters Body.Data.Targets.$.DeadLetterQueue.VSwitchIds.
- Update API GetRule: add response parameters Body.Data.Targets.$.DeadLetterQueue.VpcId.
- Update API ListEventStreamings: add response parameters Body.Data.EventStreamings.$.RunOptions.Throttling.
- Update API PutTargets: add request parameters Targets.$.DeadLetterQueue.Network.
- Update API PutTargets: add request parameters Targets.$.DeadLetterQueue.SecurityGroupId.
- Update API PutTargets: add request parameters Targets.$.DeadLetterQueue.VSwitchIds.
- Update API PutTargets: add request parameters Targets.$.DeadLetterQueue.VpcId.
- Update API UpdateEventStreaming: add request parameters RunOptions.Throttling.


2025-04-25 Version: 6.1.0
- Support API CheckServiceLinkedRoleForProduct.
- Update API CreateEventStreaming: add request parameters Sink.SinkBaiLianParameters.
- Update API CreateEventStreaming: add request parameters Source.SourceMySQLParameters.
- Update API GetEventStreaming: add response parameters Body.Data.Sink.SinkBaiLianParameters.
- Update API GetEventStreaming: add response parameters Body.Data.Source.SourceMySQLParameters.
- Update API ListEventStreamings: add response parameters Body.Data.EventStreamings.$.Sink.SinkBaiLianParameters.
- Update API ListEventStreamings: add response parameters Body.Data.EventStreamings.$.Source.SourceMySQLParameters.
- Update API UpdateEventStreaming: add request parameters Sink.SinkBaiLianParameters.
- Update API UpdateEventStreaming: add request parameters Source.SourceMySQLParameters.


2025-04-15 Version: 6.0.0
- Update API CreateEventStreaming: add request parameters Tags.
- Update API CreateEventStreaming: add request parameters RunOptions.DeadLetterQueue.Network.
- Update API CreateEventStreaming: add request parameters RunOptions.DeadLetterQueue.SecurityGroupId.
- Update API CreateEventStreaming: add request parameters RunOptions.DeadLetterQueue.VSwitchIds.
- Update API CreateEventStreaming: add request parameters RunOptions.DeadLetterQueue.VpcId.
- Update API CreateEventStreaming: add request parameters Sink.SinkKafkaParameters.Headers.
- Update API CreateEventStreaming: add request parameters Sink.SinkOpenSourceRabbitMQParameters.AuthType.
- Update API CreateEventStreaming: add request parameters Source.SourceOpenSourceRabbitMQParameters.AuthType.
- Update API CreateEventStreaming: update request parameters Sink.SinkOpenSourceRabbitMQParameters.Exchange' type has changed.
- Update API CreateEventStreaming: delete request parameters Sink.SinkOpenSourceRabbitMQParameters.Exchange.
- Update API CreateEventStreaming: update request parameters Sink.SinkOpenSourceRabbitMQParameters.QueueName' type has changed.
- Update API CreateEventStreaming: delete request parameters Sink.SinkOpenSourceRabbitMQParameters.QueueName.
- Update API GetEventStreaming: add response parameters Body.Data.RunOptions.DeadLetterQueue.Network.
- Update API GetEventStreaming: add response parameters Body.Data.RunOptions.DeadLetterQueue.SecurityGroupId.
- Update API GetEventStreaming: add response parameters Body.Data.RunOptions.DeadLetterQueue.VSwitchIds.
- Update API GetEventStreaming: add response parameters Body.Data.RunOptions.DeadLetterQueue.VpcId.
- Update API GetEventStreaming: add response parameters Body.Data.Sink.SinkKafkaParameters.Headers.
- Update API GetEventStreaming: add response parameters Body.Data.Sink.SinkOpenSourceRabbitMQParameters.AuthType.
- Update API GetEventStreaming: add response parameters Body.Data.Source.SourceOpenSourceRabbitMQParameters.AuthType.
- Update API GetEventStreaming: update response parameters Body.Data.Sink.SinkOpenSourceRabbitMQParameters.NetworkType' type has changed.
- Update API GetEventStreaming: delete response parameters Body.Data.Sink.SinkOpenSourceRabbitMQParameters.NetworkType.
- Update API GetEventStreaming: update response parameters Body.Data.Sink.SinkOpenSourceRabbitMQParameters.SecurityGroupId' type has changed.
- Update API GetEventStreaming: delete response parameters Body.Data.Sink.SinkOpenSourceRabbitMQParameters.SecurityGroupId.
- Update API GetEventStreaming: update response parameters Body.Data.Sink.SinkOpenSourceRabbitMQParameters.VSwitchIds' type has changed.
- Update API GetEventStreaming: delete response parameters Body.Data.Sink.SinkOpenSourceRabbitMQParameters.VSwitchIds.
- Update API GetEventStreaming: update response parameters Body.Data.Sink.SinkOpenSourceRabbitMQParameters.VpcId' type has changed.
- Update API GetEventStreaming: delete response parameters Body.Data.Sink.SinkOpenSourceRabbitMQParameters.VpcId.
- Update API ListEventStreamings: add request parameters Tags.
- Update API ListEventStreamings: add response parameters Body.Data.EventStreamings.$.RunOptions.DeadLetterQueue.Network.
- Update API ListEventStreamings: add response parameters Body.Data.EventStreamings.$.RunOptions.DeadLetterQueue.SecurityGroupId.
- Update API ListEventStreamings: add response parameters Body.Data.EventStreamings.$.RunOptions.DeadLetterQueue.VSwitchIds.
- Update API ListEventStreamings: add response parameters Body.Data.EventStreamings.$.RunOptions.DeadLetterQueue.VpcId.
- Update API ListEventStreamings: add response parameters Body.Data.EventStreamings.$.Sink.SinkOpenSourceRabbitMQParameters.AuthType.
- Update API ListEventStreamings: add response parameters Body.Data.EventStreamings.$.Source.SourceOpenSourceRabbitMQParameters.AuthType.
- Update API ListEventStreamings: update response parameters Body.Data.EventStreamings.$.Sink.SinkOpenSourceRabbitMQParameters.Exchange' type has changed.
- Update API ListEventStreamings: delete response parameters Body.Data.EventStreamings.$.Sink.SinkOpenSourceRabbitMQParameters.Exchange.
- Update API ListEventStreamings: update response parameters Body.Data.EventStreamings.$.Sink.SinkOpenSourceRabbitMQParameters.NetworkType' type has changed.
- Update API ListEventStreamings: delete response parameters Body.Data.EventStreamings.$.Sink.SinkOpenSourceRabbitMQParameters.NetworkType.
- Update API ListEventStreamings: update response parameters Body.Data.EventStreamings.$.Sink.SinkOpenSourceRabbitMQParameters.QueueName' type has changed.
- Update API ListEventStreamings: delete response parameters Body.Data.EventStreamings.$.Sink.SinkOpenSourceRabbitMQParameters.QueueName.
- Update API ListEventStreamings: update response parameters Body.Data.EventStreamings.$.Sink.SinkOpenSourceRabbitMQParameters.SecurityGroupId' type has changed.
- Update API ListEventStreamings: delete response parameters Body.Data.EventStreamings.$.Sink.SinkOpenSourceRabbitMQParameters.SecurityGroupId.
- Update API ListEventStreamings: update response parameters Body.Data.EventStreamings.$.Sink.SinkOpenSourceRabbitMQParameters.VSwitchIds' type has changed.
- Update API ListEventStreamings: delete response parameters Body.Data.EventStreamings.$.Sink.SinkOpenSourceRabbitMQParameters.VSwitchIds.
- Update API ListEventStreamings: update response parameters Body.Data.EventStreamings.$.Sink.SinkOpenSourceRabbitMQParameters.VpcId' type has changed.
- Update API ListEventStreamings: delete response parameters Body.Data.EventStreamings.$.Sink.SinkOpenSourceRabbitMQParameters.VpcId.
- Update API UpdateEventStreaming: add request parameters RunOptions.DeadLetterQueue.Network.
- Update API UpdateEventStreaming: add request parameters RunOptions.DeadLetterQueue.SecurityGroupId.
- Update API UpdateEventStreaming: add request parameters RunOptions.DeadLetterQueue.VSwitchIds.
- Update API UpdateEventStreaming: add request parameters RunOptions.DeadLetterQueue.VpcId.
- Update API UpdateEventStreaming: add request parameters Sink.SinkOpenSourceRabbitMQParameters.
- Update API UpdateEventStreaming: add request parameters Sink.SinkKafkaParameters.Headers.
- Update API UpdateEventStreaming: add request parameters Source.SourceOpenSourceRabbitMQParameters.


2025-03-03 Version: 5.0.1
- Update API CreateEventStreaming: update param Sink.
- Update API CreateEventStreaming: update param Source.
- Update API ListEventStreamings: update response param.
- Update API UpdateEventStreaming: update param Sink.
- Update API UpdateEventStreaming: update param Source.


2025-03-03 Version: 5.0.0
- Delete API EventCenterCheckEnabledOnDefaultBus.
- Delete API EventCenterDisableOnDefaultBus.
- Delete API EventCenterEnableOnDefaultBus.
- Update API CreateEventStreaming: update param EventStreamingName.
- Update API CreateEventStreaming: update param RunOptions.
- Update API CreateEventStreaming: update param Sink.
- Update API CreateEventStreaming: update param Source.
- Update API CreateRule: update param EventTargets.
- Update API DeleteEventStreaming: add param RegionId.
- Update API DeleteEventStreaming: update param EventStreamingName.
- Update API EventCenterQueryEvents: update param Body.
- Update API GetEventStreaming: add param RegionId.
- Update API GetEventStreaming: update param EventStreamingName.
- Update API GetEventStreaming: update response param.
- Update API ListEventStreamings: add param RegionId.
- Update API ListEventStreamings: update response param.
- Update API ListTargets: update response param.
- Update API PutTargets: update param Targets.
- Update API UpdateEventSource: update param ExternalSourceConfig.
- Update API UpdateEventStreaming: add param RegionId.
- Update API UpdateEventStreaming: update param EventStreamingName.
- Update API UpdateEventStreaming: update param RunOptions.
- Update API UpdateEventStreaming: update param Sink.
- Update API UpdateEventStreaming: update param Source.


2024-07-12 Version: 4.1.6
- Update API CreateEventStreaming: update param Sink.
- Update API GetEventStreaming: update response param.
- Update API ListEventStreamings: update response param.
- Update API UpdateEventStreaming: update param Sink.


2024-06-28 Version: 4.1.5
- Update API CreateEventStreaming: update param Sink.
- Update API ListEventStreamings: update response param.
- Update API UpdateEventStreaming: update param Sink.


2024-06-27 Version: 4.1.4
- Update API CreateEventStreaming: update param Sink.
- Update API UpdateEventStreaming: update param Sink.


2024-06-25 Version: 4.1.3
- Generated python 2020-04-01 for eventbridge.

2024-06-24 Version: 4.1.2
- Update API CreateEventSource: add param ExternalSourceConfig.
- Update API CreateEventSource: add param ExternalSourceType.
- Update API CreateEventSource: add param LinkedExternalSource.
- Update API CreateEventStreaming: update param RunOptions.
- Update API CreateEventStreaming: update param Sink.
- Update API CreateEventStreaming: update param Source.
- Update API DeleteEventBus: update response param.
- Update API EventCenterQueryEvents: update param Body.
- Update API GetEventStreaming: update response param.
- Update API GetRule: update response param.
- Update API ListEventStreamings: update response param.
- Update API UpdateEventSource: add param ExternalSourceConfig.
- Update API UpdateEventSource: add param ExternalSourceType.
- Update API UpdateEventSource: add param LinkedExternalSource.
- Update API UpdateEventStreaming: update param RunOptions.
- Update API UpdateEventStreaming: update param Sink.
- Update API UpdateEventStreaming: update param Source.


2024-05-31 Version: 4.1.1
- Update API CreateEventStreaming: update param Source.
- Update API GetEventStreaming: update response param.
- Update API ListEventStreamings: update response param.
- Update API UpdateEventStreaming: update param Source.


2024-05-11 Version: 4.1.0
- Support API EventCenterCheckEnabledOnDefaultBus.
- Support API EventCenterDisableOnDefaultBus.
- Support API EventCenterEnableOnDefaultBus.
- Support API EventCenterQueryEvents.
- Update API CreateEventBus: update response param.
- Update API CreateEventStreaming: update param Source.
- Update API CreateServiceLinkedRoleForProduct: update response param.
- Update API DeleteEventBus: update response param.
- Update API DeleteEventSource: add param EventBusName.
- Update API DeleteEventSource: update response param.
- Update API DeleteRule: update response param.
- Update API DeleteTargets: update response param.
- Update API GetEventStreaming: update response param.
- Update API ListEventBuses: update response param.
- Update API ListEventStreamings: update response param.
- Update API UpdateEventStreaming: update param Source.
- Update API UpdateRule: update response param.


2024-04-09 Version: 4.0.1
- Update API CreateEventBus: update response param.
- Update API CreateEventStreaming: update param Source.
- Update API CreateServiceLinkedRoleForProduct: update response param.
- Update API DeleteEventBus: update response param.
- Update API DeleteEventSource: add param EventBusName.
- Update API DeleteEventSource: update response param.
- Update API DeleteRule: update response param.
- Update API DeleteTargets: update response param.
- Update API GetEventStreaming: update response param.
- Update API ListEventBuses: update response param.
- Update API ListEventStreamings: update response param.
- Update API UpdateEventStreaming: update param Source.
- Update API UpdateRule: update response param.


2024-03-14 Version: 4.0.0
- Update API CreateEventStreaming: update param Sink.
- Update API CreateEventStreaming: update param Source.
- Update API CreateRule: update param EventTargets.
- Update API DeleteEventStreaming: update response param.
- Update API DisableRule: update response param.
- Update API EnableRule: update response param.
- Update API GetEventStreaming: update response param.
- Update API ListUserDefinedEventSources: update response param.
- Update API PauseEventStreaming: update response param.
- Update API StartEventStreaming: update response param.
- Update API UpdateEventStreaming: update param Sink.
- Update API UpdateEventStreaming: update param Source.


2024-02-28 Version: 3.0.0
- Update API CreateEventStreaming: update param Sink.
- Update API CreateEventStreaming: update param Source.
- Update API DisableRule: update response param.
- Update API EnableRule: update response param.
- Update API GetEventStreaming: update response param.
- Update API ListUserDefinedEventSources: update response param.
- Update API StartEventStreaming: update response param.
- Update API UpdateEventStreaming: update param Sink.
- Update API UpdateEventStreaming: update param Source.


2023-12-28 Version: 2.0.4
- Generated python 2020-04-01 for eventbridge.

2023-11-23 Version: 2.0.3
- Generated python 2020-04-01 for eventbridge.

2023-11-07 Version: 2.0.2
- Generated python 2020-04-01 for eventbridge.

2023-09-14 Version: 2.0.1
- Generated python 2020-04-01 for eventbridge.

2023-06-09 Version: 2.0.0
- Add listTargets api.

2023-04-21 Version: 1.0.8
- Update api param.

2023-04-13 Version: 1.0.7
- Add new api.

2023-04-07 Version: 1.0.6
- Update Api check.

2023-03-22 Version: 1.0.5
- Add new interface.

2023-02-27 Version: 1.0.4
- Add new interface.

2023-02-16 Version: 1.0.3
- Add new interface.

2023-02-09 Version: 1.0.2
- Mask some parameters.

2023-01-12 Version: 1.0.1
- Update EventBridge API.

2022-12-19 Version: 1.0.0
- Supported EventBridge API.

