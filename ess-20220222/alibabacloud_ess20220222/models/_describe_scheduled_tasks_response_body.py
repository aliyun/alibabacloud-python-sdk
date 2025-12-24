# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeScheduledTasksResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scheduled_tasks: List[main_models.DescribeScheduledTasksResponseBodyScheduledTasks] = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The information collection of the scheduled tasks.
        self.scheduled_tasks = scheduled_tasks
        # The total number of scheduled tasks.
        self.total_count = total_count

    def validate(self):
        if self.scheduled_tasks:
            for v1 in self.scheduled_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ScheduledTasks'] = []
        if self.scheduled_tasks is not None:
            for k1 in self.scheduled_tasks:
                result['ScheduledTasks'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scheduled_tasks = []
        if m.get('ScheduledTasks') is not None:
            for k1 in m.get('ScheduledTasks'):
                temp_model = main_models.DescribeScheduledTasksResponseBodyScheduledTasks()
                self.scheduled_tasks.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeScheduledTasksResponseBodyScheduledTasks(DaraModel):
    def __init__(
        self,
        description: str = None,
        desired_capacity: int = None,
        launch_expiration_time: int = None,
        launch_time: str = None,
        max_value: int = None,
        min_value: int = None,
        recurrence_end_time: str = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
        scaling_group_id: str = None,
        scheduled_action: str = None,
        scheduled_task_id: str = None,
        scheduled_task_name: str = None,
        task_enabled: bool = None,
    ):
        # The description of the scheduled task.
        self.description = description
        # The expected number of instances in the scaling group. If you set `Scaling Method` to `Configure Number of Instances in Scaling Group`, you can specify this parameter.
        self.desired_capacity = desired_capacity
        # The time window during which the scheduled task can be retried. Unit: seconds. Valid values: 0 to 21600.
        self.launch_expiration_time = launch_expiration_time
        # The point in time at which the scheduled task is triggered.
        self.launch_time = launch_time
        # The maximum number of instances that must be contained in the scaling group. If you set `Scaling Method` to `Configure Number of Instances in Scaling Group`, you can specify this parameter.
        self.max_value = max_value
        # The minimum number of instances that must be contained in the scaling group. If you set `Scaling Method` to `Configure Number of Instances in Scaling Group`, you can specify this parameter.
        self.min_value = min_value
        # The end time of the recurrence of the scheduled task.
        self.recurrence_end_time = recurrence_end_time
        # The recurring interval of the scheduled task.
        self.recurrence_type = recurrence_type
        # The frequency of recurrence of the scheduled task.
        self.recurrence_value = recurrence_value
        # The ID of the scaling group to which the scheduled task belongs.
        self.scaling_group_id = scaling_group_id
        # The scaling rule of the scheduled task. A value is returned for this parameter only after you specify ScheduledActions.
        self.scheduled_action = scheduled_action
        # The ID of the scheduled task.
        self.scheduled_task_id = scheduled_task_id
        # The name of the scheduled task.
        self.scheduled_task_name = scheduled_task_name
        # Indicates whether the scheduled task is enabled.
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

        if self.recurrence_end_time is not None:
            result['RecurrenceEndTime'] = self.recurrence_end_time

        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type

        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value

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

        if m.get('RecurrenceEndTime') is not None:
            self.recurrence_end_time = m.get('RecurrenceEndTime')

        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')

        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')

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

        return self

