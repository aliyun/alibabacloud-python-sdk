# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTopHotKeysRequest(DaraModel):
    def __init__(
        self,
        console_context: str = None,
        end_time: str = None,
        instance_id: str = None,
        node_id: str = None,
        start_time: str = None,
    ):
        # The reserved parameter.
        self.console_context = console_context
        # The end of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > 
        # 
        # *   The end time must be later than the start time.
        # 
        # *   Only data within the last four days can be queried.
        # 
        # *   The maximum interval between the **start time** and the** end time** is 3 hours.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the ApsaraDB for Redis instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the data shard on the ApsaraDB for Redis instance.
        self.node_id = node_id
        # The beginning of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

