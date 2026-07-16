# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class UpdateConsumerOffsetRequest(DaraModel):
    def __init__(
        self,
        consumer_id: str = None,
        instance_id: str = None,
        offsets: List[main_models.UpdateConsumerOffsetRequestOffsets] = None,
        region_id: str = None,
        reset_type: str = None,
        time: str = None,
        topic: str = None,
    ):
        # Consumer Group name.
        # 
        # - Can only contain letters, numbers, hyphens (-), and underscores (_).
        # 
        # - Length must be **3-64** characters. If more than **64** characters are provided, they will be automatically truncated.
        # 
        # - Cannot be modified once created.
        # 
        # This parameter is required.
        self.consumer_id = consumer_id
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # When resetType is offset, this parameter is used to set the consumer offset for each partition of a topic for the consumer group.
        self.offsets = offsets
        # Region ID of the instance to which the Group belongs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Type of consumer group offset reset, supporting the following two types:
        # 
        # - **timestamp** (default)
        # 
        # - **offset**
        self.reset_type = reset_type
        # Time parameter in Unix timestamp format, in milliseconds.
        # The parameter range should be **less than 0** or **within the retention period of the consumer offset**. This parameter only takes effect when resetType is timestamp.
        # 
        # - To reset to the latest consumer offset, pass -1.
        # 
        # - To reset to the earliest consumer offset, pass -2.
        self.time = time
        # Topic name.
        # 
        # - Can only contain letters, numbers, underscores (_), and hyphens (-).
        # 
        # - Length must be **3-64** characters. If more than **64** characters are provided, they will be automatically truncated.
        # 
        # - Cannot be modified once created.
        # 
        # **To set the consumer offset for all topics subscribed by the current consumer, pass an empty string.**
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        if self.offsets:
            for v1 in self.offsets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['Offsets'] = []
        if self.offsets is not None:
            for k1 in self.offsets:
                result['Offsets'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reset_type is not None:
            result['ResetType'] = self.reset_type

        if self.time is not None:
            result['Time'] = self.time

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.offsets = []
        if m.get('Offsets') is not None:
            for k1 in m.get('Offsets'):
                temp_model = main_models.UpdateConsumerOffsetRequestOffsets()
                self.offsets.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class UpdateConsumerOffsetRequestOffsets(DaraModel):
    def __init__(
        self,
        offset: int = None,
        partition: int = None,
    ):
        # Partition offset.
        self.offset = offset
        # Partition ID.
        self.partition = partition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.offset is not None:
            result['Offset'] = self.offset

        if self.partition is not None:
            result['Partition'] = self.partition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('Partition') is not None:
            self.partition = m.get('Partition')

        return self

