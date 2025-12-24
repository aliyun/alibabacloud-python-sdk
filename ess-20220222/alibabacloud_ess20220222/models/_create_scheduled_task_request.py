# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateScheduledTaskRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        desired_capacity: int = None,
        launch_expiration_time: int = None,
        launch_time: str = None,
        max_value: int = None,
        min_value: int = None,
        owner_account: str = None,
        owner_id: int = None,
        recurrence_end_time: str = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
        scheduled_action: str = None,
        scheduled_task_name: str = None,
        task_enabled: bool = None,
    ):
        # The description of the scheduled task. The description must be 2 to 200 characters in length.
        self.description = description
        # The expected number of instances in the scaling group if you specify the ScalingGroupId parameter.
        # 
        # > You must specify the `DesiredCapacity` parameter when you create a scaling group.
        self.desired_capacity = desired_capacity
        # The time period during which the failed scheduled task can be retried. Unit: seconds. Valid values: 0 to 1800.
        # 
        # Default value: 600.
        self.launch_expiration_time = launch_expiration_time
        # The point in time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard. The time must be in UTC. You cannot trigger a scheduled task more than 90 days after its creation.
        # 
        # *   If you specify `RecurrenceType`, the scheduled task is repeatedly triggered at the point in time that is specified by LaunchTime.
        # *   If you do not specify `RecurrenceType`, the scheduled task is triggered only once at the time point that is specified by LaunchTime.
        self.launch_time = launch_time
        # The maximum number of instances in the scaling group if you specify the ScalingGroupId parameter.
        self.max_value = max_value
        # The minimum number of instances in the scaling group if you specify the ScalingGroupId parameter.
        self.min_value = min_value
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The end time of the scheduled task. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mmZ format.
        # 
        # The time must be in UTC. You cannot enter a point in time that is later than 365 days from the point in time at which the scheduled task is created.
        self.recurrence_end_time = recurrence_end_time
        # The interval at which the scheduled task is repeated. Valid values:
        # 
        # *   Daily: The scheduled task is executed once every specified number of days.
        # *   Weekly: The scheduled task is executed on each specified day of the week.
        # *   Monthly: The scheduled task is executed on each specified day of the month.
        # *   Cron: The scheduled task is executed based on the specified cron expression.
        # 
        # You must specify the `RecurrenceType` and `RecurrenceValue` parameters at the same time.
        self.recurrence_type = recurrence_type
        # The number of recurrences of the scheduled task.
        # 
        # *   If you set the `RecurrenceType` parameter to `Daily`, you can specify only one value for this parameter. Valid values: 1 to 31.
        # *   If you set the `RecurrenceType` parameter to `Weekly`, you can specify multiple values for this parameter. Separate the values with commas (,). The values that correspond to Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday are 0, 1, 2, 3, 4, 5, and 6.``
        # *   If you set the `RecurrenceType` parameter to `Monthly`, you can specify two values in the `A-B` format for this parameter. Valid values of A and B: 1 to 31. B must be greater than or equal to A.
        # *   If you set the `RecurrenceType` parameter to `Cron`, you can specify a cron expression. A cron expression is written in UTC time and consists of the following fields: minute, hour, day, month, and week. The expression can contain the letters L and W and the following wildcard characters: commas (,), question marks (?), hyphens (-), asterisks (\\*), number signs (#), and forward slashes (/).
        # 
        # You must specify both the `RecurrenceType` parameter and the `RecurrenceValue` parameter.
        self.recurrence_value = recurrence_value
        # The region ID of the scheduled task.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group. If you specify this parameter, the number of instances in the scaling group will be changed when the scheduled task is triggered.
        # 
        # If you specify `ScalingGroupId`, you must also specify at least one of the following parameters: `MinValue`, `MaxValue`, and `DesiredCapacity`. You cannot specify `ScheduledAction` and `ScalingGroupId` at the same time.
        self.scaling_group_id = scaling_group_id
        # The scaling rule that you want to execute when the scheduled task is triggered. Specify the unique identifier of the scaling rule.
        # 
        # If you specify `ScheduledAction`, the scheduled task uses an existing scaling rule. You cannot specify `ScheduledAction` and `ScalingGroupId` at the same time.
        self.scheduled_action = scheduled_action
        # The name of the scheduled task. The name must be 2 to 64 characters in length, and can contain letters, digits, underscores (_), hyphens (-), and periods (.). The name must start with a letter or a digit. The name of the scheduled task must be unique in the region and within the Alibaba Cloud account.
        # 
        # If you do not specify this parameter, the value of the `ScheduledTaskId` parameter is used.
        self.scheduled_task_name = scheduled_task_name
        # Specifies whether to enable the scheduled task.
        # 
        # *   true
        # *   false
        # 
        # Default value: true.
        self.task_enabled = task_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.desired_capacity is not None:
            result['DesiredCapacity'] = self.desired_capacity

        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time

        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time

        if self.max_value is not None:
            result['MaxValue'] = self.max_value

        if self.min_value is not None:
            result['MinValue'] = self.min_value

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.recurrence_end_time is not None:
            result['RecurrenceEndTime'] = self.recurrence_end_time

        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type

        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.scheduled_action is not None:
            result['ScheduledAction'] = self.scheduled_action

        if self.scheduled_task_name is not None:
            result['ScheduledTaskName'] = self.scheduled_task_name

        if self.task_enabled is not None:
            result['TaskEnabled'] = self.task_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DesiredCapacity') is not None:
            self.desired_capacity = m.get('DesiredCapacity')

        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')

        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')

        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')

        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RecurrenceEndTime') is not None:
            self.recurrence_end_time = m.get('RecurrenceEndTime')

        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')

        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('ScheduledAction') is not None:
            self.scheduled_action = m.get('ScheduledAction')

        if m.get('ScheduledTaskName') is not None:
            self.scheduled_task_name = m.get('ScheduledTaskName')

        if m.get('TaskEnabled') is not None:
            self.task_enabled = m.get('TaskEnabled')

        return self

