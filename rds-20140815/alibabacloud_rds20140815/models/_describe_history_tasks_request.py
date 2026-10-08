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
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        to_exec_time: int = None,
        to_start_time: str = None,
    ):
        # The minimum execution duration used to filter tasks. Only tasks whose execution duration is greater than this value are returned. Unit: seconds. Default value: 0, which indicates no restriction.
        self.from_exec_time = from_exec_time
        # The beginning of the time range to query based on task start time. Only tasks that started after this time are returned. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC+0. The earliest supported time is 30 days before the current time. If a time earlier than 30 days is specified, it is automatically converted to 30 days before the current time.
        # 
        # This parameter is required.
        self.from_start_time = from_start_time
        # The instance ID. Separate multiple instance IDs with commas (,). A maximum of 30 instance IDs are supported. Default value: empty, which indicates no restriction.
        self.instance_id = instance_id
        # Currently, only Instance is supported.
        self.instance_type = instance_type
        self.owner_id = owner_id
        # The page number. Valid values: positive integers.
        # Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **10 to 100**. Default value: **10**.
        self.page_size = page_size
        # The region ID of the pending event. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The task status. Valid values:
        # - **Scheduled**: Waiting to be executed.
        # - **Running**: Running.
        # - **Succeed**: Succeeded.
        # - **Failed**: Failed.
        # - **Cancelling**: Being terminated.
        # - **Canceled**: Terminated.
        # - **Waiting**: Waiting for the scheduled time.
        # 
        # To query multiple statuses, separate them with commas (,). Default value: empty, which indicates all statuses.
        self.status = status
        # The task ID. You can call the DescribeTasks operation to obtain the task ID. Separate multiple task IDs with commas (,). A maximum of 30 task IDs are supported. Default value: empty, which indicates no restriction.
        self.task_id = task_id
        # The task type. Separate multiple task types with commas (,). A maximum of 30 task types are supported. Default value: empty, which indicates no restriction.
        self.task_type = task_type
        # The maximum execution duration used to filter tasks. Only tasks whose execution duration is not less than this value are returned. Unit: seconds. Default value: 0, which indicates no restriction.
        self.to_exec_time = to_exec_time
        # The end of the time range to query based on task start time. Only tasks that started before this time are returned. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC+0.
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

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

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

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

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

