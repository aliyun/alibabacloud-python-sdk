# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class CreateEventStreamingRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        metadata: str = None,
        run_options: main_models.CreateEventStreamingRequestRunOptions = None,
        sink: main_models.CreateEventStreamingRequestSink = None,
        source: main_models.CreateEventStreamingRequestSource = None,
        tags: List[main_models.CreateEventStreamingRequestTags] = None,
        transforms: List[main_models.CreateEventStreamingRequestTransforms] = None,
    ):
        # The description of the event stream.
        self.description = description
        # The name of the event stream.
        # 
        # This parameter is required.
        self.event_streaming_name = event_streaming_name
        # The event filtering rule. If not specified, all events are matched.
        self.filter_pattern = filter_pattern
        self.metadata = metadata
        # The runtime environment parameters.
        self.run_options = run_options
        # The event target. You must select exactly one Sink type.
        self.sink = sink
        # The event provider. You must select exactly one Source type.
        self.source = source
        # The tag list. A maximum of 20 items are supported.
        self.tags = tags
        # The Transform-related configurations.
        self.transforms = transforms

    def validate(self):
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
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

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.run_options is not None:
            result['RunOptions'] = self.run_options.to_map()

        if self.sink is not None:
            result['Sink'] = self.sink.to_map()

        if self.source is not None:
            result['Source'] = self.source.to_map()

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

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

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('RunOptions') is not None:
            temp_model = main_models.CreateEventStreamingRequestRunOptions()
            self.run_options = temp_model.from_map(m.get('RunOptions'))

        if m.get('Sink') is not None:
            temp_model = main_models.CreateEventStreamingRequestSink()
            self.sink = temp_model.from_map(m.get('Sink'))

        if m.get('Source') is not None:
            temp_model = main_models.CreateEventStreamingRequestSource()
            self.source = temp_model.from_map(m.get('Source'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateEventStreamingRequestTags()
                self.tags.append(temp_model.from_map(k1))

        self.transforms = []
        if m.get('Transforms') is not None:
            for k1 in m.get('Transforms'):
                temp_model = main_models.CreateEventStreamingRequestTransforms()
                self.transforms.append(temp_model.from_map(k1))

        return self

class CreateEventStreamingRequestTransforms(DaraModel):
    def __init__(
        self,
        arn: str = None,
        bai_lian_agent_transform_parameters: main_models.BaiLianAgentTransformParameters = None,
        dash_scope_transform_parameters: main_models.DashScopeTransformParameters = None,
        embedding_transform_parameters: main_models.EmbeddingTransformParameters = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the cloud service, such as the ARN of a function in Function Compute.
        self.arn = arn
        self.bai_lian_agent_transform_parameters = bai_lian_agent_transform_parameters
        self.dash_scope_transform_parameters = dash_scope_transform_parameters
        self.embedding_transform_parameters = embedding_transform_parameters

    def validate(self):
        if self.bai_lian_agent_transform_parameters:
            self.bai_lian_agent_transform_parameters.validate()
        if self.dash_scope_transform_parameters:
            self.dash_scope_transform_parameters.validate()
        if self.embedding_transform_parameters:
            self.embedding_transform_parameters.validate()

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

        if self.embedding_transform_parameters is not None:
            result['EmbeddingTransformParameters'] = self.embedding_transform_parameters.to_map()

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

        if m.get('EmbeddingTransformParameters') is not None:
            temp_model = main_models.EmbeddingTransformParameters()
            self.embedding_transform_parameters = temp_model.from_map(m.get('EmbeddingTransformParameters'))

        return self

class CreateEventStreamingRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSource(DaraModel):
    def __init__(
        self,
        source_apache_kafka_parameters: main_models.CreateEventStreamingRequestSourceSourceApacheKafkaParameters = None,
        source_apache_rocket_mqcheckpoint_parameters: main_models.CreateEventStreamingRequestSourceSourceApacheRocketMQCheckpointParameters = None,
        source_customized_kafka_connector_parameters: main_models.CreateEventStreamingRequestSourceSourceCustomizedKafkaConnectorParameters = None,
        source_customized_kafka_parameters: main_models.CreateEventStreamingRequestSourceSourceCustomizedKafkaParameters = None,
        source_dtsparameters: main_models.CreateEventStreamingRequestSourceSourceDTSParameters = None,
        source_event_bus_parameters: main_models.CreateEventStreamingRequestSourceSourceEventBusParameters = None,
        source_fei_shu_docs_parameters: main_models.SourceFeiShuDocsParameters = None,
        source_jdbcparameters: main_models.SourceJDBCParameters = None,
        source_kafka_parameters: main_models.CreateEventStreamingRequestSourceSourceKafkaParameters = None,
        source_mnsparameters: main_models.CreateEventStreamingRequestSourceSourceMNSParameters = None,
        source_mqttparameters: main_models.CreateEventStreamingRequestSourceSourceMQTTParameters = None,
        source_my_sqlparameters: main_models.SourceMySQLParameters = None,
        source_ossparameters: main_models.CreateEventStreamingRequestSourceSourceOSSParameters = None,
        source_open_source_rabbit_mqparameters: main_models.CreateEventStreamingRequestSourceSourceOpenSourceRabbitMQParameters = None,
        source_postgre_sqlparameters: main_models.SourcePostgreSQLParameters = None,
        source_prometheus_parameters: main_models.CreateEventStreamingRequestSourceSourcePrometheusParameters = None,
        source_rabbit_mqmeta_parameters: main_models.SourceRabbitMQMetaParameters = None,
        source_rabbit_mqmsg_sync_parameters: main_models.SourceRabbitMQMsgSyncParameters = None,
        source_rabbit_mqparameters: main_models.CreateEventStreamingRequestSourceSourceRabbitMQParameters = None,
        source_rocket_mqcheckpoint_parameters: main_models.CreateEventStreamingRequestSourceSourceRocketMQCheckpointParameters = None,
        source_rocket_mqparameters: main_models.CreateEventStreamingRequestSourceSourceRocketMQParameters = None,
        source_slsparameters: main_models.CreateEventStreamingRequestSourceSourceSLSParameters = None,
    ):
        # The open-source Kafka parameter settings.
        self.source_apache_kafka_parameters = source_apache_kafka_parameters
        # The Source RocketMQ checkpoint parameters.
        self.source_apache_rocket_mqcheckpoint_parameters = source_apache_rocket_mqcheckpoint_parameters
        # The custom connector Apache Kafka event source.
        self.source_customized_kafka_connector_parameters = source_customized_kafka_connector_parameters
        # The custom Kafka event source.
        self.source_customized_kafka_parameters = source_customized_kafka_parameters
        # The Source DTS parameters.
        self.source_dtsparameters = source_dtsparameters
        self.source_event_bus_parameters = source_event_bus_parameters
        self.source_fei_shu_docs_parameters = source_fei_shu_docs_parameters
        self.source_jdbcparameters = source_jdbcparameters
        # The Source Kafka parameters.
        self.source_kafka_parameters = source_kafka_parameters
        # The Source MNS parameters.
        self.source_mnsparameters = source_mnsparameters
        # The Source MQTT parameters.
        self.source_mqttparameters = source_mqttparameters
        self.source_my_sqlparameters = source_my_sqlparameters
        # The Source OSS event source.
        self.source_ossparameters = source_ossparameters
        self.source_open_source_rabbit_mqparameters = source_open_source_rabbit_mqparameters
        self.source_postgre_sqlparameters = source_postgre_sqlparameters
        # The Source Prometheus event source.
        self.source_prometheus_parameters = source_prometheus_parameters
        self.source_rabbit_mqmeta_parameters = source_rabbit_mqmeta_parameters
        self.source_rabbit_mqmsg_sync_parameters = source_rabbit_mqmsg_sync_parameters
        # The Source RabbitMQ parameters.
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        # The Source RocketMQ checkpoint parameters.
        self.source_rocket_mqcheckpoint_parameters = source_rocket_mqcheckpoint_parameters
        # The Source RocketMQ parameters.
        self.source_rocket_mqparameters = source_rocket_mqparameters
        # The Source SLS parameters.
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
        if self.source_fei_shu_docs_parameters:
            self.source_fei_shu_docs_parameters.validate()
        if self.source_jdbcparameters:
            self.source_jdbcparameters.validate()
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

        if self.source_fei_shu_docs_parameters is not None:
            result['SourceFeiShuDocsParameters'] = self.source_fei_shu_docs_parameters.to_map()

        if self.source_jdbcparameters is not None:
            result['SourceJDBCParameters'] = self.source_jdbcparameters.to_map()

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
            temp_model = main_models.CreateEventStreamingRequestSourceSourceApacheKafkaParameters()
            self.source_apache_kafka_parameters = temp_model.from_map(m.get('SourceApacheKafkaParameters'))

        if m.get('SourceApacheRocketMQCheckpointParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSourceSourceApacheRocketMQCheckpointParameters()
            self.source_apache_rocket_mqcheckpoint_parameters = temp_model.from_map(m.get('SourceApacheRocketMQCheckpointParameters'))

        if m.get('SourceCustomizedKafkaConnectorParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSourceSourceCustomizedKafkaConnectorParameters()
            self.source_customized_kafka_connector_parameters = temp_model.from_map(m.get('SourceCustomizedKafkaConnectorParameters'))

        if m.get('SourceCustomizedKafkaParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSourceSourceCustomizedKafkaParameters()
            self.source_customized_kafka_parameters = temp_model.from_map(m.get('SourceCustomizedKafkaParameters'))

        if m.get('SourceDTSParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSourceSourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m.get('SourceDTSParameters'))

        if m.get('SourceEventBusParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSourceSourceEventBusParameters()
            self.source_event_bus_parameters = temp_model.from_map(m.get('SourceEventBusParameters'))

        if m.get('SourceFeiShuDocsParameters') is not None:
            temp_model = main_models.SourceFeiShuDocsParameters()
            self.source_fei_shu_docs_parameters = temp_model.from_map(m.get('SourceFeiShuDocsParameters'))

        if m.get('SourceJDBCParameters') is not None:
            temp_model = main_models.SourceJDBCParameters()
            self.source_jdbcparameters = temp_model.from_map(m.get('SourceJDBCParameters'))

        if m.get('SourceKafkaParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSourceSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m.get('SourceKafkaParameters'))

        if m.get('SourceMNSParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSourceSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m.get('SourceMNSParameters'))

        if m.get('SourceMQTTParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSourceSourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m.get('SourceMQTTParameters'))

        if m.get('SourceMySQLParameters') is not None:
            temp_model = main_models.SourceMySQLParameters()
            self.source_my_sqlparameters = temp_model.from_map(m.get('SourceMySQLParameters'))

        if m.get('SourceOSSParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSourceSourceOSSParameters()
            self.source_ossparameters = temp_model.from_map(m.get('SourceOSSParameters'))

        if m.get('SourceOpenSourceRabbitMQParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSourceSourceOpenSourceRabbitMQParameters()
            self.source_open_source_rabbit_mqparameters = temp_model.from_map(m.get('SourceOpenSourceRabbitMQParameters'))

        if m.get('SourcePostgreSQLParameters') is not None:
            temp_model = main_models.SourcePostgreSQLParameters()
            self.source_postgre_sqlparameters = temp_model.from_map(m.get('SourcePostgreSQLParameters'))

        if m.get('SourcePrometheusParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSourceSourcePrometheusParameters()
            self.source_prometheus_parameters = temp_model.from_map(m.get('SourcePrometheusParameters'))

        if m.get('SourceRabbitMQMetaParameters') is not None:
            temp_model = main_models.SourceRabbitMQMetaParameters()
            self.source_rabbit_mqmeta_parameters = temp_model.from_map(m.get('SourceRabbitMQMetaParameters'))

        if m.get('SourceRabbitMQMsgSyncParameters') is not None:
            temp_model = main_models.SourceRabbitMQMsgSyncParameters()
            self.source_rabbit_mqmsg_sync_parameters = temp_model.from_map(m.get('SourceRabbitMQMsgSyncParameters'))

        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSourceSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m.get('SourceRabbitMQParameters'))

        if m.get('SourceRocketMQCheckpointParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSourceSourceRocketMQCheckpointParameters()
            self.source_rocket_mqcheckpoint_parameters = temp_model.from_map(m.get('SourceRocketMQCheckpointParameters'))

        if m.get('SourceRocketMQParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSourceSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m.get('SourceRocketMQParameters'))

        if m.get('SourceSLSParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSourceSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m.get('SourceSLSParameters'))

        return self

class CreateEventStreamingRequestSourceSourceSLSParameters(DaraModel):
    def __init__(
        self,
        consume_position: str = None,
        log_store: str = None,
        project: str = None,
        role_name: str = None,
    ):
        # The starting consumption offset. You can select the earliest or latest offset, which corresponds to "begin" or "end" respectively. You can also start consumption from a specified time in seconds.
        self.consume_position = consume_position
        # The Logstore of Simple Log Service.
        self.log_store = log_store
        # The project of Simple Log Service.
        self.project = project
        # The role name used to authorize the event bus EventBridge to read SLS log content. When creating the role in the Resource Access Management (RAM) console, select "Alibaba Cloud Service" and set "Trusted Service" to "EventBridge".
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

class CreateEventStreamingRequestSourceSourceRocketMQParameters(DaraModel):
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
        # The authentication type.
        self.auth_type = auth_type
        # The message encoding format. Valid values:
        # - JSON
        # - Text
        # - Binary
        self.body_data_type = body_data_type
        # The SQL filter statement.
        self.filter_sql = filter_sql
        # The message filter type.
        self.filter_type = filter_type
        # The Group ID of the ApsaraMQ for RocketMQ instance.
        self.group_id = group_id
        # The instance endpoint.
        self.instance_endpoint = instance_endpoint
        # The region where the ApsaraMQ for RocketMQ instance resides.
        self.instance_id = instance_id
        # The instance network information. Valid values:
        # - PublicNetwork
        # - PrivateNetwork
        self.instance_network = instance_network
        # The instance password.
        self.instance_password = instance_password
        # The security group information of the instance.
        self.instance_security_group_id = instance_security_group_id
        # The instance type. Valid values:
        # 
        # - Cloud_4: Alibaba Cloud ApsaraMQ for RocketMQ 4.0 instance (default)
        # - Cloud_5: Alibaba Cloud ApsaraMQ for RocketMQ 5.0 instance
        # - SelfBuilt: self-managed Apache RocketMQ cluster
        self.instance_type = instance_type
        # The instance username.
        self.instance_username = instance_username
        # The vSwitch information of the instance.
        self.instance_vswitch_ids = instance_vswitch_ids
        # The VPC information of the instance.
        self.instance_vpc_id = instance_vpc_id
        # The network type. Valid values:
        # 
        # - PublicNetwork
        # - PrivateNetwork
        self.network = network
        # The consumption offset of the message. Valid values:
        # - CONSUME_FROM_LAST_OFFSET: starts consumption from the latest offset.
        # - CONSUME_FROM_FIRST_OFFSET: starts consumption from the earliest offset.
        # - CONSUME_FROM_TIMESTAMP: starts consumption from the offset at a specified point in time.
        # 
        # Default value: CONSUME_FROM_LAST_OFFSET.
        self.offset = offset
        # The region ID.
        self.region_id = region_id
        # The security group for cross-border tasks.
        self.security_group_id = security_group_id
        # The filter tag of the message.
        self.tag = tag
        # The timestamp. This parameter is valid only when the Offset parameter is set to CONSUME_FROM_TIMESTAMP.
        self.timestamp = timestamp
        # The topic of the messaging service.
        self.topic = topic
        # The vSwitch IDs for cross-border tasks.
        self.v_switch_ids = v_switch_ids
        # The VPC ID for cross-border tasks.
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

class CreateEventStreamingRequestSourceSourceRocketMQCheckpointParameters(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
        topics: List[str] = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The instance type.
        self.instance_type = instance_type
        # The region ID.
        self.region_id = region_id
        # The message topic.
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

class CreateEventStreamingRequestSourceSourceRabbitMQParameters(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        network_type: str = None,
        queue_name: str = None,
        region_id: str = None,
        security_group_id: str = None,
        v_switch_ids: str = None,
        virtual_host_name: str = None,
        vpc_id: str = None,
    ):
        # The instance ID of the ApsaraMQ for RabbitMQ instance.
        self.instance_id = instance_id
        self.network_type = network_type
        # The queue name of the ApsaraMQ for RabbitMQ instance.
        self.queue_name = queue_name
        # The region ID.
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.v_switch_ids = v_switch_ids
        # The vhost name of the ApsaraMQ for RabbitMQ instance.
        self.virtual_host_name = virtual_host_name
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateEventStreamingRequestSourceSourcePrometheusParameters(DaraModel):
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
        # The region ID.
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

class CreateEventStreamingRequestSourceSourceOpenSourceRabbitMQParameters(DaraModel):
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

class CreateEventStreamingRequestSourceSourceOSSParameters(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        delimiter: str = None,
        load_format: str = None,
        load_mode: str = None,
        prefix: str = None,
        role_name: str = None,
    ):
        # The bucket name in Object Storage Service (OSS).
        self.bucket_name = bucket_name
        # The delimiter. In chunked loading mode, this delimiter is used as the text chunking identifier. The default delimiter is the newline character 
        # .
        self.delimiter = delimiter
        # The document loader.
        self.load_format = load_format
        # The data loading mode. single indicates single-document loading, and element indicates chunked loading. Valid values: single/element. Default value: single.
        self.load_mode = load_mode
        # The file path prefix.
        self.prefix = prefix
        # The role name used to authorize the event bus EventBridge to read OSS files. The role must have at least read-only permissions on OSS.
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

class CreateEventStreamingRequestSourceSourceMQTTParameters(DaraModel):
    def __init__(
        self,
        body_data_type: str = None,
        instance_id: str = None,
        network_type: str = None,
        region_id: str = None,
        security_group_id: str = None,
        topic: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        # The message encoding format. Valid values:
        # - JSON
        # - Text
        # - Binary
        self.body_data_type = body_data_type
        # The instance ID.
        self.instance_id = instance_id
        self.network_type = network_type
        # The region ID.
        self.region_id = region_id
        self.security_group_id = security_group_id
        # The topic of the message.
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
        if self.body_data_type is not None:
            result['BodyDataType'] = self.body_data_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

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
        if m.get('BodyDataType') is not None:
            self.body_data_type = m.get('BodyDataType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

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

class CreateEventStreamingRequestSourceSourceMNSParameters(DaraModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        # Specifies whether to enable Base64 decoding. Default value: true.
        self.is_base_64decode = is_base_64decode
        # The queue name.
        self.queue_name = queue_name
        # The region ID.
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

class CreateEventStreamingRequestSourceSourceKafkaParameters(DaraModel):
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
        # The Group ID of the consumer that subscribes to the topic.
        self.consumer_group = consumer_group
        # The instance ID.
        self.instance_id = instance_id
        # The network configuration. Default value: Default. For VPC networks, use PublicNetwork.
        self.network = network
        # The offset.
        self.offset_reset = offset_reset
        # The region ID.
        self.region_id = region_id
        # The security group ID.
        self.security_group_id = security_group_id
        # The topic name.
        self.topic = topic
        # The vSwitch ID.
        self.v_switch_ids = v_switch_ids
        # The encoding and decoding format of the message body. Valid values:
        # - JSON
        # - Text
        # - Binary
        self.value_data_type = value_data_type
        # VPC ID。
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

class CreateEventStreamingRequestSourceSourceEventBusParameters(DaraModel):
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

class CreateEventStreamingRequestSourceSourceDTSParameters(DaraModel):
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
        # The network address and port number of the data subscription channel.
        self.broker_url = broker_url
        # The consumption offset, which is the timestamp when the SDK client consumes the first data record. The value is a UNIX timestamp.
        self.init_check_point = init_check_point
        # The password of the consumer group account.
        self.password = password
        # The consumer group ID.
        self.sid = sid
        # The task ID.
        self.task_id = task_id
        # The subscription topic of the data subscription channel.
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

class CreateEventStreamingRequestSourceSourceCustomizedKafkaParameters(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The instance ID of the ApsaraMQ for Kafka instance.
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

class CreateEventStreamingRequestSourceSourceCustomizedKafkaConnectorParameters(DaraModel):
    def __init__(
        self,
        connector_package_url: str = None,
        connector_parameters: main_models.CreateEventStreamingRequestSourceSourceCustomizedKafkaConnectorParametersConnectorParameters = None,
        worker_parameters: Dict[str, Any] = None,
    ):
        # The download URL of the OSS resource ZIP package.
        self.connector_package_url = connector_package_url
        # The connector parameters.
        self.connector_parameters = connector_parameters
        # The Kafka instance configuration.
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
            temp_model = main_models.CreateEventStreamingRequestSourceSourceCustomizedKafkaConnectorParametersConnectorParameters()
            self.connector_parameters = temp_model.from_map(m.get('ConnectorParameters'))

        if m.get('WorkerParameters') is not None:
            self.worker_parameters = m.get('WorkerParameters')

        return self

class CreateEventStreamingRequestSourceSourceCustomizedKafkaConnectorParametersConnectorParameters(DaraModel):
    def __init__(
        self,
        config: Dict[str, Any] = None,
        name: str = None,
    ):
        # The connector configuration.
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

class CreateEventStreamingRequestSourceSourceApacheRocketMQCheckpointParameters(DaraModel):
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
        # The instance endpoint.
        self.instance_endpoint = instance_endpoint
        # The instance password.
        self.instance_password = instance_password
        # The instance username.
        self.instance_username = instance_username
        # The network type.
        self.network_type = network_type
        # The region ID.
        self.region_id = region_id
        # The security group ID.
        self.security_group_id = security_group_id
        # The message topic.
        self.topics = topics
        # The vSwitch ID.
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

class CreateEventStreamingRequestSourceSourceApacheKafkaParameters(DaraModel):
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
        ssl_key_password: str = None,
        ssl_keystore_certificate_chain: str = None,
        ssl_keystore_key: main_models.CreateEventStreamingRequestSourceSourceApacheKafkaParametersSslKeystoreKey = None,
        ssl_truststore_certificates: str = None,
        topic: str = None,
        v_switch_ids: str = None,
        value_data_type: str = None,
        vpc_id: str = None,
    ):
        # The bootstrap servers.
        self.bootstraps = bootstraps
        # The consumer group name.
        self.consumer_group = consumer_group
        # The Kafka network type.
        self.network_type = network_type
        # The consumption offset. latest: the system reads data from the latest offset. earliest: the system reads data from the earliest offset. This configuration applies only to the first initialization of an unused Group.
        self.offset_reset = offset_reset
        # The Kafka SASL authentication mechanism.
        self.sasl_mechanism = sasl_mechanism
        # The Kafka SASL authentication password.
        self.sasl_password = sasl_password
        # The Kafka SASL authentication username.
        self.sasl_user = sasl_user
        # The security group ID of the Kafka source.
        self.security_group_id = security_group_id
        # The Kafka security protocol type. Valid values: SASL_SSL, PLAINTEXT, SASL_PLAINTEXT.
        self.security_protocol = security_protocol
        # [Required for encrypted private key] The Kafka client private key password. This parameter is required when the client private key is encrypted (the PEM file contains \\"Proc-Type: 4,ENCRYPTED\\" or \\"ENCRYPTED\\" markers). Leave this parameter empty if the private key is not encrypted. This password is used only to decrypt the private key and is unrelated to Kafka authentication.
        self.ssl_key_password = ssl_key_password
        # [Required for mutual authentication] The Kafka client certificate chain. This parameter is required when the Kafka server enables mutual SSL authentication (ssl.client.auth=required). Format: Base64-encoded PEM format, containing the client certificate and the complete certificate chain (client certificate first, intermediate CA certificate next, root CA certificate optional). Ensure that each PEM file content starts with \\"-----BEGIN CERTIFICATE-----\\" and ends with \\"-----END CERTIFICATE-----\\", then Base64-encode the concatenated content.
        self.ssl_keystore_certificate_chain = ssl_keystore_certificate_chain
        # [Required for bidirectional authentication] The SSL private key configuration object. When the Kafka server enables bidirectional SSL authentication, provide the client private key. Only KMS pattern is supported: specify the Key Management Service EPS resource that stores the private key through KmsArn. The system retrieves the private key content from KMS only in memory for higher security. Configuration example: {\\"KmsArn\\": \\"acs:kms:cn-hangzhou:123456789:secret/ssl-key-xxxx\\", \\"KmsSecretValueKey\\": \\"keystore_private_key\\"}
        self.ssl_keystore_key = ssl_keystore_key
        # [Required for SSL] The Kafka server trust certificate. Used to authenticate the SSL certificate of the Kafka Broker and prevent man-in-the-middle attacks. Format: Base64-encoded PEM format, typically containing the CA certificate of the Kafka server or the server certificate itself. Example: Base64-encode the PEM file content of the CA certificate (ensure it starts with \\"-----BEGIN CERTIFICATE-----\\" and ends with \\"-----END CERTIFICATE-----\\"). If Kafka uses a self-signed certificate, provide the CA certificate that issued the certificate.
        self.ssl_truststore_certificates = ssl_truststore_certificates
        # The topic name.
        self.topic = topic
        # The vSwitch ID list of the Kafka source.
        self.v_switch_ids = v_switch_ids
        # The data type. Valid values: Text, Binary, Json.
        self.value_data_type = value_data_type
        # The VPC ID of the Kafka source.
        self.vpc_id = vpc_id

    def validate(self):
        if self.ssl_keystore_key:
            self.ssl_keystore_key.validate()

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

        if self.ssl_key_password is not None:
            result['SslKeyPassword'] = self.ssl_key_password

        if self.ssl_keystore_certificate_chain is not None:
            result['SslKeystoreCertificateChain'] = self.ssl_keystore_certificate_chain

        if self.ssl_keystore_key is not None:
            result['SslKeystoreKey'] = self.ssl_keystore_key.to_map()

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

        if m.get('SslKeyPassword') is not None:
            self.ssl_key_password = m.get('SslKeyPassword')

        if m.get('SslKeystoreCertificateChain') is not None:
            self.ssl_keystore_certificate_chain = m.get('SslKeystoreCertificateChain')

        if m.get('SslKeystoreKey') is not None:
            temp_model = main_models.CreateEventStreamingRequestSourceSourceApacheKafkaParametersSslKeystoreKey()
            self.ssl_keystore_key = temp_model.from_map(m.get('SslKeystoreKey'))

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

class CreateEventStreamingRequestSourceSourceApacheKafkaParametersSslKeystoreKey(DaraModel):
    def __init__(
        self,
        kms_arn: str = None,
        kms_secret_value_key: str = None,
    ):
        # [Required] The KMS resource ARN that stores the SSL private key. Used to locate the Key Management Service instance that stores the client private key. Format example: \\"acs:kms:cn-hangzhou:123456789:secret/ssl-keystore-key-xxxx\\". Obtain this value from the ARN information of the corresponding key in the KMS console.
        self.kms_arn = kms_arn
        # [KMS KV mode] The key name in the KMS secret. When the KMS secret is stored in a key-value (KV) structure, specify this parameter to indicate the key corresponding to the SSL private key. Example: if the KMS secret is \\"{"ssl_keystore_key":"-----BEGIN PRIVATE KEY-----...","ssl_truststore_key":"..."}\\", specify \\"ssl_keystore_key\\". Leave this parameter empty if the KMS secret is in plain text mode (directly stores the PEM content of the private key).
        self.kms_secret_value_key = kms_secret_value_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kms_arn is not None:
            result['KmsArn'] = self.kms_arn

        if self.kms_secret_value_key is not None:
            result['KmsSecretValueKey'] = self.kms_secret_value_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KmsArn') is not None:
            self.kms_arn = m.get('KmsArn')

        if m.get('KmsSecretValueKey') is not None:
            self.kms_secret_value_key = m.get('KmsSecretValueKey')

        return self

class CreateEventStreamingRequestSink(DaraModel):
    def __init__(
        self,
        sink_agent_run_parameters: main_models.SinkAgentRunParameters = None,
        sink_apache_kafka_parameters: main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParameters = None,
        sink_apache_rocket_mqcheckpoint_parameters: main_models.CreateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParameters = None,
        sink_api_destination_parameters: main_models.SinkApiDestinationParameters = None,
        sink_bai_lian_parameters: main_models.SinkBaiLianParameters = None,
        sink_customized_kafka_connector_parameters: main_models.CreateEventStreamingRequestSinkSinkCustomizedKafkaConnectorParameters = None,
        sink_customized_kafka_parameters: main_models.CreateEventStreamingRequestSinkSinkCustomizedKafkaParameters = None,
        sink_dash_vector_parameters: main_models.CreateEventStreamingRequestSinkSinkDashVectorParameters = None,
        sink_data_hub_parameters: main_models.CreateEventStreamingRequestSinkSinkDataHubParameters = None,
        sink_data_works_trigger_parameters: main_models.SinkDataWorksTriggerParameters = None,
        sink_doris_parameters: main_models.CreateEventStreamingRequestSinkSinkDorisParameters = None,
        sink_event_house_parameters: main_models.CreateEventStreamingRequestSinkSinkEventHouseParameters = None,
        sink_fc_parameters: main_models.CreateEventStreamingRequestSinkSinkFcParameters = None,
        sink_fnf_parameters: main_models.CreateEventStreamingRequestSinkSinkFnfParameters = None,
        sink_https_parameters: main_models.SinkHttpsParameters = None,
        sink_kafka_parameters: main_models.CreateEventStreamingRequestSinkSinkKafkaParameters = None,
        sink_mnsparameters: main_models.CreateEventStreamingRequestSinkSinkMNSParameters = None,
        sink_mqttparameters: main_models.SinkMQTTParameters = None,
        sink_ossparameters: main_models.SinkOSSParameters = None,
        sink_open_source_rabbit_mqparameters: main_models.CreateEventStreamingRequestSinkSinkOpenSourceRabbitMQParameters = None,
        sink_prometheus_parameters: main_models.CreateEventStreamingRequestSinkSinkPrometheusParameters = None,
        sink_rabbit_mqmeta_parameters: main_models.SinkRabbitMQMetaParameters = None,
        sink_rabbit_mqmsg_sync_parameters: main_models.SinkRabbitMQMsgSyncParameters = None,
        sink_rabbit_mqparameters: main_models.CreateEventStreamingRequestSinkSinkRabbitMQParameters = None,
        sink_rocket_mqcheckpoint_parameters: main_models.CreateEventStreamingRequestSinkSinkRocketMQCheckpointParameters = None,
        sink_rocket_mqparameters: main_models.CreateEventStreamingRequestSinkSinkRocketMQParameters = None,
        sink_slsparameters: main_models.CreateEventStreamingRequestSinkSinkSLSParameters = None,
    ):
        self.sink_agent_run_parameters = sink_agent_run_parameters
        # The description.
        self.sink_apache_kafka_parameters = sink_apache_kafka_parameters
        # The event source type.
        self.sink_apache_rocket_mqcheckpoint_parameters = sink_apache_rocket_mqcheckpoint_parameters
        self.sink_api_destination_parameters = sink_api_destination_parameters
        self.sink_bai_lian_parameters = sink_bai_lian_parameters
        # The Sink Kafka connector parameters.
        self.sink_customized_kafka_connector_parameters = sink_customized_kafka_connector_parameters
        # The Sink Kafka parameters.
        self.sink_customized_kafka_parameters = sink_customized_kafka_parameters
        # The Sink DashVector parameters.
        self.sink_dash_vector_parameters = sink_dash_vector_parameters
        # The Sink DataHub parameters.
        self.sink_data_hub_parameters = sink_data_hub_parameters
        self.sink_data_works_trigger_parameters = sink_data_works_trigger_parameters
        # The event source type.
        self.sink_doris_parameters = sink_doris_parameters
        # The event target name.
        self.sink_event_house_parameters = sink_event_house_parameters
        # The function target.
        self.sink_fc_parameters = sink_fc_parameters
        # The Sink Fnf parameters.
        self.sink_fnf_parameters = sink_fnf_parameters
        self.sink_https_parameters = sink_https_parameters
        # The Sink Kafka parameters.
        self.sink_kafka_parameters = sink_kafka_parameters
        # The MNS event target.
        self.sink_mnsparameters = sink_mnsparameters
        self.sink_mqttparameters = sink_mqttparameters
        self.sink_ossparameters = sink_ossparameters
        self.sink_open_source_rabbit_mqparameters = sink_open_source_rabbit_mqparameters
        # The Sink Prometheus parameters.
        self.sink_prometheus_parameters = sink_prometheus_parameters
        self.sink_rabbit_mqmeta_parameters = sink_rabbit_mqmeta_parameters
        self.sink_rabbit_mqmsg_sync_parameters = sink_rabbit_mqmsg_sync_parameters
        # The Sink RabbitMQ parameters.
        self.sink_rabbit_mqparameters = sink_rabbit_mqparameters
        # The event source type.
        self.sink_rocket_mqcheckpoint_parameters = sink_rocket_mqcheckpoint_parameters
        # Sink RocketMQ Parameters
        self.sink_rocket_mqparameters = sink_rocket_mqparameters
        # Sink SLS Parameters
        self.sink_slsparameters = sink_slsparameters

    def validate(self):
        if self.sink_agent_run_parameters:
            self.sink_agent_run_parameters.validate()
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
        if self.sink_event_house_parameters:
            self.sink_event_house_parameters.validate()
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
        if self.sink_mqttparameters:
            self.sink_mqttparameters.validate()
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
        if self.sink_agent_run_parameters is not None:
            result['SinkAgentRunParameters'] = self.sink_agent_run_parameters.to_map()

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

        if self.sink_event_house_parameters is not None:
            result['SinkEventHouseParameters'] = self.sink_event_house_parameters.to_map()

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

        if self.sink_mqttparameters is not None:
            result['SinkMQTTParameters'] = self.sink_mqttparameters.to_map()

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
        if m.get('SinkAgentRunParameters') is not None:
            temp_model = main_models.SinkAgentRunParameters()
            self.sink_agent_run_parameters = temp_model.from_map(m.get('SinkAgentRunParameters'))

        if m.get('SinkApacheKafkaParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParameters()
            self.sink_apache_kafka_parameters = temp_model.from_map(m.get('SinkApacheKafkaParameters'))

        if m.get('SinkApacheRocketMQCheckpointParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParameters()
            self.sink_apache_rocket_mqcheckpoint_parameters = temp_model.from_map(m.get('SinkApacheRocketMQCheckpointParameters'))

        if m.get('SinkApiDestinationParameters') is not None:
            temp_model = main_models.SinkApiDestinationParameters()
            self.sink_api_destination_parameters = temp_model.from_map(m.get('SinkApiDestinationParameters'))

        if m.get('SinkBaiLianParameters') is not None:
            temp_model = main_models.SinkBaiLianParameters()
            self.sink_bai_lian_parameters = temp_model.from_map(m.get('SinkBaiLianParameters'))

        if m.get('SinkCustomizedKafkaConnectorParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkCustomizedKafkaConnectorParameters()
            self.sink_customized_kafka_connector_parameters = temp_model.from_map(m.get('SinkCustomizedKafkaConnectorParameters'))

        if m.get('SinkCustomizedKafkaParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkCustomizedKafkaParameters()
            self.sink_customized_kafka_parameters = temp_model.from_map(m.get('SinkCustomizedKafkaParameters'))

        if m.get('SinkDashVectorParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDashVectorParameters()
            self.sink_dash_vector_parameters = temp_model.from_map(m.get('SinkDashVectorParameters'))

        if m.get('SinkDataHubParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDataHubParameters()
            self.sink_data_hub_parameters = temp_model.from_map(m.get('SinkDataHubParameters'))

        if m.get('SinkDataWorksTriggerParameters') is not None:
            temp_model = main_models.SinkDataWorksTriggerParameters()
            self.sink_data_works_trigger_parameters = temp_model.from_map(m.get('SinkDataWorksTriggerParameters'))

        if m.get('SinkDorisParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDorisParameters()
            self.sink_doris_parameters = temp_model.from_map(m.get('SinkDorisParameters'))

        if m.get('SinkEventHouseParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkEventHouseParameters()
            self.sink_event_house_parameters = temp_model.from_map(m.get('SinkEventHouseParameters'))

        if m.get('SinkFcParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkFcParameters()
            self.sink_fc_parameters = temp_model.from_map(m.get('SinkFcParameters'))

        if m.get('SinkFnfParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkFnfParameters()
            self.sink_fnf_parameters = temp_model.from_map(m.get('SinkFnfParameters'))

        if m.get('SinkHttpsParameters') is not None:
            temp_model = main_models.SinkHttpsParameters()
            self.sink_https_parameters = temp_model.from_map(m.get('SinkHttpsParameters'))

        if m.get('SinkKafkaParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkKafkaParameters()
            self.sink_kafka_parameters = temp_model.from_map(m.get('SinkKafkaParameters'))

        if m.get('SinkMNSParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkMNSParameters()
            self.sink_mnsparameters = temp_model.from_map(m.get('SinkMNSParameters'))

        if m.get('SinkMQTTParameters') is not None:
            temp_model = main_models.SinkMQTTParameters()
            self.sink_mqttparameters = temp_model.from_map(m.get('SinkMQTTParameters'))

        if m.get('SinkOSSParameters') is not None:
            temp_model = main_models.SinkOSSParameters()
            self.sink_ossparameters = temp_model.from_map(m.get('SinkOSSParameters'))

        if m.get('SinkOpenSourceRabbitMQParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkOpenSourceRabbitMQParameters()
            self.sink_open_source_rabbit_mqparameters = temp_model.from_map(m.get('SinkOpenSourceRabbitMQParameters'))

        if m.get('SinkPrometheusParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkPrometheusParameters()
            self.sink_prometheus_parameters = temp_model.from_map(m.get('SinkPrometheusParameters'))

        if m.get('SinkRabbitMQMetaParameters') is not None:
            temp_model = main_models.SinkRabbitMQMetaParameters()
            self.sink_rabbit_mqmeta_parameters = temp_model.from_map(m.get('SinkRabbitMQMetaParameters'))

        if m.get('SinkRabbitMQMsgSyncParameters') is not None:
            temp_model = main_models.SinkRabbitMQMsgSyncParameters()
            self.sink_rabbit_mqmsg_sync_parameters = temp_model.from_map(m.get('SinkRabbitMQMsgSyncParameters'))

        if m.get('SinkRabbitMQParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRabbitMQParameters()
            self.sink_rabbit_mqparameters = temp_model.from_map(m.get('SinkRabbitMQParameters'))

        if m.get('SinkRocketMQCheckpointParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQCheckpointParameters()
            self.sink_rocket_mqcheckpoint_parameters = temp_model.from_map(m.get('SinkRocketMQCheckpointParameters'))

        if m.get('SinkRocketMQParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQParameters()
            self.sink_rocket_mqparameters = temp_model.from_map(m.get('SinkRocketMQParameters'))

        if m.get('SinkSLSParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkSLSParameters()
            self.sink_slsparameters = temp_model.from_map(m.get('SinkSLSParameters'))

        return self

class CreateEventStreamingRequestSinkSinkSLSParameters(DaraModel):
    def __init__(
        self,
        body: main_models.CreateEventStreamingRequestSinkSinkSLSParametersBody = None,
        content_schema: main_models.CreateEventStreamingRequestSinkSinkSLSParametersContentSchema = None,
        content_type: main_models.CreateEventStreamingRequestSinkSinkSLSParametersContentType = None,
        log_store: main_models.CreateEventStreamingRequestSinkSinkSLSParametersLogStore = None,
        project: main_models.CreateEventStreamingRequestSinkSinkSLSParametersProject = None,
        role_name: main_models.CreateEventStreamingRequestSinkSinkSLSParametersRoleName = None,
        topic: main_models.CreateEventStreamingRequestSinkSinkSLSParametersTopic = None,
    ):
        # The content sent to Simple Log Service.
        self.body = body
        # The custom log key-value pairs. This parameter takes effect only when ContentType is set to KeyValue. Each key-value pair is represented by Key_n and Value_n.
        self.content_schema = content_schema
        # The Simple Log Service data format. You can select the default format or configure specified key-value pairs. Valid values:
        # 
        # - JSON
        # - KeyValue
        self.content_type = content_type
        # The Logstore of Simple Log Service.
        self.log_store = log_store
        # The project of Simple Log Service.
        self.project = project
        # To grant authorization to the event bus EventBridge to use this role to read Simple Log Service log content, the following conditions must be met: when creating the role used by the service in the Resource Access Management (RAM) console, select "Alibaba Cloud Service", and set "Trusted Service" to "event bus".
        self.role_name = role_name
        # The topic where the log resides, corresponding to the Simple Log Service reserved field "__topic__".
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
            temp_model = main_models.CreateEventStreamingRequestSinkSinkSLSParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('ContentSchema') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkSLSParametersContentSchema()
            self.content_schema = temp_model.from_map(m.get('ContentSchema'))

        if m.get('ContentType') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkSLSParametersContentType()
            self.content_type = temp_model.from_map(m.get('ContentType'))

        if m.get('LogStore') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkSLSParametersLogStore()
            self.log_store = temp_model.from_map(m.get('LogStore'))

        if m.get('Project') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkSLSParametersProject()
            self.project = temp_model.from_map(m.get('Project'))

        if m.get('RoleName') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkSLSParametersRoleName()
            self.role_name = temp_model.from_map(m.get('RoleName'))

        if m.get('Topic') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkSLSParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        return self

class CreateEventStreamingRequestSinkSinkSLSParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The topic where the log resides, corresponding to the Simple Log Service reserved field "__topic__".
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkSLSParametersRoleName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # To grant authorization to the event bus EventBridge to use this role to read Simple Log Service log content, the following conditions must be met: when creating the role used by the service in the Resource Access Management (RAM) console, select "Alibaba Cloud Service", and set "Trusted Service" to "event bus".
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkSLSParametersProject(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The project of Simple Log Service.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkSLSParametersLogStore(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The Logstore of Simple Log Service.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkSLSParametersContentType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format.
        self.form = form
        # The template style.
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

class CreateEventStreamingRequestSinkSinkSLSParametersContentSchema(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The template style.
        self.form = form
        # The template style.
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

class CreateEventStreamingRequestSinkSinkSLSParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format.
        self.form = form
        # The template style.
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

class CreateEventStreamingRequestSinkSinkRocketMQParameters(DaraModel):
    def __init__(
        self,
        body: main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersBody = None,
        delivery_order_type: main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersDeliveryOrderType = None,
        instance_endpoint: main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceEndpoint = None,
        instance_id: main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceId = None,
        instance_password: main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersInstancePassword = None,
        instance_type: main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceType = None,
        instance_username: main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceUsername = None,
        keys: main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersKeys = None,
        network: main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersNetwork = None,
        properties: main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersProperties = None,
        security_group_id: main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersSecurityGroupId = None,
        sharding_key: main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersShardingKey = None,
        tags: main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersTags = None,
        topic: main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersTopic = None,
        v_switch_ids: main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersVSwitchIds = None,
        vpc_id: main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersVpcId = None,
    ):
        # The message content.
        self.body = body
        self.delivery_order_type = delivery_order_type
        # The instance endpoint.
        self.instance_endpoint = instance_endpoint
        # The event target type is MSMQ for RocketMQ.
        self.instance_id = instance_id
        # The instance password.
        self.instance_password = instance_password
        # The instance type.
        self.instance_type = instance_type
        # The instance username.
        self.instance_username = instance_username
        # The filter properties.
        self.keys = keys
        # The network type. Valid values:
        # - PublicNetwork
        # - PrivateNetwork
        self.network = network
        # The filter properties.
        self.properties = properties
        # The security group ID.
        self.security_group_id = security_group_id
        self.sharding_key = sharding_key
        # The filter properties.
        self.tags = tags
        # The topic of the MSMQ for RocketMQ instance.
        self.topic = topic
        # The vSwitch ID.
        self.v_switch_ids = v_switch_ids
        # The VPC ID.
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
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('DeliveryOrderType') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersDeliveryOrderType()
            self.delivery_order_type = temp_model.from_map(m.get('DeliveryOrderType'))

        if m.get('InstanceEndpoint') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceEndpoint()
            self.instance_endpoint = temp_model.from_map(m.get('InstanceEndpoint'))

        if m.get('InstanceId') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m.get('InstanceId'))

        if m.get('InstancePassword') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersInstancePassword()
            self.instance_password = temp_model.from_map(m.get('InstancePassword'))

        if m.get('InstanceType') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceType()
            self.instance_type = temp_model.from_map(m.get('InstanceType'))

        if m.get('InstanceUsername') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceUsername()
            self.instance_username = temp_model.from_map(m.get('InstanceUsername'))

        if m.get('Keys') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersKeys()
            self.keys = temp_model.from_map(m.get('Keys'))

        if m.get('Network') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        if m.get('Properties') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('SecurityGroupId') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersSecurityGroupId()
            self.security_group_id = temp_model.from_map(m.get('SecurityGroupId'))

        if m.get('ShardingKey') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersShardingKey()
            self.sharding_key = temp_model.from_map(m.get('ShardingKey'))

        if m.get('Tags') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Topic') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        if m.get('VpcId') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQParametersVpcId()
            self.vpc_id = temp_model.from_map(m.get('VpcId'))

        return self

class CreateEventStreamingRequestSinkSinkRocketMQParametersVpcId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The event transformation format. Default value: CONSTANT.
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

class CreateEventStreamingRequestSinkSinkRocketMQParametersVSwitchIds(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
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

class CreateEventStreamingRequestSinkSinkRocketMQParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The topic name of the MSMQ for RocketMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkRocketMQParametersTags(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format.
        self.form = form
        # The template style.
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

class CreateEventStreamingRequestSinkSinkRocketMQParametersShardingKey(DaraModel):
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

class CreateEventStreamingRequestSinkSinkRocketMQParametersSecurityGroupId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The security group ID.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkRocketMQParametersProperties(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format.
        self.form = form
        # The template style.
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

class CreateEventStreamingRequestSinkSinkRocketMQParametersNetwork(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The network type. Valid values:          
        # - PublicNetwork
        # - PrivateNetwork
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkRocketMQParametersKeys(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format.
        self.form = form
        # The template style.
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

class CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceUsername(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The instance username.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The instance type. Valid values:
        # 
        # - Cloud_4: Alibaba Cloud ApsaraMQ for RocketMQ 4.0 instance (default)
        # - Cloud_5: Alibaba Cloud ApsaraMQ for RocketMQ 5.0 instance
        # - SelfBuilt: self-managed Apache RocketMQ cluster
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkRocketMQParametersInstancePassword(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The instance password.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The instance ID of MSMQ for RocketMQ.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceEndpoint(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The instance endpoint.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkRocketMQParametersDeliveryOrderType(DaraModel):
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

class CreateEventStreamingRequestSinkSinkRocketMQParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format.
        self.form = form
        # The template style.
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

class CreateEventStreamingRequestSinkSinkRocketMQCheckpointParameters(DaraModel):
    def __init__(
        self,
        consume_timestamp: main_models.CreateEventStreamingRequestSinkSinkRocketMQCheckpointParametersConsumeTimestamp = None,
        group: main_models.CreateEventStreamingRequestSinkSinkRocketMQCheckpointParametersGroup = None,
        instance_id: str = None,
        instance_type: str = None,
        topic: main_models.CreateEventStreamingRequestSinkSinkRocketMQCheckpointParametersTopic = None,
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
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQCheckpointParametersConsumeTimestamp()
            self.consume_timestamp = temp_model.from_map(m.get('ConsumeTimestamp'))

        if m.get('Group') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQCheckpointParametersGroup()
            self.group = temp_model.from_map(m.get('Group'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Topic') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRocketMQCheckpointParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        return self

class CreateEventStreamingRequestSinkSinkRocketMQCheckpointParametersTopic(DaraModel):
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

class CreateEventStreamingRequestSinkSinkRocketMQCheckpointParametersGroup(DaraModel):
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

class CreateEventStreamingRequestSinkSinkRocketMQCheckpointParametersConsumeTimestamp(DaraModel):
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

class CreateEventStreamingRequestSinkSinkRabbitMQParameters(DaraModel):
    def __init__(
        self,
        body: main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersBody = None,
        exchange: main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersExchange = None,
        instance_id: main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId = None,
        message_id: main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersMessageId = None,
        network_type: main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersNetworkType = None,
        properties: main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersProperties = None,
        queue_name: main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersQueueName = None,
        routing_key: main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey = None,
        security_group_id: main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersSecurityGroupId = None,
        target_type: main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersTargetType = None,
        v_switch_ids: main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersVSwitchIds = None,
        virtual_host_name: main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName = None,
        vpc_id: main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersVpcId = None,
    ):
        # The message content.
        self.body = body
        # The Exchange mode. This parameter is required only when TargetType is set to Exchange.
        self.exchange = exchange
        # The target service type is ApsaraMQ for RabbitMQ.
        self.instance_id = instance_id
        # The message ID.
        self.message_id = message_id
        self.network_type = network_type
        # The filter properties.
        self.properties = properties
        # The Queue mode. This parameter is required only when TargetType is set to Queue.
        self.queue_name = queue_name
        # The routing rule of the message. This parameter is required only when TargetType is set to Exchange.
        self.routing_key = routing_key
        self.security_group_id = security_group_id
        # The target type.
        self.target_type = target_type
        self.v_switch_ids = v_switch_ids
        # The vhost name of the ApsaraMQ for RabbitMQ instance.
        self.virtual_host_name = virtual_host_name
        self.vpc_id = vpc_id

    def validate(self):
        if self.body:
            self.body.validate()
        if self.exchange:
            self.exchange.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.message_id:
            self.message_id.validate()
        if self.network_type:
            self.network_type.validate()
        if self.properties:
            self.properties.validate()
        if self.queue_name:
            self.queue_name.validate()
        if self.routing_key:
            self.routing_key.validate()
        if self.security_group_id:
            self.security_group_id.validate()
        if self.target_type:
            self.target_type.validate()
        if self.v_switch_ids:
            self.v_switch_ids.validate()
        if self.virtual_host_name:
            self.virtual_host_name.validate()
        if self.vpc_id:
            self.vpc_id.validate()

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

        if self.network_type is not None:
            result['NetworkType'] = self.network_type.to_map()

        if self.properties is not None:
            result['Properties'] = self.properties.to_map()

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()

        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key.to_map()

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id.to_map()

        if self.target_type is not None:
            result['TargetType'] = self.target_type.to_map()

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()

        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Exchange') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersExchange()
            self.exchange = temp_model.from_map(m.get('Exchange'))

        if m.get('InstanceId') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m.get('InstanceId'))

        if m.get('MessageId') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m.get('MessageId'))

        if m.get('NetworkType') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersNetworkType()
            self.network_type = temp_model.from_map(m.get('NetworkType'))

        if m.get('Properties') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('QueueName') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersQueueName()
            self.queue_name = temp_model.from_map(m.get('QueueName'))

        if m.get('RoutingKey') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey()
            self.routing_key = temp_model.from_map(m.get('RoutingKey'))

        if m.get('SecurityGroupId') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersSecurityGroupId()
            self.security_group_id = temp_model.from_map(m.get('SecurityGroupId'))

        if m.get('TargetType') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersTargetType()
            self.target_type = temp_model.from_map(m.get('TargetType'))

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        if m.get('VirtualHostName') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName()
            self.virtual_host_name = temp_model.from_map(m.get('VirtualHostName'))

        if m.get('VpcId') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkRabbitMQParametersVpcId()
            self.vpc_id = temp_model.from_map(m.get('VpcId'))

        return self

class CreateEventStreamingRequestSinkSinkRabbitMQParametersVpcId(DaraModel):
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

class CreateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The vhost name of the ApsaraMQ for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkRabbitMQParametersVSwitchIds(DaraModel):
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

class CreateEventStreamingRequestSinkSinkRabbitMQParametersTargetType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The target type. Valid values:
        # - Exchange: Exchange mode.
        # - Queue: Queue mode.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkRabbitMQParametersSecurityGroupId(DaraModel):
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

class CreateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The routing rule of the message.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkRabbitMQParametersQueueName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The queue name of the instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkRabbitMQParametersProperties(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format.
        self.form = form
        # The template style.
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

class CreateEventStreamingRequestSinkSinkRabbitMQParametersNetworkType(DaraModel):
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

class CreateEventStreamingRequestSinkSinkRabbitMQParametersMessageId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format.
        self.form = form
        # The template style.
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

class CreateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The instance ID of the ApsaraMQ for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkRabbitMQParametersExchange(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The name of the exchange in the MSMQ for RabbitMQ instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkRabbitMQParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format.
        self.form = form
        # The template style.
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

class CreateEventStreamingRequestSinkSinkPrometheusParameters(DaraModel):
    def __init__(
        self,
        authorization_type: main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersAuthorizationType = None,
        data: main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersData = None,
        header_parameters: main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersHeaderParameters = None,
        network_type: main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersNetworkType = None,
        password: main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersPassword = None,
        security_group_id: main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersSecurityGroupId = None,
        url: main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersURL = None,
        username: main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersUsername = None,
        v_switch_id: main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersVSwitchId = None,
        vpc_id: main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersVpcId = None,
    ):
        # The authentication method.
        self.authorization_type = authorization_type
        # The metric content.
        self.data = data
        # The data structure of request header parameters.
        self.header_parameters = header_parameters
        # The network type.
        self.network_type = network_type
        # The password.
        self.password = password
        # The security group ID.
        self.security_group_id = security_group_id
        # The Prometheus Remote Write URL address.
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
            temp_model = main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersAuthorizationType()
            self.authorization_type = temp_model.from_map(m.get('AuthorizationType'))

        if m.get('Data') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HeaderParameters') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersHeaderParameters()
            self.header_parameters = temp_model.from_map(m.get('HeaderParameters'))

        if m.get('NetworkType') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersNetworkType()
            self.network_type = temp_model.from_map(m.get('NetworkType'))

        if m.get('Password') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersPassword()
            self.password = temp_model.from_map(m.get('Password'))

        if m.get('SecurityGroupId') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersSecurityGroupId()
            self.security_group_id = temp_model.from_map(m.get('SecurityGroupId'))

        if m.get('URL') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersURL()
            self.url = temp_model.from_map(m.get('URL'))

        if m.get('Username') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersUsername()
            self.username = temp_model.from_map(m.get('Username'))

        if m.get('VSwitchId') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersVSwitchId()
            self.v_switch_id = temp_model.from_map(m.get('VSwitchId'))

        if m.get('VpcId') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkPrometheusParametersVpcId()
            self.vpc_id = temp_model.from_map(m.get('VpcId'))

        return self

class CreateEventStreamingRequestSinkSinkPrometheusParametersVpcId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
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

class CreateEventStreamingRequestSinkSinkPrometheusParametersVSwitchId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
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

class CreateEventStreamingRequestSinkSinkPrometheusParametersUsername(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
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

class CreateEventStreamingRequestSinkSinkPrometheusParametersURL(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # The template style. This parameter is empty when Form is set to CONSTANT.
        self.template = template
        # The Prometheus Remote Write URL address.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkPrometheusParametersSecurityGroupId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The security group ID.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkPrometheusParametersPassword(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
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

class CreateEventStreamingRequestSinkSinkPrometheusParametersNetworkType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The network type.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkPrometheusParametersHeaderParameters(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format.
        self.form = form
        # The HTTP request header template style. Specify this parameter when Form is set to TEMPLATE. The result after event content transformation must be in JSON format.
        self.template = template
        # - If Form is CONSTANT: the constant value.
        # - If Form is JSONPATH: the JSONPath-extracted content.
        # - If Form is TEMPLATE: the template variable.
        # 
        # Note: The Value field cannot exceed 10240 characters.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkPrometheusParametersData(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: JSONPATH.
        self.form = form
        # The template style.
        self.template = template
        # The metric content.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkPrometheusParametersAuthorizationType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
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

class CreateEventStreamingRequestSinkSinkOpenSourceRabbitMQParameters(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        body: main_models.CreateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersBody = None,
        endpoint: str = None,
        exchange: str = None,
        message_id: main_models.CreateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersMessageId = None,
        network_type: str = None,
        password: str = None,
        properties: main_models.CreateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersProperties = None,
        queue_name: str = None,
        routing_key: main_models.CreateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersRoutingKey = None,
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
            temp_model = main_models.CreateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Exchange') is not None:
            self.exchange = m.get('Exchange')

        if m.get('MessageId') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m.get('MessageId'))

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Properties') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('RoutingKey') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersRoutingKey()
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

class CreateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersRoutingKey(DaraModel):
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

class CreateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersProperties(DaraModel):
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

class CreateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersMessageId(DaraModel):
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

class CreateEventStreamingRequestSinkSinkOpenSourceRabbitMQParametersBody(DaraModel):
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

class CreateEventStreamingRequestSinkSinkMNSParameters(DaraModel):
    def __init__(
        self,
        body: main_models.CreateEventStreamingRequestSinkSinkMNSParametersBody = None,
        is_base_64encode: main_models.CreateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode = None,
        queue_name: main_models.CreateEventStreamingRequestSinkSinkMNSParametersQueueName = None,
    ):
        # The message content.
        self.body = body
        # Specifies whether to enable Base64 encoding.
        self.is_base_64encode = is_base_64encode
        # The target service type is Simple Message Queue (formerly MNS).
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
            temp_model = main_models.CreateEventStreamingRequestSinkSinkMNSParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('IsBase64Encode') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode()
            self.is_base_64encode = temp_model.from_map(m.get('IsBase64Encode'))

        if m.get('QueueName') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkMNSParametersQueueName()
            self.queue_name = temp_model.from_map(m.get('QueueName'))

        return self

class CreateEventStreamingRequestSinkSinkMNSParametersQueueName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The queue name of Simple Message Queue (formerly MNS).
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The event transformation format. Default value: CONSTANT.
        self.form = form
        # The template style.
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

class CreateEventStreamingRequestSinkSinkMNSParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format.
        self.form = form
        # The template style.
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

class CreateEventStreamingRequestSinkSinkKafkaParameters(DaraModel):
    def __init__(
        self,
        acks: main_models.CreateEventStreamingRequestSinkSinkKafkaParametersAcks = None,
        compression_type: str = None,
        dynamic_topic: main_models.CreateEventStreamingRequestSinkSinkKafkaParametersDynamicTopic = None,
        headers: main_models.CreateEventStreamingRequestSinkSinkKafkaParametersHeaders = None,
        instance_id: main_models.CreateEventStreamingRequestSinkSinkKafkaParametersInstanceId = None,
        key: main_models.CreateEventStreamingRequestSinkSinkKafkaParametersKey = None,
        topic: main_models.CreateEventStreamingRequestSinkSinkKafkaParametersTopic = None,
        value: main_models.CreateEventStreamingRequestSinkSinkKafkaParametersValue = None,
    ):
        # The acknowledgment mode for writing to Kafka:
        # - acks=0: No response is required from the server. This mode provides high performance but a high risk of data loss.
        # - acks=1: A response is returned after the primary node writes successfully. This mode provides moderate performance and a moderate risk of data loss. Data loss may occur if the primary node goes down.
        # - acks=all: A response is returned only after the primary node writes successfully and the secondary nodes complete synchronization. This mode provides lower performance but higher data security. Data loss occurs only if both the primary and secondary nodes go down.
        self.acks = acks
        self.compression_type = compression_type
        # Specifies the target Topic routing strategy for messages. If both the Topic parameter and the DynamicTopic parameter are specified, the DynamicTopic parameter takes precedence. Two configuration modes are supported:
        #     1. **Static constant mode**: directly specify a fixed Topic name string (for example, "order_created"). All messages are sent to this Topic.
        #     2. **Dynamic extraction mode**: specify a standard JSONPath expression (for example, "$.user.id" or "$.metadata.category"). The system parses the upstream message body and extracts the matching field value as the target Topic name.
        self.dynamic_topic = dynamic_topic
        self.headers = headers
        # The event target type is MSMQ for Apache Kafka.
        self.instance_id = instance_id
        # The message key.
        self.key = key
        # The topic name.
        self.topic = topic
        # The message body.
        self.value = value

    def validate(self):
        if self.acks:
            self.acks.validate()
        if self.dynamic_topic:
            self.dynamic_topic.validate()
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

        if self.dynamic_topic is not None:
            result['DynamicTopic'] = self.dynamic_topic.to_map()

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
            temp_model = main_models.CreateEventStreamingRequestSinkSinkKafkaParametersAcks()
            self.acks = temp_model.from_map(m.get('Acks'))

        if m.get('CompressionType') is not None:
            self.compression_type = m.get('CompressionType')

        if m.get('DynamicTopic') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkKafkaParametersDynamicTopic()
            self.dynamic_topic = temp_model.from_map(m.get('DynamicTopic'))

        if m.get('Headers') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkKafkaParametersHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('InstanceId') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkKafkaParametersInstanceId()
            self.instance_id = temp_model.from_map(m.get('InstanceId'))

        if m.get('Key') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkKafkaParametersKey()
            self.key = temp_model.from_map(m.get('Key'))

        if m.get('Topic') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkKafkaParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        if m.get('Value') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkKafkaParametersValue()
            self.value = temp_model.from_map(m.get('Value'))

        return self

class CreateEventStreamingRequestSinkSinkKafkaParametersValue(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format.
        self.form = form
        # The template style.
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

class CreateEventStreamingRequestSinkSinkKafkaParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
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

class CreateEventStreamingRequestSinkSinkKafkaParametersKey(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
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

class CreateEventStreamingRequestSinkSinkKafkaParametersInstanceId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
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

class CreateEventStreamingRequestSinkSinkKafkaParametersHeaders(DaraModel):
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

class CreateEventStreamingRequestSinkSinkKafkaParametersDynamicTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation type.
        # CONSTANT: constant.
        # JSONPATH: extracts content from upstream based on a path.
        self.form = form
        # The template.
        self.template = template
        # The value.
        # [_single.params.Sink.props.SinkKafkaParameters.D
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkKafkaParametersAcks(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The acknowledgment mode for writing to Kafka:
        # - acks=0: No response is required from the server. This mode provides high performance but a high risk of data loss.
        # - acks=1: A response is returned after the primary node writes successfully. This mode provides moderate performance and a moderate risk of data loss. Data loss may occur if the primary node goes down.
        # - acks=all: A response is returned only after the primary node writes successfully and the secondary nodes complete synchronization. This mode provides lower performance but higher data security. Data loss occurs only if both the primary and secondary nodes go down.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkFnfParameters(DaraModel):
    def __init__(
        self,
        execution_name: main_models.CreateEventStreamingRequestSinkSinkFnfParametersExecutionName = None,
        flow_name: main_models.CreateEventStreamingRequestSinkSinkFnfParametersFlowName = None,
        input: main_models.CreateEventStreamingRequestSinkSinkFnfParametersInput = None,
        role_name: main_models.CreateEventStreamingRequestSinkSinkFnfParametersRoleName = None,
    ):
        # The execution name.
        self.execution_name = execution_name
        # The flow name.
        self.flow_name = flow_name
        # The execution input information.
        self.input = input
        # The role configuration.
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
            temp_model = main_models.CreateEventStreamingRequestSinkSinkFnfParametersExecutionName()
            self.execution_name = temp_model.from_map(m.get('ExecutionName'))

        if m.get('FlowName') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkFnfParametersFlowName()
            self.flow_name = temp_model.from_map(m.get('FlowName'))

        if m.get('Input') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkFnfParametersInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('RoleName') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkFnfParametersRoleName()
            self.role_name = temp_model.from_map(m.get('RoleName'))

        return self

class CreateEventStreamingRequestSinkSinkFnfParametersRoleName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
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

class CreateEventStreamingRequestSinkSinkFnfParametersInput(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Valid values:
        # 
        # - ORIGINAL: complete event
        # - JSONPATH: partial event
        # - CONSTANT: constant
        # - TEMPLATE: template
        # 
        # For more information, see [Event transformation](https://www.alibabacloud.com/help/en/eventbridge/user-guide/event-transformation).
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

class CreateEventStreamingRequestSinkSinkFnfParametersFlowName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
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

class CreateEventStreamingRequestSinkSinkFnfParametersExecutionName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT. Valid values:
        # 
        # - JSONPATH: partial event
        # - CONSTANT: constant
        # - TEMPLATE: template
        # 
        # For more information, see [Event transformation](https://www.alibabacloud.com/help/en/eventbridge/user-guide/event-transformation).
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

class CreateEventStreamingRequestSinkSinkFcParameters(DaraModel):
    def __init__(
        self,
        body: main_models.CreateEventStreamingRequestSinkSinkFcParametersBody = None,
        concurrency: main_models.CreateEventStreamingRequestSinkSinkFcParametersConcurrency = None,
        data_format: main_models.CreateEventStreamingRequestSinkSinkFcParametersDataFormat = None,
        function_name: main_models.CreateEventStreamingRequestSinkSinkFcParametersFunctionName = None,
        invocation_type: main_models.CreateEventStreamingRequestSinkSinkFcParametersInvocationType = None,
        qualifier: main_models.CreateEventStreamingRequestSinkSinkFcParametersQualifier = None,
        service_name: main_models.CreateEventStreamingRequestSinkSinkFcParametersServiceName = None,
    ):
        # The content body sent to the function.
        self.body = body
        # The delivery concurrency. The minimum value is 1.
        self.concurrency = concurrency
        self.data_format = data_format
        # The function name.
        self.function_name = function_name
        # The invocation type. Valid values:
        # - Sync: Synchronous.
        # - Async: Asynchronous.
        self.invocation_type = invocation_type
        # The service version.
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
            temp_model = main_models.CreateEventStreamingRequestSinkSinkFcParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Concurrency') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkFcParametersConcurrency()
            self.concurrency = temp_model.from_map(m.get('Concurrency'))

        if m.get('DataFormat') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkFcParametersDataFormat()
            self.data_format = temp_model.from_map(m.get('DataFormat'))

        if m.get('FunctionName') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkFcParametersFunctionName()
            self.function_name = temp_model.from_map(m.get('FunctionName'))

        if m.get('InvocationType') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkFcParametersInvocationType()
            self.invocation_type = temp_model.from_map(m.get('InvocationType'))

        if m.get('Qualifier') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkFcParametersQualifier()
            self.qualifier = temp_model.from_map(m.get('Qualifier'))

        if m.get('ServiceName') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkFcParametersServiceName()
            self.service_name = temp_model.from_map(m.get('ServiceName'))

        return self

class CreateEventStreamingRequestSinkSinkFcParametersServiceName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # The template style.
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

class CreateEventStreamingRequestSinkSinkFcParametersQualifier(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The service version.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkFcParametersInvocationType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The invocation type. Valid values:
        # - Sync: Synchronous.
        # - Async: Asynchronous.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkFcParametersFunctionName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
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

class CreateEventStreamingRequestSinkSinkFcParametersDataFormat(DaraModel):
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

class CreateEventStreamingRequestSinkSinkFcParametersConcurrency(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # The template style.
        self.template = template
        # The delivery concurrency. The minimum value is 1.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkFcParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Valid values:
        # 
        # - ORIGINAL: complete event
        # - JSONPATH: partial event
        # - CONSTANT: constant
        # - TEMPLATE: template
        # 
        # For more information, see [Event transformation](https://www.alibabacloud.com/help/en/eventbridge/user-guide/event-transformation).
        self.form = form
        # The template style.
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

class CreateEventStreamingRequestSinkSinkEventHouseParameters(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        event_table_name: str = None,
        mapping_rules: List[main_models.CreateEventStreamingRequestSinkSinkEventHouseParametersMappingRules] = None,
        namespace_name: str = None,
    ):
        # The catalog name.
        self.catalog_name = catalog_name
        # The name of the target table.
        self.event_table_name = event_table_name
        # The field mapping rules.
        self.mapping_rules = mapping_rules
        # The namespace of the target table.
        self.namespace_name = namespace_name

    def validate(self):
        if self.mapping_rules:
            for v1 in self.mapping_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.event_table_name is not None:
            result['EventTableName'] = self.event_table_name

        result['MappingRules'] = []
        if self.mapping_rules is not None:
            for k1 in self.mapping_rules:
                result['MappingRules'].append(k1.to_map() if k1 else None)

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('EventTableName') is not None:
            self.event_table_name = m.get('EventTableName')

        self.mapping_rules = []
        if m.get('MappingRules') is not None:
            for k1 in m.get('MappingRules'):
                temp_model = main_models.CreateEventStreamingRequestSinkSinkEventHouseParametersMappingRules()
                self.mapping_rules.append(temp_model.from_map(k1))

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        return self

class CreateEventStreamingRequestSinkSinkEventHouseParametersMappingRules(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        column_type: str = None,
        column_value: main_models.CreateEventStreamingRequestSinkSinkEventHouseParametersMappingRulesColumnValue = None,
    ):
        # The column name.
        self.column_name = column_name
        # The column type.
        self.column_type = column_type
        # The column value extraction rule.
        self.column_value = column_value

    def validate(self):
        if self.column_value:
            self.column_value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.column_type is not None:
            result['ColumnType'] = self.column_type

        if self.column_value is not None:
            result['ColumnValue'] = self.column_value.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')

        if m.get('ColumnValue') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkEventHouseParametersMappingRulesColumnValue()
            self.column_value = temp_model.from_map(m.get('ColumnValue'))

        return self

class CreateEventStreamingRequestSinkSinkEventHouseParametersMappingRulesColumnValue(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation method, such as JSONPATH.
        self.form = form
        # The template configuration.
        self.template = template
        # The extraction path, such as $.data.value.name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkDorisParameters(DaraModel):
    def __init__(
        self,
        be_http_endpoint: main_models.CreateEventStreamingRequestSinkSinkDorisParametersBeHttpEndpoint = None,
        body: main_models.CreateEventStreamingRequestSinkSinkDorisParametersBody = None,
        database: main_models.CreateEventStreamingRequestSinkSinkDorisParametersDatabase = None,
        fe_http_endpoint: main_models.CreateEventStreamingRequestSinkSinkDorisParametersFeHttpEndpoint = None,
        network_type: main_models.CreateEventStreamingRequestSinkSinkDorisParametersNetworkType = None,
        password: main_models.CreateEventStreamingRequestSinkSinkDorisParametersPassword = None,
        query_endpoint: main_models.CreateEventStreamingRequestSinkSinkDorisParametersQueryEndpoint = None,
        security_group_id: main_models.CreateEventStreamingRequestSinkSinkDorisParametersSecurityGroupId = None,
        table: main_models.CreateEventStreamingRequestSinkSinkDorisParametersTable = None,
        user_name: main_models.CreateEventStreamingRequestSinkSinkDorisParametersUserName = None,
        v_switch_ids: main_models.CreateEventStreamingRequestSinkSinkDorisParametersVSwitchIds = None,
        vpc_id: main_models.CreateEventStreamingRequestSinkSinkDorisParametersVpcId = None,
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
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDorisParametersBeHttpEndpoint()
            self.be_http_endpoint = temp_model.from_map(m.get('BeHttpEndpoint'))

        if m.get('Body') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDorisParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Database') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDorisParametersDatabase()
            self.database = temp_model.from_map(m.get('Database'))

        if m.get('FeHttpEndpoint') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDorisParametersFeHttpEndpoint()
            self.fe_http_endpoint = temp_model.from_map(m.get('FeHttpEndpoint'))

        if m.get('NetworkType') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDorisParametersNetworkType()
            self.network_type = temp_model.from_map(m.get('NetworkType'))

        if m.get('Password') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDorisParametersPassword()
            self.password = temp_model.from_map(m.get('Password'))

        if m.get('QueryEndpoint') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDorisParametersQueryEndpoint()
            self.query_endpoint = temp_model.from_map(m.get('QueryEndpoint'))

        if m.get('SecurityGroupId') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDorisParametersSecurityGroupId()
            self.security_group_id = temp_model.from_map(m.get('SecurityGroupId'))

        if m.get('Table') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDorisParametersTable()
            self.table = temp_model.from_map(m.get('Table'))

        if m.get('UserName') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDorisParametersUserName()
            self.user_name = temp_model.from_map(m.get('UserName'))

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDorisParametersVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        if m.get('VpcId') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDorisParametersVpcId()
            self.vpc_id = temp_model.from_map(m.get('VpcId'))

        return self

class CreateEventStreamingRequestSinkSinkDorisParametersVpcId(DaraModel):
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

class CreateEventStreamingRequestSinkSinkDorisParametersVSwitchIds(DaraModel):
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

class CreateEventStreamingRequestSinkSinkDorisParametersUserName(DaraModel):
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

class CreateEventStreamingRequestSinkSinkDorisParametersTable(DaraModel):
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

class CreateEventStreamingRequestSinkSinkDorisParametersSecurityGroupId(DaraModel):
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

class CreateEventStreamingRequestSinkSinkDorisParametersQueryEndpoint(DaraModel):
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

class CreateEventStreamingRequestSinkSinkDorisParametersPassword(DaraModel):
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

class CreateEventStreamingRequestSinkSinkDorisParametersNetworkType(DaraModel):
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

class CreateEventStreamingRequestSinkSinkDorisParametersFeHttpEndpoint(DaraModel):
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

class CreateEventStreamingRequestSinkSinkDorisParametersDatabase(DaraModel):
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

class CreateEventStreamingRequestSinkSinkDorisParametersBody(DaraModel):
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

class CreateEventStreamingRequestSinkSinkDorisParametersBeHttpEndpoint(DaraModel):
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

class CreateEventStreamingRequestSinkSinkDataHubParameters(DaraModel):
    def __init__(
        self,
        body: main_models.CreateEventStreamingRequestSinkSinkDataHubParametersBody = None,
        project: main_models.CreateEventStreamingRequestSinkSinkDataHubParametersProject = None,
        role_name: main_models.CreateEventStreamingRequestSinkSinkDataHubParametersRoleName = None,
        topic: main_models.CreateEventStreamingRequestSinkSinkDataHubParametersTopic = None,
        topic_schema: main_models.CreateEventStreamingRequestSinkSinkDataHubParametersTopicSchema = None,
        topic_type: main_models.CreateEventStreamingRequestSinkSinkDataHubParametersTopicType = None,
    ):
        # The Record content template for the BLOB type.
        self.body = body
        # The DataHub project name.
        self.project = project
        # The task role name.
        self.role_name = role_name
        # The DataHub topic name.
        self.topic = topic
        # The topic content schema for the TUPLE type.
        self.topic_schema = topic_schema
        # The topic type. Valid values:                 
        # - TUPLE
        # - BLOB
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
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDataHubParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Project') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDataHubParametersProject()
            self.project = temp_model.from_map(m.get('Project'))

        if m.get('RoleName') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDataHubParametersRoleName()
            self.role_name = temp_model.from_map(m.get('RoleName'))

        if m.get('Topic') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDataHubParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        if m.get('TopicSchema') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDataHubParametersTopicSchema()
            self.topic_schema = temp_model.from_map(m.get('TopicSchema'))

        if m.get('TopicType') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDataHubParametersTopicType()
            self.topic_type = temp_model.from_map(m.get('TopicType'))

        return self

class CreateEventStreamingRequestSinkSinkDataHubParametersTopicType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The topic type. Valid values:                     
        # - TUPLE
        # - BLOB
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkDataHubParametersTopicSchema(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format.
        self.form = form
        # The template style.
        self.template = template
        # The topic content schema for the TUPLE type.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkDataHubParametersTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The DataHub topic name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkDataHubParametersRoleName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The task role name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkDataHubParametersProject(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT.
        self.form = form
        # None.
        self.template = template
        # The DataHub project name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkDataHubParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format.
        self.form = form
        # None.
        self.template = template
        # The Record content template for the BLOB type.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkDashVectorParameters(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        collection: str = None,
        dash_vector_schema_parameters: List[main_models.CreateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParameters] = None,
        instance_id: str = None,
        network: str = None,
        operation: str = None,
        partition: main_models.CreateEventStreamingRequestSinkSinkDashVectorParametersPartition = None,
        primary_key_id: main_models.CreateEventStreamingRequestSinkSinkDashVectorParametersPrimaryKeyId = None,
        vector: main_models.CreateEventStreamingRequestSinkSinkDashVectorParametersVector = None,
    ):
        # The API key created in the DashVector console.
        self.api_key = api_key
        # The collection name.
        self.collection = collection
        # The schema field definition of the table entry when inserting into DashVector. The result after event content transformation must be in JSON format.
        self.dash_vector_schema_parameters = dash_vector_schema_parameters
        # The instance ID.
        self.instance_id = instance_id
        # The network type.
        self.network = network
        # The DashVector database operation type.
        self.operation = operation
        # The partition. Default value: default.
        self.partition = partition
        # The primary key ID for inserting or deleting records.
        # 
        # > If this field is not specified, a random primary key ID is used.
        self.primary_key_id = primary_key_id
        # The vector of the record to be inserted into DashVector.
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
                temp_model = main_models.CreateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParameters()
                self.dash_vector_schema_parameters.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Partition') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDashVectorParametersPartition()
            self.partition = temp_model.from_map(m.get('Partition'))

        if m.get('PrimaryKeyId') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDashVectorParametersPrimaryKeyId()
            self.primary_key_id = temp_model.from_map(m.get('PrimaryKeyId'))

        if m.get('Vector') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDashVectorParametersVector()
            self.vector = temp_model.from_map(m.get('Vector'))

        return self

class CreateEventStreamingRequestSinkSinkDashVectorParametersVector(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format.
        self.form = form
        # None.
        self.template = template
        # The JSONPath-extracted content.
        # > The Value field cannot exceed 10240 characters.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkDashVectorParametersPrimaryKeyId(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format.
        self.form = form
        # The primary key ID template. Specify this parameter only when Form is set to TEMPLATE.
        self.template = template
        # - If Form is JSONPATH: the JSONPath-extracted content.
        # - If Form is TEMPLATE: the template variable.
        # > The Value field cannot exceed 10240 characters.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkDashVectorParametersPartition(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format.
        self.form = form
        # None.
        self.template = template
        # - If Form is CONSTANT: the constant value.
        # - If Form is JSONPATH: the JSONPath-extracted content.
        # > The Value field cannot exceed 10240 characters.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParameters(DaraModel):
    def __init__(
        self,
        name: main_models.CreateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersName = None,
        type: main_models.CreateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersType = None,
        value: main_models.CreateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersValue = None,
    ):
        # The property name.
        self.name = name
        # The DashVector property type.
        self.type = type
        # The property value.
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
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersName()
            self.name = temp_model.from_map(m.get('Name'))

        if m.get('Type') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersType()
            self.type = temp_model.from_map(m.get('Type'))

        if m.get('Value') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersValue()
            self.value = temp_model.from_map(m.get('Value'))

        return self

class CreateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersValue(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # Form
        self.form = form
        # Template
        self.template = template
        # Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersType(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # Form
        self.form = form
        # Template
        self.template = template
        # Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkDashVectorParametersDashVectorSchemaParametersName(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # Form
        self.form = form
        # Template
        self.template = template
        # Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestSinkSinkCustomizedKafkaParameters(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The instance ID of MSMQ for Apache Kafka.
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

class CreateEventStreamingRequestSinkSinkCustomizedKafkaConnectorParameters(DaraModel):
    def __init__(
        self,
        connector_package_url: str = None,
        connector_parameters: main_models.CreateEventStreamingRequestSinkSinkCustomizedKafkaConnectorParametersConnectorParameters = None,
        worker_parameters: Dict[str, Any] = None,
    ):
        # The OSS file download URL.
        self.connector_package_url = connector_package_url
        # Parses the properties file in the current ZIP package.
        self.connector_parameters = connector_parameters
        # The instance configuration.
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
            temp_model = main_models.CreateEventStreamingRequestSinkSinkCustomizedKafkaConnectorParametersConnectorParameters()
            self.connector_parameters = temp_model.from_map(m.get('ConnectorParameters'))

        if m.get('WorkerParameters') is not None:
            self.worker_parameters = m.get('WorkerParameters')

        return self

class CreateEventStreamingRequestSinkSinkCustomizedKafkaConnectorParametersConnectorParameters(DaraModel):
    def __init__(
        self,
        config: Dict[str, Any] = None,
        name: str = None,
    ):
        # The connector configuration.
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

class CreateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParameters(DaraModel):
    def __init__(
        self,
        consume_timestamp: main_models.CreateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersConsumeTimestamp = None,
        group: main_models.CreateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersGroup = None,
        instance_endpoint: str = None,
        instance_password: str = None,
        instance_username: str = None,
        network_type: str = None,
        security_group_id: str = None,
        topic: main_models.CreateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersTopic = None,
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
            temp_model = main_models.CreateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersConsumeTimestamp()
            self.consume_timestamp = temp_model.from_map(m.get('ConsumeTimestamp'))

        if m.get('Group') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersGroup()
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
            temp_model = main_models.CreateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersTopic()
            self.topic = temp_model.from_map(m.get('Topic'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersTopic(DaraModel):
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

class CreateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersGroup(DaraModel):
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

class CreateEventStreamingRequestSinkSinkApacheRocketMQCheckpointParametersConsumeTimestamp(DaraModel):
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

class CreateEventStreamingRequestSinkSinkApacheKafkaParameters(DaraModel):
    def __init__(
        self,
        acks: str = None,
        bootstraps: str = None,
        compression_type: str = None,
        dynamic_topic: main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersDynamicTopic = None,
        headers: main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersHeaders = None,
        key: main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersKey = None,
        network_type: main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersNetworkType = None,
        sasl_mechanism: str = None,
        sasl_password: str = None,
        sasl_user: str = None,
        security_group_id: main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersSecurityGroupId = None,
        security_protocol: str = None,
        ssl_key_password: str = None,
        ssl_keystore_certificate_chain: str = None,
        ssl_keystore_key: main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersSslKeystoreKey = None,
        ssl_truststore_certificates: str = None,
        topic: str = None,
        v_switch_ids: main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersVSwitchIds = None,
        value: main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersValue = None,
        vpc_id: main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersVpcId = None,
    ):
        self.acks = acks
        # The initial endpoint of the Kafka cluster.
        self.bootstraps = bootstraps
        self.compression_type = compression_type
        # Specifies the target Topic routing strategy for messages. If both the Topic parameter and the DynamicTopic parameter are specified, the DynamicTopic parameter takes precedence. Two configuration modes are supported:
        #     1. **Static constant mode**: directly specify a fixed Topic name string (for example, "order_created"). All messages are sent to this Topic.
        #     2. **Dynamic extraction mode**: specify a standard JSONPath expression (for example, "$.user.id" or "$.metadata.category"). The system parses the upstream message body and extracts the matching field value as the target Topic name.
        self.dynamic_topic = dynamic_topic
        self.headers = headers
        self.key = key
        self.network_type = network_type
        self.sasl_mechanism = sasl_mechanism
        self.sasl_password = sasl_password
        self.sasl_user = sasl_user
        self.security_group_id = security_group_id
        self.security_protocol = security_protocol
        # [Required for encrypted private key] The Kafka client private key password. This parameter is required when the client private key is encrypted (the PEM file contains \\"Proc-Type: 4,ENCRYPTED\\" or \\"ENCRYPTED\\" markers). Leave this parameter empty if the private key is not encrypted. This password is used only to decrypt the private key and is unrelated to Kafka authentication.
        self.ssl_key_password = ssl_key_password
        # [Required for mutual authentication] The Kafka client certificate chain. This parameter is required when the Kafka server enables mutual SSL authentication (ssl.client.auth=required). Format: Base64-encoded PEM format, containing the client certificate and the complete certificate chain (client certificate first, intermediate CA certificate next, root CA certificate optional). Ensure that each PEM file content starts with \\"-----BEGIN CERTIFICATE-----\\" and ends with \\"-----END CERTIFICATE-----\\", then Base64-encode the concatenated content.
        self.ssl_keystore_certificate_chain = ssl_keystore_certificate_chain
        # [Required for bidirectional authentication] The SSL private key configuration object. When the Kafka server enables bidirectional SSL authentication, you must provide the client private key. Only KMS pattern is supported: specify the Key Management EPS resource that stores the private key by using KmsArn. The system retrieves the private key content from KMS only in memory, which provides higher security. Configuration example: {\\"KmsArn\\": \\"acs:kms:ap-southeast-1:123456789:secret/ssl-key-xxxx\\", \\"KmsSecretValueKey\\": \\"keystore_private_key\\"}
        self.ssl_keystore_key = ssl_keystore_key
        # [Required for SSL] The Kafka server trust certificate. Used to authenticate the validity of the Kafka Broker SSL certificate and prevent man-in-the-middle attacks. Format: Base64 encoding of PEM format, typically containing the CA certificate or the server certificate of the Kafka server. Example: Base64-encode the PEM file content of the CA certificate (ensure it starts with \\"-----BEGIN CERTIFICATE-----\\" and ends with \\"-----END CERTIFICATE-----\\"). If Kafka uses a self-signed certificate, provide the CA certificate that issued it.
        self.ssl_truststore_certificates = ssl_truststore_certificates
        self.topic = topic
        self.v_switch_ids = v_switch_ids
        self.value = value
        self.vpc_id = vpc_id

    def validate(self):
        if self.dynamic_topic:
            self.dynamic_topic.validate()
        if self.headers:
            self.headers.validate()
        if self.key:
            self.key.validate()
        if self.network_type:
            self.network_type.validate()
        if self.security_group_id:
            self.security_group_id.validate()
        if self.ssl_keystore_key:
            self.ssl_keystore_key.validate()
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

        if self.dynamic_topic is not None:
            result['DynamicTopic'] = self.dynamic_topic.to_map()

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

        if self.ssl_key_password is not None:
            result['SslKeyPassword'] = self.ssl_key_password

        if self.ssl_keystore_certificate_chain is not None:
            result['SslKeystoreCertificateChain'] = self.ssl_keystore_certificate_chain

        if self.ssl_keystore_key is not None:
            result['SslKeystoreKey'] = self.ssl_keystore_key.to_map()

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

        if m.get('DynamicTopic') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersDynamicTopic()
            self.dynamic_topic = temp_model.from_map(m.get('DynamicTopic'))

        if m.get('Headers') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('Key') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersKey()
            self.key = temp_model.from_map(m.get('Key'))

        if m.get('NetworkType') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersNetworkType()
            self.network_type = temp_model.from_map(m.get('NetworkType'))

        if m.get('SaslMechanism') is not None:
            self.sasl_mechanism = m.get('SaslMechanism')

        if m.get('SaslPassword') is not None:
            self.sasl_password = m.get('SaslPassword')

        if m.get('SaslUser') is not None:
            self.sasl_user = m.get('SaslUser')

        if m.get('SecurityGroupId') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersSecurityGroupId()
            self.security_group_id = temp_model.from_map(m.get('SecurityGroupId'))

        if m.get('SecurityProtocol') is not None:
            self.security_protocol = m.get('SecurityProtocol')

        if m.get('SslKeyPassword') is not None:
            self.ssl_key_password = m.get('SslKeyPassword')

        if m.get('SslKeystoreCertificateChain') is not None:
            self.ssl_keystore_certificate_chain = m.get('SslKeystoreCertificateChain')

        if m.get('SslKeystoreKey') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersSslKeystoreKey()
            self.ssl_keystore_key = temp_model.from_map(m.get('SslKeystoreKey'))

        if m.get('SslTruststoreCertificates') is not None:
            self.ssl_truststore_certificates = m.get('SslTruststoreCertificates')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        if m.get('Value') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersValue()
            self.value = temp_model.from_map(m.get('Value'))

        if m.get('VpcId') is not None:
            temp_model = main_models.CreateEventStreamingRequestSinkSinkApacheKafkaParametersVpcId()
            self.vpc_id = temp_model.from_map(m.get('VpcId'))

        return self

class CreateEventStreamingRequestSinkSinkApacheKafkaParametersVpcId(DaraModel):
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

class CreateEventStreamingRequestSinkSinkApacheKafkaParametersValue(DaraModel):
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

class CreateEventStreamingRequestSinkSinkApacheKafkaParametersVSwitchIds(DaraModel):
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

class CreateEventStreamingRequestSinkSinkApacheKafkaParametersSslKeystoreKey(DaraModel):
    def __init__(
        self,
        kms_arn: str = None,
        kms_secret_value_key: str = None,
    ):
        # [Required] The KMS resource ARN that stores the SSL private key. Used to locate the Key Management Service instance that stores the client private key. Format example: \\"acs:kms:cn-hangzhou:123456789:secret/ssl-keystore-key-xxxx\\". Obtain this value from the ARN information of the corresponding key in the KMS console.
        self.kms_arn = kms_arn
        # [KMS KV mode] The key name in the KMS secret. When the KMS secret is stored in a key-value (KV) structure, specify this parameter to indicate the key corresponding to the SSL private key. Example: if the KMS secret is \\"{"ssl_keystore_key":"-----BEGIN PRIVATE KEY-----...","ssl_truststore_key":"..."}\\", specify \\"ssl_keystore_key\\". Leave this parameter empty if the KMS secret is in plain text mode (directly stores the PEM content of the private key).
        self.kms_secret_value_key = kms_secret_value_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kms_arn is not None:
            result['KmsArn'] = self.kms_arn

        if self.kms_secret_value_key is not None:
            result['KmsSecretValueKey'] = self.kms_secret_value_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KmsArn') is not None:
            self.kms_arn = m.get('KmsArn')

        if m.get('KmsSecretValueKey') is not None:
            self.kms_secret_value_key = m.get('KmsSecretValueKey')

        return self

class CreateEventStreamingRequestSinkSinkApacheKafkaParametersSecurityGroupId(DaraModel):
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

class CreateEventStreamingRequestSinkSinkApacheKafkaParametersNetworkType(DaraModel):
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

class CreateEventStreamingRequestSinkSinkApacheKafkaParametersKey(DaraModel):
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

class CreateEventStreamingRequestSinkSinkApacheKafkaParametersHeaders(DaraModel):
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

class CreateEventStreamingRequestSinkSinkApacheKafkaParametersDynamicTopic(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation type.
        # CONSTANT: constant.
        # JSONPATH: extracts content from upstream based on a path.
        self.form = form
        # The template.
        self.template = template
        # The value.
        # [_single.params.Sink.props.SinkKafkaParameters.D
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEventStreamingRequestRunOptions(DaraModel):
    def __init__(
        self,
        batch_window: main_models.CreateEventStreamingRequestRunOptionsBatchWindow = None,
        business_option: main_models.CreateEventStreamingRequestRunOptionsBusinessOption = None,
        dead_letter_queue: main_models.CreateEventStreamingRequestRunOptionsDeadLetterQueue = None,
        errors_tolerance: str = None,
        maximum_tasks: int = None,
        retry_strategy: main_models.CreateEventStreamingRequestRunOptionsRetryStrategy = None,
        throttling: int = None,
    ):
        # The batch window.
        self.batch_window = batch_window
        self.business_option = business_option
        # Specifies whether to enable the dead-letter queue. By default, the dead-letter queue is disabled, and messages that exceed the retry policy are discarded.
        self.dead_letter_queue = dead_letter_queue
        # The exception tolerance policy. Valid values:
        # - NONE: No tolerance for exceptions.
        # - ALL: Tolerate all exceptions.
        self.errors_tolerance = errors_tolerance
        # The concurrency.
        self.maximum_tasks = maximum_tasks
        # The retry policy when event delivery fails.
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
            temp_model = main_models.CreateEventStreamingRequestRunOptionsBatchWindow()
            self.batch_window = temp_model.from_map(m.get('BatchWindow'))

        if m.get('BusinessOption') is not None:
            temp_model = main_models.CreateEventStreamingRequestRunOptionsBusinessOption()
            self.business_option = temp_model.from_map(m.get('BusinessOption'))

        if m.get('DeadLetterQueue') is not None:
            temp_model = main_models.CreateEventStreamingRequestRunOptionsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m.get('DeadLetterQueue'))

        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')

        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')

        if m.get('RetryStrategy') is not None:
            temp_model = main_models.CreateEventStreamingRequestRunOptionsRetryStrategy()
            self.retry_strategy = temp_model.from_map(m.get('RetryStrategy'))

        if m.get('Throttling') is not None:
            self.throttling = m.get('Throttling')

        return self

class CreateEventStreamingRequestRunOptionsRetryStrategy(DaraModel):
    def __init__(
        self,
        maximum_event_age_in_seconds: int = None,
        maximum_retry_attempts: int = None,
        push_retry_strategy: str = None,
    ):
        # The maximum retry time.
        self.maximum_event_age_in_seconds = maximum_event_age_in_seconds
        # The maximum number of retry attempts.
        self.maximum_retry_attempts = maximum_retry_attempts
        # The retry policy. Valid values:
        # - BACKOFF_RETRY: Backoff retry.
        # - EXPONENTIAL_DECAY_RETRY: Exponential decay retry.
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

class CreateEventStreamingRequestRunOptionsDeadLetterQueue(DaraModel):
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

class CreateEventStreamingRequestRunOptionsBusinessOption(DaraModel):
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

class CreateEventStreamingRequestRunOptionsBatchWindow(DaraModel):
    def __init__(
        self,
        count_based_window: int = None,
        time_based_window: int = None,
    ):
        # The maximum number of events that the window can contain. When this threshold is reached, the data in the window is pushed downstream. If multiple windows exist, a push is triggered when any window meets the threshold.
        self.count_based_window = count_based_window
        # The maximum time range (in seconds) of events that the window can contain. When this threshold is reached, the data in the window is pushed downstream. If multiple windows exist, a push is triggered when any window meets the threshold.
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

