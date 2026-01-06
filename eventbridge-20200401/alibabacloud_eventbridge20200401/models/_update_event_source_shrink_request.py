# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEventSourceShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        event_bus_name: str = None,
        event_source_name: str = None,
        external_source_config_shrink: str = None,
        external_source_type: str = None,
        linked_external_source: bool = None,
        source_http_event_parameters_shrink: str = None,
        source_kafka_parameters_shrink: str = None,
        source_mnsparameters_shrink: str = None,
        source_ossevent_parameters_shrink: str = None,
        source_rabbit_mqparameters_shrink: str = None,
        source_rocket_mqparameters_shrink: str = None,
        source_slsparameters_shrink: str = None,
        source_scheduled_event_parameters_shrink: str = None,
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
        self.external_source_config_shrink = external_source_config_shrink
        # The type of the external data source.
        self.external_source_type = external_source_type
        # Specifies whether to connect to an external data source.
        self.linked_external_source = linked_external_source
        # The parameters that are configured if the event source is HTTP events.
        self.source_http_event_parameters_shrink = source_http_event_parameters_shrink
        # The parameters that are configured if the event source is Message Queue for Apache Kafka.
        self.source_kafka_parameters_shrink = source_kafka_parameters_shrink
        # The parameters that are configured if the event source is Message Service (MNS).
        self.source_mnsparameters_shrink = source_mnsparameters_shrink
        self.source_ossevent_parameters_shrink = source_ossevent_parameters_shrink
        # The parameters that are configured if the event source is Message Queue for RabbitMQ.
        self.source_rabbit_mqparameters_shrink = source_rabbit_mqparameters_shrink
        # The parameters that are configured if the event source is Message Queue for Apache RocketMQ.
        self.source_rocket_mqparameters_shrink = source_rocket_mqparameters_shrink
        # SourceSLSParameters
        self.source_slsparameters_shrink = source_slsparameters_shrink
        # The parameters that are configured if you specify scheduled events as the event source.
        self.source_scheduled_event_parameters_shrink = source_scheduled_event_parameters_shrink

    def validate(self):
        pass

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

        if self.external_source_config_shrink is not None:
            result['ExternalSourceConfig'] = self.external_source_config_shrink

        if self.external_source_type is not None:
            result['ExternalSourceType'] = self.external_source_type

        if self.linked_external_source is not None:
            result['LinkedExternalSource'] = self.linked_external_source

        if self.source_http_event_parameters_shrink is not None:
            result['SourceHttpEventParameters'] = self.source_http_event_parameters_shrink

        if self.source_kafka_parameters_shrink is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters_shrink

        if self.source_mnsparameters_shrink is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters_shrink

        if self.source_ossevent_parameters_shrink is not None:
            result['SourceOSSEventParameters'] = self.source_ossevent_parameters_shrink

        if self.source_rabbit_mqparameters_shrink is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters_shrink

        if self.source_rocket_mqparameters_shrink is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters_shrink

        if self.source_slsparameters_shrink is not None:
            result['SourceSLSParameters'] = self.source_slsparameters_shrink

        if self.source_scheduled_event_parameters_shrink is not None:
            result['SourceScheduledEventParameters'] = self.source_scheduled_event_parameters_shrink

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
            self.external_source_config_shrink = m.get('ExternalSourceConfig')

        if m.get('ExternalSourceType') is not None:
            self.external_source_type = m.get('ExternalSourceType')

        if m.get('LinkedExternalSource') is not None:
            self.linked_external_source = m.get('LinkedExternalSource')

        if m.get('SourceHttpEventParameters') is not None:
            self.source_http_event_parameters_shrink = m.get('SourceHttpEventParameters')

        if m.get('SourceKafkaParameters') is not None:
            self.source_kafka_parameters_shrink = m.get('SourceKafkaParameters')

        if m.get('SourceMNSParameters') is not None:
            self.source_mnsparameters_shrink = m.get('SourceMNSParameters')

        if m.get('SourceOSSEventParameters') is not None:
            self.source_ossevent_parameters_shrink = m.get('SourceOSSEventParameters')

        if m.get('SourceRabbitMQParameters') is not None:
            self.source_rabbit_mqparameters_shrink = m.get('SourceRabbitMQParameters')

        if m.get('SourceRocketMQParameters') is not None:
            self.source_rocket_mqparameters_shrink = m.get('SourceRocketMQParameters')

        if m.get('SourceSLSParameters') is not None:
            self.source_slsparameters_shrink = m.get('SourceSLSParameters')

        if m.get('SourceScheduledEventParameters') is not None:
            self.source_scheduled_event_parameters_shrink = m.get('SourceScheduledEventParameters')

        return self

