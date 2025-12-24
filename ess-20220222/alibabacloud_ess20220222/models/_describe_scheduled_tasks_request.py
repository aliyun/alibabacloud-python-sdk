# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeScheduledTasksRequest(DaraModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
        scheduled_actions: List[str] = None,
        scheduled_task_ids: List[str] = None,
        scheduled_task_names: List[str] = None,
        task_enabled: bool = None,
        task_name: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The interval at which scheduled task N is repeatedly executed. Valid values:
        # 
        # *   Daily: Scheduled task N is executed once every specified number of days.
        # *   Weekly: Scheduled task N is executed on each specified day of a week.
        # *   Monthly: Scheduled task N is executed on each specified day of a month.
        # *   Cron: Scheduled task N is executed based on the specified Cron expression.
        self.recurrence_type = recurrence_type
        # The number of times scheduled task N is repeatedly executed.
        # 
        # You can specify this parameter only if you set RecurrenceType to Weekly. Separate multiple values with commas (,). The values that correspond to Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday are 0, 1, 2, 3, 4, 5, and 6.
        self.recurrence_value = recurrence_value
        # The region ID of the scaling group to which the scheduled task belongs.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the scaling group to which the scheduled task belongs.
        self.scaling_group_id = scaling_group_id
        # The scaling rules of the scheduled tasks. Once the scheduled tasks are triggered, the scaling rules are executed.
        self.scheduled_actions = scheduled_actions
        # The IDs of the scheduled tasks that you want to query.
        self.scheduled_task_ids = scheduled_task_ids
        # The names of the scheduled tasks that you want to query.
        self.scheduled_task_names = scheduled_task_names
        # Specifies whether scheduled task N is enabled.
        # 
        # *   true
        # *   false
        self.task_enabled = task_enabled
        # The name of scheduled task N. Fuzzy search based on keywords is supported.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type

        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.scheduled_actions is not None:
            result['ScheduledActions'] = self.scheduled_actions

        if self.scheduled_task_ids is not None:
            result['ScheduledTaskIds'] = self.scheduled_task_ids

        if self.scheduled_task_names is not None:
            result['ScheduledTaskNames'] = self.scheduled_task_names

        if self.task_enabled is not None:
            result['TaskEnabled'] = self.task_enabled

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')

        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('ScheduledActions') is not None:
            self.scheduled_actions = m.get('ScheduledActions')

        if m.get('ScheduledTaskIds') is not None:
            self.scheduled_task_ids = m.get('ScheduledTaskIds')

        if m.get('ScheduledTaskNames') is not None:
            self.scheduled_task_names = m.get('ScheduledTaskNames')

        if m.get('TaskEnabled') is not None:
            self.task_enabled = m.get('TaskEnabled')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

