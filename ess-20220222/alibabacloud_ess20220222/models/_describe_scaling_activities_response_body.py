# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeScalingActivitiesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scaling_activities: List[main_models.DescribeScalingActivitiesResponseBodyScalingActivities] = None,
        total_count: int = None,
    ):
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The collection of scaling activity information.
        self.scaling_activities = scaling_activities
        # The total number of scaling activity records.
        self.total_count = total_count

    def validate(self):
        if self.scaling_activities:
            for v1 in self.scaling_activities:
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

        result['ScalingActivities'] = []
        if self.scaling_activities is not None:
            for k1 in self.scaling_activities:
                result['ScalingActivities'].append(k1.to_map() if k1 else None)

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

        self.scaling_activities = []
        if m.get('ScalingActivities') is not None:
            for k1 in m.get('ScalingActivities'):
                temp_model = main_models.DescribeScalingActivitiesResponseBodyScalingActivities()
                self.scaling_activities.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeScalingActivitiesResponseBodyScalingActivities(DaraModel):
    def __init__(
        self,
        activity_metadata: str = None,
        attached_capacity: str = None,
        auto_created_capacity: str = None,
        cause: str = None,
        created_capacity: int = None,
        created_instances: List[str] = None,
        description: str = None,
        destroyed_capacity: int = None,
        destroyed_instances: List[str] = None,
        detail: str = None,
        end_time: str = None,
        error_code: str = None,
        error_message: str = None,
        error_messages: List[main_models.DescribeScalingActivitiesResponseBodyScalingActivitiesErrorMessages] = None,
        instance_refresh_task_id: str = None,
        lifecycle_hook_context: main_models.DescribeScalingActivitiesResponseBodyScalingActivitiesLifecycleHookContext = None,
        progress: int = None,
        scaling_activity_id: str = None,
        scaling_group_id: str = None,
        scaling_instance_number: int = None,
        start_time: str = None,
        started_capacity: int = None,
        started_instances: List[str] = None,
        status_code: str = None,
        status_message: str = None,
        stopped_capacity: int = None,
        stopped_instances: List[str] = None,
        total_capacity: str = None,
        trigger_source_id: str = None,
        trigger_source_type: str = None,
    ):
        # The metadata of the scaling activity.
        self.activity_metadata = activity_metadata
        # The total number of manually added instances in the scaling group after the scaling activity is completed.
        self.attached_capacity = attached_capacity
        # The total number of instances in the scaling group that are generated through automatic creation after you execute the scaling activity.
        self.auto_created_capacity = auto_created_capacity
        # The cause that triggered the scaling activity.
        self.cause = cause
        # The number of instances created during the current scaling activity.
        self.created_capacity = created_capacity
        # The list of instances created during the current scaling activity.
        self.created_instances = created_instances
        # The description of the scaling activity.
        self.description = description
        # The number of instances released during the current scaling activity.
        self.destroyed_capacity = destroyed_capacity
        # The list of instances released during the current scaling activity.
        self.destroyed_instances = destroyed_instances
        # The details of the scaling activity.
        self.detail = detail
        # The end time of the scaling activity. The time is displayed in UTC and follows the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format.
        self.end_time = end_time
        # The error code returned when the scaling activity fails.
        self.error_code = error_code
        # The error message returned when the scaling activity fails.
        self.error_message = error_message
        # The error messages returned when the scaling activity fails or is partially successful.
        self.error_messages = error_messages
        # The ID of the instance refresh task.
        self.instance_refresh_task_id = instance_refresh_task_id
        # The context information of the lifecycle hook.
        self.lifecycle_hook_context = lifecycle_hook_context
        # The progress of the scaling activity.
        self.progress = progress
        # The ID of the scaling activity.
        self.scaling_activity_id = scaling_activity_id
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # - If the scaling activity is a scale-out activity, this parameter indicates the number of instances that are created or started from the stopped and reclaimed state during the scaling activity.
        # 
        # - If the scaling activity is a scale-in activity, this parameter indicates the number of instances that are deleted or enter the stopped and reclaimed state during the scaling activity.
        self.scaling_instance_number = scaling_instance_number
        # The start time of the scaling activity. The time is displayed in UTC and follows the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format.
        self.start_time = start_time
        # The number of instances started from the economical mode during the current scaling activity.
        self.started_capacity = started_capacity
        # The list of instances started from the economical mode during the current scaling activity.
        self.started_instances = started_instances
        # The status of the scaling activity. Valid values:
        #  
        # - Successful: The scaling activity is successful. 
        # - Warning: The scaling activity is partially successful. 
        # - Failed: The scaling activity failed. 
        # - InProgress: The scaling activity is in progress. 
        # - Rejected: The request to execute the scaling activity is rejected.
        self.status_code = status_code
        # The status message of the scaling activity.
        self.status_message = status_message
        # The number of instances that entered the economical mode during the current scaling activity.
        self.stopped_capacity = stopped_capacity
        # The list of instances that entered the economical mode during the current scaling activity.
        self.stopped_instances = stopped_instances
        # The total number of instances in the scaling group after the scaling activity is completed.
        self.total_capacity = total_capacity
        # The ID of the trigger source for the scaling activity. Valid values:
        # - Cms trigger source ID: displayed as the event-triggered task ID.
        # - Api trigger source ID: displayed as the Alibaba Cloud account ID or RAM user ID.
        # - Ess trigger source ID: displayed as empty.
        self.trigger_source_id = trigger_source_id
        # The type of the trigger source for the scaling activity. Valid values:
        # - Cms: The scaling activity is triggered by an event-triggered task.
        # - Api: The scaling activity is triggered by a user through an API call.
        # - Ess: The scaling activity is triggered by a system task.
        self.trigger_source_type = trigger_source_type

    def validate(self):
        if self.error_messages:
            for v1 in self.error_messages:
                 if v1:
                    v1.validate()
        if self.lifecycle_hook_context:
            self.lifecycle_hook_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_metadata is not None:
            result['ActivityMetadata'] = self.activity_metadata

        if self.attached_capacity is not None:
            result['AttachedCapacity'] = self.attached_capacity

        if self.auto_created_capacity is not None:
            result['AutoCreatedCapacity'] = self.auto_created_capacity

        if self.cause is not None:
            result['Cause'] = self.cause

        if self.created_capacity is not None:
            result['CreatedCapacity'] = self.created_capacity

        if self.created_instances is not None:
            result['CreatedInstances'] = self.created_instances

        if self.description is not None:
            result['Description'] = self.description

        if self.destroyed_capacity is not None:
            result['DestroyedCapacity'] = self.destroyed_capacity

        if self.destroyed_instances is not None:
            result['DestroyedInstances'] = self.destroyed_instances

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        result['ErrorMessages'] = []
        if self.error_messages is not None:
            for k1 in self.error_messages:
                result['ErrorMessages'].append(k1.to_map() if k1 else None)

        if self.instance_refresh_task_id is not None:
            result['InstanceRefreshTaskId'] = self.instance_refresh_task_id

        if self.lifecycle_hook_context is not None:
            result['LifecycleHookContext'] = self.lifecycle_hook_context.to_map()

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.scaling_instance_number is not None:
            result['ScalingInstanceNumber'] = self.scaling_instance_number

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.started_capacity is not None:
            result['StartedCapacity'] = self.started_capacity

        if self.started_instances is not None:
            result['StartedInstances'] = self.started_instances

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        if self.stopped_capacity is not None:
            result['StoppedCapacity'] = self.stopped_capacity

        if self.stopped_instances is not None:
            result['StoppedInstances'] = self.stopped_instances

        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity

        if self.trigger_source_id is not None:
            result['TriggerSourceId'] = self.trigger_source_id

        if self.trigger_source_type is not None:
            result['TriggerSourceType'] = self.trigger_source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityMetadata') is not None:
            self.activity_metadata = m.get('ActivityMetadata')

        if m.get('AttachedCapacity') is not None:
            self.attached_capacity = m.get('AttachedCapacity')

        if m.get('AutoCreatedCapacity') is not None:
            self.auto_created_capacity = m.get('AutoCreatedCapacity')

        if m.get('Cause') is not None:
            self.cause = m.get('Cause')

        if m.get('CreatedCapacity') is not None:
            self.created_capacity = m.get('CreatedCapacity')

        if m.get('CreatedInstances') is not None:
            self.created_instances = m.get('CreatedInstances')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestroyedCapacity') is not None:
            self.destroyed_capacity = m.get('DestroyedCapacity')

        if m.get('DestroyedInstances') is not None:
            self.destroyed_instances = m.get('DestroyedInstances')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        self.error_messages = []
        if m.get('ErrorMessages') is not None:
            for k1 in m.get('ErrorMessages'):
                temp_model = main_models.DescribeScalingActivitiesResponseBodyScalingActivitiesErrorMessages()
                self.error_messages.append(temp_model.from_map(k1))

        if m.get('InstanceRefreshTaskId') is not None:
            self.instance_refresh_task_id = m.get('InstanceRefreshTaskId')

        if m.get('LifecycleHookContext') is not None:
            temp_model = main_models.DescribeScalingActivitiesResponseBodyScalingActivitiesLifecycleHookContext()
            self.lifecycle_hook_context = temp_model.from_map(m.get('LifecycleHookContext'))

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('ScalingInstanceNumber') is not None:
            self.scaling_instance_number = m.get('ScalingInstanceNumber')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StartedCapacity') is not None:
            self.started_capacity = m.get('StartedCapacity')

        if m.get('StartedInstances') is not None:
            self.started_instances = m.get('StartedInstances')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        if m.get('StoppedCapacity') is not None:
            self.stopped_capacity = m.get('StoppedCapacity')

        if m.get('StoppedInstances') is not None:
            self.stopped_instances = m.get('StoppedInstances')

        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')

        if m.get('TriggerSourceId') is not None:
            self.trigger_source_id = m.get('TriggerSourceId')

        if m.get('TriggerSourceType') is not None:
            self.trigger_source_type = m.get('TriggerSourceType')

        return self

