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
        # The type of elastic scaling task to query. Currently, only **SPEC** is supported, which indicates querying the automatic performance scaling history.
        # 
        # This parameter is required.
        self.auto_scaling_task_type = auto_scaling_task_type
        # The end time of the query task. Specify the value as a UNIX timestamp. Unit: milliseconds.
        # > The end time must be later than the start time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The instance ID.
        # 
        # > Currently, only ApsaraDB RDS for MySQL instances are supported.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The start time of the query task. Specify the value as a UNIX timestamp. Unit: milliseconds.
        # 
        # > The start time cannot be earlier than 45 days before the current time.
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

