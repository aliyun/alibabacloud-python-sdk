# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDeadlockHistogramRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        node_id: str = None,
        start_time: int = None,
        status: str = None,
    ):
        # The end of the time range to query. The format is a UNIX timestamp in milliseconds.
        # >Notice: The value is of the Long type. Precision loss may occur during the serialization/deserialization procedure. The value must not be greater than 9007199254740991.</notice>
        # 
        # This parameter is required.
        self.end_time = end_time
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The node ID.
        # 
        # > For PolarDB for MySQL instances, you must specify the node ID.
        self.node_id = node_id
        # The beginning of the time range to query. The format is a UNIX timestamp in milliseconds.
        # 
        # > The start time can be at most 7 days earlier than the end time.
        # 
        # >Notice: The value is of the Long type. Precision loss may occur during the serialization/deserialization procedure. The value must not be greater than 9007199254740991.</notice>
        # 
        # This parameter is required.
        self.start_time = start_time
        # The analysis status of the task.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

