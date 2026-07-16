# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableAutoTopicCreationRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        operate: str = None,
        partition_num: int = None,
        region_id: str = None,
        update_partition: bool = None,
    ):
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Currently only these three request parameters are supported:
        # 
        # - enable: Enable automatic topic creation.
        # 
        # - disable: Disable automatic topic creation.
        # 
        # - updatePartition: Modify the number of partitions for automatic creation.
        self.operate = operate
        # Adjust the default number of partitions for automatically created topics.
        # 
        # > This value is passed only when the Operate value is updatePartition, or when UpdatePartition is true.
        self.partition_num = partition_num
        # Region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Modify the number of partitions for automatic creation.
        # 
        # > If this parameter is set to true, the Operate parameter must be updatePartition or left empty.
        self.update_partition = update_partition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.operate is not None:
            result['Operate'] = self.operate

        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.update_partition is not None:
            result['UpdatePartition'] = self.update_partition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Operate') is not None:
            self.operate = m.get('Operate')

        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UpdatePartition') is not None:
            self.update_partition = m.get('UpdatePartition')

        return self

