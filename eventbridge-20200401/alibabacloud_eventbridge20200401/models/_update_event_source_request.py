# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class UpdateEventSourceRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        event_bus_name: str = None,
        event_source_name: str = None,
        external_source_config: Dict[str, Any] = None,
        external_source_type: str = None,
        linked_external_source: bool = None,
        source_http_event_parameters: main_models.UpdateEventSourceRequestSourceHttpEventParameters = None,
        source_kafka_parameters: main_models.UpdateEventSourceRequestSourceKafkaParameters = None,
        source_mnsparameters: main_models.UpdateEventSourceRequestSourceMNSParameters = None,
        source_ossevent_parameters: main_models.UpdateEventSourceRequestSourceOSSEventParameters = None,
        source_rabbit_mqparameters: main_models.UpdateEventSourceRequestSourceRabbitMQParameters = None,
        source_rocket_mqparameters: main_models.UpdateEventSourceRequestSourceRocketMQParameters = None,
        source_slsparameters: main_models.UpdateEventSourceRequestSourceSLSParameters = None,
        source_scheduled_event_parameters: main_models.UpdateEventSourceRequestSourceScheduledEventParameters = None,
    ):
        # The description of the event source.
        self.description = description
        # The event bus with which the event source is associated.
        # 
        # This parameter is required.
        self.event_bus_name = event_bus_name
        # The name of the event source.
        # 
        # This parameter is required.
        self.event_source_name = event_source_name
        # The configurations of the external data source.
        self.external_source_config = external_source_config
        # The type of the external data source.
        self.external_source_type = external_source_type
        # Specifies whether to connect to an external data source.
        self.linked_external_source = linked_external_source
        # The parameters that are configured if the event source is HTTP events.
        self.source_http_event_parameters = source_http_event_parameters
        # The parameters that are configured if the event source is Message Queue for Apache Kafka.
        self.source_kafka_parameters = source_kafka_parameters
        # The parameters that are configured if the event source is Message Service (MNS).
        self.source_mnsparameters = source_mnsparameters
        self.source_ossevent_parameters = source_ossevent_parameters
        # The parameters that are configured if the event source is Message Queue for RabbitMQ.
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        # The parameters that are configured if the event source is Message Queue for Apache RocketMQ.
        self.source_rocket_mqparameters = source_rocket_mqparameters
        # SourceSLSParameters
        self.source_slsparameters = source_slsparameters
        # The parameters that are configured if you specify scheduled events as the event source.
        self.source_scheduled_event_parameters = source_scheduled_event_parameters

    def validate(self):
        if self.source_http_event_parameters:
            self.source_http_event_parameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_ossevent_parameters:
            self.source_ossevent_parameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()
        if self.source_scheduled_event_parameters:
            self.source_scheduled_event_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name

        if self.external_source_config is not None:
            result['ExternalSourceConfig'] = self.external_source_config

        if self.external_source_type is not None:
            result['ExternalSourceType'] = self.external_source_type

        if self.linked_external_source is not None:
            result['LinkedExternalSource'] = self.linked_external_source

        if self.source_http_event_parameters is not None:
            result['SourceHttpEventParameters'] = self.source_http_event_parameters.to_map()

        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()

        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()

        if self.source_ossevent_parameters is not None:
            result['SourceOSSEventParameters'] = self.source_ossevent_parameters.to_map()

        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()

        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()

        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()

        if self.source_scheduled_event_parameters is not None:
            result['SourceScheduledEventParameters'] = self.source_scheduled_event_parameters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')

        if m.get('ExternalSourceConfig') is not None:
            self.external_source_config = m.get('ExternalSourceConfig')

        if m.get('ExternalSourceType') is not None:
            self.external_source_type = m.get('ExternalSourceType')

        if m.get('LinkedExternalSource') is not None:
            self.linked_external_source = m.get('LinkedExternalSource')

        if m.get('SourceHttpEventParameters') is not None:
            temp_model = main_models.UpdateEventSourceRequestSourceHttpEventParameters()
            self.source_http_event_parameters = temp_model.from_map(m.get('SourceHttpEventParameters'))

        if m.get('SourceKafkaParameters') is not None:
            temp_model = main_models.UpdateEventSourceRequestSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m.get('SourceKafkaParameters'))

        if m.get('SourceMNSParameters') is not None:
            temp_model = main_models.UpdateEventSourceRequestSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m.get('SourceMNSParameters'))

        if m.get('SourceOSSEventParameters') is not None:
            temp_model = main_models.UpdateEventSourceRequestSourceOSSEventParameters()
            self.source_ossevent_parameters = temp_model.from_map(m.get('SourceOSSEventParameters'))

        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = main_models.UpdateEventSourceRequestSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m.get('SourceRabbitMQParameters'))

        if m.get('SourceRocketMQParameters') is not None:
            temp_model = main_models.UpdateEventSourceRequestSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m.get('SourceRocketMQParameters'))

        if m.get('SourceSLSParameters') is not None:
            temp_model = main_models.UpdateEventSourceRequestSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m.get('SourceSLSParameters'))

        if m.get('SourceScheduledEventParameters') is not None:
            temp_model = main_models.UpdateEventSourceRequestSourceScheduledEventParameters()
            self.source_scheduled_event_parameters = temp_model.from_map(m.get('SourceScheduledEventParameters'))

        return self

