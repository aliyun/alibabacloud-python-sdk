# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateConsumerOffsetShrinkRequest(DaraModel):
    def __init__(
        self,
        consumer_id: str = None,
        instance_id: str = None,
        offsets_shrink: str = None,
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
        self.offsets_shrink = offsets_shrink
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
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.offsets_shrink is not None:
            result['Offsets'] = self.offsets_shrink

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

        if m.get('Offsets') is not None:
            self.offsets_shrink = m.get('Offsets')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

