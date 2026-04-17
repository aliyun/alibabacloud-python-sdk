# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMessageRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        instance_id: str = None,
        offset: str = None,
        partition: str = None,
        query_type: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        # The beginning of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        self.begin_time = begin_time
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The consumer offset of the partition.
        self.offset = offset
        # The partition ID.
        self.partition = partition
        # The query type. Valid values:
        # 
        # *   byOffset: queries messages by offset. If you select this value, you must configure Partition and Offset.
        # *   byTimestamp: queries messages by time. If you select this value, you must configure BeginTime.
        # 
        # This parameter is required.
        self.query_type = query_type
        # The ID of the region where the resource resides.
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
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.partition is not None:
            result['Partition'] = self.partition

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('Partition') is not None:
            self.partition = m.get('Partition')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

