# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class UpdateEventStreamingRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        run_options: main_models.UpdateEventStreamingRequestRunOptions = None,
        sink: main_models.UpdateEventStreamingRequestSink = None,
        source: main_models.UpdateEventStreamingRequestSource = None,
        transforms: List[main_models.UpdateEventStreamingRequestTransforms] = None,
    ):
        # The description of the event stream.
        self.description = description
        # The name of the event stream.
        # 
        # This parameter is required.
        self.event_streaming_name = event_streaming_name
        # The rule that is used to filter events. If you leave this parameter empty, all events are matched.
        # 
        # This parameter is required.
        self.filter_pattern = filter_pattern
        # The parameters that are configured for the runtime environment.
        self.run_options = run_options
        # The event target. You must and can specify only one event target.
        # 
        # This parameter is required.
        self.sink = sink
        # The event provider, which is also known as the event source. You must and can specify only one event source.
        # 
        # This parameter is required.
        self.source = source
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
            temp_model = main_models.UpdateEventStreamingRequestRunOptions()
            self.run_options = temp_model.from_map(m.get('RunOptions'))

        if m.get('Sink') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSink()
            self.sink = temp_model.from_map(m.get('Sink'))

        if m.get('Source') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSource()
            self.source = temp_model.from_map(m.get('Source'))

        self.transforms = []
        if m.get('Transforms') is not None:
            for k1 in m.get('Transforms'):
                temp_model = main_models.UpdateEventStreamingRequestTransforms()
                self.transforms.append(temp_model.from_map(k1))

        return self

class UpdateEventStreamingRequestTransforms(DaraModel):
    def __init__(
        self,
        arn: str = None,
        bai_lian_agent_transform_parameters: main_models.BaiLianAgentTransformParameters = None,
        dash_scope_transform_parameters: main_models.DashScopeTransformParameters = None,
    ):
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