class DescribeScalingActivitiesResponseBodyScalingActivitiesLifecycleHookContext(DaraModel):
    def __init__(
        self,
        disable_lifecycle_hook: bool = None,
        ignored_lifecycle_hook_ids: List[str] = None,
    ):
        # Specifies whether all lifecycle hooks are disabled for the scaling activity. Valid values:
        # 
        # - true: Disabled.
        # - false: Not disabled.
        self.disable_lifecycle_hook = disable_lifecycle_hook
        # The list of IDs of the lifecycle hooks disabled for the scaling activity.
        self.ignored_lifecycle_hook_ids = ignored_lifecycle_hook_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disable_lifecycle_hook is not None:
            result['DisableLifecycleHook'] = self.disable_lifecycle_hook

        if self.ignored_lifecycle_hook_ids is not None:
            result['IgnoredLifecycleHookIds'] = self.ignored_lifecycle_hook_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableLifecycleHook') is not None:
            self.disable_lifecycle_hook = m.get('DisableLifecycleHook')

        if m.get('IgnoredLifecycleHookIds') is not None:
            self.ignored_lifecycle_hook_ids = m.get('IgnoredLifecycleHookIds')

        return self

class DescribeScalingActivitiesResponseBodyScalingActivitiesErrorMessages(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        failed_instance_ids: List[str] = None,
        message: str = None,
    ):
        # The error code returned when the scaling activity fails or is partially successful.
        self.code = code
        # The exception description of the scaling activity.
        self.description = description
        # The list of failed instance ID.
        self.failed_instance_ids = failed_instance_ids
        # The error messages returned when the scaling activity fails or is partially successful.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.description is not None:
            result['Description'] = self.description

        if self.failed_instance_ids is not None:
            result['FailedInstanceIds'] = self.failed_instance_ids

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FailedInstanceIds') is not None:
            self.failed_instance_ids = m.get('FailedInstanceIds')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