class UpdateEventSourceRequestSourceScheduledEventParameters(DaraModel):
    def __init__(
        self,
        schedule: str = None,
        time_zone: str = None,
        user_data: str = None,
    ):
        # The cron expression.
        self.schedule = schedule
        # The time zone in which the cron expression is executed.
        self.time_zone = time_zone
        # The user data that is displayed in a JSON string.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.schedule is not None:
            result['Schedule'] = self.schedule

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class UpdateEventSourceRequestSourceSLSParameters(DaraModel):
    def __init__(
        self,
        consume_position: str = None,
        log_store: str = None,
        project: str = None,
        role_name: str = None,
    ):
        # The starting consumer offset. The value begin indicates the earliest offset, and the value end indicates the latest offset. You can also specify a time in seconds to start consumption.
        self.consume_position = consume_position
        # The Log Service Logstore.
        self.log_store = log_store
        # The Log Service project.
        self.project = project
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the RAM console. For information about the permission policy of this role, see Create a custom event source of the Log Service type.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consume_position is not None:
            result['ConsumePosition'] = self.consume_position

        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.project is not None:
            result['Project'] = self.project

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumePosition') is not None:
            self.consume_position = m.get('ConsumePosition')

        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

class UpdateEventSourceRequestSourceRocketMQParameters(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        group_id: str = None,
        instance_endpoint: str = None,
        instance_id: str = None,
        instance_network: str = None,
        instance_password: str = None,
        instance_security_group_id: str = None,
        instance_type: str = None,
        instance_username: str = None,
        instance_vswitch_ids: str = None,
        instance_vpc_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
    ):
        # The authentication type. You can set this parameter to ACL or leave this parameter empty.
        self.auth_type = auth_type
        # The ID of the consumer group on the Message Queue for Apache RocketMQ instance.
        self.group_id = group_id
        # The endpoint that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_endpoint = instance_endpoint
        # The ID of the Message Queue for Apache RocketMQ instance. For more information, see [Limits](https://help.aliyun.com/document_detail/163289.html).
        self.instance_id = instance_id
        # None.
        self.instance_network = instance_network
        # The password that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_password = instance_password
        # The ID of the security group to which the Message Queue for Apache RocketMQ instance belongs.
        self.instance_security_group_id = instance_security_group_id
        # The type of the Message Queue for Apache RocketMQ instance. Valid values:
        # 
        # *   Cloud_4: Message Queue for Apache RocketMQ 4.0 instance.
        # *   Cloud_5: Message Queue for Apache RocketMQ 5.0 instance.
        self.instance_type = instance_type
        # The username that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_username = instance_username
        # The ID of the vSwitch with which the Message Queue for Apache RocketMQ instance is associated.
        self.instance_vswitch_ids = instance_vswitch_ids
        # The ID of the virtual private cloud (VPC) in which the Message Queue for Apache RocketMQ instance resides.
        self.instance_vpc_id = instance_vpc_id
        # The offset from which message consumption starts. Valid values:
        # 
        # *   CONSUME_FROM_LAST_OFFSET: Start message consumption from the latest offset.
        # *   CONSUME_FROM_FIRST_OFFSET: Start message consumption from the earliest offset.
        # *   CONSUME_FROM_TIMESTAMP: Start message consumption from the offset at the specified point in time.
        # 
        # Default value: CONSUME_FROM_LAST_OFFSET.
        self.offset = offset
        # The region where the Message Queue for Apache RocketMQ instance resides.
        self.region_id = region_id
        # The tag that is used to filter messages.
        self.tag = tag
        # The timestamp that specifies the time from which messages are consumed. This parameter is valid only if you set Offset to CONSUME_FROM_TIMESTAMP.
        self.timestamp = timestamp
        # The name of the topic on the Message Queue for Apache RocketMQ instance. For more information, see [Limits](https://help.aliyun.com/document_detail/163289.html).
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.group_id is not None:
            result['GroupID'] = self.group_id

        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network

        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password

        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username

        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids

        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')

        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')

        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')

        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')

        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')

        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class UpdateEventSourceRequestSourceRabbitMQParameters(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_name: str = None,
        region_id: str = None,
        virtual_host_name: str = None,
    ):
        # The ID of the Message Queue for RabbitMQ instance. For more information, see [Limits](https://help.aliyun.com/document_detail/163289.html).
        self.instance_id = instance_id
        # The name of the queue on the Message Queue for RabbitMQ instance. For more information, see [Limits](https://help.aliyun.com/document_detail/163289.html).
        self.queue_name = queue_name
        # The ID of the region where the Message Queue for RabbitMQ instance resides.
        self.region_id = region_id
        # The name of the vhost of the Message Queue for RabbitMQ instance. For more information, see [Limits](https://help.aliyun.com/document_detail/163289.html).
        self.virtual_host_name = virtual_host_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')

        return self

