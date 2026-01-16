# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class EventSourceParameters(DaraModel):
    def __init__(
        self,
        source_dtsparameters: main_models.SourceDTSParameters = None,
        source_kafka_parameters: main_models.SourceKafkaParameters = None,
        source_mnsparameters: main_models.SourceMNSParameters = None,
        source_mqttparameters: main_models.SourceMQTTParameters = None,
        source_rabbit_mqparameters: main_models.SourceRabbitMQParameters = None,
        source_rocket_mqparameters: main_models.SourceRocketMQParameters = None,
    ):
        self.source_dtsparameters = source_dtsparameters
        self.source_kafka_parameters = source_kafka_parameters
        self.source_mnsparameters = source_mnsparameters
        self.source_mqttparameters = source_mqttparameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        self.source_rocket_mqparameters = source_rocket_mqparameters

    def validate(self):
        if self.source_dtsparameters:
            self.source_dtsparameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_mqttparameters:
            self.source_mqttparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_dtsparameters is not None:
            result['sourceDTSParameters'] = self.source_dtsparameters.to_map()

        if self.source_kafka_parameters is not None:
            result['sourceKafkaParameters'] = self.source_kafka_parameters.to_map()

        if self.source_mnsparameters is not None:
            result['sourceMNSParameters'] = self.source_mnsparameters.to_map()

        if self.source_mqttparameters is not None:
            result['sourceMQTTParameters'] = self.source_mqttparameters.to_map()

        if self.source_rabbit_mqparameters is not None:
            result['sourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()

        if self.source_rocket_mqparameters is not None:
            result['sourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceDTSParameters') is not None:
            temp_model = main_models.SourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m.get('sourceDTSParameters'))

        if m.get('sourceKafkaParameters') is not None:
            temp_model = main_models.SourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m.get('sourceKafkaParameters'))

        if m.get('sourceMNSParameters') is not None:
            temp_model = main_models.SourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m.get('sourceMNSParameters'))

        if m.get('sourceMQTTParameters') is not None:
            temp_model = main_models.SourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m.get('sourceMQTTParameters'))

        if m.get('sourceRabbitMQParameters') is not None:
            temp_model = main_models.SourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m.get('sourceRabbitMQParameters'))

        if m.get('sourceRocketMQParameters') is not None:
            temp_model = main_models.SourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m.get('sourceRocketMQParameters'))

        return self

