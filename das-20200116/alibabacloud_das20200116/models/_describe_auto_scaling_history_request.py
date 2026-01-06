# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAutoScalingHistoryRequest(DaraModel):
    def __init__(
        self,
        auto_scaling_task_type: str = None,
        end_time: int = None,
        instance_id: str = None,
        start_time: int = None,
    ):
        # The type of the auto scaling task that you want to query. Set the value to **SPEC**, which indicates that you can query the history of only automatic performance scaling tasks.
        # 
        # This parameter is required.
        self.auto_scaling_task_type = auto_scaling_task_type
        # The end of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > The end time must be later than the start time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The instance ID.
        # 
        # > Only ApsaraDB RDS for MySQL instances are supported.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The beginning of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > The maximum time range that can be specified is 45 days.
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
        if self.auto_scaling_task_type is not None:
            result['AutoScalingTaskType'] = self.auto_scaling_task_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoScalingTaskType') is not None:
            self.auto_scaling_task_type = m.get('AutoScalingTaskType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

