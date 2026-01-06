# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class ListEventStreamingsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListEventStreamingsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. Valid values:
        # 
        # Success: The request is successful.
        # 
        # Other codes: The request failed. For more information about error codes, see Error codes.
        self.code = code
        # The returned data.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. The value true indicates that the request is successful.
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
            temp_model = main_models.ListEventStreamingsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListEventStreamingsResponseBodyData(DaraModel):
    def __init__(
        self,
        event_streamings: List[main_models.ListEventStreamingsResponseBodyDataEventStreamings] = None,
        next_token: str = None,
        total: int = None,
    ):
        # The event streams.
        self.event_streamings = event_streamings
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists. You must specify the pagination token in the next request.
        self.next_token = next_token
        # The total number of records.
        self.total = total

    def validate(self):
        if self.event_streamings:
            for v1 in self.event_streamings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventStreamings'] = []
        if self.event_streamings is not None:
            for k1 in self.event_streamings:
                result['EventStreamings'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_streamings = []
        if m.get('EventStreamings') is not None:
            for k1 in m.get('EventStreamings'):
                temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamings()
                self.event_streamings.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListEventStreamingsResponseBodyDataEventStreamings(DaraModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        run_options: main_models.ListEventStreamingsResponseBodyDataEventStreamingsRunOptions = None,
        sink: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSink = None,
        source: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSource = None,
        status: str = None,
        transforms: List[main_models.ListEventStreamingsResponseBodyDataEventStreamingsTransforms] = None,
    ):
        # The description of the event stream.
        self.description = description
        # The name of the event stream.
        self.event_streaming_name = event_streaming_name
        # The rule that is used to filter events. If you leave this parameter empty, all events are matched.
        self.filter_pattern = filter_pattern
        # The parameters that are returned for the runtime environment.
        self.run_options = run_options
        # The event target.
        self.sink = sink
        # The event provider, which is also known as the event source.
        self.source = source
        # The status of the event stream that is returned.
        self.status = status
        # The transformation-related configurations.
        self.transforms = transforms

    def validate(self):
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

        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')

        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')

        if m.get('RunOptions') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsRunOptions()
            self.run_options = temp_model.from_map(m.get('RunOptions'))

        if m.get('Sink') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSink()
            self.sink = temp_model.from_map(m.get('Sink'))

        if m.get('Source') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSource()
            self.source = temp_model.from_map(m.get('Source'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.transforms = []
        if m.get('Transforms') is not None:
            for k1 in m.get('Transforms'):
                temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsTransforms()
                self.transforms.append(temp_model.from_map(k1))

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsTransforms(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSource(DaraModel):
    def __init__(
        self,
        source_apache_rocket_mqcheckpoint_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceApacheRocketMQCheckpointParameters = None,
        source_customized_kafka_connector_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceCustomizedKafkaConnectorParameters = None,
        source_customized_kafka_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceCustomizedKafkaParameters = None,
        source_dtsparameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceDTSParameters = None,
        source_event_bus_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceEventBusParameters = None,
        source_kafka_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceKafkaParameters = None,
        source_mnsparameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMNSParameters = None,
        source_mqttparameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMQTTParameters = None,
        source_my_sqlparameters: main_models.SourceMySQLParameters = None,
        source_ossparameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceOSSParameters = None,
        source_open_source_rabbit_mqparameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceOpenSourceRabbitMQParameters = None,
        source_postgre_sqlparameters: main_models.SourcePostgreSQLParameters = None,
        source_prometheus_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourcePrometheusParameters = None,
        source_rabbit_mqmeta_parameters: main_models.SourceRabbitMQMetaParameters = None,
        source_rabbit_mqmsg_sync_parameters: main_models.SourceRabbitMQMsgSyncParameters = None,
        source_rabbit_mqparameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRabbitMQParameters = None,
        source_rocket_mqcheckpoint_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRocketMQCheckpointParameters = None,
        source_rocket_mqparameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRocketMQParameters = None,
        source_slsparameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceSLSParameters = None,
    ):
        self.source_apache_rocket_mqcheckpoint_parameters = source_apache_rocket_mqcheckpoint_parameters
        self.source_customized_kafka_connector_parameters = source_customized_kafka_connector_parameters
        self.source_customized_kafka_parameters = source_customized_kafka_parameters
        # The parameters that are returned if Data Transmission Service (DTS) is specified as the event source.
        self.source_dtsparameters = source_dtsparameters
        self.source_event_bus_parameters = source_event_bus_parameters
        # The parameters that are returned if ApsaraMQ for Kafka is specified as the event source.
        self.source_kafka_parameters = source_kafka_parameters
        # The parameters that are returned if Message Queue (MNS) is specified as the event source.
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
        # The parameters that are returned if ApsaraMQ for RabbitMQ is specified as the event source.
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        self.source_rocket_mqcheckpoint_parameters = source_rocket_mqcheckpoint_parameters
        # The parameters that are returned if ApsaraMQ for RocketMQ is specified as the event source.
        self.source_rocket_mqparameters = source_rocket_mqparameters
        # The parameters that are returned if Simple Log Service is specified as the event source.
        self.source_slsparameters = source_slsparameters

    def validate(self):
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
        if m.get('SourceApacheRocketMQCheckpointParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceApacheRocketMQCheckpointParameters()
            self.source_apache_rocket_mqcheckpoint_parameters = temp_model.from_map(m.get('SourceApacheRocketMQCheckpointParameters'))

        if m.get('SourceCustomizedKafkaConnectorParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceCustomizedKafkaConnectorParameters()
            self.source_customized_kafka_connector_parameters = temp_model.from_map(m.get('SourceCustomizedKafkaConnectorParameters'))

        if m.get('SourceCustomizedKafkaParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceCustomizedKafkaParameters()
            self.source_customized_kafka_parameters = temp_model.from_map(m.get('SourceCustomizedKafkaParameters'))

        if m.get('SourceDTSParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m.get('SourceDTSParameters'))

        if m.get('SourceEventBusParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceEventBusParameters()
            self.source_event_bus_parameters = temp_model.from_map(m.get('SourceEventBusParameters'))

        if m.get('SourceKafkaParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m.get('SourceKafkaParameters'))

        if m.get('SourceMNSParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m.get('SourceMNSParameters'))

        if m.get('SourceMQTTParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m.get('SourceMQTTParameters'))

        if m.get('SourceMySQLParameters') is not None:
            temp_model = main_models.SourceMySQLParameters()
            self.source_my_sqlparameters = temp_model.from_map(m.get('SourceMySQLParameters'))

        if m.get('SourceOSSParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceOSSParameters()
            self.source_ossparameters = temp_model.from_map(m.get('SourceOSSParameters'))

        if m.get('SourceOpenSourceRabbitMQParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceOpenSourceRabbitMQParameters()
            self.source_open_source_rabbit_mqparameters = temp_model.from_map(m.get('SourceOpenSourceRabbitMQParameters'))

        if m.get('SourcePostgreSQLParameters') is not None:
            temp_model = main_models.SourcePostgreSQLParameters()
            self.source_postgre_sqlparameters = temp_model.from_map(m.get('SourcePostgreSQLParameters'))

        if m.get('SourcePrometheusParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourcePrometheusParameters()
            self.source_prometheus_parameters = temp_model.from_map(m.get('SourcePrometheusParameters'))

        if m.get('SourceRabbitMQMetaParameters') is not None:
            temp_model = main_models.SourceRabbitMQMetaParameters()
            self.source_rabbit_mqmeta_parameters = temp_model.from_map(m.get('SourceRabbitMQMetaParameters'))

        if m.get('SourceRabbitMQMsgSyncParameters') is not None:
            temp_model = main_models.SourceRabbitMQMsgSyncParameters()
            self.source_rabbit_mqmsg_sync_parameters = temp_model.from_map(m.get('SourceRabbitMQMsgSyncParameters'))

        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m.get('SourceRabbitMQParameters'))

        if m.get('SourceRocketMQCheckpointParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRocketMQCheckpointParameters()
            self.source_rocket_mqcheckpoint_parameters = temp_model.from_map(m.get('SourceRocketMQCheckpointParameters'))

        if m.get('SourceRocketMQParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m.get('SourceRocketMQParameters'))

        if m.get('SourceSLSParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m.get('SourceSLSParameters'))

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceSLSParameters(DaraModel):
    def __init__(
        self,
        consume_position: str = None,
        consumer_group: str = None,
        log_store: str = None,
        project: str = None,
        role_name: str = None,
    ):
        # The consumer offset. The value begin indicates the earliest offset. The value end indicates the latest offset. You can also specify a time in seconds to start message consumption.
        self.consume_position = consume_position
        # The group ID of the consumer that subscribes to the topic.
        self.consumer_group = consumer_group
        # The Simple Log Service Logstore.
        self.log_store = log_store
        # The Simple Log Service project.
        self.project = project
        # The role name. If you want to authorize EventBridge to use this role to read logs in Simple Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the Resource Access Management (RAM) console.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRocketMQParameters(DaraModel):
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
        # The authentication method.
        self.auth_type = auth_type
        self.body_data_type = body_data_type
        self.filter_sql = filter_sql
        self.filter_type = filter_type
        # The ID of the consumer group on the ApsaraMQ for RocketMQ instance.
        self.group_id = group_id
        # The endpoint that is used to access the ApsaraMQ for RocketMQ instance.
        self.instance_endpoint = instance_endpoint
        # The ID of the ApsaraMQ for RocketMQ instance
        self.instance_id = instance_id
        # The network type of the ApsaraMQ for RocketMQ instance. Valid values:
        # 
        # *   PublicNetwork
        # *   PrivateNetwork
        self.instance_network = instance_network
        # The password that is used to access the ApsaraMQ for RocketMQ instance.
        self.instance_password = instance_password
        # The ID of the security group to which the ApsaraMQ for RocketMQ instance belongs.
        self.instance_security_group_id = instance_security_group_id
        # The type of the ApsaraMQ for RocketMQ instance.
        self.instance_type = instance_type
        # The username that is used to access the ApsaraMQ for RocketMQ instance.
        self.instance_username = instance_username
        # The ID of the vSwitch with which the ApsaraMQ for RocketMQ instance is associated.
        self.instance_vswitch_ids = instance_vswitch_ids
        # The ID of the virtual private cloud (VPC) to which the ApsaraMQ for RocketMQ instance belongs.
        self.instance_vpc_id = instance_vpc_id
        self.network = network
        # The offset from which messages are consumed. Valid values: CONSUMEFROMLASTOFFSET: Messages are consumed from the latest offset. CONSUMEFROMFIRSTOFFSET: Messages are consumed from the earliest offset. CONSUME_FROM_TIMESTAMP: Messages are consumed from the offset at the specified point in time.
        self.offset = offset
        # The ID of the region where the ApsaraMQ for RocketMQ instance resides.
        self.region_id = region_id
        self.security_group_id = security_group_id
        # The tag that is used to filter messages.
        self.tag = tag
        # The timestamp that indicates the time from which messages are consumed. This parameter is valid only if Offset is set to CONSUMEFROMTIMESTAMP.
        self.timestamp = timestamp
        # The topic from which messages are sent.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRocketMQCheckpointParameters(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRabbitMQParameters(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_name: str = None,
        region_id: str = None,
        virtual_host_name: str = None,
    ):
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.instance_id = instance_id
        # The name of the queue on the ApsaraMQ for RabbitMQ instance.
        self.queue_name = queue_name
        # The ID of the region where the ApsaraMQ for RabbitMQ instance resides.
        self.region_id = region_id
        # The name of the vhost to which the ApsaraMQ for RabbitMQ instance belongs.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourcePrometheusParameters(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceOpenSourceRabbitMQParameters(DaraModel):
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
        # VPC ID。
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

class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceOSSParameters(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMQTTParameters(DaraModel):
    def __init__(
        self,
        body_data_type: str = None,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        self.body_data_type = body_data_type
        # The ID of the ApsaraMQ for MQTT instance.
        self.instance_id = instance_id
        # The ID of the region where the ApsaraMQ for MQTT instance resides.
        self.region_id = region_id
        # The name of the topic on the ApsaraMQ for MQTT instance.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMNSParameters(DaraModel):
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
        # The ID of the region where the MNS queue resides.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceKafkaParameters(DaraModel):
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
        # The group ID of the consumer that subscribes to the topic.
        self.consumer_group = consumer_group
        # The ID of the ApsaraMQ for Kafka instance.
        self.instance_id = instance_id
        # The network type. Default value: Default. The value PublicNetwork indicates a VPC.
        self.network = network
        # The offset from which messages are consumed.
        self.offset_reset = offset_reset
        # The ID of the region where the ApsaraMQ for Kafka instance resides.
        self.region_id = region_id
        # The ID of the security group to which the ApsaraMQ for Kafka instance belongs.
        self.security_group_id = security_group_id
        # The name of the topic on the ApsaraMQ for Kafka instance.
        self.topic = topic
        # The ID of the vSwitch with which the ApsaraMQ for Kafka instance is associated.
        self.v_switch_ids = v_switch_ids
        self.value_data_type = value_data_type
        # The ID of the VPC to which the ApsaraMQ for Kafka instance belongs.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceEventBusParameters(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceDTSParameters(DaraModel):
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
        # The URL and port number of the change tracking instance.
        self.broker_url = broker_url
        # The UNIX timestamp that is generated when the SDK client consumes the first data record.
        self.init_check_point = init_check_point
        # The consumer group password.
        self.password = password
        # The consumer group ID.
        self.sid = sid
        # The task ID.
        self.task_id = task_id
        # The name of the tracked topic of the change tracking instance.
        self.topic = topic
        # The consumer group username.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceCustomizedKafkaParameters(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceCustomizedKafkaConnectorParameters(DaraModel):
    def __init__(
        self,
        connector_package_url: str = None,
        connector_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceCustomizedKafkaConnectorParametersConnectorParameters = None,
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
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceCustomizedKafkaConnectorParametersConnectorParameters()
            self.connector_parameters = temp_model.from_map(m.get('ConnectorParameters'))

        if m.get('WorkerParameters') is not None:
            self.worker_parameters = m.get('WorkerParameters')

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceCustomizedKafkaConnectorParametersConnectorParameters(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceApacheRocketMQCheckpointParameters(DaraModel):
    def __init__(
        self,
        instance_endpoint: str = None,
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

class ListEventStreamingsResponseBodyDataEventStreamingsSink(DaraModel):
    def __init__(
        self,
        sink_apache_rocket_mqcheckpoint_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkApacheRocketMQCheckpointParameters = None,
        sink_api_destination_parameters: main_models.SinkApiDestinationParameters = None,
        sink_bai_lian_parameters: main_models.SinkBaiLianParameters = None,
        sink_customized_kafka_connector_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkCustomizedKafkaConnectorParameters = None,
        sink_customized_kafka_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkCustomizedKafkaParameters = None,
        sink_dash_vector_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParameters = None,
        sink_data_hub_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParameters = None,
        sink_doris_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParameters = None,
        sink_fc_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParameters = None,
        sink_fnf_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParameters = None,
        sink_https_parameters: main_models.SinkHttpsParameters = None,
        sink_kafka_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParameters = None,
        sink_mnsparameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParameters = None,
        sink_ossparameters: main_models.SinkOSSParameters = None,
        sink_open_source_rabbit_mqparameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkOpenSourceRabbitMQParameters = None,
        sink_rabbit_mqmeta_parameters: main_models.SinkRabbitMQMetaParameters = None,
        sink_rabbit_mqmsg_sync_parameters: main_models.SinkRabbitMQMsgSyncParameters = None,
        sink_rabbit_mqparameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParameters = None,
        sink_rocket_mqcheckpoint_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQCheckpointParameters = None,
        sink_rocket_mqparameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParameters = None,
        sink_slsparameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParameters = None,
    ):
        self.sink_apache_rocket_mqcheckpoint_parameters = sink_apache_rocket_mqcheckpoint_parameters
        self.sink_api_destination_parameters = sink_api_destination_parameters
        self.sink_bai_lian_parameters = sink_bai_lian_parameters
        self.sink_customized_kafka_connector_parameters = sink_customized_kafka_connector_parameters
        self.sink_customized_kafka_parameters = sink_customized_kafka_parameters
        self.sink_dash_vector_parameters = sink_dash_vector_parameters
        self.sink_data_hub_parameters = sink_data_hub_parameters
        self.sink_doris_parameters = sink_doris_parameters
        # The parameters that are returned if Function Compute is specified as the event target.
        self.sink_fc_parameters = sink_fc_parameters
        # The parameters that are returned if CloudFlow is specified as the event target.
        self.sink_fnf_parameters = sink_fnf_parameters
        self.sink_https_parameters = sink_https_parameters
        # The parameters that are returned if ApsaraMQ for Kafka is specified as the event target.
        self.sink_kafka_parameters = sink_kafka_parameters
        # The parameters that are returned if MNS is specified as the event target.
        self.sink_mnsparameters = sink_mnsparameters
        self.sink_ossparameters = sink_ossparameters
        self.sink_open_source_rabbit_mqparameters = sink_open_source_rabbit_mqparameters
        self.sink_rabbit_mqmeta_parameters = sink_rabbit_mqmeta_parameters
        self.sink_rabbit_mqmsg_sync_parameters = sink_rabbit_mqmsg_sync_parameters
        # The parameters that are returned if ApsaraMQ for RabbitMQ is specified as the event target.
        self.sink_rabbit_mqparameters = sink_rabbit_mqparameters
        self.sink_rocket_mqcheckpoint_parameters = sink_rocket_mqcheckpoint_parameters
        # The parameters that are returned if ApsaraMQ for RocketMQ is specified as the event target.
        self.sink_rocket_mqparameters = sink_rocket_mqparameters
        # The parameters that are returned if Simple Log Service is specified as the event target.
        self.sink_slsparameters = sink_slsparameters

    def validate(self):
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
        if m.get('SinkApacheRocketMQCheckpointParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkApacheRocketMQCheckpointParameters()
            self.sink_apache_rocket_mqcheckpoint_parameters = temp_model.from_map(m.get('SinkApacheRocketMQCheckpointParameters'))

        if m.get('SinkApiDestinationParameters') is not None:
            temp_model = main_models.SinkApiDestinationParameters()
            self.sink_api_destination_parameters = temp_model.from_map(m.get('SinkApiDestinationParameters'))

        if m.get('SinkBaiLianParameters') is not None:
            temp_model = main_models.SinkBaiLianParameters()
            self.sink_bai_lian_parameters = temp_model.from_map(m.get('SinkBaiLianParameters'))

        if m.get('SinkCustomizedKafkaConnectorParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkCustomizedKafkaConnectorParameters()
            self.sink_customized_kafka_connector_parameters = temp_model.from_map(m.get('SinkCustomizedKafkaConnectorParameters'))

        if m.get('SinkCustomizedKafkaParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkCustomizedKafkaParameters()
            self.sink_customized_kafka_parameters = temp_model.from_map(m.get('SinkCustomizedKafkaParameters'))

        if m.get('SinkDashVectorParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParameters()
            self.sink_dash_vector_parameters = temp_model.from_map(m.get('SinkDashVectorParameters'))

        if m.get('SinkDataHubParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParameters()
            self.sink_data_hub_parameters = temp_model.from_map(m.get('SinkDataHubParameters'))

        if m.get('SinkDorisParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParameters()
            self.sink_doris_parameters = temp_model.from_map(m.get('SinkDorisParameters'))

        if m.get('SinkFcParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParameters()
            self.sink_fc_parameters = temp_model.from_map(m.get('SinkFcParameters'))

        if m.get('SinkFnfParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParameters()
            self.sink_fnf_parameters = temp_model.from_map(m.get('SinkFnfParameters'))

        if m.get('SinkHttpsParameters') is not None:
            temp_model = main_models.SinkHttpsParameters()
            self.sink_https_parameters = temp_model.from_map(m.get('SinkHttpsParameters'))

        if m.get('SinkKafkaParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParameters()
            self.sink_kafka_parameters = temp_model.from_map(m.get('SinkKafkaParameters'))

        if m.get('SinkMNSParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParameters()
            self.sink_mnsparameters = temp_model.from_map(m.get('SinkMNSParameters'))

        if m.get('SinkOSSParameters') is not None:
            temp_model = main_models.SinkOSSParameters()
            self.sink_ossparameters = temp_model.from_map(m.get('SinkOSSParameters'))

        if m.get('SinkOpenSourceRabbitMQParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkOpenSourceRabbitMQParameters()
            self.sink_open_source_rabbit_mqparameters = temp_model.from_map(m.get('SinkOpenSourceRabbitMQParameters'))

        if m.get('SinkRabbitMQMetaParameters') is not None:
            temp_model = main_models.SinkRabbitMQMetaParameters()
            self.sink_rabbit_mqmeta_parameters = temp_model.from_map(m.get('SinkRabbitMQMetaParameters'))

        if m.get('SinkRabbitMQMsgSyncParameters') is not None:
            temp_model = main_models.SinkRabbitMQMsgSyncParameters()
            self.sink_rabbit_mqmsg_sync_parameters = temp_model.from_map(m.get('SinkRabbitMQMsgSyncParameters'))

        if m.get('SinkRabbitMQParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParameters()
            self.sink_rabbit_mqparameters = temp_model.from_map(m.get('SinkRabbitMQParameters'))

        if m.get('SinkRocketMQCheckpointParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQCheckpointParameters()
            self.sink_rocket_mqcheckpoint_parameters = temp_model.from_map(m.get('SinkRocketMQCheckpointParameters'))

        if m.get('SinkRocketMQParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParameters()
            self.sink_rocket_mqparameters = temp_model.from_map(m.get('SinkRocketMQParameters'))

        if m.get('SinkSLSParameters') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParameters()
            self.sink_slsparameters = temp_model.from_map(m.get('SinkSLSParameters'))

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParameters(DaraModel):
    def __init__(
        self,
        body: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersBody = None,
        content_schema: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersContentSchema = None,
        content_type: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersContentType = None,
        log_store: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersLogStore = None,
        project: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersProject = None,
        role_name: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersRoleName = None,
        topic: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersTopic = None,
    ):
        # The message body that is sent to Simple Log Service.
        self.body = body
        self.content_schema = content_schema
        self.content_type = content_type
        # The Simple Log Service Logstore.
        self.log_store = log_store
        # The Simple Log Service project.
        self.project = project
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the RAM console.
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
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('ContentSchema') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersContentSchema()
            self.content_schema = temp_model.from_map(m.get('ContentSchema'))

        if m.get('ContentType') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersContentType()
            self.content_type = temp_model.from_map(m.get('ContentType'))

        if m.get('LogStore') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersLogStore()
            self.log_store = temp_model.from_map(m.get('LogStore'))

        if m.get('Project') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersProject()
            self.project = temp_model.from_map(m.get('Project'))

        if m.get('RoleName') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersRoleName()
            self.role_name = temp_model.from_map(m.get('RoleName'))

        if m.get('Topic') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the topic in which logs are stored. The topic corresponds to the topic reserved field in Simple Log Service.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersRoleName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersProject(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The Simple Log Service project.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersLogStore(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The Simple Log Service Logstore.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersContentType(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersContentSchema(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before transformation.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParameters(DaraModel):
    def __init__(
        self,
        body: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersBody = None,
        delivery_order_type: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersDeliveryOrderType = None,
        instance_endpoint: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceEndpoint = None,
        instance_id: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceId = None,
        instance_password: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstancePassword = None,
        instance_type: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceType = None,
        instance_username: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceUsername = None,
        keys: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersKeys = None,
        network: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersNetwork = None,
        properties: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersProperties = None,
        security_group_id: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersSecurityGroupId = None,
        sharding_key: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersShardingKey = None,
        tags: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTags = None,
        topic: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTopic = None,
        v_switch_ids: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersVSwitchIds = None,
        vpc_id: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersVpcId = None,
    ):
        # The message content.
        self.body = body
        self.delivery_order_type = delivery_order_type
        self.instance_endpoint = instance_endpoint
        # The ID of the ApsaraMQ for RocketMQ instance.
        self.instance_id = instance_id
        self.instance_password = instance_password
        self.instance_type = instance_type
        self.instance_username = instance_username
        # The keys that are used to filter messages.
        self.keys = keys
        self.network = network
        # The properties that are used to filter messages.
        self.properties = properties
        self.security_group_id = security_group_id
        self.sharding_key = sharding_key
        # The tags that are used to filter messages.
        self.tags = tags
        # The topic on the ApsaraMQ for RocketMQ instance.
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
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('DeliveryOrderType') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersDeliveryOrderType()
            self.delivery_order_type = temp_model.from_map(m.get('DeliveryOrderType'))

        if m.get('InstanceEndpoint') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceEndpoint()
            self.instance_endpoint = temp_model.from_map(m.get('InstanceEndpoint'))

        if m.get('InstanceId') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m.get('InstanceId'))

        if m.get('InstancePassword') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstancePassword()
            self.instance_password = temp_model.from_map(m.get('InstancePassword'))

        if m.get('InstanceType') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceType()
            self.instance_type = temp_model.from_map(m.get('InstanceType'))

        if m.get('InstanceUsername') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceUsername()
            self.instance_username = temp_model.from_map(m.get('InstanceUsername'))

        if m.get('Keys') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersKeys()
            self.keys = temp_model.from_map(m.get('Keys'))

        if m.get('Network') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        if m.get('Properties') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('SecurityGroupId') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersSecurityGroupId()
            self.security_group_id = temp_model.from_map(m.get('SecurityGroupId'))

        if m.get('ShardingKey') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersShardingKey()
            self.sharding_key = temp_model.from_map(m.get('ShardingKey'))

        if m.get('Tags') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Topic') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        if m.get('VpcId') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersVpcId()
            self.vpc_id = temp_model.from_map(m.get('VpcId'))

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersVpcId(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersVSwitchIds(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The topic on the ApsaraMQ for RocketMQ instance.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTags(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before transformation.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersShardingKey(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersSecurityGroupId(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersProperties(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before transformation.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersNetwork(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersKeys(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before transformation.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceUsername(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceType(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstancePassword(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The ID of the ApsaraMQ for RocketMQ instance.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceEndpoint(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersDeliveryOrderType(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before transformation.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQCheckpointParameters(DaraModel):
    def __init__(
        self,
        consume_timestamp: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQCheckpointParametersConsumeTimestamp = None,
        group: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQCheckpointParametersGroup = None,
        instance_id: str = None,
        instance_type: str = None,
        topic: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQCheckpointParametersTopic = None,
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
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQCheckpointParametersConsumeTimestamp()
            self.consume_timestamp = temp_model.from_map(m.get('ConsumeTimestamp'))

        if m.get('Group') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQCheckpointParametersGroup()
            self.group = temp_model.from_map(m.get('Group'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Topic') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQCheckpointParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQCheckpointParametersTopic(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQCheckpointParametersGroup(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQCheckpointParametersConsumeTimestamp(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParameters(DaraModel):
    def __init__(
        self,
        body: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersBody = None,
        exchange: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersExchange = None,
        instance_id: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersInstanceId = None,
        message_id: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersMessageId = None,
        properties: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersProperties = None,
        queue_name: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersQueueName = None,
        routing_key: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersRoutingKey = None,
        target_type: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersTargetType = None,
        virtual_host_name: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersVirtualHostName = None,
    ):
        # The message content.
        self.body = body
        # The exchange mode. This parameter is required only if TargetType is set to Exchange.
        self.exchange = exchange
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.instance_id = instance_id
        # The message ID.
        self.message_id = message_id
        # The properties that are used to filter messages.
        self.properties = properties
        # The queue mode. This parameter is required only if TargetType is set to Queue.
        self.queue_name = queue_name
        # The rule that is used to route messages. This parameter is required only if TargetType is set to Exchange.
        self.routing_key = routing_key
        # The type of the resource to which events are delivered.
        self.target_type = target_type
        # The name of the vhost to which the ApsaraMQ for RabbitMQ instance belongs.
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
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Exchange') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersExchange()
            self.exchange = temp_model.from_map(m.get('Exchange'))

        if m.get('InstanceId') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m.get('InstanceId'))

        if m.get('MessageId') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m.get('MessageId'))

        if m.get('Properties') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('QueueName') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersQueueName()
            self.queue_name = temp_model.from_map(m.get('QueueName'))

        if m.get('RoutingKey') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersRoutingKey()
            self.routing_key = temp_model.from_map(m.get('RoutingKey'))

        if m.get('TargetType') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersTargetType()
            self.target_type = temp_model.from_map(m.get('TargetType'))

        if m.get('VirtualHostName') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersVirtualHostName()
            self.virtual_host_name = temp_model.from_map(m.get('VirtualHostName'))

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersVirtualHostName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the vhost to which the ApsaraMQ for RabbitMQ instance belongs.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersTargetType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The type of the resource to which events are delivered. Valid values: Exchange and Queue.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersRoutingKey(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The rule that is used to route messages.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersQueueName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the queue on the ApsaraMQ for RabbitMQ instance.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersProperties(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before transformation.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersMessageId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before transformation.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersInstanceId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The ID of the ApsaraMQ for RabbitMQ instance.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersExchange(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the exchange on the ApsaraMQ for RabbitMQ instance.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before transformation.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkOpenSourceRabbitMQParameters(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        body: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkOpenSourceRabbitMQParametersBody = None,
        endpoint: str = None,
        exchange: str = None,
        message_id: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkOpenSourceRabbitMQParametersMessageId = None,
        network_type: str = None,
        password: str = None,
        properties: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkOpenSourceRabbitMQParametersProperties = None,
        queue_name: str = None,
        routing_key: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkOpenSourceRabbitMQParametersRoutingKey = None,
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
        # VPC ID。
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
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkOpenSourceRabbitMQParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Exchange') is not None:
            self.exchange = m.get('Exchange')

        if m.get('MessageId') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkOpenSourceRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m.get('MessageId'))

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Properties') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkOpenSourceRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('RoutingKey') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkOpenSourceRabbitMQParametersRoutingKey()
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkOpenSourceRabbitMQParametersRoutingKey(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkOpenSourceRabbitMQParametersProperties(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkOpenSourceRabbitMQParametersMessageId(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkOpenSourceRabbitMQParametersBody(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParameters(DaraModel):
    def __init__(
        self,
        body: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersBody = None,
        is_base_64encode: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersIsBase64Encode = None,
        queue_name: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersQueueName = None,
    ):
        # The message content.
        self.body = body
        # Indicates whether Base64 encoding is enabled.
        self.is_base_64encode = is_base_64encode
        # The name of the MNS queue.
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
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('IsBase64Encode') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersIsBase64Encode()
            self.is_base_64encode = temp_model.from_map(m.get('IsBase64Encode'))

        if m.get('QueueName') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersQueueName()
            self.queue_name = temp_model.from_map(m.get('QueueName'))

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersQueueName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersIsBase64Encode(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # Indicates that Base64 encoding is enabled.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before transformation.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParameters(DaraModel):
    def __init__(
        self,
        acks: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersAcks = None,
        compression_type: str = None,
        instance_id: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersInstanceId = None,
        key: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersKey = None,
        topic: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersTopic = None,
        value: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersValue = None,
    ):
        # The acknowledgment (ACK) mode.
        # 
        # *   If you set this parameter to 0, no response is returned from the broker. In this mode, the performance is high, but the risk of data loss is also high.
        # *   If you set this parameter to 1, a response is returned when data is written to the leader. In this mode, the performance and the risk of data loss are moderate. Data loss may occur if a failure occurs on the leader.
        # *   If you set this parameter to all, a response is returned when data is written to the leader and synchronized to the followers. In this mode, the performance is low, but the risk of data loss is also low. Data loss occurs if the leader and the followers fail at the same time.
        self.acks = acks
        self.compression_type = compression_type
        # The ID of the ApsaraMQ for Kafka instance.
        self.instance_id = instance_id
        # The message key.
        self.key = key
        # The name of the topic on the ApsaraMQ for Kafka instance.
        self.topic = topic
        # The message body.
        self.value = value

    def validate(self):
        if self.acks:
            self.acks.validate()
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
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersAcks()
            self.acks = temp_model.from_map(m.get('Acks'))

        if m.get('CompressionType') is not None:
            self.compression_type = m.get('CompressionType')

        if m.get('InstanceId') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersInstanceId()
            self.instance_id = temp_model.from_map(m.get('InstanceId'))

        if m.get('Key') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersKey()
            self.key = temp_model.from_map(m.get('Key'))

        if m.get('Topic') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        if m.get('Value') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersValue()
            self.value = temp_model.from_map(m.get('Value'))

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersValue(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before transformation.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the topic on the ApsaraMQ for Kafka instance.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersKey(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersInstanceId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The ID of the ApsaraMQ for Kafka instance.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersAcks(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The ACK mode.
        # 
        # *   If you set this parameter to 0, no response is returned from the broker. In this mode, the performance is high, but the risk of data loss is also high.
        # *   If you set this parameter to 1, a response is returned when data is written to the leader. In this mode, the performance and the risk of data loss are moderate. Data loss may occur if a failure occurs on the leader.
        # *   If you set this parameter to all, a response is returned when data is written to the leader and synchronized to the followers. In this mode, the performance is low, but the risk of data loss is also low. Data loss occurs if the leader and the followers fail at the same time.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParameters(DaraModel):
    def __init__(
        self,
        execution_name: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersExecutionName = None,
        flow_name: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersFlowName = None,
        input: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersInput = None,
        role_name: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersRoleName = None,
    ):
        # The execution name.
        self.execution_name = execution_name
        # The flow name.
        self.flow_name = flow_name
        # The input information of the execution.
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
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersExecutionName()
            self.execution_name = temp_model.from_map(m.get('ExecutionName'))

        if m.get('FlowName') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersFlowName()
            self.flow_name = temp_model.from_map(m.get('FlowName'))

        if m.get('Input') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('RoleName') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersRoleName()
            self.role_name = temp_model.from_map(m.get('RoleName'))

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersRoleName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which events are transformed.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersInput(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The input information of the execution.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersFlowName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which events are transformed.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersExecutionName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which events are transformed.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParameters(DaraModel):
    def __init__(
        self,
        body: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersBody = None,
        concurrency: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersConcurrency = None,
        data_format: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersDataFormat = None,
        function_name: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersFunctionName = None,
        invocation_type: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersInvocationType = None,
        qualifier: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersQualifier = None,
        service_name: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersServiceName = None,
    ):
        # The message body that is delivered to Function Compute.
        self.body = body
        # The delivery concurrency. Minimum value: 1.
        self.concurrency = concurrency
        self.data_format = data_format
        # The function name.
        self.function_name = function_name
        # The invocation mode. Valid values:
        # 
        # *   Sync
        # *   Async
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
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Concurrency') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersConcurrency()
            self.concurrency = temp_model.from_map(m.get('Concurrency'))

        if m.get('DataFormat') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersDataFormat()
            self.data_format = temp_model.from_map(m.get('DataFormat'))

        if m.get('FunctionName') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersFunctionName()
            self.function_name = temp_model.from_map(m.get('FunctionName'))

        if m.get('InvocationType') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersInvocationType()
            self.invocation_type = temp_model.from_map(m.get('InvocationType'))

        if m.get('Qualifier') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersQualifier()
            self.qualifier = temp_model.from_map(m.get('Qualifier'))

        if m.get('ServiceName') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersServiceName()
            self.service_name = temp_model.from_map(m.get('ServiceName'))

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersServiceName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The service name.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersQualifier(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersInvocationType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The invocation mode. Valid values:
        # 
        # *   Sync
        # *   Async
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersFunctionName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersDataFormat(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersConcurrency(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form
        # None.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that is used to transform events.
        self.form = form
        # The template based on which events are transformed.
        self.template = template
        # The value before transformation.
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParameters(DaraModel):
    def __init__(
        self,
        be_http_endpoint: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersBeHttpEndpoint = None,
        body: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersBody = None,
        database: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersDatabase = None,
        fe_http_endpoint: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersFeHttpEndpoint = None,
        network_type: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersNetworkType = None,
        password: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersPassword = None,
        query_endpoint: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersQueryEndpoint = None,
        security_group_id: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersSecurityGroupId = None,
        table: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersTable = None,
        user_name: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersUserName = None,
        v_switch_ids: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersVSwitchIds = None,
        vpc_id: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersVpcId = None,
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
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersBeHttpEndpoint()
            self.be_http_endpoint = temp_model.from_map(m.get('BeHttpEndpoint'))

        if m.get('Body') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Database') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersDatabase()
            self.database = temp_model.from_map(m.get('Database'))

        if m.get('FeHttpEndpoint') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersFeHttpEndpoint()
            self.fe_http_endpoint = temp_model.from_map(m.get('FeHttpEndpoint'))

        if m.get('NetworkType') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersNetworkType()
            self.network_type = temp_model.from_map(m.get('NetworkType'))

        if m.get('Password') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersPassword()
            self.password = temp_model.from_map(m.get('Password'))

        if m.get('QueryEndpoint') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersQueryEndpoint()
            self.query_endpoint = temp_model.from_map(m.get('QueryEndpoint'))

        if m.get('SecurityGroupId') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersSecurityGroupId()
            self.security_group_id = temp_model.from_map(m.get('SecurityGroupId'))

        if m.get('Table') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersTable()
            self.table = temp_model.from_map(m.get('Table'))

        if m.get('UserName') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersUserName()
            self.user_name = temp_model.from_map(m.get('UserName'))

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        if m.get('VpcId') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersVpcId()
            self.vpc_id = temp_model.from_map(m.get('VpcId'))

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersVpcId(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersVSwitchIds(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersUserName(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersTable(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersSecurityGroupId(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersQueryEndpoint(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersPassword(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersNetworkType(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersFeHttpEndpoint(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersDatabase(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersBody(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDorisParametersBeHttpEndpoint(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParameters(DaraModel):
    def __init__(
        self,
        body: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersBody = None,
        project: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersProject = None,
        role_name: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersRoleName = None,
        topic: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersTopic = None,
        topic_schema: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersTopicSchema = None,
        topic_type: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersTopicType = None,
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
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Project') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersProject()
            self.project = temp_model.from_map(m.get('Project'))

        if m.get('RoleName') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersRoleName()
            self.role_name = temp_model.from_map(m.get('RoleName'))

        if m.get('Topic') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        if m.get('TopicSchema') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersTopicSchema()
            self.topic_schema = temp_model.from_map(m.get('TopicSchema'))

        if m.get('TopicType') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersTopicType()
            self.topic_type = temp_model.from_map(m.get('TopicType'))

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersTopicType(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersTopicSchema(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersTopic(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersRoleName(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersProject(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDataHubParametersBody(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParameters(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        collection: str = None,
        dash_vector_schema_parameters: List[main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersDashVectorSchemaParameters] = None,
        instance_id: str = None,
        network: str = None,
        operation: str = None,
        partition: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersPartition = None,
        primary_key_id: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersPrimaryKeyId = None,
        vector: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersVector = None,
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
                temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersDashVectorSchemaParameters()
                self.dash_vector_schema_parameters.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Partition') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersPartition()
            self.partition = temp_model.from_map(m.get('Partition'))

        if m.get('PrimaryKeyId') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersPrimaryKeyId()
            self.primary_key_id = temp_model.from_map(m.get('PrimaryKeyId'))

        if m.get('Vector') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersVector()
            self.vector = temp_model.from_map(m.get('Vector'))

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersVector(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersPrimaryKeyId(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersPartition(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersDashVectorSchemaParameters(DaraModel):
    def __init__(
        self,
        name: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersDashVectorSchemaParametersName = None,
        type: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersDashVectorSchemaParametersType = None,
        value: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersDashVectorSchemaParametersValue = None,
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
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersDashVectorSchemaParametersName()
            self.name = temp_model.from_map(m.get('Name'))

        if m.get('Type') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersDashVectorSchemaParametersType()
            self.type = temp_model.from_map(m.get('Type'))

        if m.get('Value') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersDashVectorSchemaParametersValue()
            self.value = temp_model.from_map(m.get('Value'))

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersDashVectorSchemaParametersValue(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersDashVectorSchemaParametersType(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkDashVectorParametersDashVectorSchemaParametersName(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkCustomizedKafkaParameters(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkCustomizedKafkaConnectorParameters(DaraModel):
    def __init__(
        self,
        connector_package_url: str = None,
        connector_parameters: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkCustomizedKafkaConnectorParametersConnectorParameters = None,
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
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkCustomizedKafkaConnectorParametersConnectorParameters()
            self.connector_parameters = temp_model.from_map(m.get('ConnectorParameters'))

        if m.get('WorkerParameters') is not None:
            self.worker_parameters = m.get('WorkerParameters')

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkCustomizedKafkaConnectorParametersConnectorParameters(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkApacheRocketMQCheckpointParameters(DaraModel):
    def __init__(
        self,
        consume_timestamp: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkApacheRocketMQCheckpointParametersConsumeTimestamp = None,
        group: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkApacheRocketMQCheckpointParametersGroup = None,
        instance_endpoint: str = None,
        instance_password: str = None,
        instance_username: str = None,
        network_type: str = None,
        security_group_id: str = None,
        topic: main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkApacheRocketMQCheckpointParametersTopic = None,
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
        # VPC ID。
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
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkApacheRocketMQCheckpointParametersConsumeTimestamp()
            self.consume_timestamp = temp_model.from_map(m.get('ConsumeTimestamp'))

        if m.get('Group') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkApacheRocketMQCheckpointParametersGroup()
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
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkApacheRocketMQCheckpointParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkApacheRocketMQCheckpointParametersTopic(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkApacheRocketMQCheckpointParametersGroup(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkApacheRocketMQCheckpointParametersConsumeTimestamp(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsRunOptions(DaraModel):
    def __init__(
        self,
        batch_window: main_models.ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsBatchWindow = None,
        business_option: main_models.ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsBusinessOption = None,
        dead_letter_queue: main_models.ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsDeadLetterQueue = None,
        errors_tolerance: str = None,
        maximum_tasks: int = None,
        retry_strategy: main_models.ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsRetryStrategy = None,
        throttling: int = None,
    ):
        # The batch window.
        self.batch_window = batch_window
        self.business_option = business_option
        # Indicates whether dead-letter queues are enabled. By default, dead-letter queues are disabled. Events that fail to be pushed are discarded after the maximum number of retries that is specified by the retry policy is reached.
        self.dead_letter_queue = dead_letter_queue
        # The exception tolerance policy. Valid values: NONE and ALL.
        self.errors_tolerance = errors_tolerance
        # The maximum number of concurrent tasks.
        self.maximum_tasks = maximum_tasks
        # The retry policy that is used if events fail to be pushed.
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
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsBatchWindow()
            self.batch_window = temp_model.from_map(m.get('BatchWindow'))

        if m.get('BusinessOption') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsBusinessOption()
            self.business_option = temp_model.from_map(m.get('BusinessOption'))

        if m.get('DeadLetterQueue') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m.get('DeadLetterQueue'))

        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')

        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')

        if m.get('RetryStrategy') is not None:
            temp_model = main_models.ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsRetryStrategy()
            self.retry_strategy = temp_model.from_map(m.get('RetryStrategy'))

        if m.get('Throttling') is not None:
            self.throttling = m.get('Throttling')

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsRetryStrategy(DaraModel):
    def __init__(
        self,
        push_retry_strategy: str = None,
    ):
        # The retry policy. Valid values: BACKOFF_RETRY and EXPONENTIAL_DECAY_RETRY.
        self.push_retry_strategy = push_retry_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')

        return self

class ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsDeadLetterQueue(DaraModel):
    def __init__(
        self,
        arn: str = None,
        network: str = None,
        security_group_id: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        # The ARN of the dead-letter queue.
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

class ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsBusinessOption(DaraModel):
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

class ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsBatchWindow(DaraModel):
    def __init__(
        self,
        count_based_window: int = None,
        time_based_window: int = None,
    ):
        # The maximum number of events that are allowed in the batch window. When this threshold is reached, data in the window is pushed to the downstream service. When multiple batch windows exist, data is pushed if triggering conditions are met in one of the windows.
        self.count_based_window = count_based_window
        # The maximum period of time during which events are allowed in the batch window. Unit: seconds. When this threshold is reached, data in the window is pushed to the downstream service. When multiple batch windows exist, data is pushed if triggering conditions are met in one of the windows.
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

