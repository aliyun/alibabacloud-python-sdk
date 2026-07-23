# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class DeleteEventAnalysisJobRequest(DaraModel):
    def __init__(
        self,
        source_resource: main_models.DeleteEventAnalysisJobRequestSourceResource = None,
    ):
        # The identifier of the source resource.
        # 
        # This parameter is required.
        self.source_resource = source_resource

    def validate(self):
        if self.source_resource:
            self.source_resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_resource is not None:
            result['SourceResource'] = self.source_resource.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceResource') is not None:
            temp_model = main_models.DeleteEventAnalysisJobRequestSourceResource()
            self.source_resource = temp_model.from_map(m.get('SourceResource'))

        return self

class DeleteEventAnalysisJobRequestSourceResource(DaraModel):
    def __init__(
        self,
        kafka: main_models.DeleteEventAnalysisJobRequestSourceResourceKafka = None,
        rocket_mq: main_models.DeleteEventAnalysisJobRequestSourceResourceRocketMQ = None,
    ):
        # The Kafka data source.
        self.kafka = kafka
        # The RocketMQ data source.
        self.rocket_mq = rocket_mq

    def validate(self):
        if self.kafka:
            self.kafka.validate()
        if self.rocket_mq:
            self.rocket_mq.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kafka is not None:
            result['Kafka'] = self.kafka.to_map()

        if self.rocket_mq is not None:
            result['RocketMQ'] = self.rocket_mq.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Kafka') is not None:
            temp_model = main_models.DeleteEventAnalysisJobRequestSourceResourceKafka()
            self.kafka = temp_model.from_map(m.get('Kafka'))

        if m.get('RocketMQ') is not None:
            temp_model = main_models.DeleteEventAnalysisJobRequestSourceResourceRocketMQ()
            self.rocket_mq = temp_model.from_map(m.get('RocketMQ'))

        return self

class DeleteEventAnalysisJobRequestSourceResourceRocketMQ(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        # The instance ID of the RocketMQ instance.
        self.instance_id = instance_id
        # The type of the RocketMQ instance.
        self.instance_type = instance_type
        # The region of the RocketMQ instance.
        self.region_id = region_id
        # The name of the RocketMQ topic.
        self.topic = topic

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

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class DeleteEventAnalysisJobRequestSourceResourceKafka(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        # The instance ID of the Kafka instance.
        self.instance_id = instance_id
        # The region of the Kafka instance.
        self.region_id = region_id
        # The name of the Kafka topic.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

