# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class ListUserDefinedEventSourcesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListUserDefinedEventSourcesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. Valid values:
        # 
        # *   Success: The request is successful.
        # *   Other codes: The request failed. For more information about error codes, see Error codes.
        self.code = code
        # The data returned.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. The value true indicates that the operation is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListUserDefinedEventSourcesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListUserDefinedEventSourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        event_source_list: List[main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceList] = None,
        next_token: str = None,
        total: int = None,
    ):
        # The event sources.
        self.event_source_list = event_source_list
        # If excess return values exist when you configure Limit, this parameter is returned.
        self.next_token = next_token
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.event_source_list:
            for v1 in self.event_source_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventSourceList'] = []
        if self.event_source_list is not None:
            for k1 in self.event_source_list:
                result['EventSourceList'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_source_list = []
        if m.get('EventSourceList') is not None:
            for k1 in m.get('EventSourceList'):
                temp_model = main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceList()
                self.event_source_list.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListUserDefinedEventSourcesResponseBodyDataEventSourceList(DaraModel):
    def __init__(
        self,
        arn: str = None,
        ctime: float = None,
        event_bus_name: str = None,
        external_source_type: str = None,
        name: str = None,
        source_http_event_parameters: main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceHttpEventParameters = None,
        source_kafka_parameters: main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceKafkaParameters = None,
        source_mnsparameters: main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceMNSParameters = None,
        source_ossevent_parameters: main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceOSSEventParameters = None,
        source_rabbit_mqparameters: main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRabbitMQParameters = None,
        source_rocket_mqparameters: main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRocketMQParameters = None,
        source_slsparameters: main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceSLSParameters = None,
        source_scheduled_event_parameters: main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceScheduledEventParameters = None,
        status: str = None,
        type: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the queried event source.
        self.arn = arn
        # The timestamp that indicates when the event source was created.
        self.ctime = ctime
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The type of the event source.
        self.external_source_type = external_source_type
        # The name of the queried event source.
        self.name = name
        # The parameters that are returned if HTTP events are specified as the event source.
        self.source_http_event_parameters = source_http_event_parameters
        # The parameters that are returned if Message Queue for Apache Kafka is specified as the event source.
        self.source_kafka_parameters = source_kafka_parameters
        # The parameters that are returned if Simple Message Queue (formerly MNS) (SMQ) is specified as the event source.
        self.source_mnsparameters = source_mnsparameters
        self.source_ossevent_parameters = source_ossevent_parameters
        # The parameters that are returned if Message Queue for RabbitMQ is specified as the event source.
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        # The parameters that are returned if Message Queue for Apache RocketMQ is specified as the event source.
        self.source_rocket_mqparameters = source_rocket_mqparameters
        # The parameters that are returned if Simple Log Service is specified as the event source.
        self.source_slsparameters = source_slsparameters
        # The parameters that are returned if scheduled events are specified as the event source.
        self.source_scheduled_event_parameters = source_scheduled_event_parameters
        # The status of the queried event source. The returned value Activated indicates that the event source is activated.
        self.status = status
        # The type of the queried event source. The returned value UserDefined indicates that the event source is a custom event source.
        self.type = type

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
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.ctime is not None:
            result['Ctime'] = self.ctime

        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.external_source_type is not None:
            result['ExternalSourceType'] = self.external_source_type

        if self.name is not None:
            result['Name'] = self.name

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

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')

        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('ExternalSourceType') is not None:
            self.external_source_type = m.get('ExternalSourceType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SourceHttpEventParameters') is not None:
            temp_model = main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceHttpEventParameters()
            self.source_http_event_parameters = temp_model.from_map(m.get('SourceHttpEventParameters'))

        if m.get('SourceKafkaParameters') is not None:
            temp_model = main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m.get('SourceKafkaParameters'))

        if m.get('SourceMNSParameters') is not None:
            temp_model = main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m.get('SourceMNSParameters'))

        if m.get('SourceOSSEventParameters') is not None:
            temp_model = main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceOSSEventParameters()
            self.source_ossevent_parameters = temp_model.from_map(m.get('SourceOSSEventParameters'))

        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m.get('SourceRabbitMQParameters'))

        if m.get('SourceRocketMQParameters') is not None:
            temp_model = main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m.get('SourceRocketMQParameters'))

        if m.get('SourceSLSParameters') is not None:
            temp_model = main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m.get('SourceSLSParameters'))

        if m.get('SourceScheduledEventParameters') is not None:
            temp_model = main_models.ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceScheduledEventParameters()
            self.source_scheduled_event_parameters = temp_model.from_map(m.get('SourceScheduledEventParameters'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceScheduledEventParameters(DaraModel):
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
        # The JSON string.
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

class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceSLSParameters(DaraModel):
    def __init__(
        self,
        consume_position: str = None,
        log_store: str = None,
        project: str = None,
        role_name: str = None,
    ):
        # The consumer offset. The value begin indicates the earliest offset, and the value end indicates the latest offset. You can also specify a time in seconds to start consumption.
        self.consume_position = consume_position
        # The Simple Log Service Logstore.
        self.log_store = log_store
        # The Simple Log Service project.
        self.project = project
        # The role name. If you want to authorize EventBridge to use this role to read logs in Simple Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the Resource Access Management (RAM) console. For information about the permission policy of this role, see Create a custom event source of the Log Service type.
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

class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRocketMQParameters(DaraModel):
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
        timestamp: float = None,
        topic: str = None,
    ):
        # The authentication type. This parameter can be set to ACL or left empty.
        self.auth_type = auth_type
        # The ID of the consumer group on the Message Queue for Apache RocketMQ instance.
        self.group_id = group_id
        # The endpoint that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_endpoint = instance_endpoint
        # The ID of the Message Queue for Apache RocketMQ instance. For more information, see [Limits](https://help.aliyun.com/document_detail/163289.html).
        self.instance_id = instance_id
        # The type of network over which the Message Queue for Apache RocketMQ instance is accessed.
        self.instance_network = instance_network
        # The password that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_password = instance_password
        # The ID of the security group to which the Message Queue for Apache RocketMQ instance belongs.
        self.instance_security_group_id = instance_security_group_id
        # The instance type. Valid values: CLOUD_4, CLOUD_5, and SELF_BUILT. The value CLOUD_4 indicates that the instance is a Message Queue for Apache RocketMQ 4.0 instance. The value CLOUD_5 indicates that the instance is a Message Queue for Apache RocketMQ 5.0 instance. The value SELF_BUILT indicates that the instance is a self-managed RocketMQ instance.
        self.instance_type = instance_type
        # The username that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_username = instance_username
        # The ID of the vSwitch with which the Message Queue for Apache RocketMQ instance is associated.
        self.instance_vswitch_ids = instance_vswitch_ids
        # The ID of the virtual private cloud (VPC) in which the Message Queue for Apache RocketMQ instance is deployed.
        self.instance_vpc_id = instance_vpc_id
        # The offset from which messages are consumed. Valid values:
        # 
        # *   CONSUME_FROM_LAST_OFFSET: Messages are consumed from the latest offset.
        # *   CONSUME_FROM_FIRST_OFFSET: Messages are consumed from the earliest offset.
        # *   CONSUME_FROM_TIMESTAMP: Messages are consumed from the offset at the specified point in time.
        # 
        # Default value: CONSUME_FROM_LAST_OFFSET.
        self.offset = offset
        # The ID of the region where the Message Queue for Apache RocketMQ instance resides.
        self.region_id = region_id
        # The tag that is used to filter messages.
        self.tag = tag
        # The timestamp that indicates the time from which messages are consumed. This parameter is valid only if Offset is set to CONSUME_FROM_TIMESTAMP.
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
            result['GroupId'] = self.group_id

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

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

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

class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRabbitMQParameters(DaraModel):
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

class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceOSSEventParameters(DaraModel):
    def __init__(
        self,
        event_types: List[str] = None,
        match_rules: Any = None,
        sts_role_arn: str = None,
    ):
        self.event_types = event_types
        self.match_rules = match_rules
        self.sts_role_arn = sts_role_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_types is not None:
            result['EventTypes'] = self.event_types

        if self.match_rules is not None:
            result['MatchRules'] = self.match_rules

        if self.sts_role_arn is not None:
            result['StsRoleArn'] = self.sts_role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTypes') is not None:
            self.event_types = m.get('EventTypes')

        if m.get('MatchRules') is not None:
            self.match_rules = m.get('MatchRules')

        if m.get('StsRoleArn') is not None:
            self.sts_role_arn = m.get('StsRoleArn')

        return self

class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceMNSParameters(DaraModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        # Indicates whether Base64 decoding is enabled. By default, Base64 decoding is enabled.
        self.is_base_64decode = is_base_64decode
        # The name of the SMQ queue.
        self.queue_name = queue_name
        # The ID of the region where the SMQ queue resides.
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

class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceKafkaParameters(DaraModel):
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
        # The ID of the consumer group that subscribes to the topic on the Message Queue for Apache Kafka instance.
        self.consumer_group = consumer_group
        # The ID of the Message Queue for Apache Kafka instance.
        self.instance_id = instance_id
        # The maximum number of consumers.
        self.maximum_tasks = maximum_tasks
        # The network type. Valid values: Default and PublicNetwork. Default value: Default. The value PublicNetwork indicates a self-managed network.
        self.network = network
        # The consumer offset.
        self.offset_reset = offset_reset
        # The ID of the region where the Message Queue for Apache Kafka instance resides.
        self.region_id = region_id
        # The ID of the security group to which the Message Queue for Apache Kafka instance belongs.
        self.security_group_id = security_group_id
        # The topic name.
        self.topic = topic
        # The ID of the vSwitch with which the Message Queue for Apache Kafka instance is associated.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC in which the Message Queue for Apache Kafka instance is deployed.
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

class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceHttpEventParameters(DaraModel):
    def __init__(
        self,
        ip: List[str] = None,
        method: List[str] = None,
        public_web_hook_url: List[str] = None,
        referer: List[str] = None,
        security_config: str = None,
        type: str = None,
        vpc_web_hook_url: List[str] = None,
    ):
        # The CIDR block that is used for security settings. This parameter is required only if SecurityConfig is set to ip. You can enter a CIDR block or an IP address.
        self.ip = ip
        # The HTTP request method that is supported by the generated webhook URL. You can select multiple values. Valid values:
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
        # The Internet request URL.
        self.public_web_hook_url = public_web_hook_url
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
        # The internal request URL.
        self.vpc_web_hook_url = vpc_web_hook_url

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

        if self.public_web_hook_url is not None:
            result['PublicWebHookUrl'] = self.public_web_hook_url

        if self.referer is not None:
            result['Referer'] = self.referer

        if self.security_config is not None:
            result['SecurityConfig'] = self.security_config

        if self.type is not None:
            result['Type'] = self.type

        if self.vpc_web_hook_url is not None:
            result['VpcWebHookUrl'] = self.vpc_web_hook_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('PublicWebHookUrl') is not None:
            self.public_web_hook_url = m.get('PublicWebHookUrl')

        if m.get('Referer') is not None:
            self.referer = m.get('Referer')

        if m.get('SecurityConfig') is not None:
            self.security_config = m.get('SecurityConfig')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VpcWebHookUrl') is not None:
            self.vpc_web_hook_url = m.get('VpcWebHookUrl')

        return self

