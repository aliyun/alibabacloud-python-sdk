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
        # The name of the consumer group.
        # 
        # *   The name can contain letters, digits, hyphens (-), and underscores (_).
        # *   The name must be **3 to 64** characters in length. If a name contains more than **64** characters, the name is automatically truncated.
        # *   The name of a consumer group cannot be changed after the consumer group is created.
        # 
        # This parameter is required.
        self.consumer_id = consumer_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # If you set resetType to offset, you can use this parameter to reset the consumer offset of each partition of a specific topic in the consumer group.
        self.offsets_shrink = offsets_shrink
        # The region ID of the instance to which the consumer group belongs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The method that is used to reset the consumer offsets of the subscribed topics of a consumer group. Valid values:
        # 
        # *   **timestamp** (default)
        # *   **offset**
        self.reset_type = reset_type
        # The point in time when message consumption starts. The value of this parameter is a UNIX timestamp in milliseconds. The value of this parameter must be **less than 0** or **within the retention period of the consumer offset**. This parameter takes effect only if you set resetType to timestamp.
        # 
        # *   If you want to reset the consumer offset to the latest offset, set this parameter to -1.
        # *   If you want to reset the consumer offset to the earliest offset, set this parameter to -2.
        self.time = time
        # The topic name.
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must be **3 to 64** characters in length. If a name contains more than **64** characters, the name is automatically truncated.
        # *   The name of a topic cannot be changed after the topic is created.
        # 
        # **If you want to reset the consumer offsets of all topics to which the consumer subscribes, specify an empty string.**
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

