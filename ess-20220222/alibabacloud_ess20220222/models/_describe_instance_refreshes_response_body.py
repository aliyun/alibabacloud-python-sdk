# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceRefreshesResponseBody(DaraModel):
    def __init__(
        self,
        instance_refresh_tasks: List[main_models.DescribeInstanceRefreshesResponseBodyInstanceRefreshTasks] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The instance refresh tasks.
        self.instance_refresh_tasks = instance_refresh_tasks
        # The maximum number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of instance refresh tasks.
        self.total_count = total_count

    def validate(self):
        if self.instance_refresh_tasks:
            for v1 in self.instance_refresh_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceRefreshTasks'] = []
        if self.instance_refresh_tasks is not None:
            for k1 in self.instance_refresh_tasks:
                result['InstanceRefreshTasks'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_refresh_tasks = []
        if m.get('InstanceRefreshTasks') is not None:
            for k1 in m.get('InstanceRefreshTasks'):
                temp_model = main_models.DescribeInstanceRefreshesResponseBodyInstanceRefreshTasks()
                self.instance_refresh_tasks.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstanceRefreshesResponseBodyInstanceRefreshTasks(DaraModel):
    def __init__(
        self,
        checkpoint_pause_time: int = None,
        checkpoints: List[main_models.DescribeInstanceRefreshesResponseBodyInstanceRefreshTasksCheckpoints] = None,
        desired_configuration: main_models.DescribeInstanceRefreshesResponseBodyInstanceRefreshTasksDesiredConfiguration = None,
        detail: str = None,
        end_time: str = None,
        finished_update_capacity: int = None,
        instance_refresh_task_id: str = None,
        max_healthy_percentage: int = None,
        min_healthy_percentage: int = None,
        region_id: str = None,
        scaling_group_id: str = None,
        skip_matching: bool = None,
        start_time: str = None,
        status: str = None,
        total_need_update_capacity: int = None,
    ):
        self.checkpoint_pause_time = checkpoint_pause_time
        self.checkpoints = checkpoints
        # The desired configurations of the instance refresh task.
        self.desired_configuration = desired_configuration
        # The reason why the instance refresh task failed to be executed.
        self.detail = detail
        # The end time of the instance refresh task.
        self.end_time = end_time
        # The refreshed number of instances in the scaling group.
        self.finished_update_capacity = finished_update_capacity
        # The ID of the instance refresh task.
        self.instance_refresh_task_id = instance_refresh_task_id
        # The ratio by which the number of instances in the scaling group can exceed the upper limit for the number of instances in the scaling group during instance refresh.
        self.max_healthy_percentage = max_healthy_percentage
        # The ratio of the number of instances that provide services to the total number of instances in the scaling group during instance refresh.
        self.min_healthy_percentage = min_healthy_percentage
        # The region ID of the scaling group.
        self.region_id = region_id
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # Indicates whether instances that match the desired scaling configuration are skipped.
        # 
        # >  The system determines the match based on the ID of the desired scaling configuration rather than individual configuration items.
        # 
        # Valid values:
        # 
        # *   true: Instances that match the desired scaling configuration are skipped. When you initiate an instance refresh task, the system checks the configurations of all instances. The refresh operation is skipped for instances created based on the desired scaling configuration.
        # *   false: Instances that match the desired scaling configuration are not skipped. When an instance refresh task is initiated, all instances in the scaling group at the time of initiation are refreshed.
        self.skip_matching = skip_matching
        # The start time of the instance refresh task.
        self.start_time = start_time
        # The status of the instance refresh task. Valid values:
        # 
        # *   Pending: The instance refresh task is created and is waiting to be scheduled.
        # *   InProgress: The instance refresh task is being executed.
        # *   Paused: The instance refresh task is suspended.
        # *   Failed: The instance refresh task failed to be executed.
        # *   Successful: The instance refresh task is successful.
        # *   Cancelling: The instance refresh task is being canceled.
        # *   Cancelled: The instance refresh task is canceled.
        # *   RollbackInProgress: The instance refresh task is being rolled back.
        # *   RollbackSuccessful: The instance refresh task is rolled back.
        # *   RollbackFailed: The instance refresh task fails to be rolled back.
        self.status = status
        # The total number of instances whose configurations are refreshed.
        self.total_need_update_capacity = total_need_update_capacity

    def validate(self):
        if self.checkpoints:
            for v1 in self.checkpoints:
                 if v1:
                    v1.validate()
        if self.desired_configuration:
            self.desired_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checkpoint_pause_time is not None:
            result['CheckpointPauseTime'] = self.checkpoint_pause_time

        result['Checkpoints'] = []
        if self.checkpoints is not None:
            for k1 in self.checkpoints:
                result['Checkpoints'].append(k1.to_map() if k1 else None)

        if self.desired_configuration is not None:
            result['DesiredConfiguration'] = self.desired_configuration.to_map()

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.finished_update_capacity is not None:
            result['FinishedUpdateCapacity'] = self.finished_update_capacity

        if self.instance_refresh_task_id is not None:
            result['InstanceRefreshTaskId'] = self.instance_refresh_task_id

        if self.max_healthy_percentage is not None:
            result['MaxHealthyPercentage'] = self.max_healthy_percentage

        if self.min_healthy_percentage is not None:
            result['MinHealthyPercentage'] = self.min_healthy_percentage

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.skip_matching is not None:
            result['SkipMatching'] = self.skip_matching

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.total_need_update_capacity is not None:
            result['TotalNeedUpdateCapacity'] = self.total_need_update_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckpointPauseTime') is not None:
            self.checkpoint_pause_time = m.get('CheckpointPauseTime')

        self.checkpoints = []
        if m.get('Checkpoints') is not None:
            for k1 in m.get('Checkpoints'):
                temp_model = main_models.DescribeInstanceRefreshesResponseBodyInstanceRefreshTasksCheckpoints()
                self.checkpoints.append(temp_model.from_map(k1))

        if m.get('DesiredConfiguration') is not None:
            temp_model = main_models.DescribeInstanceRefreshesResponseBodyInstanceRefreshTasksDesiredConfiguration()
            self.desired_configuration = temp_model.from_map(m.get('DesiredConfiguration'))

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FinishedUpdateCapacity') is not None:
            self.finished_update_capacity = m.get('FinishedUpdateCapacity')

        if m.get('InstanceRefreshTaskId') is not None:
            self.instance_refresh_task_id = m.get('InstanceRefreshTaskId')

        if m.get('MaxHealthyPercentage') is not None:
            self.max_healthy_percentage = m.get('MaxHealthyPercentage')

        if m.get('MinHealthyPercentage') is not None:
            self.min_healthy_percentage = m.get('MinHealthyPercentage')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('SkipMatching') is not None:
            self.skip_matching = m.get('SkipMatching')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalNeedUpdateCapacity') is not None:
            self.total_need_update_capacity = m.get('TotalNeedUpdateCapacity')

        return self

class DescribeInstanceRefreshesResponseBodyInstanceRefreshTasksDesiredConfiguration(DaraModel):
    def __init__(
        self,
        containers: List[main_models.DescribeInstanceRefreshesResponseBodyInstanceRefreshTasksDesiredConfigurationContainers] = None,
        image_id: str = None,
        launch_template_id: str = None,
        launch_template_overrides: List[main_models.DescribeInstanceRefreshesResponseBodyInstanceRefreshTasksDesiredConfigurationLaunchTemplateOverrides] = None,
        launch_template_version: str = None,
        scaling_configuration_id: str = None,
    ):
        self.containers = containers
        # The ID of the image file that provides the image resource for Auto Scaling to create instances.
        self.image_id = image_id
        self.launch_template_id = launch_template_id
        self.launch_template_overrides = launch_template_overrides
        self.launch_template_version = launch_template_version
        # The ID of the scaling configuration.
        self.scaling_configuration_id = scaling_configuration_id

    def validate(self):
        if self.containers:
            for v1 in self.containers:
                 if v1:
                    v1.validate()
        if self.launch_template_overrides:
            for v1 in self.launch_template_overrides:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Containers'] = []
        if self.containers is not None:
            for k1 in self.containers:
                result['Containers'].append(k1.to_map() if k1 else None)

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        result['LaunchTemplateOverrides'] = []
        if self.launch_template_overrides is not None:
            for k1 in self.launch_template_overrides:
                result['LaunchTemplateOverrides'].append(k1.to_map() if k1 else None)

        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version

        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.containers = []
        if m.get('Containers') is not None:
            for k1 in m.get('Containers'):
                temp_model = main_models.DescribeInstanceRefreshesResponseBodyInstanceRefreshTasksDesiredConfigurationContainers()
                self.containers.append(temp_model.from_map(k1))

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        self.launch_template_overrides = []
        if m.get('LaunchTemplateOverrides') is not None:
            for k1 in m.get('LaunchTemplateOverrides'):
                temp_model = main_models.DescribeInstanceRefreshesResponseBodyInstanceRefreshTasksDesiredConfigurationLaunchTemplateOverrides()
                self.launch_template_overrides.append(temp_model.from_map(k1))

        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')

        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')

        return self

class DescribeInstanceRefreshesResponseBodyInstanceRefreshTasksDesiredConfigurationLaunchTemplateOverrides(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        return self

class DescribeInstanceRefreshesResponseBodyInstanceRefreshTasksDesiredConfigurationContainers(DaraModel):
    def __init__(
        self,
        args: List[str] = None,
        commands: List[str] = None,
        environment_vars: List[main_models.DescribeInstanceRefreshesResponseBodyInstanceRefreshTasksDesiredConfigurationContainersEnvironmentVars] = None,
        image: str = None,
        name: str = None,
    ):
        self.args = args
        self.commands = commands
        self.environment_vars = environment_vars
        self.image = image
        self.name = name

    def validate(self):
        if self.environment_vars:
            for v1 in self.environment_vars:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['Args'] = self.args

        if self.commands is not None:
            result['Commands'] = self.commands

        result['EnvironmentVars'] = []
        if self.environment_vars is not None:
            for k1 in self.environment_vars:
                result['EnvironmentVars'].append(k1.to_map() if k1 else None)

        if self.image is not None:
            result['Image'] = self.image

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Commands') is not None:
            self.commands = m.get('Commands')

        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k1 in m.get('EnvironmentVars'):
                temp_model = main_models.DescribeInstanceRefreshesResponseBodyInstanceRefreshTasksDesiredConfigurationContainersEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k1))

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeInstanceRefreshesResponseBodyInstanceRefreshTasksDesiredConfigurationContainersEnvironmentVars(DaraModel):
    def __init__(
        self,
        field_ref_field_path: str = None,
        key: str = None,
        value: str = None,
    ):
        self.field_ref_field_path = field_ref_field_path
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_ref_field_path is not None:
            result['FieldRefFieldPath'] = self.field_ref_field_path

        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRefFieldPath') is not None:
            self.field_ref_field_path = m.get('FieldRefFieldPath')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeInstanceRefreshesResponseBodyInstanceRefreshTasksCheckpoints(DaraModel):
    def __init__(
        self,
        percentage: int = None,
    ):
        self.percentage = percentage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.percentage is not None:
            result['Percentage'] = self.percentage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        return self

