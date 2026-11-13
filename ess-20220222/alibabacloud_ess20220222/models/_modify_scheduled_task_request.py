# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class ModifyScheduledTaskRequest(DaraModel):
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
        resource_owner_id: int = None,
        scaling_group_id: str = None,
        scheduled_action: str = None,
        scheduled_task_id: str = None,
        scheduled_task_name: str = None,
        task_enabled: bool = None,
        warm_pool_capacity_options: main_models.ModifyScheduledTaskRequestWarmPoolCapacityOptions = None,
    ):
        # The description of the scheduled task. The description must be 2 to 200 characters in length.
        self.description = description
        # The expected number of instances in the scaling group. This parameter is available only when the scaling method of the scheduled task is set to specifying the number of instances in the scaling group.
        # > The scaling group must support setting the expected number of instances. Specifically, DesiredCapacity must be specified when the scaling group is created.
        self.desired_capacity = desired_capacity
        # The period of time during which Auto Scaling retries to execute the scheduled task after the trigger operation fails. Unit: seconds. Valid values: 0 to 1800.
        # 
        # Default value: 600.
        self.launch_expiration_time = launch_expiration_time
        # The time at which the scheduled task is executed. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mmZ format. The time must be in UTC. You cannot specify a time that is later than 90 days from the date of modification.
        # 
        # - If RecurrenceType is specified, the time specified by this parameter is the default time for recurring execution.
        # 
        # - If RecurrenceType is not specified, the task is executed only once at the specified date and time.
        self.launch_time = launch_time
        # The maximum number of instances in the scaling group. This parameter is available only when the scaling method of the scheduled task is set to specifying the number of instances in the scaling group.
        self.max_value = max_value
        # The minimum number of instances in the scaling group. This parameter is available only when the scaling method of the scheduled task is set to specifying the number of instances in the scaling group.
        self.min_value = min_value
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The end time of the scheduled task for recurring execution. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mmZ format. The time must be in UTC. You cannot specify a time that is later than 365 days from the date of modification.
        self.recurrence_end_time = recurrence_end_time
        # The recurrence type of the scheduled task. Valid values:
        #  
        # - Daily: The scheduled task is executed once every specified number of days.
        # - Weekly: The scheduled task is executed on specified days of each week.
        # - Monthly: The scheduled task is executed on specified days of each month.
        # - Cron: The scheduled task is executed based on the specified cron expression.
        # 
        # After modification, both RecurrenceType and RecurrenceValue must be valid.
        self.recurrence_type = recurrence_type
        # The recurrence value of the scheduled task.
        # 
        # - If RecurrenceType is set to Daily, only one value can be entered. Valid values: 1 to 31.
        # - If RecurrenceType is set to Weekly, multiple values can be entered and must be separated by commas (,). For example, the values for Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday are 0,1,2,3,4,5,6.
        # - If RecurrenceType is set to Monthly, the format is A-B. Valid values of A and B: 1 to 31. B must be greater than or equal to A.
        # - If RecurrenceType is set to Cron, the value represents UTC time and supports a five-field expression for minutes, hours, days, months, and weeks. Wildcards such as commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), L, and W are supported.
        # 
        # After modification, both RecurrenceType and RecurrenceValue must be valid.
        self.recurrence_value = recurrence_value
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the scaling group for which you want to modify the number of instances when the scheduled task is triggered. This parameter is available only when the scaling method is set to specifying the number of instances in the scaling group. After you specify ScalingGroupId, you must specify a value for at least one of the following parameters: MinValue, MaxValue, and DesiredCapacity.
        # 
        # > You cannot specify both ScheduledAction and ScalingGroupId at the same time.
        self.scaling_group_id = scaling_group_id
        # The unique identifier of the scaling rule. This parameter is available only when the scaling method is set to selecting an existing scaling rule. Select a created scaling rule and enter its unique identifier, which can be viewed on the scaling rule details page.
        # 
        # > You cannot specify both ScheduledAction and ScalingGroupId at the same time.
        self.scheduled_action = scheduled_action
        # The ID of the scheduled task.
        # 
        # This parameter is required.
        self.scheduled_task_id = scheduled_task_id
        # The name of the scheduled task. The name must be 2 to 64 characters in length and start with a letter, digit, or Chinese character. It can contain periods (.), underscores (_), and hyphens (-). The name must be unique within the same region and Alibaba Cloud account.
        self.scheduled_task_name = scheduled_task_name
        # Specifies whether to enable the scheduled task. Valid values:
        # 
        # - true: Enables the scheduled task.
        # - false: Disables the scheduled task.
        # 
        # Default value: true.
        self.task_enabled = task_enabled
        # The warm pool capacity configuration of the scaling group. This parameter is valid only when a warm pool is configured for the scaling group.
        self.warm_pool_capacity_options = warm_pool_capacity_options

    def validate(self):
        if self.warm_pool_capacity_options:
            self.warm_pool_capacity_options.validate()

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

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.scheduled_action is not None:
            result['ScheduledAction'] = self.scheduled_action

        if self.scheduled_task_id is not None:
            result['ScheduledTaskId'] = self.scheduled_task_id

        if self.scheduled_task_name is not None:
            result['ScheduledTaskName'] = self.scheduled_task_name

        if self.task_enabled is not None:
            result['TaskEnabled'] = self.task_enabled

        if self.warm_pool_capacity_options is not None:
            result['WarmPoolCapacityOptions'] = self.warm_pool_capacity_options.to_map()

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

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('ScheduledAction') is not None:
            self.scheduled_action = m.get('ScheduledAction')

        if m.get('ScheduledTaskId') is not None:
            self.scheduled_task_id = m.get('ScheduledTaskId')

        if m.get('ScheduledTaskName') is not None:
            self.scheduled_task_name = m.get('ScheduledTaskName')

        if m.get('TaskEnabled') is not None:
            self.task_enabled = m.get('TaskEnabled')

        if m.get('WarmPoolCapacityOptions') is not None:
            temp_model = main_models.ModifyScheduledTaskRequestWarmPoolCapacityOptions()
            self.warm_pool_capacity_options = temp_model.from_map(m.get('WarmPoolCapacityOptions'))

        return self

class ModifyScheduledTaskRequestWarmPoolCapacityOptions(DaraModel):
    def __init__(
        self,
        desired_group_prepared_capacity: int = None,
        min_capacity: int = None,
    ):
        # The expected number of warmed instances.
        self.desired_group_prepared_capacity = desired_group_prepared_capacity
        # The minimum number of instances in the warm pool.
        self.min_capacity = min_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desired_group_prepared_capacity is not None:
            result['DesiredGroupPreparedCapacity'] = self.desired_group_prepared_capacity

        if self.min_capacity is not None:
            result['MinCapacity'] = self.min_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesiredGroupPreparedCapacity') is not None:
            self.desired_group_prepared_capacity = m.get('DesiredGroupPreparedCapacity')

        if m.get('MinCapacity') is not None:
            self.min_capacity = m.get('MinCapacity')

        return self

