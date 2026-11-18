# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHistoryTasksStatRequest(DaraModel):
    def __init__(
        self,
        from_exec_time: int = None,
        from_start_time: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        to_exec_time: int = None,
        to_start_time: str = None,
    ):
        # The minimum execution duration of a task. This parameter is used to filter tasks whose execution duration is greater than the specified value. Unit: seconds. Default value: 0. A value of 0 indicates that no limit is applied.
        self.from_exec_time = from_exec_time
        # The start time of the query period. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm</i>Z format (UTC).
        # 
        # This parameter is required.
        self.from_start_time = from_start_time
        # The instance ID.
        self.instance_id = instance_id
        # The ID of the region to which the pending events belong. You can call the DescribeRegions operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The task status. This parameter is used to filter tasks by status. Valid values:
        # - **Scheduled**: Pending execution.
        # - **Running**: Running.
        # - **Succeed**: Succeeded.
        # - **Failed**: Failed.
        # - **Cancelling**: Cancelling.
        # - **Canceled**: Canceled.
        # - **Waiting**: Waiting for the scheduled time.
        # Default value: empty. An empty value indicates that all statuses are selected. Separate multiple statuses with commas (,).
        self.status = status
        # The task ID. This parameter is used to query tasks with known IDs. Default value: empty. An empty value indicates that no limit is applied. Separate multiple task IDs with commas (,). You can specify up to 30 task IDs.
        self.task_id = task_id
        # The task type.
        self.task_type = task_type
        # The maximum execution duration of a task. This parameter is used to filter tasks whose execution duration is less than or equal to the specified value. Unit: seconds. Default value: 0. A value of 0 indicates that no limit is applied.
        self.to_exec_time = to_exec_time
        # The end time of the query period. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm</i>Z format (UTC).
        # 
        # This parameter is required.
        self.to_start_time = to_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_exec_time is not None:
            result['FromExecTime'] = self.from_exec_time

        if self.from_start_time is not None:
            result['FromStartTime'] = self.from_start_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.to_exec_time is not None:
            result['ToExecTime'] = self.to_exec_time

        if self.to_start_time is not None:
            result['ToStartTime'] = self.to_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromExecTime') is not None:
            self.from_exec_time = m.get('FromExecTime')

        if m.get('FromStartTime') is not None:
            self.from_start_time = m.get('FromStartTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('ToExecTime') is not None:
            self.to_exec_time = m.get('ToExecTime')

        if m.get('ToStartTime') is not None:
            self.to_start_time = m.get('ToStartTime')

        return self

