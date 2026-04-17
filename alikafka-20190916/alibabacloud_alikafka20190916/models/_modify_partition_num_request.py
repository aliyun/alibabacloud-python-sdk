# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPartitionNumRequest(DaraModel):
    def __init__(
        self,
        add_partition_num: int = None,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        # The number of partitions that you want to add to the topic.
        # 
        # *   The value must be an integer that is greater than 0.
        # *   To reduce the risk of data skew, we recommend that you set the value to a multiple of 6.
        # *   The number of total partitions ranges from 1 to 360.
        # 
        # This parameter is required.
        self.add_partition_num = add_partition_num
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The topic name.
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
        if self.add_partition_num is not None:
            result['AddPartitionNum'] = self.add_partition_num

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddPartitionNum') is not None:
            self.add_partition_num = m.get('AddPartitionNum')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

