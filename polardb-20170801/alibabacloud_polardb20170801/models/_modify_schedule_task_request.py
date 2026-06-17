# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyScheduleTaskRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        planned_end_time: str = None,
        planned_start_time: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: str = None,
    ):
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the details of all clusters in your account, including cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The latest time to start the scheduled task. The time is in the `YYYY-MM-DDThh:mm:ssZ` format. The time is displayed in UTC.
        # 
        # > - The latest start time must be at least 30 minutes later than the earliest start time.
        # 
        # - If you specify `PlannedStartTime` but not this parameter, the latest start time of the task is `PlannedStartTime + 30 minutes` by default. For example, if you set `PlannedStartTime` to `2021-01-14T09:00:00Z` and leave this parameter empty, the task will be executed no later than `2021-01-14T09:30:00Z`.
        # 
        # This parameter is required.
        self.planned_end_time = planned_end_time
        # The earliest time to start the scheduled task. The time is in the `YYYY-MM-DDThh:mm:ssZ` format. The time is displayed in UTC.
        # 
        # > - The start time can be any point in time within the next 24 hours. For example, if the current time is `2021-01-14T09:00:00Z`, you can set the start time to a value in the range of `2021-01-14T09:00:00Z` to `2021-01-15T09:00:00Z`.
        # 
        # - If you leave this parameter empty, the task is executed immediately.
        # 
        # This parameter is required.
        self.planned_start_time = planned_start_time
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The task ID.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time

        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')

        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