class UpdateEventSourceRequestSourceOSSEventParameters(DaraModel):
    def __init__(
        self,
        event_types: List[str] = None,
        match_rules: List[List[main_models.UpdateEventSourceRequestSourceOSSEventParametersMatchRules]] = None,
        sts_role_arn: str = None,
    ):
        self.event_types = event_types
        self.match_rules = match_rules
        self.sts_role_arn = sts_role_arn

    def validate(self):
        if self.match_rules:
            for v1 in self.match_rules:
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_types is not None:
            result['EventTypes'] = self.event_types

        result['MatchRules'] = []
        if self.match_rules is not None:
            for k1 in self.match_rules:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['MatchRules'].append(l1)

        if self.sts_role_arn is not None:
            result['StsRoleArn'] = self.sts_role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTypes') is not None:
            self.event_types = m.get('EventTypes')

        self.match_rules = []
        if m.get('MatchRules') is not None:
            for k1 in m.get('MatchRules'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.UpdateEventSourceRequestSourceOSSEventParametersMatchRules()
                    l1.append(temp_model.from_map(k2))
                self.match_rules.append(l1)

        if m.get('StsRoleArn') is not None:
            self.sts_role_arn = m.get('StsRoleArn')

        return self

class UpdateEventSourceRequestSourceOSSEventParametersMatchRules(DaraModel):
    def __init__(
        self,
        suffix: str = None,
        match_state: bool = None,
        prefix: str = None,
        name: str = None,
    ):
        self.suffix = suffix
        self.match_state = match_state
        self.prefix = prefix
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.suffix is not None:
            result['Suffix'] = self.suffix

        if self.match_state is not None:
            result['MatchState'] = self.match_state

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Suffix') is not None:
            self.suffix = m.get('Suffix')

        if m.get('MatchState') is not None:
            self.match_state = m.get('MatchState')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpdateEventSourceRequestSourceMNSParameters(DaraModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        # Indicates whether Base64 decoding is enabled. By default, Base64 decoding is enabled.
        self.is_base_64decode = is_base_64decode
        # The name of the MNS queue.
        self.queue_name = queue_name
        # The region where the MNS queue resides.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class UpdateEventSourceRequestSourceKafkaParameters(DaraModel):
    def __init__(
        self,
        consumer_group: str = None,
        instance_id: str = None,
        maximum_tasks: int = None,
        network: str = None,
        offset_reset: str = None,
        region_id: str = None,
        security_group_id: str = None,
        topic: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        # The ID of the consumer group that subscribes to the topic.
        self.consumer_group = consumer_group
        # The ID of the Message Queue for Apache Kafka instance.
        self.instance_id = instance_id
        # The maximum number of consumers.
        self.maximum_tasks = maximum_tasks
        # The network. Valid values: Default and PublicNetwork. Default value: Default. The value PublicNetwork indicates a self-managed network.
        self.network = network
        # The consumer offset.
        self.offset_reset = offset_reset
        # The ID of the region where the Message Queue for Apache Kafka instance resides.
        self.region_id = region_id
        # The ID of the security group to which the Message Queue for Apache Kafka instance belongs. This parameter is required only if you set Network to PublicNetwork.
        self.security_group_id = security_group_id
        # The name of the topic on the Message Queue for Apache Kafka instance.
        self.topic = topic
        # The ID of the vSwitch with which the Message Queue for Apache Kafka instance is associated. This parameter is required only if you set Network to PublicNetwork.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC in which the Message Queue for Apache Kafka instance resides. This parameter is required only if you set Network to PublicNetwork.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks

        if self.network is not None:
            result['Network'] = self.network

        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class UpdateEventSourceRequestSourceHttpEventParameters(DaraModel):
    def __init__(
        self,
        ip: List[str] = None,
        method: List[str] = None,
        referer: List[str] = None,
        security_config: str = None,
        type: str = None,
    ):
        # The CIDR block that is used for security settings. This parameter is required only if SecurityConfig is set to ip. You can enter a CIDR block or an IP address.
        self.ip = ip
        # The HTTP request method supported by the generated webhook URL. You can select multiple values. Valid values:
        # 
        # *   GET
        # *   POST
        # *   PUT
        # *   PATCH
        # *   DELETE
        # *   HEAD
        # *   OPTIONS
        # *   TRACE
        # *   CONNECT
        self.method = method
        # The security domain name. This parameter is required only if SecurityConfig is set to referer. You can enter a domain name.
        self.referer = referer
        # The type of security settings. Valid values:
        # 
        # *   none: No configuration is required.
        # *   ip: CIDR block.
        # *   referer: security domain name.
        self.security_config = security_config
        # The protocol type that is supported by the generated webhook URL. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        # *   HTTP\\&HTTPS
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.method is not None:
            result['Method'] = self.method

        if self.referer is not None:
            result['Referer'] = self.referer

        if self.security_config is not None:
            result['SecurityConfig'] = self.security_config

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Referer') is not None:
            self.referer = m.get('Referer')

        if m.get('SecurityConfig') is not None:
            self.security_config = m.get('SecurityConfig')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

