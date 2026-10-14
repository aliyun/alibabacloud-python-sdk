# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHistoryTasksRequest(DaraModel):
    def __init__(
        self,
        from_exec_time: int = None,
        from_start_time: str = None,
        instance_id: str = None,
        instance_type: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        to_exec_time: int = None,
        to_start_time: str = None,
    ):
        # The minimum execution duration of the task. This parameter is used to filter tasks whose execution duration is greater than this value. Unit: seconds. Default value: 0, which indicates no limit.
        self.from_exec_time = from_exec_time
        # The start time of the time range to query task start times. Tasks that start after this time are queried. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. The earliest supported time is 30 days ago. If the specified time is more than 30 days before the current time, it is automatically changed to 30 days ago.
        # 
        # This parameter is required.
        self.from_start_time = from_start_time
        # The cluster ID. You can specify multiple cluster IDs separated by commas (,). You can specify up to 30 cluster IDs. If this parameter is left empty, historical tasks of all clusters in the region are queried by default.
        self.instance_id = instance_id
        # The instance type. Set the value to Instance.
        self.instance_type = instance_type
        # The page number of the query result. Valid values: positive integers. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 10 to 100. Default value: 10.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The task status. Valid values:
        # 
        # - **Scheduled**: Pending execution.
        # 
        # - **Running**: Running.
        # 
        # - **Succeed**: Succeeded.
        # 
        # - **Failed**: Failed.
        # 
        # - **Cancelling**: Being canceled.
        # 
        # - **Canceled**: Canceled.
        # 
        # - **Waiting**: Waiting for the scheduled time.
        # 
        # You can specify multiple values separated by commas (,). If this parameter is left empty, all statuses are queried by default.
        self.status = status
        # The task ID. You can specify multiple task IDs separated by commas (,). You can specify up to 30 task IDs. If this parameter is left empty, historical tasks of all clusters are queried by default.
        self.task_id = task_id
        # The task type. This parameter is used to query tasks of a specific type. You can specify multiple task types separated by commas (,). You can specify up to 30 task types. If this parameter is left empty, no limit is applied.
        self.task_type = task_type
        # The maximum execution duration of the task. This parameter is used to filter tasks whose execution duration does not exceed this value. Unit: seconds. Default value: 0, which indicates no limit.
        self.to_exec_time = to_exec_time
        # The end time of the time range to query task start times. Tasks that start before this time are queried. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
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

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

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

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

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