class UpdateEventStreamingRequestSource(DaraModel):
    def __init__(
        self,
        source_apache_kafka_parameters: main_models.UpdateEventStreamingRequestSourceSourceApacheKafkaParameters = None,
        source_apache_rocket_mqcheckpoint_parameters: main_models.UpdateEventStreamingRequestSourceSourceApacheRocketMQCheckpointParameters = None,
        source_customized_kafka_connector_parameters: main_models.UpdateEventStreamingRequestSourceSourceCustomizedKafkaConnectorParameters = None,
        source_customized_kafka_parameters: main_models.UpdateEventStreamingRequestSourceSourceCustomizedKafkaParameters = None,
        source_dtsparameters: main_models.UpdateEventStreamingRequestSourceSourceDTSParameters = None,
        source_event_bus_parameters: main_models.UpdateEventStreamingRequestSourceSourceEventBusParameters = None,
        source_kafka_parameters: main_models.UpdateEventStreamingRequestSourceSourceKafkaParameters = None,
        source_mnsparameters: main_models.UpdateEventStreamingRequestSourceSourceMNSParameters = None,
        source_mqttparameters: main_models.UpdateEventStreamingRequestSourceSourceMQTTParameters = None,
        source_my_sqlparameters: main_models.SourceMySQLParameters = None,
        source_ossparameters: main_models.UpdateEventStreamingRequestSourceSourceOSSParameters = None,
        source_open_source_rabbit_mqparameters: main_models.UpdateEventStreamingRequestSourceSourceOpenSourceRabbitMQParameters = None,
        source_postgre_sqlparameters: main_models.SourcePostgreSQLParameters = None,
        source_prometheus_parameters: main_models.UpdateEventStreamingRequestSourceSourcePrometheusParameters = None,
        source_rabbit_mqmeta_parameters: main_models.SourceRabbitMQMetaParameters = None,
        source_rabbit_mqmsg_sync_parameters: main_models.SourceRabbitMQMsgSyncParameters = None,
        source_rabbit_mqparameters: main_models.UpdateEventStreamingRequestSourceSourceRabbitMQParameters = None,
        source_rocket_mqcheckpoint_parameters: main_models.UpdateEventStreamingRequestSourceSourceRocketMQCheckpointParameters = None,
        source_rocket_mqparameters: main_models.UpdateEventStreamingRequestSourceSourceRocketMQParameters = None,
        source_slsparameters: main_models.UpdateEventStreamingRequestSourceSourceSLSParameters = None,
    ):
        self.source_apache_kafka_parameters = source_apache_kafka_parameters
        self.source_apache_rocket_mqcheckpoint_parameters = source_apache_rocket_mqcheckpoint_parameters
        self.source_customized_kafka_connector_parameters = source_customized_kafka_connector_parameters
        self.source_customized_kafka_parameters = source_customized_kafka_parameters
        # The parameters that are configured if you specify Data Transmission Service (DTS) as the event source.
        self.source_dtsparameters = source_dtsparameters
        self.source_event_bus_parameters = source_event_bus_parameters
        # The parameters that are configured if you specify ApsaraMQ for Kafka as the event source.
        self.source_kafka_parameters = source_kafka_parameters
        # The parameters that are configured if you specify Message Service (MNS) as the event source.
        self.source_mnsparameters = source_mnsparameters
        # The parameters that are configured if you specify ApsaraMQ for MQTT as the event source.
        self.source_mqttparameters = source_mqttparameters
        self.source_my_sqlparameters = source_my_sqlparameters
        self.source_ossparameters = source_ossparameters
        self.source_open_source_rabbit_mqparameters = source_open_source_rabbit_mqparameters
        self.source_postgre_sqlparameters = source_postgre_sqlparameters
        # The parameters that are configured if you specify Managed Service for Prometheus as the event source.
        self.source_prometheus_parameters = source_prometheus_parameters
        self.source_rabbit_mqmeta_parameters = source_rabbit_mqmeta_parameters
        self.source_rabbit_mqmsg_sync_parameters = source_rabbit_mqmsg_sync_parameters
        # The parameters that are configured if you specify ApsaraMQ for RabbitMQ as the event source.
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        self.source_rocket_mqcheckpoint_parameters = source_rocket_mqcheckpoint_parameters
        # The parameters that are configured if you specify ApsaraMQ for RocketMQ as the event source.
        self.source_rocket_mqparameters = source_rocket_mqparameters
        # The parameters that are configured if you specify Simple Log Service as the event source.
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
            temp_model = main_models.UpdateEventStreamingRequestSourceSourceApacheKafkaParameters()
            self.source_apache_kafka_parameters = temp_model.from_map(m.get('SourceApacheKafkaParameters'))

        if m.get('SourceApacheRocketMQCheckpointParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSourceSourceApacheRocketMQCheckpointParameters()
            self.source_apache_rocket_mqcheckpoint_parameters = temp_model.from_map(m.get('SourceApacheRocketMQCheckpointParameters'))

        if m.get('SourceCustomizedKafkaConnectorParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSourceSourceCustomizedKafkaConnectorParameters()
            self.source_customized_kafka_connector_parameters = temp_model.from_map(m.get('SourceCustomizedKafkaConnectorParameters'))

        if m.get('SourceCustomizedKafkaParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSourceSourceCustomizedKafkaParameters()
            self.source_customized_kafka_parameters = temp_model.from_map(m.get('SourceCustomizedKafkaParameters'))

        if m.get('SourceDTSParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSourceSourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m.get('SourceDTSParameters'))

        if m.get('SourceEventBusParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSourceSourceEventBusParameters()
            self.source_event_bus_parameters = temp_model.from_map(m.get('SourceEventBusParameters'))

        if m.get('SourceKafkaParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSourceSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m.get('SourceKafkaParameters'))

        if m.get('SourceMNSParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSourceSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m.get('SourceMNSParameters'))

        if m.get('SourceMQTTParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSourceSourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m.get('SourceMQTTParameters'))

        if m.get('SourceMySQLParameters') is not None:
            temp_model = main_models.SourceMySQLParameters()
            self.source_my_sqlparameters = temp_model.from_map(m.get('SourceMySQLParameters'))

        if m.get('SourceOSSParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSourceSourceOSSParameters()
            self.source_ossparameters = temp_model.from_map(m.get('SourceOSSParameters'))

        if m.get('SourceOpenSourceRabbitMQParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSourceSourceOpenSourceRabbitMQParameters()
            self.source_open_source_rabbit_mqparameters = temp_model.from_map(m.get('SourceOpenSourceRabbitMQParameters'))

        if m.get('SourcePostgreSQLParameters') is not None:
            temp_model = main_models.SourcePostgreSQLParameters()
            self.source_postgre_sqlparameters = temp_model.from_map(m.get('SourcePostgreSQLParameters'))

        if m.get('SourcePrometheusParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSourceSourcePrometheusParameters()
            self.source_prometheus_parameters = temp_model.from_map(m.get('SourcePrometheusParameters'))

        if m.get('SourceRabbitMQMetaParameters') is not None:
            temp_model = main_models.SourceRabbitMQMetaParameters()
            self.source_rabbit_mqmeta_parameters = temp_model.from_map(m.get('SourceRabbitMQMetaParameters'))

        if m.get('SourceRabbitMQMsgSyncParameters') is not None:
            temp_model = main_models.SourceRabbitMQMsgSyncParameters()
            self.source_rabbit_mqmsg_sync_parameters = temp_model.from_map(m.get('SourceRabbitMQMsgSyncParameters'))

        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSourceSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m.get('SourceRabbitMQParameters'))

        if m.get('SourceRocketMQCheckpointParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSourceSourceRocketMQCheckpointParameters()
            self.source_rocket_mqcheckpoint_parameters = temp_model.from_map(m.get('SourceRocketMQCheckpointParameters'))

        if m.get('SourceRocketMQParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSourceSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m.get('SourceRocketMQParameters'))

        if m.get('SourceSLSParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSourceSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m.get('SourceSLSParameters'))

        return self

class UpdateEventStreamingRequestSourceSourceSLSParameters(DaraModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        # The role name. If you want to authorize EventBridge to use this role to read logs in Simple Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the Resource Access Management (RAM) console.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

class UpdateEventStreamingRequestSourceSourceRocketMQParameters(DaraModel):
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
        # The endpoint that you want to use to access the ApsaraMQ for RocketMQ instance.
        self.instance_endpoint = instance_endpoint
        # The ID of the ApsaraMQ for RocketMQ instance.
        self.instance_id = instance_id
        # The network type of the ApsaraMQ for RocketMQ instance. Valid values:
        # 
        # PublicNetwork and PrivateNetwork.
        self.instance_network = instance_network
        # The password that you want to use to access the ApsaraMQ for RocketMQ instance.
        self.instance_password = instance_password
        # The ID of the security group to which the ApsaraMQ for RocketMQ instance belongs.
        self.instance_security_group_id = instance_security_group_id
        # The type of the ApsaraMQ for RocketMQ instance.
        self.instance_type = instance_type
        # The username that you want to use to access the ApsaraMQ for RocketMQ instance.
        self.instance_username = instance_username
        # The ID of the vSwitch with which the ApsaraMQ for RocketMQ instance is associated.
        self.instance_vswitch_ids = instance_vswitch_ids
        # The ID of the VPC in which the ApsaraMQ for RocketMQ instance is deployed.
        self.instance_vpc_id = instance_vpc_id
        self.network = network
        # The offset from which messages are consumed. Valid values:
        # 
        # *   CONSUMEFROMLASTOFFSET: Messages are consumed from the latest offset.
        # *   CONSUMEFROMFIRSTOFFSET: Messages are consumed from the earliest offset.
        # *   CONSUMEFROMTIMESTAMP: Messages are consumed from the offset at the specified point in time.
        # 
        # Default value: CONSUMEFROMLASTOFFSET.
        self.offset = offset
        # The ID of the region where the ApsaraMQ for RocketMQ instance resides.
        self.region_id = region_id
        self.security_group_id = security_group_id
        # The tag that you want to use to filter messages.
        self.tag = tag
        # The timestamp that specifies the time from which messages are consumed. This parameter is valid only if you set Offset to CONSUMEFROMTIMESTAMP.
        self.timestamp = timestamp
        # The name of the topic on the ApsaraMQ for RocketMQ instance.
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

class UpdateEventStreamingRequestSourceSourceRocketMQCheckpointParameters(DaraModel):
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

class UpdateEventStreamingRequestSourceSourceRabbitMQParameters(DaraModel):
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
        # The name of the vhost of the ApsaraMQ for RabbitMQ instance.
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

class UpdateEventStreamingRequestSourceSourcePrometheusParameters(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_type: str = None,
        external_labels: str = None,
        labels: str = None,
        region_id: str = None,
        role_name: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The data type.
        self.data_type = data_type
        self.external_labels = external_labels
        # The labels.
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

class UpdateEventStreamingRequestSourceSourceOpenSourceRabbitMQParameters(DaraModel):
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

class UpdateEventStreamingRequestSourceSourceOSSParameters(DaraModel):
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

class UpdateEventStreamingRequestSourceSourceMQTTParameters(DaraModel):
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

class UpdateEventStreamingRequestSourceSourceMNSParameters(DaraModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        # Specifies whether to enable Base64 encoding. Default value: true.
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

class UpdateEventStreamingRequestSourceSourceKafkaParameters(DaraModel):
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
        # The network setting. Default value: Default. The value PublicNetwork specifies a virtual private cloud (VPC).
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
        # The encoding or decoding method. Valid values: Json, Text, and Binary. The value Json specifies that binary data is decoded into strings based on UTF-8 encoding and then parsed into the JSON format. The value Text specifies that binary data is decoded into strings based on UTF-8 encoding and then put into the payload. The value Binary specifies that binary data is encoded into strings based on Base64 encoding and then put into the payload.
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

class UpdateEventStreamingRequestSourceSourceEventBusParameters(DaraModel):
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

class UpdateEventStreamingRequestSourceSourceDTSParameters(DaraModel):
    def __init__(
        self,
        broker_url: str = None,
        init_check_point: int = None,
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

class UpdateEventStreamingRequestSourceSourceCustomizedKafkaParameters(DaraModel):
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

class UpdateEventStreamingRequestSourceSourceCustomizedKafkaConnectorParameters(DaraModel):
    def __init__(
        self,
        connector_package_url: str = None,
        connector_parameters: main_models.UpdateEventStreamingRequestSourceSourceCustomizedKafkaConnectorParametersConnectorParameters = None,
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
            temp_model = main_models.UpdateEventStreamingRequestSourceSourceCustomizedKafkaConnectorParametersConnectorParameters()
            self.connector_parameters = temp_model.from_map(m.get('ConnectorParameters'))

        if m.get('WorkerParameters') is not None:
            self.worker_parameters = m.get('WorkerParameters')

        return self

class UpdateEventStreamingRequestSourceSourceCustomizedKafkaConnectorParametersConnectorParameters(DaraModel):
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

class UpdateEventStreamingRequestSourceSourceApacheRocketMQCheckpointParameters(DaraModel):
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

class UpdateEventStreamingRequestSourceSourceApacheKafkaParameters(DaraModel):
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

class UpdateEventStreamingRequestSink(DaraModel):
    def __init__(
        self,
        sink_apache_kafka_parameters: main_models.UpdateEventStreamingRequestSinkSinkApacheKafkaParameters = None,
        sink_apache_rocket_mqcheckpoint_parameters: main_models.UpdateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParameters = None,
        sink_api_destination_parameters: main_models.SinkApiDestinationParameters = None,
        sink_bai_lian_parameters: main_models.SinkBaiLianParameters = None,
        sink_customized_kafka_connector_parameters: main_models.UpdateEventStreamingRequestSinkSinkCustomizedKafkaConnectorParameters = None,
        sink_customized_kafka_parameters: main_models.UpdateEventStreamingRequestSinkSinkCustomizedKafkaParameters = None,
        sink_dash_vector_parameters: main_models.UpdateEventStreamingRequestSinkSinkDashVectorParameters = None,
        sink_data_hub_parameters: main_models.UpdateEventStreamingRequestSinkSinkDataHubParameters = None,
        sink_data_works_trigger_parameters: main_models.SinkDataWorksTriggerParameters = None,
        sink_doris_parameters: main_models.UpdateEventStreamingRequestSinkSinkDorisParameters = None,
        sink_fc_parameters: main_models.UpdateEventStreamingRequestSinkSinkFcParameters = None,
        sink_fnf_parameters: main_models.UpdateEventStreamingRequestSinkSinkFnfParameters = None,
        sink_https_parameters: main_models.SinkHttpsParameters = None,
        sink_kafka_parameters: main_models.UpdateEventStreamingRequestSinkSinkKafkaParameters = None,
        sink_mnsparameters: main_models.UpdateEventStreamingRequestSinkSinkMNSParameters = None,
        sink_ossparameters: main_models.SinkOSSParameters = None,
        sink_open_source_rabbit_mqparameters: main_models.UpdateEventStreamingRequestSinkSinkOpenSourceRabbitMQParameters = None,
        sink_prometheus_parameters: main_models.UpdateEventStreamingRequestSinkSinkPrometheusParameters = None,
        sink_rabbit_mqmeta_parameters: main_models.SinkRabbitMQMetaParameters = None,
        sink_rabbit_mqmsg_sync_parameters: main_models.SinkRabbitMQMsgSyncParameters = None,
        sink_rabbit_mqparameters: main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParameters = None,
        sink_rocket_mqcheckpoint_parameters: main_models.UpdateEventStreamingRequestSinkSinkRocketMQCheckpointParameters = None,
        sink_rocket_mqparameters: main_models.UpdateEventStreamingRequestSinkSinkRocketMQParameters = None,
        sink_slsparameters: main_models.UpdateEventStreamingRequestSinkSinkSLSParameters = None,
    ):
        self.sink_apache_kafka_parameters = sink_apache_kafka_parameters
        # The parameters that are configured if you specify Apache RocketMQ (Offset Data) as the event target.
        self.sink_apache_rocket_mqcheckpoint_parameters = sink_apache_rocket_mqcheckpoint_parameters
        self.sink_api_destination_parameters = sink_api_destination_parameters
        # The parameters that are configured if you specify BaiLian as the event target.
        self.sink_bai_lian_parameters = sink_bai_lian_parameters
        # The parameters that are configured if you specify Kafka Sink Connect as the event target.
        self.sink_customized_kafka_connector_parameters = sink_customized_kafka_connector_parameters
        # The parameters that are configured if you specify Kafka Source Connect as the event target.
        self.sink_customized_kafka_parameters = sink_customized_kafka_parameters
        # The parameters that are configured if you specify DashVector as the event target.
        self.sink_dash_vector_parameters = sink_dash_vector_parameters
        # The parameters that are configured if you specify DataHub as the event target.
        self.sink_data_hub_parameters = sink_data_hub_parameters
        self.sink_data_works_trigger_parameters = sink_data_works_trigger_parameters
        # The type of the event source.
        self.sink_doris_parameters = sink_doris_parameters
        # The parameters that are configured if you specify Function Compute as the event target.
        self.sink_fc_parameters = sink_fc_parameters
        # The parameters that are configured if you specify CloudFlow as the event target.
        self.sink_fnf_parameters = sink_fnf_parameters
        self.sink_https_parameters = sink_https_parameters
        # The parameters that are configured if you specify ApsaraMQ for Kafka as the event target.
        self.sink_kafka_parameters = sink_kafka_parameters
        # The parameters that are configured if you specify Simple Message Queue (SMQ, formerly MNS) as the event target.
        self.sink_mnsparameters = sink_mnsparameters
        self.sink_ossparameters = sink_ossparameters
        # The parameters that are configured if you specify open source RabbitMQ as the event target.
        self.sink_open_source_rabbit_mqparameters = sink_open_source_rabbit_mqparameters
        # The parameters that are configured if you specify Managed Service for Prometheus as the event target.
        self.sink_prometheus_parameters = sink_prometheus_parameters
        self.sink_rabbit_mqmeta_parameters = sink_rabbit_mqmeta_parameters
        self.sink_rabbit_mqmsg_sync_parameters = sink_rabbit_mqmsg_sync_parameters
        # The parameters that are configured if you specify ApsaraMQ for RabbitMQ as the event target.
        self.sink_rabbit_mqparameters = sink_rabbit_mqparameters
        # The parameters that are configured if you specify ApsaraMQ for RocketMQ (Offset Data) as the event target.
        self.sink_rocket_mqcheckpoint_parameters = sink_rocket_mqcheckpoint_parameters
        # The parameters that are configured if you specify ApsaraMQ for RocketMQ as the event target.
        self.sink_rocket_mqparameters = sink_rocket_mqparameters
        # The parameters that are configured if you specify Simple Log Service as the event target.
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
        if self.sink_prometheus_parameters:
            self.sink_prometheus_parameters.validate()
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

        if self.sink_prometheus_parameters is not None:
            result['SinkPrometheusParameters'] = self.sink_prometheus_parameters.to_map()

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
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkApacheKafkaParameters()
            self.sink_apache_kafka_parameters = temp_model.from_map(m.get('SinkApacheKafkaParameters'))

        if m.get('SinkApacheRocketMQCheckpointParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParameters()
            self.sink_apache_rocket_mqcheckpoint_parameters = temp_model.from_map(m.get('SinkApacheRocketMQCheckpointParameters'))

        if m.get('SinkApiDestinationParameters') is not None:
            temp_model = main_models.SinkApiDestinationParameters()
            self.sink_api_destination_parameters = temp_model.from_map(m.get('SinkApiDestinationParameters'))

        if m.get('SinkBaiLianParameters') is not None:
            temp_model = main_models.SinkBaiLianParameters()
            self.sink_bai_lian_parameters = temp_model.from_map(m.get('SinkBaiLianParameters'))

        if m.get('SinkCustomizedKafkaConnectorParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkCustomizedKafkaConnectorParameters()
            self.sink_customized_kafka_connector_parameters = temp_model.from_map(m.get('SinkCustomizedKafkaConnectorParameters'))

        if m.get('SinkCustomizedKafkaParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkCustomizedKafkaParameters()
            self.sink_customized_kafka_parameters = temp_model.from_map(m.get('SinkCustomizedKafkaParameters'))

        if m.get('SinkDashVectorParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDashVectorParameters()
            self.sink_dash_vector_parameters = temp_model.from_map(m.get('SinkDashVectorParameters'))

        if m.get('SinkDataHubParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDataHubParameters()
            self.sink_data_hub_parameters = temp_model.from_map(m.get('SinkDataHubParameters'))

        if m.get('SinkDataWorksTriggerParameters') is not None:
            temp_model = main_models.SinkDataWorksTriggerParameters()
            self.sink_data_works_trigger_parameters = temp_model.from_map(m.get('SinkDataWorksTriggerParameters'))

        if m.get('SinkDorisParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDorisParameters()
            self.sink_doris_parameters = temp_model.from_map(m.get('SinkDorisParameters'))

        if m.get('SinkFcParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkFcParameters()
            self.sink_fc_parameters = temp_model.from_map(m.get('SinkFcParameters'))

        if m.get('SinkFnfParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkFnfParameters()
            self.sink_fnf_parameters = temp_model.from_map(m.get('SinkFnfParameters'))

        if m.get('SinkHttpsParameters') is not None:
            temp_model = main_models.SinkHttpsParameters()
            self.sink_https_parameters = temp_model.from_map(m.get('SinkHttpsParameters'))

        if m.get('SinkKafkaParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkKafkaParameters()
            self.sink_kafka_parameters = temp_model.from_map(m.get('SinkKafkaParameters'))

        if m.get('SinkMNSParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkMNSParameters()
            self.sink_mnsparameters = temp_model.from_map(m.get('SinkMNSParameters'))

        if m.get('SinkOSSParameters') is not None:
            temp_model = main_models.SinkOSSParameters()
            self.sink_ossparameters = temp_model.from_map(m.get('SinkOSSParameters'))

        if m.get('SinkOpenSourceRabbitMQParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkOpenSourceRabbitMQParameters()
            self.sink_open_source_rabbit_mqparameters = temp_model.from_map(m.get('SinkOpenSourceRabbitMQParameters'))

        if m.get('SinkPrometheusParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkPrometheusParameters()
            self.sink_prometheus_parameters = temp_model.from_map(m.get('SinkPrometheusParameters'))

        if m.get('SinkRabbitMQMetaParameters') is not None:
            temp_model = main_models.SinkRabbitMQMetaParameters()
            self.sink_rabbit_mqmeta_parameters = temp_model.from_map(m.get('SinkRabbitMQMetaParameters'))

        if m.get('SinkRabbitMQMsgSyncParameters') is not None:
            temp_model = main_models.SinkRabbitMQMsgSyncParameters()
            self.sink_rabbit_mqmsg_sync_parameters = temp_model.from_map(m.get('SinkRabbitMQMsgSyncParameters'))

        if m.get('SinkRabbitMQParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParameters()
            self.sink_rabbit_mqparameters = temp_model.from_map(m.get('SinkRabbitMQParameters'))

        if m.get('SinkRocketMQCheckpointParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQCheckpointParameters()
            self.sink_rocket_mqcheckpoint_parameters = temp_model.from_map(m.get('SinkRocketMQCheckpointParameters'))

        if m.get('SinkRocketMQParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQParameters()
            self.sink_rocket_mqparameters = temp_model.from_map(m.get('SinkRocketMQParameters'))

        if m.get('SinkSLSParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkSLSParameters()
            self.sink_slsparameters = temp_model.from_map(m.get('SinkSLSParameters'))

        return self

class UpdateEventStreamingRequestSinkSinkSLSParameters(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateEventStreamingRequestSinkSinkSLSParametersBody = None,
        content_schema: main_models.UpdateEventStreamingRequestSinkSinkSLSParametersContentSchema = None,
        content_type: main_models.UpdateEventStreamingRequestSinkSinkSLSParametersContentType = None,
        log_store: main_models.UpdateEventStreamingRequestSinkSinkSLSParametersLogStore = None,
        project: main_models.UpdateEventStreamingRequestSinkSinkSLSParametersProject = None,
        role_name: main_models.UpdateEventStreamingRequestSinkSinkSLSParametersRoleName = None,
        topic: main_models.UpdateEventStreamingRequestSinkSinkSLSParametersTopic = None,
    ):
        # The message body that you want to deliver to Simple Log Service.
        self.body = body
        # The key-value pair of custom logs. This parameter takes effect only if you set ContentType to KeyValue. Each key-value pair is in the Key_n, Value_n format.
        self.content_schema = content_schema
        # The format of the Simple Log Service data. Valid values:
        # 
        # *   JSON
        # *   KeyValue
        self.content_type = content_type
        # The Simple Log Service Logstore.
        self.log_store = log_store
        # The Simple Log Service project.
        self.project = project
        # The role name. If you want to authorize EventBridge to use this role to read logs in Simple Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the Resource Access Management (RAM) console.
        self.role_name = role_name
        # The topic that you want to use to store logs. This parameter corresponds to the reserved field topic in Simple Log Service.
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
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkSLSParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('ContentSchema') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkSLSParametersContentSchema()
            self.content_schema = temp_model.from_map(m.get('ContentSchema'))

        if m.get('ContentType') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkSLSParametersContentType()
            self.content_type = temp_model.from_map(m.get('ContentType'))

        if m.get('LogStore') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkSLSParametersLogStore()
            self.log_store = temp_model.from_map(m.get('LogStore'))

        if m.get('Project') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkSLSParametersProject()
            self.project = temp_model.from_map(m.get('Project'))

        if m.get('RoleName') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkSLSParametersRoleName()
            self.role_name = temp_model.from_map(m.get('RoleName'))

        if m.get('Topic') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkSLSParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        return self

class UpdateEventStreamingRequestSinkSinkSLSParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The topic that you want to use to store logs. This parameter corresponds to the reserved field topic in Simple Log Service.
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

class UpdateEventStreamingRequestSinkSinkSLSParametersRoleName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The role name. If you want to authorize EventBridge to use this role to read logs in Simple Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the RAM console.
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

class UpdateEventStreamingRequestSinkSinkSLSParametersProject(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
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

class UpdateEventStreamingRequestSinkSinkSLSParametersLogStore(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
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

class UpdateEventStreamingRequestSinkSinkSLSParametersContentType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The format of the Simple Log Service data.
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

class UpdateEventStreamingRequestSinkSinkSLSParametersContentSchema(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The key-value pair of custom logs.
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

class UpdateEventStreamingRequestSinkSinkSLSParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value before event transformation.
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

class UpdateEventStreamingRequestSinkSinkRocketMQParameters(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersBody = None,
        delivery_order_type: main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersDeliveryOrderType = None,
        instance_endpoint: main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceEndpoint = None,
        instance_id: main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceId = None,
        instance_password: main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersInstancePassword = None,
        instance_type: main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceType = None,
        instance_username: main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceUsername = None,
        keys: main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersKeys = None,
        network: main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersNetwork = None,
        properties: main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersProperties = None,
        security_group_id: main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersSecurityGroupId = None,
        sharding_key: main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersShardingKey = None,
        tags: main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersTags = None,
        topic: main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersTopic = None,
        v_switch_ids: main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersVSwitchIds = None,
        vpc_id: main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersVpcId = None,
    ):
        # The message body.
        self.body = body
        # The type of the message delivery order. This parameter is optional. Default value: Concurrently.
        self.delivery_order_type = delivery_order_type
        # The endpoint that is used to access the instance.
        self.instance_endpoint = instance_endpoint
        # The ID of the ApsaraMQ for RocketMQ instance.
        self.instance_id = instance_id
        # The password that is used to access the instance.
        self.instance_password = instance_password
        # The instance type.
        self.instance_type = instance_type
        # The username that is used to access the instance.
        self.instance_username = instance_username
        # The keys that you want to use to filter messages.
        self.keys = keys
        # The network type. Valid values:
        # 
        # *   PublicNetwork
        # *   PrivateNetwork
        self.network = network
        # The attributes that you want to use to filter messages.
        self.properties = properties
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The sharding key.
        # 
        # >  If you set DeliveryOrderType to Orderly, this parameter is required. If you specify ApsaraMQ for RocketMQ as the event source, you can leave this parameter empty. In this case, the combined value of BrokerName and QueueId is used as the sharding key.
        self.sharding_key = sharding_key
        # The tags that you want to use to filter messages.
        self.tags = tags
        # The name of the topic on the ApsaraMQ for RocketMQ instance.
        self.topic = topic
        # The vSwitch ID.
        self.v_switch_ids = v_switch_ids
        # The virtual private cloud (VPC) ID.
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
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('DeliveryOrderType') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersDeliveryOrderType()
            self.delivery_order_type = temp_model.from_map(m.get('DeliveryOrderType'))

        if m.get('InstanceEndpoint') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceEndpoint()
            self.instance_endpoint = temp_model.from_map(m.get('InstanceEndpoint'))

        if m.get('InstanceId') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m.get('InstanceId'))

        if m.get('InstancePassword') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersInstancePassword()
            self.instance_password = temp_model.from_map(m.get('InstancePassword'))

        if m.get('InstanceType') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceType()
            self.instance_type = temp_model.from_map(m.get('InstanceType'))

        if m.get('InstanceUsername') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceUsername()
            self.instance_username = temp_model.from_map(m.get('InstanceUsername'))

        if m.get('Keys') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersKeys()
            self.keys = temp_model.from_map(m.get('Keys'))

        if m.get('Network') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        if m.get('Properties') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('SecurityGroupId') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersSecurityGroupId()
            self.security_group_id = temp_model.from_map(m.get('SecurityGroupId'))

        if m.get('ShardingKey') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersShardingKey()
            self.sharding_key = temp_model.from_map(m.get('ShardingKey'))

        if m.get('Tags') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Topic') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        if m.get('VpcId') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQParametersVpcId()
            self.vpc_id = temp_model.from_map(m.get('VpcId'))

        return self

class UpdateEventStreamingRequestSinkSinkRocketMQParametersVpcId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The VPC ID.
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

class UpdateEventStreamingRequestSinkSinkRocketMQParametersVSwitchIds(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The vSwitch ID.
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

class UpdateEventStreamingRequestSinkSinkRocketMQParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the topic on the ApsaraMQ for RocketMQ instance.
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

class UpdateEventStreamingRequestSinkSinkRocketMQParametersTags(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value before event transformation.
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

class UpdateEventStreamingRequestSinkSinkRocketMQParametersShardingKey(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value of the sharding key.
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

class UpdateEventStreamingRequestSinkSinkRocketMQParametersSecurityGroupId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The ID of the security group.
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

class UpdateEventStreamingRequestSinkSinkRocketMQParametersProperties(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value before event transformation.
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

class UpdateEventStreamingRequestSinkSinkRocketMQParametersNetwork(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The network type. Valid values:
        # 
        # *   PublicNetwork
        # *   PrivateNetwork
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

class UpdateEventStreamingRequestSinkSinkRocketMQParametersKeys(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value before event transformation.
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

class UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceUsername(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The username that is used to access the instance.
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

class UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The instance type. Valid values:
        # 
        # *   Cloud_4 (default): ApsaraMQ for RocketMQ 4.0 instance
        # *   Cloud_5: ApsaraMQ for RocketMQ 5.0 instance
        # *   SelfBuilt: self-managed Apache RocketMQ cluster
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

class UpdateEventStreamingRequestSinkSinkRocketMQParametersInstancePassword(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The password that is used to access the instance.
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

class UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
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

class UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceEndpoint(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The endpoint that is used to access the instance.
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

class UpdateEventStreamingRequestSinkSinkRocketMQParametersDeliveryOrderType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The type of the message delivery order. Valid values:
        # 
        # *   **Orderly**
        # *   **Concurrently**
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

class UpdateEventStreamingRequestSinkSinkRocketMQParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value before event transformation.
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

class UpdateEventStreamingRequestSinkSinkRocketMQCheckpointParameters(DaraModel):
    def __init__(
        self,
        consume_timestamp: main_models.UpdateEventStreamingRequestSinkSinkRocketMQCheckpointParametersConsumeTimestamp = None,
        group: main_models.UpdateEventStreamingRequestSinkSinkRocketMQCheckpointParametersGroup = None,
        instance_id: str = None,
        instance_type: str = None,
        topic: main_models.UpdateEventStreamingRequestSinkSinkRocketMQCheckpointParametersTopic = None,
    ):
        # The timestamp that specifies the time from which messages are consumed.
        self.consume_timestamp = consume_timestamp
        # The ID of the consumer group.
        self.group = group
        # The ID of the ApsaraMQ for RocketMQ instance.
        self.instance_id = instance_id
        # The instance type. Valid values:
        # 
        # *   Cloud_4: ApsaraMQ for RocketMQ 4.0 instance
        # *   Cloud_5: ApsaraMQ for RocketMQ 5.0 instance
        self.instance_type = instance_type
        # The name of the topic on the ApsaraMQ for RocketMQ instance.
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
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQCheckpointParametersConsumeTimestamp()
            self.consume_timestamp = temp_model.from_map(m.get('ConsumeTimestamp'))

        if m.get('Group') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQCheckpointParametersGroup()
            self.group = temp_model.from_map(m.get('Group'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Topic') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRocketMQCheckpointParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        return self

class UpdateEventStreamingRequestSinkSinkRocketMQCheckpointParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The name of the topic on the ApsaraMQ for RocketMQ instance.
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

class UpdateEventStreamingRequestSinkSinkRocketMQCheckpointParametersGroup(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The ID of the consumer group.
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

class UpdateEventStreamingRequestSinkSinkRocketMQCheckpointParametersConsumeTimestamp(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The timestamp that specifies the time from which messages are consumed.
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

class UpdateEventStreamingRequestSinkSinkRabbitMQParameters(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersBody = None,
        exchange: main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersExchange = None,
        instance_id: main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId = None,
        message_id: main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersMessageId = None,
        properties: main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersProperties = None,
        queue_name: main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersQueueName = None,
        routing_key: main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey = None,
        target_type: main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersTargetType = None,
        virtual_host_name: main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName = None,
    ):
        # The message body.
        self.body = body
        # The exchange mode. This parameter is required only if you set TargetType to Exchange.
        self.exchange = exchange
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.instance_id = instance_id
        # The message ID.
        self.message_id = message_id
        # The attributes that you want to use to filter messages.
        self.properties = properties
        # The queue mode. This parameter is required only if you set TargetType to Queue.
        self.queue_name = queue_name
        # The rule that you want to use to route messages. This parameter is required only if you set TargetType to Exchange.
        self.routing_key = routing_key
        # The type of the resource to which you want to deliver events.
        self.target_type = target_type
        # The name of the vhost of the ApsaraMQ for RabbitMQ instance.
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
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Exchange') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersExchange()
            self.exchange = temp_model.from_map(m.get('Exchange'))

        if m.get('InstanceId') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m.get('InstanceId'))

        if m.get('MessageId') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m.get('MessageId'))

        if m.get('Properties') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('QueueName') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersQueueName()
            self.queue_name = temp_model.from_map(m.get('QueueName'))

        if m.get('RoutingKey') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey()
            self.routing_key = temp_model.from_map(m.get('RoutingKey'))

        if m.get('TargetType') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersTargetType()
            self.target_type = temp_model.from_map(m.get('TargetType'))

        if m.get('VirtualHostName') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName()
            self.virtual_host_name = temp_model.from_map(m.get('VirtualHostName'))

        return self

class UpdateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the vhost of the ApsaraMQ for RabbitMQ instance.
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

class UpdateEventStreamingRequestSinkSinkRabbitMQParametersTargetType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The type of the resource to which you want to deliver events. Valid values:
        # 
        # *   Exchange
        # *   Queue
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

class UpdateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The rule that you want to use to route messages.
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

class UpdateEventStreamingRequestSinkSinkRabbitMQParametersQueueName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
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

class UpdateEventStreamingRequestSinkSinkRabbitMQParametersProperties(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value before event transformation.
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

class UpdateEventStreamingRequestSinkSinkRabbitMQParametersMessageId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value before event transformation.
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

class UpdateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
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

class UpdateEventStreamingRequestSinkSinkRabbitMQParametersExchange(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
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

class UpdateEventStreamingRequestSinkSinkRabbitMQParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value before event transformation.
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

class UpdateEventStreamingRequestSinkSinkPrometheusParameters(DaraModel):
    def __init__(
        self,
        authorization_type: main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersAuthorizationType = None,
        data: main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersData = None,
        header_parameters: main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersHeaderParameters = None,
        network_type: main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersNetworkType = None,
        password: main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersPassword = None,
        security_group_id: main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersSecurityGroupId = None,
        url: main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersURL = None,
        username: main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersUsername = None,
        v_switch_id: main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersVSwitchId = None,
        vpc_id: main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersVpcId = None,
    ):
        # The authentication method.
        self.authorization_type = authorization_type
        # The metric data.
        self.data = data
        # The parameters that are configured for the request header.
        self.header_parameters = header_parameters
        # The network type.
        self.network_type = network_type
        # The password.
        self.password = password
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The URL for the remote write configuration item of the Managed Service for Prometheus instance.
        self.url = url
        # The username.
        self.username = username
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        if self.authorization_type:
            self.authorization_type.validate()
        if self.data:
            self.data.validate()
        if self.header_parameters:
            self.header_parameters.validate()
        if self.network_type:
            self.network_type.validate()
        if self.password:
            self.password.validate()
        if self.security_group_id:
            self.security_group_id.validate()
        if self.url:
            self.url.validate()
        if self.username:
            self.username.validate()
        if self.v_switch_id:
            self.v_switch_id.validate()
        if self.vpc_id:
            self.vpc_id.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type.to_map()

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.header_parameters is not None:
            result['HeaderParameters'] = self.header_parameters.to_map()

        if self.network_type is not None:
            result['NetworkType'] = self.network_type.to_map()

        if self.password is not None:
            result['Password'] = self.password.to_map()

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id.to_map()

        if self.url is not None:
            result['URL'] = self.url.to_map()

        if self.username is not None:
            result['Username'] = self.username.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationType') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersAuthorizationType()
            self.authorization_type = temp_model.from_map(m.get('AuthorizationType'))

        if m.get('Data') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HeaderParameters') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersHeaderParameters()
            self.header_parameters = temp_model.from_map(m.get('HeaderParameters'))

        if m.get('NetworkType') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersNetworkType()
            self.network_type = temp_model.from_map(m.get('NetworkType'))

        if m.get('Password') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersPassword()
            self.password = temp_model.from_map(m.get('Password'))

        if m.get('SecurityGroupId') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersSecurityGroupId()
            self.security_group_id = temp_model.from_map(m.get('SecurityGroupId'))

        if m.get('URL') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersURL()
            self.url = temp_model.from_map(m.get('URL'))

        if m.get('Username') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersUsername()
            self.username = temp_model.from_map(m.get('Username'))

        if m.get('VSwitchId') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersVSwitchId()
            self.v_switch_id = temp_model.from_map(m.get('VSwitchId'))

        if m.get('VpcId') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkPrometheusParametersVpcId()
            self.vpc_id = temp_model.from_map(m.get('VpcId'))

        return self

class UpdateEventStreamingRequestSinkSinkPrometheusParametersVpcId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The VPC ID.
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

class UpdateEventStreamingRequestSinkSinkPrometheusParametersVSwitchId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The vSwitch ID.
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

class UpdateEventStreamingRequestSinkSinkPrometheusParametersUsername(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The username.
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

class UpdateEventStreamingRequestSinkSinkPrometheusParametersURL(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The URL for the remote write configuration item of the Managed Service for Prometheus instance.
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

class UpdateEventStreamingRequestSinkSinkPrometheusParametersSecurityGroupId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The ID of the security group.
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

class UpdateEventStreamingRequestSinkSinkPrometheusParametersPassword(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The password.
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

class UpdateEventStreamingRequestSinkSinkPrometheusParametersNetworkType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The network type. Valid values:
        # 
        # *   PublicNetwork
        # *   PrivateNetwork
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

class UpdateEventStreamingRequestSinkSinkPrometheusParametersHeaderParameters(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        # 
        # **Valid values:**
        # 
        # *   JSONPATH
        # *   CONSTANT
        # *   TEMPLATE
        self.form = form
        # The template that you want to use for HTTP request headers. This parameter is required only if you set Form to TEMPLATE. After the event content is transformed, the data must be in JSON format.
        self.template = template
        # *   If you set Form to CONSTANT, specify a constant.
        # *   If you set Form to JSONPATH, specify a JSONPath rule.
        # *   If you set Form to TEMPLATE, specify variables for the template.
        # 
        # Note: The value of this parameter cannot exceed 10,240 characters in length.
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

class UpdateEventStreamingRequestSinkSinkPrometheusParametersData(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: JSONPATH.
        self.form = form
        # None.
        self.template = template
        # The metric data.
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

class UpdateEventStreamingRequestSinkSinkPrometheusParametersAuthorizationType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The authentication method.
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

class UpdateEventStreamingRequestSinkSinkOpenSourceRabbitMQParameters(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        body: main_models.UpdateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersBody = None,
        endpoint: str = None,
        exchange: str = None,
        message_id: main_models.UpdateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersMessageId = None,
        network_type: str = None,
        password: str = None,
        properties: main_models.UpdateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersProperties = None,
        queue_name: str = None,
        routing_key: main_models.UpdateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersRoutingKey = None,
        security_group_id: str = None,
        target_type: str = None,
        username: str = None,
        v_switch_ids: str = None,
        virtual_host_name: str = None,
        vpc_id: str = None,
    ):
        # The authentication type. Valid values:
        # 
        # *   ACL
        # *   N/A
        self.auth_type = auth_type
        # The message body.
        self.body = body
        # The endpoint used to access the open source RabbitMQ instance.
        self.endpoint = endpoint
        # The name of the exchange on the open source RabbitMQ instance. This parameter is valid only if you set TargetType to Exchange.
        self.exchange = exchange
        # The message ID.
        self.message_id = message_id
        # The network type. Valid values:
        # 
        # *   PrivateNetwork
        # *   PublicNetwork
        self.network_type = network_type
        # The password that is used to access the open source RabbitMQ instance.
        self.password = password
        # The attributes of the message.
        self.properties = properties
        # The name of the queue on the open source RabbitMQ instance. This parameter is valid only if you set TargetType to Queue.
        self.queue_name = queue_name
        # The routing key.
        self.routing_key = routing_key
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The type of the resource to which you want to deliver messages. Valid values:
        # 
        # *   **Exchange**: Messages are routed to the event target using an exchange.
        # *   **Queue**: Messages are delivered to a specific queue.
        self.target_type = target_type
        # The username that is used to access the open source RabbitMQ instance.
        self.username = username
        # The vSwitch ID.
        self.v_switch_ids = v_switch_ids
        # The name of the virtual host of the open source RabbitMQ instance.
        self.virtual_host_name = virtual_host_name
        # The VPC ID.
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
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Exchange') is not None:
            self.exchange = m.get('Exchange')

        if m.get('MessageId') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m.get('MessageId'))

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Properties') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('RoutingKey') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersRoutingKey()
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

class UpdateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersRoutingKey(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The routing key.
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

class UpdateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersProperties(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The attribute value.
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

class UpdateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersMessageId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value of the message ID.
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

class UpdateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value of the raw data.
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

class UpdateEventStreamingRequestSinkSinkMNSParameters(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateEventStreamingRequestSinkSinkMNSParametersBody = None,
        is_base_64encode: main_models.UpdateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode = None,
        queue_name: main_models.UpdateEventStreamingRequestSinkSinkMNSParametersQueueName = None,
    ):
        # The message body.
        self.body = body
        # Specifies whether to enable Base64 encoding.
        self.is_base_64encode = is_base_64encode
        # The name of the SMQ queue.
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
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkMNSParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('IsBase64Encode') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode()
            self.is_base_64encode = temp_model.from_map(m.get('IsBase64Encode'))

        if m.get('QueueName') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkMNSParametersQueueName()
            self.queue_name = temp_model.from_map(m.get('QueueName'))

        return self

class UpdateEventStreamingRequestSinkSinkMNSParametersQueueName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the SMQ queue.
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

class UpdateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # Specifies whether to enable Base64 encoding.
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

class UpdateEventStreamingRequestSinkSinkMNSParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value before event transformation.
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

class UpdateEventStreamingRequestSinkSinkKafkaParameters(DaraModel):
    def __init__(
        self,
        acks: main_models.UpdateEventStreamingRequestSinkSinkKafkaParametersAcks = None,
        compression_type: str = None,
        headers: main_models.UpdateEventStreamingRequestSinkSinkKafkaParametersHeaders = None,
        instance_id: main_models.UpdateEventStreamingRequestSinkSinkKafkaParametersInstanceId = None,
        key: main_models.UpdateEventStreamingRequestSinkSinkKafkaParametersKey = None,
        topic: main_models.UpdateEventStreamingRequestSinkSinkKafkaParametersTopic = None,
        value: main_models.UpdateEventStreamingRequestSinkSinkKafkaParametersValue = None,
    ):
        # The acknowledgment (ACK) mode.
        # 
        # *   If you set this parameter to 0, no response is returned from the broker. In this mode, the performance is high, but the risk of data loss is also high.
        # *   If you set this parameter to 1, a response is returned when data is written to the leader. In this mode, the performance and the risk of data loss are moderate. Data loss may occur if a failure occurs on the leader.
        # *   If you set this parameter to all, a response is returned when data is written to the leader and synchronized to the followers. In this mode, the performance is low, but the risk of data loss is also low. Data loss occurs if the leader and the followers fail at the same time.
        self.acks = acks
        self.compression_type = compression_type
        # The metadata added to messages in the ApsaraMQ for Kafka instance.
        self.headers = headers
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
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkKafkaParametersAcks()
            self.acks = temp_model.from_map(m.get('Acks'))

        if m.get('CompressionType') is not None:
            self.compression_type = m.get('CompressionType')

        if m.get('Headers') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkKafkaParametersHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('InstanceId') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkKafkaParametersInstanceId()
            self.instance_id = temp_model.from_map(m.get('InstanceId'))

        if m.get('Key') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkKafkaParametersKey()
            self.key = temp_model.from_map(m.get('Key'))

        if m.get('Topic') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkKafkaParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        if m.get('Value') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkKafkaParametersValue()
            self.value = temp_model.from_map(m.get('Value'))

        return self

class UpdateEventStreamingRequestSinkSinkKafkaParametersValue(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value before event transformation.
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

class UpdateEventStreamingRequestSinkSinkKafkaParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
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

class UpdateEventStreamingRequestSinkSinkKafkaParametersKey(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
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

class UpdateEventStreamingRequestSinkSinkKafkaParametersInstanceId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
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

class UpdateEventStreamingRequestSinkSinkKafkaParametersHeaders(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Valid values:
        # 
        # *   ORIGINAL: complete event
        # *   JSONPATH: partial event
        # *   CONSTANT: constant
        # *   TEMPLATE: template
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value before event transformation.
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

class UpdateEventStreamingRequestSinkSinkKafkaParametersAcks(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
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

class UpdateEventStreamingRequestSinkSinkFnfParameters(DaraModel):
    def __init__(
        self,
        execution_name: main_models.UpdateEventStreamingRequestSinkSinkFnfParametersExecutionName = None,
        flow_name: main_models.UpdateEventStreamingRequestSinkSinkFnfParametersFlowName = None,
        input: main_models.UpdateEventStreamingRequestSinkSinkFnfParametersInput = None,
        role_name: main_models.UpdateEventStreamingRequestSinkSinkFnfParametersRoleName = None,
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
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkFnfParametersExecutionName()
            self.execution_name = temp_model.from_map(m.get('ExecutionName'))

        if m.get('FlowName') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkFnfParametersFlowName()
            self.flow_name = temp_model.from_map(m.get('FlowName'))

        if m.get('Input') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkFnfParametersInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('RoleName') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkFnfParametersRoleName()
            self.role_name = temp_model.from_map(m.get('RoleName'))

        return self

class UpdateEventStreamingRequestSinkSinkFnfParametersRoleName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The role name.
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

class UpdateEventStreamingRequestSinkSinkFnfParametersInput(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want events to be transformed.
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

class UpdateEventStreamingRequestSinkSinkFnfParametersFlowName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want events to be transformed.
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

class UpdateEventStreamingRequestSinkSinkFnfParametersExecutionName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want events to be transformed.
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

class UpdateEventStreamingRequestSinkSinkFcParameters(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateEventStreamingRequestSinkSinkFcParametersBody = None,
        concurrency: main_models.UpdateEventStreamingRequestSinkSinkFcParametersConcurrency = None,
        data_format: main_models.UpdateEventStreamingRequestSinkSinkFcParametersDataFormat = None,
        function_name: main_models.UpdateEventStreamingRequestSinkSinkFcParametersFunctionName = None,
        invocation_type: main_models.UpdateEventStreamingRequestSinkSinkFcParametersInvocationType = None,
        qualifier: main_models.UpdateEventStreamingRequestSinkSinkFcParametersQualifier = None,
        service_name: main_models.UpdateEventStreamingRequestSinkSinkFcParametersServiceName = None,
    ):
        # The message body that you want to deliver to Function Compute.
        self.body = body
        # The delivery concurrency. Minimum value: 1.
        self.concurrency = concurrency
        # The rule that you want to use to transform the format of event content.
        self.data_format = data_format
        # The function name.
        self.function_name = function_name
        # The invocation mode. Valid values: Sync and Async.
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
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkFcParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Concurrency') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkFcParametersConcurrency()
            self.concurrency = temp_model.from_map(m.get('Concurrency'))

        if m.get('DataFormat') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkFcParametersDataFormat()
            self.data_format = temp_model.from_map(m.get('DataFormat'))

        if m.get('FunctionName') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkFcParametersFunctionName()
            self.function_name = temp_model.from_map(m.get('FunctionName'))

        if m.get('InvocationType') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkFcParametersInvocationType()
            self.invocation_type = temp_model.from_map(m.get('InvocationType'))

        if m.get('Qualifier') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkFcParametersQualifier()
            self.qualifier = temp_model.from_map(m.get('Qualifier'))

        if m.get('ServiceName') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkFcParametersServiceName()
            self.service_name = temp_model.from_map(m.get('ServiceName'))

        return self

class UpdateEventStreamingRequestSinkSinkFcParametersServiceName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
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

class UpdateEventStreamingRequestSinkSinkFcParametersQualifier(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
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

class UpdateEventStreamingRequestSinkSinkFcParametersInvocationType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The invocation mode.
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

class UpdateEventStreamingRequestSinkSinkFcParametersFunctionName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
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

class UpdateEventStreamingRequestSinkSinkFcParametersDataFormat(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Valid values:
        # 
        # *   ORIGINAL: complete event
        # *   JSONPATH: partial event
        # *   CONSTANT: constant
        # *   TEMPLATE: template
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value before event transformation.
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

class UpdateEventStreamingRequestSinkSinkFcParametersConcurrency(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
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

class UpdateEventStreamingRequestSinkSinkFcParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value before event transformation.
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

class UpdateEventStreamingRequestSinkSinkDorisParameters(DaraModel):
    def __init__(
        self,
        be_http_endpoint: main_models.UpdateEventStreamingRequestSinkSinkDorisParametersBeHttpEndpoint = None,
        body: main_models.UpdateEventStreamingRequestSinkSinkDorisParametersBody = None,
        database: main_models.UpdateEventStreamingRequestSinkSinkDorisParametersDatabase = None,
        fe_http_endpoint: main_models.UpdateEventStreamingRequestSinkSinkDorisParametersFeHttpEndpoint = None,
        network_type: main_models.UpdateEventStreamingRequestSinkSinkDorisParametersNetworkType = None,
        password: main_models.UpdateEventStreamingRequestSinkSinkDorisParametersPassword = None,
        query_endpoint: main_models.UpdateEventStreamingRequestSinkSinkDorisParametersQueryEndpoint = None,
        security_group_id: main_models.UpdateEventStreamingRequestSinkSinkDorisParametersSecurityGroupId = None,
        table: main_models.UpdateEventStreamingRequestSinkSinkDorisParametersTable = None,
        user_name: main_models.UpdateEventStreamingRequestSinkSinkDorisParametersUserName = None,
        v_switch_ids: main_models.UpdateEventStreamingRequestSinkSinkDorisParametersVSwitchIds = None,
        vpc_id: main_models.UpdateEventStreamingRequestSinkSinkDorisParametersVpcId = None,
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
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDorisParametersBeHttpEndpoint()
            self.be_http_endpoint = temp_model.from_map(m.get('BeHttpEndpoint'))

        if m.get('Body') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDorisParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Database') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDorisParametersDatabase()
            self.database = temp_model.from_map(m.get('Database'))

        if m.get('FeHttpEndpoint') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDorisParametersFeHttpEndpoint()
            self.fe_http_endpoint = temp_model.from_map(m.get('FeHttpEndpoint'))

        if m.get('NetworkType') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDorisParametersNetworkType()
            self.network_type = temp_model.from_map(m.get('NetworkType'))

        if m.get('Password') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDorisParametersPassword()
            self.password = temp_model.from_map(m.get('Password'))

        if m.get('QueryEndpoint') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDorisParametersQueryEndpoint()
            self.query_endpoint = temp_model.from_map(m.get('QueryEndpoint'))

        if m.get('SecurityGroupId') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDorisParametersSecurityGroupId()
            self.security_group_id = temp_model.from_map(m.get('SecurityGroupId'))

        if m.get('Table') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDorisParametersTable()
            self.table = temp_model.from_map(m.get('Table'))

        if m.get('UserName') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDorisParametersUserName()
            self.user_name = temp_model.from_map(m.get('UserName'))

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDorisParametersVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        if m.get('VpcId') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDorisParametersVpcId()
            self.vpc_id = temp_model.from_map(m.get('VpcId'))

        return self

class UpdateEventStreamingRequestSinkSinkDorisParametersVpcId(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkDorisParametersVSwitchIds(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkDorisParametersUserName(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkDorisParametersTable(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkDorisParametersSecurityGroupId(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkDorisParametersQueryEndpoint(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkDorisParametersPassword(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkDorisParametersNetworkType(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkDorisParametersFeHttpEndpoint(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkDorisParametersDatabase(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkDorisParametersBody(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkDorisParametersBeHttpEndpoint(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkDataHubParameters(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateEventStreamingRequestSinkSinkDataHubParametersBody = None,
        content_schema: main_models.UpdateEventStreamingRequestSinkSinkDataHubParametersContentSchema = None,
        content_type: main_models.UpdateEventStreamingRequestSinkSinkDataHubParametersContentType = None,
        project: main_models.UpdateEventStreamingRequestSinkSinkDataHubParametersProject = None,
        role_name: main_models.UpdateEventStreamingRequestSinkSinkDataHubParametersRoleName = None,
        topic: main_models.UpdateEventStreamingRequestSinkSinkDataHubParametersTopic = None,
        topic_schema: main_models.UpdateEventStreamingRequestSinkSinkDataHubParametersTopicSchema = None,
        topic_type: main_models.UpdateEventStreamingRequestSinkSinkDataHubParametersTopicType = None,
    ):
        # The data is of the BLOB type, and a template is defined for the record.
        self.body = body
        # The key-value pair of custom logs. This parameter takes effect only if you set ContentType to KeyValue. Each key-value pair is in the Key_n, Value_n format.
        self.content_schema = content_schema
        # The data format. Valid values:
        # 
        # *   JSON
        # *   KeyValue
        self.content_type = content_type
        # The name of the DataHub project.
        self.project = project
        # The role name.
        self.role_name = role_name
        # The name of the DataHub topic.
        self.topic = topic
        # The data is of the TUBLE type, and a schema is defined for the DataHub topic.
        self.topic_schema = topic_schema
        # The data type of the DataHub topic. Valid values:
        # 
        # *   TUPLE
        # *   BLOB
        self.topic_type = topic_type

    def validate(self):
        if self.body:
            self.body.validate()
        if self.content_schema:
            self.content_schema.validate()
        if self.content_type:
            self.content_type.validate()
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

        if self.content_schema is not None:
            result['ContentSchema'] = self.content_schema.to_map()

        if self.content_type is not None:
            result['ContentType'] = self.content_type.to_map()

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
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDataHubParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('ContentSchema') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDataHubParametersContentSchema()
            self.content_schema = temp_model.from_map(m.get('ContentSchema'))

        if m.get('ContentType') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDataHubParametersContentType()
            self.content_type = temp_model.from_map(m.get('ContentType'))

        if m.get('Project') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDataHubParametersProject()
            self.project = temp_model.from_map(m.get('Project'))

        if m.get('RoleName') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDataHubParametersRoleName()
            self.role_name = temp_model.from_map(m.get('RoleName'))

        if m.get('Topic') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDataHubParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        if m.get('TopicSchema') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDataHubParametersTopicSchema()
            self.topic_schema = temp_model.from_map(m.get('TopicSchema'))

        if m.get('TopicType') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDataHubParametersTopicType()
            self.topic_type = temp_model.from_map(m.get('TopicType'))

        return self

class UpdateEventStreamingRequestSinkSinkDataHubParametersTopicType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The data type of the DataHub topic. Valid values:
        # 
        # *   TUPLE
        # *   BLOB
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

class UpdateEventStreamingRequestSinkSinkDataHubParametersTopicSchema(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The data is of the TUBLE type, and a schema is defined for the DataHub topic.
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

class UpdateEventStreamingRequestSinkSinkDataHubParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the DataHub topic.
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

class UpdateEventStreamingRequestSinkSinkDataHubParametersRoleName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The role name.
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

class UpdateEventStreamingRequestSinkSinkDataHubParametersProject(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The name of the DataHub project.
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

class UpdateEventStreamingRequestSinkSinkDataHubParametersContentType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value before event transformation.
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

class UpdateEventStreamingRequestSinkSinkDataHubParametersContentSchema(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The template based on which you want events to be transformed.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The value before event transformation.
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

class UpdateEventStreamingRequestSinkSinkDataHubParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        self.form = form
        # None.
        self.template = template
        # The data is of the BLOB type, and a template is defined for the record.
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

class UpdateEventStreamingRequestSinkSinkDashVectorParameters(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        collection: str = None,
        dash_vector_schema_parameters: List[main_models.UpdateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParameters] = None,
        instance_id: str = None,
        network: str = None,
        operation: str = None,
        partition: main_models.UpdateEventStreamingRequestSinkSinkDashVectorParametersPartition = None,
        primary_key_id: main_models.UpdateEventStreamingRequestSinkSinkDashVectorParametersPrimaryKeyId = None,
        vector: main_models.UpdateEventStreamingRequestSinkSinkDashVectorParametersVector = None,
    ):
        # The API key that you want to create in the DashVector console.
        self.api_key = api_key
        # The collection name.
        self.collection = collection
        # The parameters in the Schema field of the table when data is inserted into DashVector. After the event content is transformed, the data must be in JSON format.
        self.dash_vector_schema_parameters = dash_vector_schema_parameters
        # The ID of the DashVector instance.
        self.instance_id = instance_id
        # The network type. Valid values:
        # 
        # *   PrivateNetwork
        # *   PublicNetwork
        self.network = network
        # The type of operation that you want to perform on the DashVector database. Valid values:
        # 
        # *   Delete
        # *   Upsert
        self.operation = operation
        # The partition. Default value: default.
        self.partition = partition
        # The ID of the primary key that you want to use when you insert or delete records. If you do not specify this parameter, a random primary key ID is returned.
        self.primary_key_id = primary_key_id
        # The vector that is recorded when data is inserted into DashVector.
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
                temp_model = main_models.UpdateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParameters()
                self.dash_vector_schema_parameters.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Partition') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDashVectorParametersPartition()
            self.partition = temp_model.from_map(m.get('Partition'))

        if m.get('PrimaryKeyId') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDashVectorParametersPrimaryKeyId()
            self.primary_key_id = temp_model.from_map(m.get('PrimaryKeyId'))

        if m.get('Vector') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDashVectorParametersVector()
            self.vector = temp_model.from_map(m.get('Vector'))

        return self

class UpdateEventStreamingRequestSinkSinkDashVectorParametersVector(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events.
        self.form = form
        # None.
        self.template = template
        # The JSONPath rule that you want to use to extract content.
        # 
        # >  The value of this parameter cannot exceed 10,240 characters in length.
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

class UpdateEventStreamingRequestSinkSinkDashVectorParametersPrimaryKeyId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Valid values:
        # 
        # *   JSONPATH
        # *   TEMPLATE
        self.form = form
        # The template that you want to use to specify primary key IDs. This parameter is required only if you set Form to TEMPLATE.
        self.template = template
        # If you set Form to JSONPATH, specify a JSONPath rule. If you set Form to TEMPLATE, specify variables for the template.
        # 
        # >  The value of this parameter cannot exceed 10,240 characters in length.
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

class UpdateEventStreamingRequestSinkSinkDashVectorParametersPartition(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Valid values:
        # 
        # *   JSONPATH
        # *   CONSTANT
        self.form = form
        # None.
        self.template = template
        # *   If you set Form to CONSTANT, specify a constant.
        # *   If you set Form to JSONPATH, specify a JSONPath rule.
        # 
        # >  The value of this parameter cannot exceed 10,240 characters in length.
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

class UpdateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParameters(DaraModel):
    def __init__(
        self,
        name: main_models.UpdateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersName = None,
        type: main_models.UpdateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersType = None,
        value: main_models.UpdateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersValue = None,
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
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersName()
            self.name = temp_model.from_map(m.get('Name'))

        if m.get('Type') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersType()
            self.type = temp_model.from_map(m.get('Type'))

        if m.get('Value') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersValue()
            self.value = temp_model.from_map(m.get('Value'))

        return self

class UpdateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersValue(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersType(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersName(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkCustomizedKafkaParameters(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the ApsaraMQ for Kafka instance.
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

class UpdateEventStreamingRequestSinkSinkCustomizedKafkaConnectorParameters(DaraModel):
    def __init__(
        self,
        connector_package_url: str = None,
        connector_parameters: main_models.UpdateEventStreamingRequestSinkSinkCustomizedKafkaConnectorParametersConnectorParameters = None,
        worker_parameters: Dict[str, Any] = None,
    ):
        # The download link of the ZIP package that includes Object Storage Service (OSS) resources.
        self.connector_package_url = connector_package_url
        # The parameters that are configured for the parsing of the .properties file in the ZIP package.
        self.connector_parameters = connector_parameters
        # The instance configurations.
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
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkCustomizedKafkaConnectorParametersConnectorParameters()
            self.connector_parameters = temp_model.from_map(m.get('ConnectorParameters'))

        if m.get('WorkerParameters') is not None:
            self.worker_parameters = m.get('WorkerParameters')

        return self

class UpdateEventStreamingRequestSinkSinkCustomizedKafkaConnectorParametersConnectorParameters(DaraModel):
    def __init__(
        self,
        config: Dict[str, Any] = None,
        name: str = None,
    ):
        # The connector configurations.
        self.config = config
        # The connector name.
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

class UpdateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParameters(DaraModel):
    def __init__(
        self,
        consume_timestamp: main_models.UpdateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersConsumeTimestamp = None,
        group: main_models.UpdateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersGroup = None,
        instance_endpoint: str = None,
        instance_password: str = None,
        instance_username: str = None,
        network_type: str = None,
        security_group_id: str = None,
        topic: main_models.UpdateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersTopic = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The timestamp that specifies the time from which messages are consumed.
        self.consume_timestamp = consume_timestamp
        # The ID of the consumer group.
        self.group = group
        # The endpoint that is used to access the Apache RocketMQ instance.
        self.instance_endpoint = instance_endpoint
        # The password that is used to access the Apache RocketMQ instance.
        self.instance_password = instance_password
        # The username that is used to access the Apache RocketMQ instance.
        self.instance_username = instance_username
        # The network type.
        # 
        # *   PublicNetwork
        # *   PrivateNetwork
        self.network_type = network_type
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The name of the topic on the Apache RocketMQ instance.
        self.topic = topic
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
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
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersConsumeTimestamp()
            self.consume_timestamp = temp_model.from_map(m.get('ConsumeTimestamp'))

        if m.get('Group') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersGroup()
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
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class UpdateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The name of the topic on the Apache RocketMQ instance.
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

class UpdateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersGroup(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The ID of the consumer group.
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

class UpdateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersConsumeTimestamp(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The method that you want to use to transform events. Default value: CONSTANT.
        self.form = form
        # The template based on which you want events to be transformed.
        self.template = template
        # The timestamp that specifies the time from which messages are consumed.
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

class UpdateEventStreamingRequestSinkSinkApacheKafkaParameters(DaraModel):
    def __init__(
        self,
        acks: str = None,
        bootstraps: str = None,
        compression_type: str = None,
        headers: main_models.UpdateEventStreamingRequestSinkSinkApacheKafkaParametersHeaders = None,
        key: main_models.UpdateEventStreamingRequestSinkSinkApacheKafkaParametersKey = None,
        network_type: main_models.UpdateEventStreamingRequestSinkSinkApacheKafkaParametersNetworkType = None,
        sasl_mechanism: str = None,
        sasl_password: str = None,
        sasl_user: str = None,
        security_group_id: main_models.UpdateEventStreamingRequestSinkSinkApacheKafkaParametersSecurityGroupId = None,
        security_protocol: str = None,
        ssl_truststore_certificates: str = None,
        topic: str = None,
        v_switch_ids: main_models.UpdateEventStreamingRequestSinkSinkApacheKafkaParametersVSwitchIds = None,
        value: main_models.UpdateEventStreamingRequestSinkSinkApacheKafkaParametersValue = None,
        vpc_id: main_models.UpdateEventStreamingRequestSinkSinkApacheKafkaParametersVpcId = None,
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
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkApacheKafkaParametersHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('Key') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkApacheKafkaParametersKey()
            self.key = temp_model.from_map(m.get('Key'))

        if m.get('NetworkType') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkApacheKafkaParametersNetworkType()
            self.network_type = temp_model.from_map(m.get('NetworkType'))

        if m.get('SaslMechanism') is not None:
            self.sasl_mechanism = m.get('SaslMechanism')

        if m.get('SaslPassword') is not None:
            self.sasl_password = m.get('SaslPassword')

        if m.get('SaslUser') is not None:
            self.sasl_user = m.get('SaslUser')

        if m.get('SecurityGroupId') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkApacheKafkaParametersSecurityGroupId()
            self.security_group_id = temp_model.from_map(m.get('SecurityGroupId'))

        if m.get('SecurityProtocol') is not None:
            self.security_protocol = m.get('SecurityProtocol')

        if m.get('SslTruststoreCertificates') is not None:
            self.ssl_truststore_certificates = m.get('SslTruststoreCertificates')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkApacheKafkaParametersVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        if m.get('Value') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkApacheKafkaParametersValue()
            self.value = temp_model.from_map(m.get('Value'))

        if m.get('VpcId') is not None:
            temp_model = main_models.UpdateEventStreamingRequestSinkSinkApacheKafkaParametersVpcId()
            self.vpc_id = temp_model.from_map(m.get('VpcId'))

        return self

class UpdateEventStreamingRequestSinkSinkApacheKafkaParametersVpcId(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkApacheKafkaParametersValue(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkApacheKafkaParametersVSwitchIds(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkApacheKafkaParametersSecurityGroupId(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkApacheKafkaParametersNetworkType(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkApacheKafkaParametersKey(DaraModel):
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

class UpdateEventStreamingRequestSinkSinkApacheKafkaParametersHeaders(DaraModel):
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

class UpdateEventStreamingRequestRunOptions(DaraModel):
    def __init__(
        self,
        batch_window: main_models.UpdateEventStreamingRequestRunOptionsBatchWindow = None,
        business_option: main_models.UpdateEventStreamingRequestRunOptionsBusinessOption = None,
        dead_letter_queue: main_models.UpdateEventStreamingRequestRunOptionsDeadLetterQueue = None,
        errors_tolerance: str = None,
        maximum_tasks: int = None,
        retry_strategy: main_models.UpdateEventStreamingRequestRunOptionsRetryStrategy = None,
        throttling: int = None,
    ):
        # The batch window.
        self.batch_window = batch_window
        self.business_option = business_option
        # Specifies whether to enable dead-letter queues. By default, dead-letter queues are disabled. Events that fail to be pushed are discarded after the maximum number of retries that is specified by the retry policy is reached.
        self.dead_letter_queue = dead_letter_queue
        # The exception tolerance policy. Valid values: NONE and ALL.
        self.errors_tolerance = errors_tolerance
        # The maximum number of concurrent tasks.
        self.maximum_tasks = maximum_tasks
        # The retry policy that you want to use if events fail to be pushed.
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
            temp_model = main_models.UpdateEventStreamingRequestRunOptionsBatchWindow()
            self.batch_window = temp_model.from_map(m.get('BatchWindow'))

        if m.get('BusinessOption') is not None:
            temp_model = main_models.UpdateEventStreamingRequestRunOptionsBusinessOption()
            self.business_option = temp_model.from_map(m.get('BusinessOption'))

        if m.get('DeadLetterQueue') is not None:
            temp_model = main_models.UpdateEventStreamingRequestRunOptionsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m.get('DeadLetterQueue'))

        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')

        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')

        if m.get('RetryStrategy') is not None:
            temp_model = main_models.UpdateEventStreamingRequestRunOptionsRetryStrategy()
            self.retry_strategy = temp_model.from_map(m.get('RetryStrategy'))

        if m.get('Throttling') is not None:
            self.throttling = m.get('Throttling')

        return self

class UpdateEventStreamingRequestRunOptionsRetryStrategy(DaraModel):
    def __init__(
        self,
        maximum_event_age_in_seconds: int = None,
        maximum_retry_attempts: int = None,
        push_retry_strategy: str = None,
    ):
        # The maximum timeout period for a retry.
        self.maximum_event_age_in_seconds = maximum_event_age_in_seconds
        # The maximum number of retries.
        self.maximum_retry_attempts = maximum_retry_attempts
        # The retry policy. Valid values: BACKOFF_RETRY and EXPONENTIAL_DECAY_RETRY.
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

class UpdateEventStreamingRequestRunOptionsDeadLetterQueue(DaraModel):
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
        # The network type of the dead-letter queue. Valid values:
        # 
        # *   PrivateNetwork
        # *   PublicNetwork
        self.network = network
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The vSwitch ID.
        self.v_switch_ids = v_switch_ids
        # The VPC ID.
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

class UpdateEventStreamingRequestRunOptionsBusinessOption(DaraModel):
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

class UpdateEventStreamingRequestRunOptionsBatchWindow(DaraModel):
    def __init__(
        self,
        count_based_window: int = None,
        time_based_window: int = None,
    ):
        # The maximum number of events that are allowed in the batch window. When this threshold is reached, data in the window is pushed to the downstream service. If multiple batch windows exist, data is pushed if the triggering conditions are met in one of the windows.
        self.count_based_window = count_based_window
        # The maximum period of time during which events are allowed in the batch window. Unit: seconds. When this threshold is reached, data in the window is pushed to the downstream service. If multiple batch windows exist, data is pushed if the triggering conditions are met in one of the windows.
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

