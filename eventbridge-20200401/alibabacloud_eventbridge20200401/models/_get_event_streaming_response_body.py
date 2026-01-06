# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class GetEventStreamingResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetEventStreamingResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For a list of error codes, see Error codes.
        self.code = code
        # The returned data.
        self.data = data
        # The error message that is returned if the request failed.
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
            temp_model = main_models.GetEventStreamingResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetEventStreamingResponseBodyData(DaraModel):
    def __init__(
        self,
        description: str = None,
        detailed_status: main_models.GetEventStreamingResponseBodyDataDetailedStatus = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        run_options: main_models.GetEventStreamingResponseBodyDataRunOptions = None,
        sink: main_models.GetEventStreamingResponseBodyDataSink = None,
        source: main_models.GetEventStreamingResponseBodyDataSource = None,
        status: str = None,
        transforms: List[main_models.GetEventStreamingResponseBodyDataTransforms] = None,
    ):
        # The description of the event stream that is returned.
        self.description = description
        self.detailed_status = detailed_status
        # The name of the event stream that is returned.
        self.event_streaming_name = event_streaming_name
        # The rule that is used to filter events. If you leave this parameter empty, all events are matched.
        self.filter_pattern = filter_pattern
        # The runtime environment-related configurations.
        self.run_options = run_options
        # The event target.
        self.sink = sink
        # The event source.
        self.source = source
        # The status of the event stream that is returned.
        self.status = status
        self.transforms = transforms

    def validate(self):
        if self.detailed_status:
            self.detailed_status.validate()
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()
        if self.transforms:
            for v1 in self.transforms:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.detailed_status is not None:
            result['DetailedStatus'] = self.detailed_status.to_map()

        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name

        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern

        if self.run_options is not None:
            result['RunOptions'] = self.run_options.to_map()

        if self.sink is not None:
            result['Sink'] = self.sink.to_map()

        if self.source is not None:
            result['Source'] = self.source.to_map()

        if self.status is not None:
            result['Status'] = self.status

        result['Transforms'] = []
        if self.transforms is not None:
            for k1 in self.transforms:
                result['Transforms'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DetailedStatus') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataDetailedStatus()
            self.detailed_status = temp_model.from_map(m.get('DetailedStatus'))

        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')

        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')

        if m.get('RunOptions') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataRunOptions()
            self.run_options = temp_model.from_map(m.get('RunOptions'))

        if m.get('Sink') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSink()
            self.sink = temp_model.from_map(m.get('Sink'))

        if m.get('Source') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSource()
            self.source = temp_model.from_map(m.get('Source'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.transforms = []
        if m.get('Transforms') is not None:
            for k1 in m.get('Transforms'):
                temp_model = main_models.GetEventStreamingResponseBodyDataTransforms()
                self.transforms.append(temp_model.from_map(k1))

        return self

class GetEventStreamingResponseBodyDataTransforms(DaraModel):
    def __init__(
        self,
        arn: str = None,
        bai_lian_agent_transform_parameters: main_models.BaiLianAgentTransformParameters = None,
        dash_scope_transform_parameters: main_models.DashScopeTransformParameters = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the cloud service, such as the ARN of a Function Compute function.
        self.arn = arn
        self.bai_lian_agent_transform_parameters = bai_lian_agent_transform_parameters
        self.dash_scope_transform_parameters = dash_scope_transform_parameters

    def validate(self):
        if self.bai_lian_agent_transform_parameters:
            self.bai_lian_agent_transform_parameters.validate()
        if self.dash_scope_transform_parameters:
            self.dash_scope_transform_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.bai_lian_agent_transform_parameters is not None:
            result['BaiLianAgentTransformParameters'] = self.bai_lian_agent_transform_parameters.to_map()

        if self.dash_scope_transform_parameters is not None:
            result['DashScopeTransformParameters'] = self.dash_scope_transform_parameters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('BaiLianAgentTransformParameters') is not None:
            temp_model = main_models.BaiLianAgentTransformParameters()
            self.bai_lian_agent_transform_parameters = temp_model.from_map(m.get('BaiLianAgentTransformParameters'))

        if m.get('DashScopeTransformParameters') is not None:
            temp_model = main_models.DashScopeTransformParameters()
            self.dash_scope_transform_parameters = temp_model.from_map(m.get('DashScopeTransformParameters'))

        return self

class GetEventStreamingResponseBodyDataSource(DaraModel):
    def __init__(
        self,
        source_apache_kafka_parameters: main_models.GetEventStreamingResponseBodyDataSourceSourceApacheKafkaParameters = None,
        source_apache_rocket_mqcheckpoint_parameters: main_models.GetEventStreamingResponseBodyDataSourceSourceApacheRocketMQCheckpointParameters = None,
        source_customized_kafka_connector_parameters: main_models.GetEventStreamingResponseBodyDataSourceSourceCustomizedKafkaConnectorParameters = None,
        source_customized_kafka_parameters: main_models.GetEventStreamingResponseBodyDataSourceSourceCustomizedKafkaParameters = None,
        source_dtsparameters: main_models.GetEventStreamingResponseBodyDataSourceSourceDTSParameters = None,
        source_event_bus_parameters: main_models.GetEventStreamingResponseBodyDataSourceSourceEventBusParameters = None,
        source_kafka_parameters: main_models.GetEventStreamingResponseBodyDataSourceSourceKafkaParameters = None,
        source_mnsparameters: main_models.GetEventStreamingResponseBodyDataSourceSourceMNSParameters = None,
        source_mqttparameters: main_models.GetEventStreamingResponseBodyDataSourceSourceMQTTParameters = None,
        source_my_sqlparameters: main_models.SourceMySQLParameters = None,
        source_ossparameters: main_models.GetEventStreamingResponseBodyDataSourceSourceOSSParameters = None,
        source_open_source_rabbit_mqparameters: main_models.GetEventStreamingResponseBodyDataSourceSourceOpenSourceRabbitMQParameters = None,
        source_postgre_sqlparameters: main_models.SourcePostgreSQLParameters = None,
        source_prometheus_parameters: main_models.GetEventStreamingResponseBodyDataSourceSourcePrometheusParameters = None,
        source_rabbit_mqmeta_parameters: main_models.SourceRabbitMQMetaParameters = None,
        source_rabbit_mqmsg_sync_parameters: main_models.SourceRabbitMQMsgSyncParameters = None,
        source_rabbit_mqparameters: main_models.GetEventStreamingResponseBodyDataSourceSourceRabbitMQParameters = None,
        source_rocket_mqcheckpoint_parameters: main_models.GetEventStreamingResponseBodyDataSourceSourceRocketMQCheckpointParameters = None,
        source_rocket_mqparameters: main_models.GetEventStreamingResponseBodyDataSourceSourceRocketMQParameters = None,
        source_slsparameters: main_models.GetEventStreamingResponseBodyDataSourceSourceSLSParameters = None,
    ):
        self.source_apache_kafka_parameters = source_apache_kafka_parameters
        # The parameters that are returned if Apache RocketMQ (Offset Data) is specified as the event source.
        self.source_apache_rocket_mqcheckpoint_parameters = source_apache_rocket_mqcheckpoint_parameters
        self.source_customized_kafka_connector_parameters = source_customized_kafka_connector_parameters
        self.source_customized_kafka_parameters = source_customized_kafka_parameters
        # The parameters that are returned if the event source is Data Transmission Service (DTS).
        self.source_dtsparameters = source_dtsparameters
        self.source_event_bus_parameters = source_event_bus_parameters
        # The parameters that are returned if ApsaraMQ for Kafka is specified as the event source.
        self.source_kafka_parameters = source_kafka_parameters
        # Source MNS Parameters
        self.source_mnsparameters = source_mnsparameters
        # The parameters that are returned if ApsaraMQ for MQTT is specified as the event source.
        self.source_mqttparameters = source_mqttparameters
        self.source_my_sqlparameters = source_my_sqlparameters
        self.source_ossparameters = source_ossparameters
        self.source_open_source_rabbit_mqparameters = source_open_source_rabbit_mqparameters
        self.source_postgre_sqlparameters = source_postgre_sqlparameters
        self.source_prometheus_parameters = source_prometheus_parameters
        self.source_rabbit_mqmeta_parameters = source_rabbit_mqmeta_parameters
        self.source_rabbit_mqmsg_sync_parameters = source_rabbit_mqmsg_sync_parameters
        # Source RabbitMQ Parameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        self.source_rocket_mqcheckpoint_parameters = source_rocket_mqcheckpoint_parameters
        # The parameters that are returned if ApsaraMQ for RocketMQ is specified as the event source.
        self.source_rocket_mqparameters = source_rocket_mqparameters
        # The parameters that are returned if the event provider is Simple Log Service.
        self.source_slsparameters = source_slsparameters

    def validate(self):
        if self.source_apache_kafka_parameters:
            self.source_apache_kafka_parameters.validate()
        if self.source_apache_rocket_mqcheckpoint_parameters:
            self.source_apache_rocket_mqcheckpoint_parameters.validate()
        if self.source_customized_kafka_connector_parameters:
            self.source_customized_kafka_connector_parameters.validate()
        if self.source_customized_kafka_parameters:
            self.source_customized_kafka_parameters.validate()
        if self.source_dtsparameters:
            self.source_dtsparameters.validate()
        if self.source_event_bus_parameters:
            self.source_event_bus_parameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_mqttparameters:
            self.source_mqttparameters.validate()
        if self.source_my_sqlparameters:
            self.source_my_sqlparameters.validate()
        if self.source_ossparameters:
            self.source_ossparameters.validate()
        if self.source_open_source_rabbit_mqparameters:
            self.source_open_source_rabbit_mqparameters.validate()
        if self.source_postgre_sqlparameters:
            self.source_postgre_sqlparameters.validate()
        if self.source_prometheus_parameters:
            self.source_prometheus_parameters.validate()
        if self.source_rabbit_mqmeta_parameters:
            self.source_rabbit_mqmeta_parameters.validate()
        if self.source_rabbit_mqmsg_sync_parameters:
            self.source_rabbit_mqmsg_sync_parameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqcheckpoint_parameters:
            self.source_rocket_mqcheckpoint_parameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_apache_kafka_parameters is not None:
            result['SourceApacheKafkaParameters'] = self.source_apache_kafka_parameters.to_map()

        if self.source_apache_rocket_mqcheckpoint_parameters is not None:
            result['SourceApacheRocketMQCheckpointParameters'] = self.source_apache_rocket_mqcheckpoint_parameters.to_map()

        if self.source_customized_kafka_connector_parameters is not None:
            result['SourceCustomizedKafkaConnectorParameters'] = self.source_customized_kafka_connector_parameters.to_map()

        if self.source_customized_kafka_parameters is not None:
            result['SourceCustomizedKafkaParameters'] = self.source_customized_kafka_parameters.to_map()

        if self.source_dtsparameters is not None:
            result['SourceDTSParameters'] = self.source_dtsparameters.to_map()

        if self.source_event_bus_parameters is not None:
            result['SourceEventBusParameters'] = self.source_event_bus_parameters.to_map()

        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()

        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()

        if self.source_mqttparameters is not None:
            result['SourceMQTTParameters'] = self.source_mqttparameters.to_map()

        if self.source_my_sqlparameters is not None:
            result['SourceMySQLParameters'] = self.source_my_sqlparameters.to_map()

        if self.source_ossparameters is not None:
            result['SourceOSSParameters'] = self.source_ossparameters.to_map()

        if self.source_open_source_rabbit_mqparameters is not None:
            result['SourceOpenSourceRabbitMQParameters'] = self.source_open_source_rabbit_mqparameters.to_map()

        if self.source_postgre_sqlparameters is not None:
            result['SourcePostgreSQLParameters'] = self.source_postgre_sqlparameters.to_map()

        if self.source_prometheus_parameters is not None:
            result['SourcePrometheusParameters'] = self.source_prometheus_parameters.to_map()

        if self.source_rabbit_mqmeta_parameters is not None:
            result['SourceRabbitMQMetaParameters'] = self.source_rabbit_mqmeta_parameters.to_map()

        if self.source_rabbit_mqmsg_sync_parameters is not None:
            result['SourceRabbitMQMsgSyncParameters'] = self.source_rabbit_mqmsg_sync_parameters.to_map()

        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()

        if self.source_rocket_mqcheckpoint_parameters is not None:
            result['SourceRocketMQCheckpointParameters'] = self.source_rocket_mqcheckpoint_parameters.to_map()

        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()

        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceApacheKafkaParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSourceSourceApacheKafkaParameters()
            self.source_apache_kafka_parameters = temp_model.from_map(m.get('SourceApacheKafkaParameters'))

        if m.get('SourceApacheRocketMQCheckpointParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSourceSourceApacheRocketMQCheckpointParameters()
            self.source_apache_rocket_mqcheckpoint_parameters = temp_model.from_map(m.get('SourceApacheRocketMQCheckpointParameters'))

        if m.get('SourceCustomizedKafkaConnectorParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSourceSourceCustomizedKafkaConnectorParameters()
            self.source_customized_kafka_connector_parameters = temp_model.from_map(m.get('SourceCustomizedKafkaConnectorParameters'))

        if m.get('SourceCustomizedKafkaParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSourceSourceCustomizedKafkaParameters()
            self.source_customized_kafka_parameters = temp_model.from_map(m.get('SourceCustomizedKafkaParameters'))

        if m.get('SourceDTSParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSourceSourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m.get('SourceDTSParameters'))

        if m.get('SourceEventBusParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSourceSourceEventBusParameters()
            self.source_event_bus_parameters = temp_model.from_map(m.get('SourceEventBusParameters'))

        if m.get('SourceKafkaParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSourceSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m.get('SourceKafkaParameters'))

        if m.get('SourceMNSParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSourceSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m.get('SourceMNSParameters'))

        if m.get('SourceMQTTParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSourceSourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m.get('SourceMQTTParameters'))

        if m.get('SourceMySQLParameters') is not None:
            temp_model = main_models.SourceMySQLParameters()
            self.source_my_sqlparameters = temp_model.from_map(m.get('SourceMySQLParameters'))

        if m.get('SourceOSSParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSourceSourceOSSParameters()
            self.source_ossparameters = temp_model.from_map(m.get('SourceOSSParameters'))

        if m.get('SourceOpenSourceRabbitMQParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSourceSourceOpenSourceRabbitMQParameters()
            self.source_open_source_rabbit_mqparameters = temp_model.from_map(m.get('SourceOpenSourceRabbitMQParameters'))

        if m.get('SourcePostgreSQLParameters') is not None:
            temp_model = main_models.SourcePostgreSQLParameters()
            self.source_postgre_sqlparameters = temp_model.from_map(m.get('SourcePostgreSQLParameters'))

        if m.get('SourcePrometheusParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSourceSourcePrometheusParameters()
            self.source_prometheus_parameters = temp_model.from_map(m.get('SourcePrometheusParameters'))

        if m.get('SourceRabbitMQMetaParameters') is not None:
            temp_model = main_models.SourceRabbitMQMetaParameters()
            self.source_rabbit_mqmeta_parameters = temp_model.from_map(m.get('SourceRabbitMQMetaParameters'))

        if m.get('SourceRabbitMQMsgSyncParameters') is not None:
            temp_model = main_models.SourceRabbitMQMsgSyncParameters()
            self.source_rabbit_mqmsg_sync_parameters = temp_model.from_map(m.get('SourceRabbitMQMsgSyncParameters'))

        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSourceSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m.get('SourceRabbitMQParameters'))

        if m.get('SourceRocketMQCheckpointParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSourceSourceRocketMQCheckpointParameters()
            self.source_rocket_mqcheckpoint_parameters = temp_model.from_map(m.get('SourceRocketMQCheckpointParameters'))

        if m.get('SourceRocketMQParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSourceSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m.get('SourceRocketMQParameters'))

        if m.get('SourceSLSParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSourceSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m.get('SourceSLSParameters'))

        return self

class GetEventStreamingResponseBodyDataSourceSourceSLSParameters(DaraModel):
    def __init__(
        self,
        consume_position: str = None,
        consumer_group: str = None,
        log_store: str = None,
        project: str = None,
        role_name: str = None,
    ):
        # The starting consumer offset. The value begin indicates the earliest offset, and the value end indicates the latest offset. You can also specify a time in seconds to start consumption.
        self.consume_position = consume_position
        # The consumer group.
        self.consumer_group = consumer_group
        # The Log Service Logstore.
        self.log_store = log_store
        # The Log Service project.
        self.project = project
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the RAM console.
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

        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group

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

        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')

        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

class GetEventStreamingResponseBodyDataSourceSourceRocketMQParameters(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        body_data_type: str = None,
        filter_sql: str = None,
        filter_type: str = None,
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
        network: str = None,
        offset: str = None,
        region_id: str = None,
        security_group_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        self.auth_type = auth_type
        self.body_data_type = body_data_type
        self.filter_sql = filter_sql
        self.filter_type = filter_type
        # The ID of the consumer group in the Message Queue for Apache RocketMQ instance.
        self.group_id = group_id
        self.instance_endpoint = instance_endpoint
        # The ID of the Message Queue for Apache RocketMQ instance.
        self.instance_id = instance_id
        self.instance_network = instance_network
        self.instance_password = instance_password
        self.instance_security_group_id = instance_security_group_id
        self.instance_type = instance_type
        self.instance_username = instance_username
        self.instance_vswitch_ids = instance_vswitch_ids
        self.instance_vpc_id = instance_vpc_id
        self.network = network
        # The consumer offset of messages. Valid values: CONSUME_FROM_LAST_OFFSET: Start consumption from the latest offset. CONSUME_FROM_FIRST_OFFSET: Start consumption from the earliest offset. CONSUME_FROM_TIMESTAMP: Start consumption from the offset at the specified point in time.
        self.offset = offset
        # The region ID of the Message Queue for Apache RocketMQ instance.
        self.region_id = region_id
        self.security_group_id = security_group_id
        # The tags that are used to filter messages.
        self.tag = tag
        # The timestamp of the offset from which consumption starts. This parameter is valid only if you set the Offset parameter to CONSUME_FROM_TIMESTAMP.
        self.timestamp = timestamp
        # The topic to which the message belongs.
        self.topic = topic
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.body_data_type is not None:
            result['BodyDataType'] = self.body_data_type

        if self.filter_sql is not None:
            result['FilterSql'] = self.filter_sql

        if self.filter_type is not None:
            result['FilterType'] = self.filter_type

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

        if self.network is not None:
            result['Network'] = self.network

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('BodyDataType') is not None:
            self.body_data_type = m.get('BodyDataType')

        if m.get('FilterSql') is not None:
            self.filter_sql = m.get('FilterSql')

        if m.get('FilterType') is not None:
            self.filter_type = m.get('FilterType')

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

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetEventStreamingResponseBodyDataSourceSourceRocketMQCheckpointParameters(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
        topics: List[str] = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.region_id = region_id
        self.topics = topics

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.topics is not None:
            result['Topics'] = self.topics

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Topics') is not None:
            self.topics = m.get('Topics')

        return self

class GetEventStreamingResponseBodyDataSourceSourceRabbitMQParameters(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_name: str = None,
        region_id: str = None,
        virtual_host_name: str = None,
    ):
        # The ID of the Message Queue for RabbitMQ instance.
        self.instance_id = instance_id
        # The name of the queue in the Message Queue for RabbitMQ instance.
        self.queue_name = queue_name
        # The region ID of the Message Queue for RabbitMQ instance.
        self.region_id = region_id
        # The vhost name of the Message Queue for RabbitMQ instance.
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

class GetEventStreamingResponseBodyDataSourceSourcePrometheusParameters(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_type: str = None,
        external_labels: str = None,
        labels: str = None,
        region_id: str = None,
        role_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.data_type = data_type
        self.external_labels = external_labels
        self.labels = labels
        self.region_id = region_id
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.external_labels is not None:
            result['ExternalLabels'] = self.external_labels

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('ExternalLabels') is not None:
            self.external_labels = m.get('ExternalLabels')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

class GetEventStreamingResponseBodyDataSourceSourceOpenSourceRabbitMQParameters(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        body_data_type: str = None,
        endpoint: str = None,
        network_type: str = None,
        password: str = None,
        queue_name: str = None,
        security_group_id: str = None,
        username: str = None,
        v_switch_ids: str = None,
        virtual_host_name: str = None,
        vpc_id: str = None,
    ):
        self.auth_type = auth_type
        self.body_data_type = body_data_type
        self.endpoint = endpoint
        self.network_type = network_type
        self.password = password
        self.queue_name = queue_name
        self.security_group_id = security_group_id
        self.username = username
        self.v_switch_ids = v_switch_ids
        self.virtual_host_name = virtual_host_name
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.body_data_type is not None:
            result['BodyDataType'] = self.body_data_type

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.password is not None:
            result['Password'] = self.password

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.username is not None:
            result['Username'] = self.username

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('BodyDataType') is not None:
            self.body_data_type = m.get('BodyDataType')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetEventStreamingResponseBodyDataSourceSourceOSSParameters(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        delimiter: str = None,
        load_format: str = None,
        load_mode: str = None,
        prefix: str = None,
        role_name: str = None,
    ):
        self.bucket_name = bucket_name
        self.delimiter = delimiter
        self.load_format = load_format
        self.load_mode = load_mode
        self.prefix = prefix
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.delimiter is not None:
            result['Delimiter'] = self.delimiter

        if self.load_format is not None:
            result['LoadFormat'] = self.load_format

        if self.load_mode is not None:
            result['LoadMode'] = self.load_mode

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('Delimiter') is not None:
            self.delimiter = m.get('Delimiter')

        if m.get('LoadFormat') is not None:
            self.load_format = m.get('LoadFormat')

        if m.get('LoadMode') is not None:
            self.load_mode = m.get('LoadMode')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

class GetEventStreamingResponseBodyDataSourceSourceMQTTParameters(DaraModel):
    def __init__(
        self,
        body_data_type: str = None,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        self.body_data_type = body_data_type
        # The instance ID.
        self.instance_id = instance_id
        # The region ID of the Message Queue for MQTT instance.
        self.region_id = region_id
        # The name of the topic in the Message Queue for MQTT instance.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body_data_type is not None:
            result['BodyDataType'] = self.body_data_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyDataType') is not None:
            self.body_data_type = m.get('BodyDataType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class GetEventStreamingResponseBodyDataSourceSourceMNSParameters(DaraModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        # Indicates whether Base64 encoding is enabled.
        self.is_base_64decode = is_base_64decode
        # The name of the MNS queue.
        self.queue_name = queue_name
        # The region ID of the MNS queue.
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

class GetEventStreamingResponseBodyDataSourceSourceKafkaParameters(DaraModel):
    def __init__(
        self,
        consumer_group: str = None,
        instance_id: str = None,
        network: str = None,
        offset_reset: str = None,
        region_id: str = None,
        security_group_id: str = None,
        topic: str = None,
        v_switch_ids: str = None,
        value_data_type: str = None,
        vpc_id: str = None,
    ):
        # The ID of the consumer group that subscribes to the topic.
        self.consumer_group = consumer_group
        # The instance ID.
        self.instance_id = instance_id
        # The network. Default value: Default. The value PublicNetwork specifies a virtual private cloud (VPC).
        self.network = network
        # The offset.
        self.offset_reset = offset_reset
        # The region ID of the Message Queue for Apache Kafka instance.
        self.region_id = region_id
        # The security group ID.
        self.security_group_id = security_group_id
        # The name of the topic.
        self.topic = topic
        # The vSwitch ID.
        self.v_switch_ids = v_switch_ids
        # The encoding or decoding format. Valid values: Json, Text, and Binary. The value Json indicates that bytes are decoded into UTF-8 strings and then parsed into JSON format. The value Text indicates that bytes are decoded into UTF-8 strings and then put into the payload. The value Binary indicates that bytes are encoded into Base64 strings and put into the payload.
        self.value_data_type = value_data_type
        # The ID of the virtual private cloud (VPC).
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

        if self.value_data_type is not None:
            result['ValueDataType'] = self.value_data_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

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

        if m.get('ValueDataType') is not None:
            self.value_data_type = m.get('ValueDataType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetEventStreamingResponseBodyDataSourceSourceEventBusParameters(DaraModel):
    def __init__(
        self,
        event_bus_name: str = None,
        event_rule_name: str = None,
    ):
        self.event_bus_name = event_bus_name
        self.event_rule_name = event_rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.event_rule_name is not None:
            result['EventRuleName'] = self.event_rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('EventRuleName') is not None:
            self.event_rule_name = m.get('EventRuleName')

        return self

class GetEventStreamingResponseBodyDataSourceSourceDTSParameters(DaraModel):
    def __init__(
        self,
        broker_url: str = None,
        init_check_point: str = None,
        password: str = None,
        sid: str = None,
        task_id: str = None,
        topic: str = None,
        username: str = None,
    ):
        # The URL and port number of the data subscription channel.
        self.broker_url = broker_url
        # The consumer offset. A consumer offset is a timestamp that indicates when the SDK client consumes the first data record. The value is a UNIX timestamp.
        self.init_check_point = init_check_point
        # The password of the consumer group.
        self.password = password
        # The ID of the consumer group.
        self.sid = sid
        # The task ID.
        self.task_id = task_id
        # The topic to which you want to subscribe by using the data subscription channel.
        self.topic = topic
        # The account of the consumer group.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.broker_url is not None:
            result['BrokerUrl'] = self.broker_url

        if self.init_check_point is not None:
            result['InitCheckPoint'] = self.init_check_point

        if self.password is not None:
            result['Password'] = self.password

        if self.sid is not None:
            result['Sid'] = self.sid

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrokerUrl') is not None:
            self.broker_url = m.get('BrokerUrl')

        if m.get('InitCheckPoint') is not None:
            self.init_check_point = m.get('InitCheckPoint')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Sid') is not None:
            self.sid = m.get('Sid')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class GetEventStreamingResponseBodyDataSourceSourceCustomizedKafkaParameters(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class GetEventStreamingResponseBodyDataSourceSourceCustomizedKafkaConnectorParameters(DaraModel):
    def __init__(
        self,
        connector_package_url: str = None,
        connector_parameters: main_models.GetEventStreamingResponseBodyDataSourceSourceCustomizedKafkaConnectorParametersConnectorParameters = None,
        worker_parameters: Dict[str, Any] = None,
    ):
        self.connector_package_url = connector_package_url
        self.connector_parameters = connector_parameters
        self.worker_parameters = worker_parameters

    def validate(self):
        if self.connector_parameters:
            self.connector_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_package_url is not None:
            result['ConnectorPackageUrl'] = self.connector_package_url

        if self.connector_parameters is not None:
            result['ConnectorParameters'] = self.connector_parameters.to_map()

        if self.worker_parameters is not None:
            result['WorkerParameters'] = self.worker_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorPackageUrl') is not None:
            self.connector_package_url = m.get('ConnectorPackageUrl')

        if m.get('ConnectorParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSourceSourceCustomizedKafkaConnectorParametersConnectorParameters()
            self.connector_parameters = temp_model.from_map(m.get('ConnectorParameters'))

        if m.get('WorkerParameters') is not None:
            self.worker_parameters = m.get('WorkerParameters')

        return self

class GetEventStreamingResponseBodyDataSourceSourceCustomizedKafkaConnectorParametersConnectorParameters(DaraModel):
    def __init__(
        self,
        config: Dict[str, Any] = None,
        name: str = None,
    ):
        self.config = config
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetEventStreamingResponseBodyDataSourceSourceApacheRocketMQCheckpointParameters(DaraModel):
    def __init__(
        self,
        instance_endpoint: str = None,
        instance_id: str = None,
        instance_password: str = None,
        instance_username: str = None,
        network_type: str = None,
        region_id: str = None,
        security_group_id: str = None,
        topics: List[str] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.instance_endpoint = instance_endpoint
        # The ID of the Apache RocketMQ instance.
        self.instance_id = instance_id
        self.instance_password = instance_password
        self.instance_username = instance_username
        self.network_type = network_type
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.topics = topics
        self.v_switch_id = v_switch_id
        # VPC ID。
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password

        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.topics is not None:
            result['Topics'] = self.topics

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')

        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Topics') is not None:
            self.topics = m.get('Topics')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetEventStreamingResponseBodyDataSourceSourceApacheKafkaParameters(DaraModel):
    def __init__(
        self,
        bootstraps: str = None,
        consumer_group: str = None,
        network_type: str = None,
        offset_reset: str = None,
        sasl_mechanism: str = None,
        sasl_password: str = None,
        sasl_user: str = None,
        security_group_id: str = None,
        security_protocol: str = None,
        ssl_truststore_certificates: str = None,
        topic: str = None,
        v_switch_ids: str = None,
        value_data_type: str = None,
        vpc_id: str = None,
    ):
        self.bootstraps = bootstraps
        self.consumer_group = consumer_group
        self.network_type = network_type
        self.offset_reset = offset_reset
        self.sasl_mechanism = sasl_mechanism
        self.sasl_password = sasl_password
        self.sasl_user = sasl_user
        self.security_group_id = security_group_id
        self.security_protocol = security_protocol
        self.ssl_truststore_certificates = ssl_truststore_certificates
        self.topic = topic
        self.v_switch_ids = v_switch_ids
        self.value_data_type = value_data_type
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bootstraps is not None:
            result['Bootstraps'] = self.bootstraps

        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset

        if self.sasl_mechanism is not None:
            result['SaslMechanism'] = self.sasl_mechanism

        if self.sasl_password is not None:
            result['SaslPassword'] = self.sasl_password

        if self.sasl_user is not None:
            result['SaslUser'] = self.sasl_user

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_protocol is not None:
            result['SecurityProtocol'] = self.security_protocol

        if self.ssl_truststore_certificates is not None:
            result['SslTruststoreCertificates'] = self.ssl_truststore_certificates

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.value_data_type is not None:
            result['ValueDataType'] = self.value_data_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bootstraps') is not None:
            self.bootstraps = m.get('Bootstraps')

        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')

        if m.get('SaslMechanism') is not None:
            self.sasl_mechanism = m.get('SaslMechanism')

        if m.get('SaslPassword') is not None:
            self.sasl_password = m.get('SaslPassword')

        if m.get('SaslUser') is not None:
            self.sasl_user = m.get('SaslUser')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityProtocol') is not None:
            self.security_protocol = m.get('SecurityProtocol')

        if m.get('SslTruststoreCertificates') is not None:
            self.ssl_truststore_certificates = m.get('SslTruststoreCertificates')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('ValueDataType') is not None:
            self.value_data_type = m.get('ValueDataType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetEventStreamingResponseBodyDataSink(DaraModel):
    def __init__(
        self,
        sink_apache_kafka_parameters: main_models.GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParameters = None,
        sink_apache_rocket_mqcheckpoint_parameters: main_models.GetEventStreamingResponseBodyDataSinkSinkApacheRocketMQCheckpointParameters = None,
        sink_api_destination_parameters: main_models.SinkApiDestinationParameters = None,
        sink_bai_lian_parameters: main_models.SinkBaiLianParameters = None,
        sink_customized_kafka_connector_parameters: main_models.GetEventStreamingResponseBodyDataSinkSinkCustomizedKafkaConnectorParameters = None,
        sink_customized_kafka_parameters: main_models.GetEventStreamingResponseBodyDataSinkSinkCustomizedKafkaParameters = None,
        sink_dash_vector_parameters: main_models.GetEventStreamingResponseBodyDataSinkSinkDashVectorParameters = None,
        sink_data_hub_parameters: main_models.GetEventStreamingResponseBodyDataSinkSinkDataHubParameters = None,
        sink_data_works_trigger_parameters: main_models.SinkDataWorksTriggerParameters = None,
        sink_doris_parameters: main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParameters = None,
        sink_fc_parameters: main_models.GetEventStreamingResponseBodyDataSinkSinkFcParameters = None,
        sink_fnf_parameters: main_models.GetEventStreamingResponseBodyDataSinkSinkFnfParameters = None,
        sink_https_parameters: main_models.SinkHttpsParameters = None,
        sink_kafka_parameters: main_models.GetEventStreamingResponseBodyDataSinkSinkKafkaParameters = None,
        sink_mnsparameters: main_models.GetEventStreamingResponseBodyDataSinkSinkMNSParameters = None,
        sink_ossparameters: main_models.SinkOSSParameters = None,
        sink_open_source_rabbit_mqparameters: main_models.GetEventStreamingResponseBodyDataSinkSinkOpenSourceRabbitMQParameters = None,
        sink_rabbit_mqmeta_parameters: main_models.SinkRabbitMQMetaParameters = None,
        sink_rabbit_mqmsg_sync_parameters: main_models.SinkRabbitMQMsgSyncParameters = None,
        sink_rabbit_mqparameters: main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParameters = None,
        sink_rocket_mqcheckpoint_parameters: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQCheckpointParameters = None,
        sink_rocket_mqparameters: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParameters = None,
        sink_slsparameters: main_models.GetEventStreamingResponseBodyDataSinkSinkSLSParameters = None,
    ):
        self.sink_apache_kafka_parameters = sink_apache_kafka_parameters
        # Sink Apache RocketMQ Checkpoint Parameters
        self.sink_apache_rocket_mqcheckpoint_parameters = sink_apache_rocket_mqcheckpoint_parameters
        self.sink_api_destination_parameters = sink_api_destination_parameters
        # Sink BaiLian Parameters
        self.sink_bai_lian_parameters = sink_bai_lian_parameters
        self.sink_customized_kafka_connector_parameters = sink_customized_kafka_connector_parameters
        self.sink_customized_kafka_parameters = sink_customized_kafka_parameters
        self.sink_dash_vector_parameters = sink_dash_vector_parameters
        self.sink_data_hub_parameters = sink_data_hub_parameters
        self.sink_data_works_trigger_parameters = sink_data_works_trigger_parameters
        self.sink_doris_parameters = sink_doris_parameters
        # The parameters that are returned if the event target is Function Compute.
        self.sink_fc_parameters = sink_fc_parameters
        # The Sink Fnf parameters.
        self.sink_fnf_parameters = sink_fnf_parameters
        self.sink_https_parameters = sink_https_parameters
        # The parameters that are returned if the event target is Message Queue for Apache Kafka.
        self.sink_kafka_parameters = sink_kafka_parameters
        # The parameters that are returned if the event target is Message Service (MNS).
        self.sink_mnsparameters = sink_mnsparameters
        self.sink_ossparameters = sink_ossparameters
        # Sink Open Source RabbitMQ Parameters
        self.sink_open_source_rabbit_mqparameters = sink_open_source_rabbit_mqparameters
        self.sink_rabbit_mqmeta_parameters = sink_rabbit_mqmeta_parameters
        self.sink_rabbit_mqmsg_sync_parameters = sink_rabbit_mqmsg_sync_parameters
        # The parameters that are returned if the event target is Message Queue for RabbitMQ.
        self.sink_rabbit_mqparameters = sink_rabbit_mqparameters
        # Sink RocketMQ Checkpoint Parameters
        self.sink_rocket_mqcheckpoint_parameters = sink_rocket_mqcheckpoint_parameters
        # The parameters that are returned if ApsaraMQ for RocketMQ is specified as the event target.
        self.sink_rocket_mqparameters = sink_rocket_mqparameters
        # The parameters that are returned if Simple Log Service is specified as the event target.
        self.sink_slsparameters = sink_slsparameters

    def validate(self):
        if self.sink_apache_kafka_parameters:
            self.sink_apache_kafka_parameters.validate()
        if self.sink_apache_rocket_mqcheckpoint_parameters:
            self.sink_apache_rocket_mqcheckpoint_parameters.validate()
        if self.sink_api_destination_parameters:
            self.sink_api_destination_parameters.validate()
        if self.sink_bai_lian_parameters:
            self.sink_bai_lian_parameters.validate()
        if self.sink_customized_kafka_connector_parameters:
            self.sink_customized_kafka_connector_parameters.validate()
        if self.sink_customized_kafka_parameters:
            self.sink_customized_kafka_parameters.validate()
        if self.sink_dash_vector_parameters:
            self.sink_dash_vector_parameters.validate()
        if self.sink_data_hub_parameters:
            self.sink_data_hub_parameters.validate()
        if self.sink_data_works_trigger_parameters:
            self.sink_data_works_trigger_parameters.validate()
        if self.sink_doris_parameters:
            self.sink_doris_parameters.validate()
        if self.sink_fc_parameters:
            self.sink_fc_parameters.validate()
        if self.sink_fnf_parameters:
            self.sink_fnf_parameters.validate()
        if self.sink_https_parameters:
            self.sink_https_parameters.validate()
        if self.sink_kafka_parameters:
            self.sink_kafka_parameters.validate()
        if self.sink_mnsparameters:
            self.sink_mnsparameters.validate()
        if self.sink_ossparameters:
            self.sink_ossparameters.validate()
        if self.sink_open_source_rabbit_mqparameters:
            self.sink_open_source_rabbit_mqparameters.validate()
        if self.sink_rabbit_mqmeta_parameters:
            self.sink_rabbit_mqmeta_parameters.validate()
        if self.sink_rabbit_mqmsg_sync_parameters:
            self.sink_rabbit_mqmsg_sync_parameters.validate()
        if self.sink_rabbit_mqparameters:
            self.sink_rabbit_mqparameters.validate()
        if self.sink_rocket_mqcheckpoint_parameters:
            self.sink_rocket_mqcheckpoint_parameters.validate()
        if self.sink_rocket_mqparameters:
            self.sink_rocket_mqparameters.validate()
        if self.sink_slsparameters:
            self.sink_slsparameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sink_apache_kafka_parameters is not None:
            result['SinkApacheKafkaParameters'] = self.sink_apache_kafka_parameters.to_map()

        if self.sink_apache_rocket_mqcheckpoint_parameters is not None:
            result['SinkApacheRocketMQCheckpointParameters'] = self.sink_apache_rocket_mqcheckpoint_parameters.to_map()

        if self.sink_api_destination_parameters is not None:
            result['SinkApiDestinationParameters'] = self.sink_api_destination_parameters.to_map()

        if self.sink_bai_lian_parameters is not None:
            result['SinkBaiLianParameters'] = self.sink_bai_lian_parameters.to_map()

        if self.sink_customized_kafka_connector_parameters is not None:
            result['SinkCustomizedKafkaConnectorParameters'] = self.sink_customized_kafka_connector_parameters.to_map()

        if self.sink_customized_kafka_parameters is not None:
            result['SinkCustomizedKafkaParameters'] = self.sink_customized_kafka_parameters.to_map()

        if self.sink_dash_vector_parameters is not None:
            result['SinkDashVectorParameters'] = self.sink_dash_vector_parameters.to_map()

        if self.sink_data_hub_parameters is not None:
            result['SinkDataHubParameters'] = self.sink_data_hub_parameters.to_map()

        if self.sink_data_works_trigger_parameters is not None:
            result['SinkDataWorksTriggerParameters'] = self.sink_data_works_trigger_parameters.to_map()

        if self.sink_doris_parameters is not None:
            result['SinkDorisParameters'] = self.sink_doris_parameters.to_map()

        if self.sink_fc_parameters is not None:
            result['SinkFcParameters'] = self.sink_fc_parameters.to_map()

        if self.sink_fnf_parameters is not None:
            result['SinkFnfParameters'] = self.sink_fnf_parameters.to_map()

        if self.sink_https_parameters is not None:
            result['SinkHttpsParameters'] = self.sink_https_parameters.to_map()

        if self.sink_kafka_parameters is not None:
            result['SinkKafkaParameters'] = self.sink_kafka_parameters.to_map()

        if self.sink_mnsparameters is not None:
            result['SinkMNSParameters'] = self.sink_mnsparameters.to_map()

        if self.sink_ossparameters is not None:
            result['SinkOSSParameters'] = self.sink_ossparameters.to_map()

        if self.sink_open_source_rabbit_mqparameters is not None:
            result['SinkOpenSourceRabbitMQParameters'] = self.sink_open_source_rabbit_mqparameters.to_map()

        if self.sink_rabbit_mqmeta_parameters is not None:
            result['SinkRabbitMQMetaParameters'] = self.sink_rabbit_mqmeta_parameters.to_map()

        if self.sink_rabbit_mqmsg_sync_parameters is not None:
            result['SinkRabbitMQMsgSyncParameters'] = self.sink_rabbit_mqmsg_sync_parameters.to_map()

        if self.sink_rabbit_mqparameters is not None:
            result['SinkRabbitMQParameters'] = self.sink_rabbit_mqparameters.to_map()

        if self.sink_rocket_mqcheckpoint_parameters is not None:
            result['SinkRocketMQCheckpointParameters'] = self.sink_rocket_mqcheckpoint_parameters.to_map()

        if self.sink_rocket_mqparameters is not None:
            result['SinkRocketMQParameters'] = self.sink_rocket_mqparameters.to_map()

        if self.sink_slsparameters is not None:
            result['SinkSLSParameters'] = self.sink_slsparameters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SinkApacheKafkaParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParameters()
            self.sink_apache_kafka_parameters = temp_model.from_map(m.get('SinkApacheKafkaParameters'))

        if m.get('SinkApacheRocketMQCheckpointParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkApacheRocketMQCheckpointParameters()
            self.sink_apache_rocket_mqcheckpoint_parameters = temp_model.from_map(m.get('SinkApacheRocketMQCheckpointParameters'))

        if m.get('SinkApiDestinationParameters') is not None:
            temp_model = main_models.SinkApiDestinationParameters()
            self.sink_api_destination_parameters = temp_model.from_map(m.get('SinkApiDestinationParameters'))

        if m.get('SinkBaiLianParameters') is not None:
            temp_model = main_models.SinkBaiLianParameters()
            self.sink_bai_lian_parameters = temp_model.from_map(m.get('SinkBaiLianParameters'))

        if m.get('SinkCustomizedKafkaConnectorParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkCustomizedKafkaConnectorParameters()
            self.sink_customized_kafka_connector_parameters = temp_model.from_map(m.get('SinkCustomizedKafkaConnectorParameters'))

        if m.get('SinkCustomizedKafkaParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkCustomizedKafkaParameters()
            self.sink_customized_kafka_parameters = temp_model.from_map(m.get('SinkCustomizedKafkaParameters'))

        if m.get('SinkDashVectorParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDashVectorParameters()
            self.sink_dash_vector_parameters = temp_model.from_map(m.get('SinkDashVectorParameters'))

        if m.get('SinkDataHubParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDataHubParameters()
            self.sink_data_hub_parameters = temp_model.from_map(m.get('SinkDataHubParameters'))

        if m.get('SinkDataWorksTriggerParameters') is not None:
            temp_model = main_models.SinkDataWorksTriggerParameters()
            self.sink_data_works_trigger_parameters = temp_model.from_map(m.get('SinkDataWorksTriggerParameters'))

        if m.get('SinkDorisParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParameters()
            self.sink_doris_parameters = temp_model.from_map(m.get('SinkDorisParameters'))

        if m.get('SinkFcParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkFcParameters()
            self.sink_fc_parameters = temp_model.from_map(m.get('SinkFcParameters'))

        if m.get('SinkFnfParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkFnfParameters()
            self.sink_fnf_parameters = temp_model.from_map(m.get('SinkFnfParameters'))

        if m.get('SinkHttpsParameters') is not None:
            temp_model = main_models.SinkHttpsParameters()
            self.sink_https_parameters = temp_model.from_map(m.get('SinkHttpsParameters'))

        if m.get('SinkKafkaParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkKafkaParameters()
            self.sink_kafka_parameters = temp_model.from_map(m.get('SinkKafkaParameters'))

        if m.get('SinkMNSParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkMNSParameters()
            self.sink_mnsparameters = temp_model.from_map(m.get('SinkMNSParameters'))

        if m.get('SinkOSSParameters') is not None:
            temp_model = main_models.SinkOSSParameters()
            self.sink_ossparameters = temp_model.from_map(m.get('SinkOSSParameters'))

        if m.get('SinkOpenSourceRabbitMQParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkOpenSourceRabbitMQParameters()
            self.sink_open_source_rabbit_mqparameters = temp_model.from_map(m.get('SinkOpenSourceRabbitMQParameters'))

        if m.get('SinkRabbitMQMetaParameters') is not None:
            temp_model = main_models.SinkRabbitMQMetaParameters()
            self.sink_rabbit_mqmeta_parameters = temp_model.from_map(m.get('SinkRabbitMQMetaParameters'))

        if m.get('SinkRabbitMQMsgSyncParameters') is not None:
            temp_model = main_models.SinkRabbitMQMsgSyncParameters()
            self.sink_rabbit_mqmsg_sync_parameters = temp_model.from_map(m.get('SinkRabbitMQMsgSyncParameters'))

        if m.get('SinkRabbitMQParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParameters()
            self.sink_rabbit_mqparameters = temp_model.from_map(m.get('SinkRabbitMQParameters'))

        if m.get('SinkRocketMQCheckpointParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQCheckpointParameters()
            self.sink_rocket_mqcheckpoint_parameters = temp_model.from_map(m.get('SinkRocketMQCheckpointParameters'))

        if m.get('SinkRocketMQParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParameters()
            self.sink_rocket_mqparameters = temp_model.from_map(m.get('SinkRocketMQParameters'))

        if m.get('SinkSLSParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkSLSParameters()
            self.sink_slsparameters = temp_model.from_map(m.get('SinkSLSParameters'))

        return self

class GetEventStreamingResponseBodyDataSinkSinkSLSParameters(DaraModel):
    def __init__(
        self,
        body: main_models.GetEventStreamingResponseBodyDataSinkSinkSLSParametersBody = None,
        content_schema: main_models.GetEventStreamingResponseBodyDataSinkSinkSLSParametersContentSchema = None,
        content_type: main_models.GetEventStreamingResponseBodyDataSinkSinkSLSParametersContentType = None,
        log_store: main_models.GetEventStreamingResponseBodyDataSinkSinkSLSParametersLogStore = None,
        project: main_models.GetEventStreamingResponseBodyDataSinkSinkSLSParametersProject = None,
        role_name: main_models.GetEventStreamingResponseBodyDataSinkSinkSLSParametersRoleName = None,
        topic: main_models.GetEventStreamingResponseBodyDataSinkSinkSLSParametersTopic = None,
    ):
        # The message content.
        self.body = body
        self.content_schema = content_schema
        self.content_type = content_type
        # The Simple Log Service Logstore.
        self.log_store = log_store
        # The Simple Log Service project.
        self.project = project
        # The role name. If you want to authorize EventBridge to use this role to read logs in Simple Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the Resource Access Management (RAM) console.
        self.role_name = role_name
        # The name of the topic in which logs are stored. The topic corresponds to the topic reserved field in Simple Log Service.
        self.topic = topic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.content_schema:
            self.content_schema.validate()
        if self.content_type:
            self.content_type.validate()
        if self.log_store:
            self.log_store.validate()
        if self.project:
            self.project.validate()
        if self.role_name:
            self.role_name.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body.to_map()

        if self.content_schema is not None:
            result['ContentSchema'] = self.content_schema.to_map()

        if self.content_type is not None:
            result['ContentType'] = self.content_type.to_map()

        if self.log_store is not None:
            result['LogStore'] = self.log_store.to_map()

        if self.project is not None:
            result['Project'] = self.project.to_map()

        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()

        if self.topic is not None:
            result['Topic'] = self.topic.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkSLSParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('ContentSchema') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkSLSParametersContentSchema()
            self.content_schema = temp_model.from_map(m.get('ContentSchema'))

        if m.get('ContentType') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkSLSParametersContentType()
            self.content_type = temp_model.from_map(m.get('ContentType'))

        if m.get('LogStore') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkSLSParametersLogStore()
            self.log_store = temp_model.from_map(m.get('LogStore'))

        if m.get('Project') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkSLSParametersProject()
            self.project = temp_model.from_map(m.get('Project'))

        if m.get('RoleName') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkSLSParametersRoleName()
            self.role_name = temp_model.from_map(m.get('RoleName'))

        if m.get('Topic') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkSLSParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        return self

class GetEventStreamingResponseBodyDataSinkSinkSLSParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The name of the topic in which logs are stored. The topic corresponds to the topic reserved field in Log Service.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkSLSParametersRoleName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the RAM console.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkSLSParametersProject(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The Log Service project.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkSLSParametersLogStore(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The Log Service Logstore.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkSLSParametersContentType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkSLSParametersContentSchema(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkSLSParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQParameters(DaraModel):
    def __init__(
        self,
        body: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersBody = None,
        delivery_order_type: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersDeliveryOrderType = None,
        instance_endpoint: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceEndpoint = None,
        instance_id: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceId = None,
        instance_password: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstancePassword = None,
        instance_type: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceType = None,
        instance_username: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceUsername = None,
        keys: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersKeys = None,
        network: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersNetwork = None,
        properties: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersProperties = None,
        security_group_id: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersSecurityGroupId = None,
        sharding_key: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersShardingKey = None,
        tags: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTags = None,
        topic: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTopic = None,
        v_switch_ids: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersVSwitchIds = None,
        vpc_id: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersVpcId = None,
    ):
        # The message content.
        self.body = body
        self.delivery_order_type = delivery_order_type
        self.instance_endpoint = instance_endpoint
        # The target service type is Message Queue for Apache RocketMQ.
        self.instance_id = instance_id
        self.instance_password = instance_password
        self.instance_type = instance_type
        self.instance_username = instance_username
        # The tags that are used to filter messages.
        self.keys = keys
        self.network = network
        # The tags that are used to filter messages.
        self.properties = properties
        self.security_group_id = security_group_id
        self.sharding_key = sharding_key
        # The tags that are used to filter messages.
        self.tags = tags
        # The name of the topic in the Message Queue for Apache RocketMQ instance.
        self.topic = topic
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        if self.body:
            self.body.validate()
        if self.delivery_order_type:
            self.delivery_order_type.validate()
        if self.instance_endpoint:
            self.instance_endpoint.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.instance_password:
            self.instance_password.validate()
        if self.instance_type:
            self.instance_type.validate()
        if self.instance_username:
            self.instance_username.validate()
        if self.keys:
            self.keys.validate()
        if self.network:
            self.network.validate()
        if self.properties:
            self.properties.validate()
        if self.security_group_id:
            self.security_group_id.validate()
        if self.sharding_key:
            self.sharding_key.validate()
        if self.tags:
            self.tags.validate()
        if self.topic:
            self.topic.validate()
        if self.v_switch_ids:
            self.v_switch_ids.validate()
        if self.vpc_id:
            self.vpc_id.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body.to_map()

        if self.delivery_order_type is not None:
            result['DeliveryOrderType'] = self.delivery_order_type.to_map()

        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()

        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password.to_map()

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type.to_map()

        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username.to_map()

        if self.keys is not None:
            result['Keys'] = self.keys.to_map()

        if self.network is not None:
            result['Network'] = self.network.to_map()

        if self.properties is not None:
            result['Properties'] = self.properties.to_map()

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id.to_map()

        if self.sharding_key is not None:
            result['ShardingKey'] = self.sharding_key.to_map()

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.topic is not None:
            result['Topic'] = self.topic.to_map()

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('DeliveryOrderType') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersDeliveryOrderType()
            self.delivery_order_type = temp_model.from_map(m.get('DeliveryOrderType'))

        if m.get('InstanceEndpoint') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceEndpoint()
            self.instance_endpoint = temp_model.from_map(m.get('InstanceEndpoint'))

        if m.get('InstanceId') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m.get('InstanceId'))

        if m.get('InstancePassword') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstancePassword()
            self.instance_password = temp_model.from_map(m.get('InstancePassword'))

        if m.get('InstanceType') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceType()
            self.instance_type = temp_model.from_map(m.get('InstanceType'))

        if m.get('InstanceUsername') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceUsername()
            self.instance_username = temp_model.from_map(m.get('InstanceUsername'))

        if m.get('Keys') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersKeys()
            self.keys = temp_model.from_map(m.get('Keys'))

        if m.get('Network') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        if m.get('Properties') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('SecurityGroupId') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersSecurityGroupId()
            self.security_group_id = temp_model.from_map(m.get('SecurityGroupId'))

        if m.get('ShardingKey') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersShardingKey()
            self.sharding_key = temp_model.from_map(m.get('ShardingKey'))

        if m.get('Tags') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Topic') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        if m.get('VpcId') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersVpcId()
            self.vpc_id = temp_model.from_map(m.get('VpcId'))

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersVpcId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersVSwitchIds(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The name of the topic in the Message Queue for Apache RocketMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTags(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersShardingKey(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersSecurityGroupId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersProperties(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersNetwork(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersKeys(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceUsername(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstancePassword(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The ID of the Message Queue for Apache RocketMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceEndpoint(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersDeliveryOrderType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQCheckpointParameters(DaraModel):
    def __init__(
        self,
        consume_timestamp: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQCheckpointParametersConsumeTimestamp = None,
        group: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQCheckpointParametersGroup = None,
        instance_id: str = None,
        instance_type: str = None,
        topic: main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQCheckpointParametersTopic = None,
    ):
        self.consume_timestamp = consume_timestamp
        self.group = group
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.topic = topic

    def validate(self):
        if self.consume_timestamp:
            self.consume_timestamp.validate()
        if self.group:
            self.group.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consume_timestamp is not None:
            result['ConsumeTimestamp'] = self.consume_timestamp.to_map()

        if self.group is not None:
            result['Group'] = self.group.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.topic is not None:
            result['Topic'] = self.topic.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumeTimestamp') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQCheckpointParametersConsumeTimestamp()
            self.consume_timestamp = temp_model.from_map(m.get('ConsumeTimestamp'))

        if m.get('Group') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQCheckpointParametersGroup()
            self.group = temp_model.from_map(m.get('Group'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Topic') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRocketMQCheckpointParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQCheckpointParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQCheckpointParametersGroup(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        # Group ID
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRocketMQCheckpointParametersConsumeTimestamp(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParameters(DaraModel):
    def __init__(
        self,
        body: main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersBody = None,
        exchange: main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersExchange = None,
        instance_id: main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersInstanceId = None,
        message_id: main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersMessageId = None,
        properties: main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersProperties = None,
        queue_name: main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersQueueName = None,
        routing_key: main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersRoutingKey = None,
        target_type: main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersTargetType = None,
        virtual_host_name: main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersVirtualHostName = None,
    ):
        # The message content.
        self.body = body
        # The exchange mode. This parameter is available only if TargetType is set to Exchange.
        self.exchange = exchange
        # The target service type is Message Queue for RabbitMQ instance.
        self.instance_id = instance_id
        # The message ID.
        self.message_id = message_id
        # The tags that are used to filter messages.
        self.properties = properties
        # The queue mode. This parameter is available only if TargetType is set to Queue.
        self.queue_name = queue_name
        # The routing rule for the message. This parameter is available only if TargetType is set to Exchange.
        self.routing_key = routing_key
        # The target type.
        self.target_type = target_type
        # The name of the vhost of the Message Queue for RabbitMQ instance.
        self.virtual_host_name = virtual_host_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.exchange:
            self.exchange.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.message_id:
            self.message_id.validate()
        if self.properties:
            self.properties.validate()
        if self.queue_name:
            self.queue_name.validate()
        if self.routing_key:
            self.routing_key.validate()
        if self.target_type:
            self.target_type.validate()
        if self.virtual_host_name:
            self.virtual_host_name.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body.to_map()

        if self.exchange is not None:
            result['Exchange'] = self.exchange.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()

        if self.message_id is not None:
            result['MessageId'] = self.message_id.to_map()

        if self.properties is not None:
            result['Properties'] = self.properties.to_map()

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()

        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key.to_map()

        if self.target_type is not None:
            result['TargetType'] = self.target_type.to_map()

        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Exchange') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersExchange()
            self.exchange = temp_model.from_map(m.get('Exchange'))

        if m.get('InstanceId') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m.get('InstanceId'))

        if m.get('MessageId') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m.get('MessageId'))

        if m.get('Properties') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('QueueName') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersQueueName()
            self.queue_name = temp_model.from_map(m.get('QueueName'))

        if m.get('RoutingKey') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersRoutingKey()
            self.routing_key = temp_model.from_map(m.get('RoutingKey'))

        if m.get('TargetType') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersTargetType()
            self.target_type = temp_model.from_map(m.get('TargetType'))

        if m.get('VirtualHostName') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersVirtualHostName()
            self.virtual_host_name = temp_model.from_map(m.get('VirtualHostName'))

        return self

class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersVirtualHostName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The vhost name of the Message Queue for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersTargetType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The type of the resource to which the event is delivered. Valid values: Exchange: exchanges. Queue: queues.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersRoutingKey(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The routing rule for the message.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersQueueName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The name of the queue in the Message Queue for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersProperties(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersMessageId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersInstanceId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The ID of the Message Queue for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersExchange(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The name of the exchange in the Message Queue for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkOpenSourceRabbitMQParameters(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        body: main_models.GetEventStreamingResponseBodyDataSinkSinkOpenSourceRabbitMQParametersBody = None,
        endpoint: str = None,
        exchange: str = None,
        message_id: main_models.GetEventStreamingResponseBodyDataSinkSinkOpenSourceRabbitMQParametersMessageId = None,
        network_type: str = None,
        password: str = None,
        properties: main_models.GetEventStreamingResponseBodyDataSinkSinkOpenSourceRabbitMQParametersProperties = None,
        queue_name: str = None,
        routing_key: main_models.GetEventStreamingResponseBodyDataSinkSinkOpenSourceRabbitMQParametersRoutingKey = None,
        security_group_id: str = None,
        target_type: str = None,
        username: str = None,
        v_switch_ids: str = None,
        virtual_host_name: str = None,
        vpc_id: str = None,
    ):
        self.auth_type = auth_type
        self.body = body
        self.endpoint = endpoint
        self.exchange = exchange
        self.message_id = message_id
        self.network_type = network_type
        self.password = password
        self.properties = properties
        self.queue_name = queue_name
        self.routing_key = routing_key
        self.security_group_id = security_group_id
        self.target_type = target_type
        self.username = username
        self.v_switch_ids = v_switch_ids
        self.virtual_host_name = virtual_host_name
        self.vpc_id = vpc_id

    def validate(self):
        if self.body:
            self.body.validate()
        if self.message_id:
            self.message_id.validate()
        if self.properties:
            self.properties.validate()
        if self.routing_key:
            self.routing_key.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.body is not None:
            result['Body'] = self.body.to_map()

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.exchange is not None:
            result['Exchange'] = self.exchange

        if self.message_id is not None:
            result['MessageId'] = self.message_id.to_map()

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.password is not None:
            result['Password'] = self.password

        if self.properties is not None:
            result['Properties'] = self.properties.to_map()

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key.to_map()

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.username is not None:
            result['Username'] = self.username

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('Body') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkOpenSourceRabbitMQParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Exchange') is not None:
            self.exchange = m.get('Exchange')

        if m.get('MessageId') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkOpenSourceRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m.get('MessageId'))

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Properties') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkOpenSourceRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('RoutingKey') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkOpenSourceRabbitMQParametersRoutingKey()
            self.routing_key = temp_model.from_map(m.get('RoutingKey'))

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetEventStreamingResponseBodyDataSinkSinkOpenSourceRabbitMQParametersRoutingKey(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkOpenSourceRabbitMQParametersProperties(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkOpenSourceRabbitMQParametersMessageId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkOpenSourceRabbitMQParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkMNSParameters(DaraModel):
    def __init__(
        self,
        body: main_models.GetEventStreamingResponseBodyDataSinkSinkMNSParametersBody = None,
        is_base_64encode: main_models.GetEventStreamingResponseBodyDataSinkSinkMNSParametersIsBase64Encode = None,
        queue_name: main_models.GetEventStreamingResponseBodyDataSinkSinkMNSParametersQueueName = None,
    ):
        # The message content.
        self.body = body
        # Indicates whether Base64 encoding is enabled.
        self.is_base_64encode = is_base_64encode
        # The target service type is MNS.
        self.queue_name = queue_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.is_base_64encode:
            self.is_base_64encode.validate()
        if self.queue_name:
            self.queue_name.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body.to_map()

        if self.is_base_64encode is not None:
            result['IsBase64Encode'] = self.is_base_64encode.to_map()

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkMNSParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('IsBase64Encode') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkMNSParametersIsBase64Encode()
            self.is_base_64encode = temp_model.from_map(m.get('IsBase64Encode'))

        if m.get('QueueName') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkMNSParametersQueueName()
            self.queue_name = temp_model.from_map(m.get('QueueName'))

        return self

class GetEventStreamingResponseBodyDataSinkSinkMNSParametersQueueName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The name of the MNS queue.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkMNSParametersIsBase64Encode(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # Specifies that Base64 encoding is enabled.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkMNSParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkKafkaParameters(DaraModel):
    def __init__(
        self,
        acks: main_models.GetEventStreamingResponseBodyDataSinkSinkKafkaParametersAcks = None,
        compression_type: str = None,
        headers: main_models.GetEventStreamingResponseBodyDataSinkSinkKafkaParametersHeaders = None,
        instance_id: main_models.GetEventStreamingResponseBodyDataSinkSinkKafkaParametersInstanceId = None,
        key: main_models.GetEventStreamingResponseBodyDataSinkSinkKafkaParametersKey = None,
        topic: main_models.GetEventStreamingResponseBodyDataSinkSinkKafkaParametersTopic = None,
        value: main_models.GetEventStreamingResponseBodyDataSinkSinkKafkaParametersValue = None,
    ):
        # The acknowledgment information.
        self.acks = acks
        self.compression_type = compression_type
        self.headers = headers
        # The target service type is Message Queue for Apache Kafka.
        self.instance_id = instance_id
        # The message key.
        self.key = key
        # The topic name.
        self.topic = topic
        # The message content.
        self.value = value

    def validate(self):
        if self.acks:
            self.acks.validate()
        if self.headers:
            self.headers.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.key:
            self.key.validate()
        if self.topic:
            self.topic.validate()
        if self.value:
            self.value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acks is not None:
            result['Acks'] = self.acks.to_map()

        if self.compression_type is not None:
            result['CompressionType'] = self.compression_type

        if self.headers is not None:
            result['Headers'] = self.headers.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()

        if self.key is not None:
            result['Key'] = self.key.to_map()

        if self.topic is not None:
            result['Topic'] = self.topic.to_map()

        if self.value is not None:
            result['Value'] = self.value.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acks') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkKafkaParametersAcks()
            self.acks = temp_model.from_map(m.get('Acks'))

        if m.get('CompressionType') is not None:
            self.compression_type = m.get('CompressionType')

        if m.get('Headers') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkKafkaParametersHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('InstanceId') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkKafkaParametersInstanceId()
            self.instance_id = temp_model.from_map(m.get('InstanceId'))

        if m.get('Key') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkKafkaParametersKey()
            self.key = temp_model.from_map(m.get('Key'))

        if m.get('Topic') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkKafkaParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        if m.get('Value') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkKafkaParametersValue()
            self.value = temp_model.from_map(m.get('Value'))

        return self

class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersValue(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The topic name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersKey(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The message key.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersInstanceId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The instance ID.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersHeaders(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersAcks(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The acknowledgment information.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkFnfParameters(DaraModel):
    def __init__(
        self,
        execution_name: main_models.GetEventStreamingResponseBodyDataSinkSinkFnfParametersExecutionName = None,
        flow_name: main_models.GetEventStreamingResponseBodyDataSinkSinkFnfParametersFlowName = None,
        input: main_models.GetEventStreamingResponseBodyDataSinkSinkFnfParametersInput = None,
        role_name: main_models.GetEventStreamingResponseBodyDataSinkSinkFnfParametersRoleName = None,
    ):
        # The execution name.
        self.execution_name = execution_name
        # The flow name.
        self.flow_name = flow_name
        # The execution input information.
        self.input = input
        # The role name.
        self.role_name = role_name

    def validate(self):
        if self.execution_name:
            self.execution_name.validate()
        if self.flow_name:
            self.flow_name.validate()
        if self.input:
            self.input.validate()
        if self.role_name:
            self.role_name.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name.to_map()

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name.to_map()

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkFnfParametersExecutionName()
            self.execution_name = temp_model.from_map(m.get('ExecutionName'))

        if m.get('FlowName') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkFnfParametersFlowName()
            self.flow_name = temp_model.from_map(m.get('FlowName'))

        if m.get('Input') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkFnfParametersInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('RoleName') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkFnfParametersRoleName()
            self.role_name = temp_model.from_map(m.get('RoleName'))

        return self

class GetEventStreamingResponseBodyDataSinkSinkFnfParametersRoleName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The role configuration.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkFnfParametersInput(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The execution input information.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkFnfParametersFlowName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The flow name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkFnfParametersExecutionName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The execution name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkFcParameters(DaraModel):
    def __init__(
        self,
        body: main_models.GetEventStreamingResponseBodyDataSinkSinkFcParametersBody = None,
        concurrency: main_models.GetEventStreamingResponseBodyDataSinkSinkFcParametersConcurrency = None,
        data_format: main_models.GetEventStreamingResponseBodyDataSinkSinkFcParametersDataFormat = None,
        function_name: main_models.GetEventStreamingResponseBodyDataSinkSinkFcParametersFunctionName = None,
        invocation_type: main_models.GetEventStreamingResponseBodyDataSinkSinkFcParametersInvocationType = None,
        qualifier: main_models.GetEventStreamingResponseBodyDataSinkSinkFcParametersQualifier = None,
        service_name: main_models.GetEventStreamingResponseBodyDataSinkSinkFcParametersServiceName = None,
    ):
        # The message body that is sent to the function.
        self.body = body
        # The delivery concurrency. Minimum value: 1.
        self.concurrency = concurrency
        self.data_format = data_format
        # The function name.
        self.function_name = function_name
        # The invocation type. Valid values: Sync: synchronous Async: asynchronous
        self.invocation_type = invocation_type
        # The alias of the service to which the function belongs.
        self.qualifier = qualifier
        # The service name.
        self.service_name = service_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.concurrency:
            self.concurrency.validate()
        if self.data_format:
            self.data_format.validate()
        if self.function_name:
            self.function_name.validate()
        if self.invocation_type:
            self.invocation_type.validate()
        if self.qualifier:
            self.qualifier.validate()
        if self.service_name:
            self.service_name.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body.to_map()

        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency.to_map()

        if self.data_format is not None:
            result['DataFormat'] = self.data_format.to_map()

        if self.function_name is not None:
            result['FunctionName'] = self.function_name.to_map()

        if self.invocation_type is not None:
            result['InvocationType'] = self.invocation_type.to_map()

        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier.to_map()

        if self.service_name is not None:
            result['ServiceName'] = self.service_name.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkFcParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Concurrency') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkFcParametersConcurrency()
            self.concurrency = temp_model.from_map(m.get('Concurrency'))

        if m.get('DataFormat') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkFcParametersDataFormat()
            self.data_format = temp_model.from_map(m.get('DataFormat'))

        if m.get('FunctionName') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkFcParametersFunctionName()
            self.function_name = temp_model.from_map(m.get('FunctionName'))

        if m.get('InvocationType') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkFcParametersInvocationType()
            self.invocation_type = temp_model.from_map(m.get('InvocationType'))

        if m.get('Qualifier') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkFcParametersQualifier()
            self.qualifier = temp_model.from_map(m.get('Qualifier'))

        if m.get('ServiceName') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkFcParametersServiceName()
            self.service_name = temp_model.from_map(m.get('ServiceName'))

        return self

class GetEventStreamingResponseBodyDataSinkSinkFcParametersServiceName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The name of the service.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkFcParametersQualifier(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The alias of the service to which the function belongs.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkFcParametersInvocationType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The invocation type.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkFcParametersFunctionName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The function name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkFcParametersDataFormat(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkFcParametersConcurrency(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The delivery concurrency. Minimum value: 1.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkFcParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform the event.
        self.form = form
        # The template based on which the event is transformed.
        self.template = template
        # The value before the transformation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDorisParameters(DaraModel):
    def __init__(
        self,
        be_http_endpoint: main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersBeHttpEndpoint = None,
        body: main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersBody = None,
        database: main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersDatabase = None,
        fe_http_endpoint: main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersFeHttpEndpoint = None,
        network_type: main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersNetworkType = None,
        password: main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersPassword = None,
        query_endpoint: main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersQueryEndpoint = None,
        security_group_id: main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersSecurityGroupId = None,
        table: main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersTable = None,
        user_name: main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersUserName = None,
        v_switch_ids: main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersVSwitchIds = None,
        vpc_id: main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersVpcId = None,
    ):
        self.be_http_endpoint = be_http_endpoint
        self.body = body
        self.database = database
        self.fe_http_endpoint = fe_http_endpoint
        self.network_type = network_type
        self.password = password
        self.query_endpoint = query_endpoint
        self.security_group_id = security_group_id
        self.table = table
        self.user_name = user_name
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        if self.be_http_endpoint:
            self.be_http_endpoint.validate()
        if self.body:
            self.body.validate()
        if self.database:
            self.database.validate()
        if self.fe_http_endpoint:
            self.fe_http_endpoint.validate()
        if self.network_type:
            self.network_type.validate()
        if self.password:
            self.password.validate()
        if self.query_endpoint:
            self.query_endpoint.validate()
        if self.security_group_id:
            self.security_group_id.validate()
        if self.table:
            self.table.validate()
        if self.user_name:
            self.user_name.validate()
        if self.v_switch_ids:
            self.v_switch_ids.validate()
        if self.vpc_id:
            self.vpc_id.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.be_http_endpoint is not None:
            result['BeHttpEndpoint'] = self.be_http_endpoint.to_map()

        if self.body is not None:
            result['Body'] = self.body.to_map()

        if self.database is not None:
            result['Database'] = self.database.to_map()

        if self.fe_http_endpoint is not None:
            result['FeHttpEndpoint'] = self.fe_http_endpoint.to_map()

        if self.network_type is not None:
            result['NetworkType'] = self.network_type.to_map()

        if self.password is not None:
            result['Password'] = self.password.to_map()

        if self.query_endpoint is not None:
            result['QueryEndpoint'] = self.query_endpoint.to_map()

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id.to_map()

        if self.table is not None:
            result['Table'] = self.table.to_map()

        if self.user_name is not None:
            result['UserName'] = self.user_name.to_map()

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeHttpEndpoint') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersBeHttpEndpoint()
            self.be_http_endpoint = temp_model.from_map(m.get('BeHttpEndpoint'))

        if m.get('Body') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Database') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersDatabase()
            self.database = temp_model.from_map(m.get('Database'))

        if m.get('FeHttpEndpoint') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersFeHttpEndpoint()
            self.fe_http_endpoint = temp_model.from_map(m.get('FeHttpEndpoint'))

        if m.get('NetworkType') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersNetworkType()
            self.network_type = temp_model.from_map(m.get('NetworkType'))

        if m.get('Password') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersPassword()
            self.password = temp_model.from_map(m.get('Password'))

        if m.get('QueryEndpoint') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersQueryEndpoint()
            self.query_endpoint = temp_model.from_map(m.get('QueryEndpoint'))

        if m.get('SecurityGroupId') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersSecurityGroupId()
            self.security_group_id = temp_model.from_map(m.get('SecurityGroupId'))

        if m.get('Table') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersTable()
            self.table = temp_model.from_map(m.get('Table'))

        if m.get('UserName') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersUserName()
            self.user_name = temp_model.from_map(m.get('UserName'))

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        if m.get('VpcId') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDorisParametersVpcId()
            self.vpc_id = temp_model.from_map(m.get('VpcId'))

        return self

class GetEventStreamingResponseBodyDataSinkSinkDorisParametersVpcId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDorisParametersVSwitchIds(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDorisParametersUserName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDorisParametersTable(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDorisParametersSecurityGroupId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDorisParametersQueryEndpoint(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDorisParametersPassword(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDorisParametersNetworkType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDorisParametersFeHttpEndpoint(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDorisParametersDatabase(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDorisParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDorisParametersBeHttpEndpoint(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDataHubParameters(DaraModel):
    def __init__(
        self,
        body: main_models.GetEventStreamingResponseBodyDataSinkSinkDataHubParametersBody = None,
        project: main_models.GetEventStreamingResponseBodyDataSinkSinkDataHubParametersProject = None,
        role_name: main_models.GetEventStreamingResponseBodyDataSinkSinkDataHubParametersRoleName = None,
        topic: main_models.GetEventStreamingResponseBodyDataSinkSinkDataHubParametersTopic = None,
        topic_schema: main_models.GetEventStreamingResponseBodyDataSinkSinkDataHubParametersTopicSchema = None,
        topic_type: main_models.GetEventStreamingResponseBodyDataSinkSinkDataHubParametersTopicType = None,
    ):
        self.body = body
        self.project = project
        self.role_name = role_name
        self.topic = topic
        self.topic_schema = topic_schema
        self.topic_type = topic_type

    def validate(self):
        if self.body:
            self.body.validate()
        if self.project:
            self.project.validate()
        if self.role_name:
            self.role_name.validate()
        if self.topic:
            self.topic.validate()
        if self.topic_schema:
            self.topic_schema.validate()
        if self.topic_type:
            self.topic_type.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body.to_map()

        if self.project is not None:
            result['Project'] = self.project.to_map()

        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()

        if self.topic is not None:
            result['Topic'] = self.topic.to_map()

        if self.topic_schema is not None:
            result['TopicSchema'] = self.topic_schema.to_map()

        if self.topic_type is not None:
            result['TopicType'] = self.topic_type.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDataHubParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Project') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDataHubParametersProject()
            self.project = temp_model.from_map(m.get('Project'))

        if m.get('RoleName') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDataHubParametersRoleName()
            self.role_name = temp_model.from_map(m.get('RoleName'))

        if m.get('Topic') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDataHubParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        if m.get('TopicSchema') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDataHubParametersTopicSchema()
            self.topic_schema = temp_model.from_map(m.get('TopicSchema'))

        if m.get('TopicType') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDataHubParametersTopicType()
            self.topic_type = temp_model.from_map(m.get('TopicType'))

        return self

class GetEventStreamingResponseBodyDataSinkSinkDataHubParametersTopicType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDataHubParametersTopicSchema(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDataHubParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDataHubParametersRoleName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDataHubParametersProject(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDataHubParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDashVectorParameters(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        collection: str = None,
        dash_vector_schema_parameters: List[main_models.GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersDashVectorSchemaParameters] = None,
        instance_id: str = None,
        network: str = None,
        operation: str = None,
        partition: main_models.GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersPartition = None,
        primary_key_id: main_models.GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersPrimaryKeyId = None,
        vector: main_models.GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersVector = None,
    ):
        self.api_key = api_key
        self.collection = collection
        self.dash_vector_schema_parameters = dash_vector_schema_parameters
        self.instance_id = instance_id
        self.network = network
        self.operation = operation
        self.partition = partition
        self.primary_key_id = primary_key_id
        self.vector = vector

    def validate(self):
        if self.dash_vector_schema_parameters:
            for v1 in self.dash_vector_schema_parameters:
                 if v1:
                    v1.validate()
        if self.partition:
            self.partition.validate()
        if self.primary_key_id:
            self.primary_key_id.validate()
        if self.vector:
            self.vector.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.collection is not None:
            result['Collection'] = self.collection

        result['DashVectorSchemaParameters'] = []
        if self.dash_vector_schema_parameters is not None:
            for k1 in self.dash_vector_schema_parameters:
                result['DashVectorSchemaParameters'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network is not None:
            result['Network'] = self.network

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.partition is not None:
            result['Partition'] = self.partition.to_map()

        if self.primary_key_id is not None:
            result['PrimaryKeyId'] = self.primary_key_id.to_map()

        if self.vector is not None:
            result['Vector'] = self.vector.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        self.dash_vector_schema_parameters = []
        if m.get('DashVectorSchemaParameters') is not None:
            for k1 in m.get('DashVectorSchemaParameters'):
                temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersDashVectorSchemaParameters()
                self.dash_vector_schema_parameters.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Partition') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersPartition()
            self.partition = temp_model.from_map(m.get('Partition'))

        if m.get('PrimaryKeyId') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersPrimaryKeyId()
            self.primary_key_id = temp_model.from_map(m.get('PrimaryKeyId'))

        if m.get('Vector') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersVector()
            self.vector = temp_model.from_map(m.get('Vector'))

        return self

class GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersVector(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersPrimaryKeyId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersPartition(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersDashVectorSchemaParameters(DaraModel):
    def __init__(
        self,
        name: main_models.GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersDashVectorSchemaParametersName = None,
        type: main_models.GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersDashVectorSchemaParametersType = None,
        value: main_models.GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersDashVectorSchemaParametersValue = None,
    ):
        self.name = name
        self.type = type
        self.value = value

    def validate(self):
        if self.name:
            self.name.validate()
        if self.type:
            self.type.validate()
        if self.value:
            self.value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name.to_map()

        if self.type is not None:
            result['Type'] = self.type.to_map()

        if self.value is not None:
            result['Value'] = self.value.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersDashVectorSchemaParametersName()
            self.name = temp_model.from_map(m.get('Name'))

        if m.get('Type') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersDashVectorSchemaParametersType()
            self.type = temp_model.from_map(m.get('Type'))

        if m.get('Value') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersDashVectorSchemaParametersValue()
            self.value = temp_model.from_map(m.get('Value'))

        return self

class GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersDashVectorSchemaParametersValue(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersDashVectorSchemaParametersType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkDashVectorParametersDashVectorSchemaParametersName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkCustomizedKafkaParameters(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class GetEventStreamingResponseBodyDataSinkSinkCustomizedKafkaConnectorParameters(DaraModel):
    def __init__(
        self,
        connector_package_url: str = None,
        connector_parameters: main_models.GetEventStreamingResponseBodyDataSinkSinkCustomizedKafkaConnectorParametersConnectorParameters = None,
        worker_parameters: Dict[str, Any] = None,
    ):
        self.connector_package_url = connector_package_url
        self.connector_parameters = connector_parameters
        self.worker_parameters = worker_parameters

    def validate(self):
        if self.connector_parameters:
            self.connector_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_package_url is not None:
            result['ConnectorPackageUrl'] = self.connector_package_url

        if self.connector_parameters is not None:
            result['ConnectorParameters'] = self.connector_parameters.to_map()

        if self.worker_parameters is not None:
            result['WorkerParameters'] = self.worker_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorPackageUrl') is not None:
            self.connector_package_url = m.get('ConnectorPackageUrl')

        if m.get('ConnectorParameters') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkCustomizedKafkaConnectorParametersConnectorParameters()
            self.connector_parameters = temp_model.from_map(m.get('ConnectorParameters'))

        if m.get('WorkerParameters') is not None:
            self.worker_parameters = m.get('WorkerParameters')

        return self

class GetEventStreamingResponseBodyDataSinkSinkCustomizedKafkaConnectorParametersConnectorParameters(DaraModel):
    def __init__(
        self,
        config: Dict[str, Any] = None,
        name: str = None,
    ):
        self.config = config
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetEventStreamingResponseBodyDataSinkSinkApacheRocketMQCheckpointParameters(DaraModel):
    def __init__(
        self,
        consume_timestamp: main_models.GetEventStreamingResponseBodyDataSinkSinkApacheRocketMQCheckpointParametersConsumeTimestamp = None,
        group: main_models.GetEventStreamingResponseBodyDataSinkSinkApacheRocketMQCheckpointParametersGroup = None,
        instance_endpoint: str = None,
        instance_password: str = None,
        instance_username: str = None,
        network_type: str = None,
        security_group_id: str = None,
        topic: main_models.GetEventStreamingResponseBodyDataSinkSinkApacheRocketMQCheckpointParametersTopic = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.consume_timestamp = consume_timestamp
        self.group = group
        self.instance_endpoint = instance_endpoint
        self.instance_password = instance_password
        self.instance_username = instance_username
        self.network_type = network_type
        self.security_group_id = security_group_id
        self.topic = topic
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        if self.consume_timestamp:
            self.consume_timestamp.validate()
        if self.group:
            self.group.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consume_timestamp is not None:
            result['ConsumeTimestamp'] = self.consume_timestamp.to_map()

        if self.group is not None:
            result['Group'] = self.group.to_map()

        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint

        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password

        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.topic is not None:
            result['Topic'] = self.topic.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumeTimestamp') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkApacheRocketMQCheckpointParametersConsumeTimestamp()
            self.consume_timestamp = temp_model.from_map(m.get('ConsumeTimestamp'))

        if m.get('Group') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkApacheRocketMQCheckpointParametersGroup()
            self.group = temp_model.from_map(m.get('Group'))

        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')

        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')

        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Topic') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkApacheRocketMQCheckpointParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetEventStreamingResponseBodyDataSinkSinkApacheRocketMQCheckpointParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkApacheRocketMQCheckpointParametersGroup(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        # Group ID
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkApacheRocketMQCheckpointParametersConsumeTimestamp(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParameters(DaraModel):
    def __init__(
        self,
        acks: str = None,
        bootstraps: str = None,
        compression_type: str = None,
        headers: main_models.GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersHeaders = None,
        key: main_models.GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersKey = None,
        network_type: main_models.GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersNetworkType = None,
        sasl_mechanism: str = None,
        sasl_password: str = None,
        sasl_user: str = None,
        security_group_id: main_models.GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersSecurityGroupId = None,
        security_protocol: str = None,
        ssl_truststore_certificates: str = None,
        topic: str = None,
        v_switch_ids: main_models.GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersVSwitchIds = None,
        value: main_models.GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersValue = None,
        vpc_id: main_models.GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersVpcId = None,
    ):
        self.acks = acks
        self.bootstraps = bootstraps
        self.compression_type = compression_type
        self.headers = headers
        self.key = key
        self.network_type = network_type
        self.sasl_mechanism = sasl_mechanism
        self.sasl_password = sasl_password
        self.sasl_user = sasl_user
        self.security_group_id = security_group_id
        self.security_protocol = security_protocol
        self.ssl_truststore_certificates = ssl_truststore_certificates
        self.topic = topic
        self.v_switch_ids = v_switch_ids
        self.value = value
        self.vpc_id = vpc_id

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.key:
            self.key.validate()
        if self.network_type:
            self.network_type.validate()
        if self.security_group_id:
            self.security_group_id.validate()
        if self.v_switch_ids:
            self.v_switch_ids.validate()
        if self.value:
            self.value.validate()
        if self.vpc_id:
            self.vpc_id.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acks is not None:
            result['Acks'] = self.acks

        if self.bootstraps is not None:
            result['Bootstraps'] = self.bootstraps

        if self.compression_type is not None:
            result['CompressionType'] = self.compression_type

        if self.headers is not None:
            result['Headers'] = self.headers.to_map()

        if self.key is not None:
            result['Key'] = self.key.to_map()

        if self.network_type is not None:
            result['NetworkType'] = self.network_type.to_map()

        if self.sasl_mechanism is not None:
            result['SaslMechanism'] = self.sasl_mechanism

        if self.sasl_password is not None:
            result['SaslPassword'] = self.sasl_password

        if self.sasl_user is not None:
            result['SaslUser'] = self.sasl_user

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id.to_map()

        if self.security_protocol is not None:
            result['SecurityProtocol'] = self.security_protocol

        if self.ssl_truststore_certificates is not None:
            result['SslTruststoreCertificates'] = self.ssl_truststore_certificates

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()

        if self.value is not None:
            result['Value'] = self.value.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acks') is not None:
            self.acks = m.get('Acks')

        if m.get('Bootstraps') is not None:
            self.bootstraps = m.get('Bootstraps')

        if m.get('CompressionType') is not None:
            self.compression_type = m.get('CompressionType')

        if m.get('Headers') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('Key') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersKey()
            self.key = temp_model.from_map(m.get('Key'))

        if m.get('NetworkType') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersNetworkType()
            self.network_type = temp_model.from_map(m.get('NetworkType'))

        if m.get('SaslMechanism') is not None:
            self.sasl_mechanism = m.get('SaslMechanism')

        if m.get('SaslPassword') is not None:
            self.sasl_password = m.get('SaslPassword')

        if m.get('SaslUser') is not None:
            self.sasl_user = m.get('SaslUser')

        if m.get('SecurityGroupId') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersSecurityGroupId()
            self.security_group_id = temp_model.from_map(m.get('SecurityGroupId'))

        if m.get('SecurityProtocol') is not None:
            self.security_protocol = m.get('SecurityProtocol')

        if m.get('SslTruststoreCertificates') is not None:
            self.ssl_truststore_certificates = m.get('SslTruststoreCertificates')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        if m.get('Value') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersValue()
            self.value = temp_model.from_map(m.get('Value'))

        if m.get('VpcId') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersVpcId()
            self.vpc_id = temp_model.from_map(m.get('VpcId'))

        return self

class GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersVpcId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersValue(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersVSwitchIds(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersSecurityGroupId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersNetworkType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersKey(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataSinkSinkApacheKafkaParametersHeaders(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEventStreamingResponseBodyDataRunOptions(DaraModel):
    def __init__(
        self,
        batch_window: main_models.GetEventStreamingResponseBodyDataRunOptionsBatchWindow = None,
        business_option: main_models.GetEventStreamingResponseBodyDataRunOptionsBusinessOption = None,
        dead_letter_queue: main_models.GetEventStreamingResponseBodyDataRunOptionsDeadLetterQueue = None,
        errors_tolerance: str = None,
        maximum_tasks: int = None,
        retry_strategy: main_models.GetEventStreamingResponseBodyDataRunOptionsRetryStrategy = None,
        throttling: int = None,
    ):
        # The batch window.
        self.batch_window = batch_window
        self.business_option = business_option
        # Indicates whether dead-letter queues are enabled. By default, dead-letter queues are disabled. Messages that fail to be pushed after allowed retries as specified by the retry policy are discarded.
        self.dead_letter_queue = dead_letter_queue
        # The fault tolerance policy. The value NONE specifies that faults are not tolerated, and the value All specifies that all faults are tolerated.
        self.errors_tolerance = errors_tolerance
        # The concurrency level.
        self.maximum_tasks = maximum_tasks
        # The information about the retry policy that is used if the event fails to be pushed.
        self.retry_strategy = retry_strategy
        self.throttling = throttling

    def validate(self):
        if self.batch_window:
            self.batch_window.validate()
        if self.business_option:
            self.business_option.validate()
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.retry_strategy:
            self.retry_strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_window is not None:
            result['BatchWindow'] = self.batch_window.to_map()

        if self.business_option is not None:
            result['BusinessOption'] = self.business_option.to_map()

        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()

        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance

        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks

        if self.retry_strategy is not None:
            result['RetryStrategy'] = self.retry_strategy.to_map()

        if self.throttling is not None:
            result['Throttling'] = self.throttling

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchWindow') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataRunOptionsBatchWindow()
            self.batch_window = temp_model.from_map(m.get('BatchWindow'))

        if m.get('BusinessOption') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataRunOptionsBusinessOption()
            self.business_option = temp_model.from_map(m.get('BusinessOption'))

        if m.get('DeadLetterQueue') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataRunOptionsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m.get('DeadLetterQueue'))

        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')

        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')

        if m.get('RetryStrategy') is not None:
            temp_model = main_models.GetEventStreamingResponseBodyDataRunOptionsRetryStrategy()
            self.retry_strategy = temp_model.from_map(m.get('RetryStrategy'))

        if m.get('Throttling') is not None:
            self.throttling = m.get('Throttling')

        return self

class GetEventStreamingResponseBodyDataRunOptionsRetryStrategy(DaraModel):
    def __init__(
        self,
        maximum_event_age_in_seconds: float = None,
        maximum_retry_attempts: float = None,
        push_retry_strategy: str = None,
    ):
        # The maximum period of time during which retries are performed.
        self.maximum_event_age_in_seconds = maximum_event_age_in_seconds
        # The maximum number of retries.
        self.maximum_retry_attempts = maximum_retry_attempts
        # The retry policy. Valid values: BACKOFFRETRY and EXPONENTIALDECAY_RETRY.
        self.push_retry_strategy = push_retry_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.maximum_event_age_in_seconds is not None:
            result['MaximumEventAgeInSeconds'] = self.maximum_event_age_in_seconds

        if self.maximum_retry_attempts is not None:
            result['MaximumRetryAttempts'] = self.maximum_retry_attempts

        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaximumEventAgeInSeconds') is not None:
            self.maximum_event_age_in_seconds = m.get('MaximumEventAgeInSeconds')

        if m.get('MaximumRetryAttempts') is not None:
            self.maximum_retry_attempts = m.get('MaximumRetryAttempts')

        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')

        return self

class GetEventStreamingResponseBodyDataRunOptionsDeadLetterQueue(DaraModel):
    def __init__(
        self,
        arn: str = None,
        network: str = None,
        security_group_id: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the dead-letter queue.
        self.arn = arn
        self.network = network
        self.security_group_id = security_group_id
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.network is not None:
            result['Network'] = self.network

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetEventStreamingResponseBodyDataRunOptionsBusinessOption(DaraModel):
    def __init__(
        self,
        business_mode: str = None,
        max_capacity_unit_count: int = None,
        min_capacity_unit_count: int = None,
    ):
        self.business_mode = business_mode
        self.max_capacity_unit_count = max_capacity_unit_count
        self.min_capacity_unit_count = min_capacity_unit_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_mode is not None:
            result['BusinessMode'] = self.business_mode

        if self.max_capacity_unit_count is not None:
            result['MaxCapacityUnitCount'] = self.max_capacity_unit_count

        if self.min_capacity_unit_count is not None:
            result['MinCapacityUnitCount'] = self.min_capacity_unit_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessMode') is not None:
            self.business_mode = m.get('BusinessMode')

        if m.get('MaxCapacityUnitCount') is not None:
            self.max_capacity_unit_count = m.get('MaxCapacityUnitCount')

        if m.get('MinCapacityUnitCount') is not None:
            self.min_capacity_unit_count = m.get('MinCapacityUnitCount')

        return self

class GetEventStreamingResponseBodyDataRunOptionsBatchWindow(DaraModel):
    def __init__(
        self,
        count_based_window: int = None,
        time_based_window: int = None,
    ):
        # The maximum number of events that are allowed in the batch window. If this threshold is reached, data in the window is pushed downstream. When multiple batch windows exist, data is pushed if triggering conditions are met in one of the windows.
        self.count_based_window = count_based_window
        # The maximum period of time during which events are allowed in the batch window. Unit: seconds. If this threshold is reached, data in the window is pushed downstream. When multiple batch windows exist, data is pushed if triggering conditions are met in one of the windows.
        self.time_based_window = time_based_window

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count_based_window is not None:
            result['CountBasedWindow'] = self.count_based_window

        if self.time_based_window is not None:
            result['TimeBasedWindow'] = self.time_based_window

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountBasedWindow') is not None:
            self.count_based_window = m.get('CountBasedWindow')

        if m.get('TimeBasedWindow') is not None:
            self.time_based_window = m.get('TimeBasedWindow')

        return self

class GetEventStreamingResponseBodyDataDetailedStatus(DaraModel):
    def __init__(
        self,
        delay_time: int = None,
        diff_offset: int = None,
        extensions: Dict[str, Any] = None,
        tps: float = None,
    ):
        self.delay_time = delay_time
        self.diff_offset = diff_offset
        self.extensions = extensions
        self.tps = tps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time

        if self.diff_offset is not None:
            result['DiffOffset'] = self.diff_offset

        if self.extensions is not None:
            result['Extensions'] = self.extensions

        if self.tps is not None:
            result['TPS'] = self.tps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')

        if m.get('DiffOffset') is not None:
            self.diff_offset = m.get('DiffOffset')

        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')

        if m.get('TPS') is not None:
            self.tps = m.get('TPS')

        return self

