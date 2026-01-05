# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDownstreamTasksResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListDownstreamTasksResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListDownstreamTasksResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDownstreamTasksResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        downstream_tasks: List[main_models.ListDownstreamTasksResponseBodyPagingInfoDownstreamTasks] = None,
        page_number: int = None,
        page_size: int = None,
        tasks: List[main_models.ListDownstreamTasksResponseBodyPagingInfoTasks] = None,
        total_count: int = None,
    ):
        # The descendant tasks.
        self.downstream_tasks = downstream_tasks
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The tasks. This parameter is deprecated and replaced by the DownstreamTasks parameter.
        self.tasks = tasks
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.downstream_tasks:
            for v1 in self.downstream_tasks:
                 if v1:
                    v1.validate()
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DownstreamTasks'] = []
        if self.downstream_tasks is not None:
            for k1 in self.downstream_tasks:
                result['DownstreamTasks'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.downstream_tasks = []
        if m.get('DownstreamTasks') is not None:
            for k1 in m.get('DownstreamTasks'):
                temp_model = main_models.ListDownstreamTasksResponseBodyPagingInfoDownstreamTasks()
                self.downstream_tasks.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.ListDownstreamTasksResponseBodyPagingInfoTasks()
                self.tasks.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDownstreamTasksResponseBodyPagingInfoTasks(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        create_time: int = None,
        create_user: str = None,
        data_source: main_models.ListDownstreamTasksResponseBodyPagingInfoTasksDataSource = None,
        description: str = None,
        env_type: str = None,
        id: int = None,
        instance_mode: str = None,
        modify_time: int = None,
        modify_user: str = None,
        name: str = None,
        owner: str = None,
        priority: int = None,
        project_env: str = None,
        project_id: int = None,
        rerun_interval: int = None,
        rerun_mode: str = None,
        rerun_times: int = None,
        runtime_resource: main_models.ListDownstreamTasksResponseBodyPagingInfoTasksRuntimeResource = None,
        step_type: str = None,
        timeout: int = None,
        trigger: main_models.ListDownstreamTasksResponseBodyPagingInfoTasksTrigger = None,
        type: str = None,
        workflow_id: int = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The creation time.
        self.create_time = create_time
        # The account ID of the creator.
        self.create_user = create_user
        # The information about the associated data source.
        self.data_source = data_source
        # The description of the task.
        self.description = description
        # The environment of the workspace. Valid values:
        # 
        # *   Prod
        # *   Dev
        self.env_type = env_type
        # The task ID.
        self.id = id
        # The instance generation mode. Valid values:
        # 
        # *   T+1
        # *   Immediately
        self.instance_mode = instance_mode
        # The modification time.
        self.modify_time = modify_time
        # The account ID of the modifier.
        self.modify_user = modify_user
        # The name of the task.
        self.name = name
        # The account ID of the task owner.
        self.owner = owner
        # The priority of the task. Valid values: 1 to 8. A larger value indicates a higher priority. Default value: 1.
        self.priority = priority
        # The environment of the workspace. This parameter is deprecated and replaced by the EnvType parameter.
        # 
        # Valid values:
        # 
        # *   Prod
        # *   Dev
        self.project_env = project_env
        # The workspace ID.
        self.project_id = project_id
        # The rerun interval. Unit: seconds.
        self.rerun_interval = rerun_interval
        # The rerun mode.
        # 
        # Valid values:
        # 
        # *   AllDenied: The task cannot be rerun regardless of whether it is successfully run or fails to run.
        # *   FailureAllowed: The task can be rerun only after it fails to run.
        # *   AllAllowed: The task can be rerun regardless of whether it is successfully run or fails to run.
        self.rerun_mode = rerun_mode
        # The number of times that the task is rerun. This parameter takes effect only if the RerunMode parameter is set to AllAllowed or FailureAllowed.
        self.rerun_times = rerun_times
        # The configurations of the runtime environment, such as the resource group information.
        self.runtime_resource = runtime_resource
        # The scheduling dependency type. Valid values:
        # 
        # *   Normal: same-cycle scheduling dependency
        # *   CrossCycle: cross-cycle scheduling dependency
        self.step_type = step_type
        # The timeout period of task running. Unit: seconds.
        self.timeout = timeout
        # The method to trigger task scheduling.
        self.trigger = trigger
        # The type of the task.
        self.type = type
        # The ID of the workflow to which the task belongs.
        self.workflow_id = workflow_id

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.runtime_resource:
            self.runtime_resource.validate()
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_mode is not None:
            result['InstanceMode'] = self.instance_mode

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.rerun_interval is not None:
            result['RerunInterval'] = self.rerun_interval

        if self.rerun_mode is not None:
            result['RerunMode'] = self.rerun_mode

        if self.rerun_times is not None:
            result['RerunTimes'] = self.rerun_times

        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource.to_map()

        if self.step_type is not None:
            result['StepType'] = self.step_type

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()

        if self.type is not None:
            result['Type'] = self.type

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('DataSource') is not None:
            temp_model = main_models.ListDownstreamTasksResponseBodyPagingInfoTasksDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceMode') is not None:
            self.instance_mode = m.get('InstanceMode')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RerunInterval') is not None:
            self.rerun_interval = m.get('RerunInterval')

        if m.get('RerunMode') is not None:
            self.rerun_mode = m.get('RerunMode')

        if m.get('RerunTimes') is not None:
            self.rerun_times = m.get('RerunTimes')

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.ListDownstreamTasksResponseBodyPagingInfoTasksRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('StepType') is not None:
            self.step_type = m.get('StepType')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Trigger') is not None:
            temp_model = main_models.ListDownstreamTasksResponseBodyPagingInfoTasksTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

class ListDownstreamTasksResponseBodyPagingInfoTasksTrigger(DaraModel):
    def __init__(
        self,
        cron: str = None,
        end_time: str = None,
        recurrence: str = None,
        start_time: str = None,
        timezone: str = None,
        type: str = None,
    ):
        # The CRON expression of the task. This parameter takes effect only if the Type parameter is set to Scheduler.
        self.cron = cron
        # The end time of the time range during which the task is periodically scheduled. This parameter takes effect only if the Type parameter is set to Scheduler.
        self.end_time = end_time
        # The running mode of the task after it is triggered. This parameter takes effect only if the Type parameter is set to Scheduler.
        # 
        # Valid values:
        # 
        # *   Pause
        # *   Skip
        # *   Normal
        self.recurrence = recurrence
        # The start time of the time range during which the task is periodically scheduled. This parameter takes effect only if the Type parameter is set to Scheduler.
        self.start_time = start_time
        # The time zone.
        self.timezone = timezone
        # The trigger type.
        # 
        # Valid values:
        # 
        # *   Scheduler: scheduling cycle-based trigger
        # *   Manual: manual trigger
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron is not None:
            result['Cron'] = self.cron

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.recurrence is not None:
            result['Recurrence'] = self.recurrence

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cron') is not None:
            self.cron = m.get('Cron')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Recurrence') is not None:
            self.recurrence = m.get('Recurrence')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListDownstreamTasksResponseBodyPagingInfoTasksRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: str = None,
        image: str = None,
        resource_group_id: str = None,
    ):
        # The default number of compute units (CUs) configured for task running.
        self.cu = cu
        # The ID of the image configured for task running.
        self.image = image
        # The ID of the resource group for scheduling configured for task running.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['Cu'] = self.cu

        if self.image is not None:
            result['Image'] = self.image

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

class ListDownstreamTasksResponseBodyPagingInfoTasksDataSource(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the data source.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListDownstreamTasksResponseBodyPagingInfoDownstreamTasks(DaraModel):
    def __init__(
        self,
        dependency_type: str = None,
        task: main_models.ListDownstreamTasksResponseBodyPagingInfoDownstreamTasksTask = None,
    ):
        # The scheduling dependency type. Valid values:
        # 
        # *   Normal: same-cycle scheduling dependency
        # *   CrossCycle: cross-cycle scheduling dependency
        self.dependency_type = dependency_type
        # The information about the task.
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dependency_type is not None:
            result['DependencyType'] = self.dependency_type

        if self.task is not None:
            result['Task'] = self.task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DependencyType') is not None:
            self.dependency_type = m.get('DependencyType')

        if m.get('Task') is not None:
            temp_model = main_models.ListDownstreamTasksResponseBodyPagingInfoDownstreamTasksTask()
            self.task = temp_model.from_map(m.get('Task'))

        return self

class ListDownstreamTasksResponseBodyPagingInfoDownstreamTasksTask(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        create_time: int = None,
        create_user: str = None,
        data_source: main_models.ListDownstreamTasksResponseBodyPagingInfoDownstreamTasksTaskDataSource = None,
        description: str = None,
        env_type: str = None,
        id: int = None,
        instance_mode: str = None,
        modify_time: int = None,
        modify_user: str = None,
        name: str = None,
        owner: str = None,
        priority: int = None,
        project_id: int = None,
        rerun_interval: int = None,
        rerun_mode: str = None,
        rerun_times: int = None,
        runtime_resource: main_models.ListDownstreamTasksResponseBodyPagingInfoDownstreamTasksTaskRuntimeResource = None,
        timeout: int = None,
        trigger: main_models.ListDownstreamTasksResponseBodyPagingInfoDownstreamTasksTaskTrigger = None,
        type: str = None,
        workflow_id: int = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The creation time.
        self.create_time = create_time
        # The account ID of the creator.
        self.create_user = create_user
        # The information about the associated data source.
        self.data_source = data_source
        # The description.
        self.description = description
        # The environment of the workspace. Valid values:
        # 
        # *   Prod
        # *   Dev
        self.env_type = env_type
        # The task ID.
        self.id = id
        # The instance generation mode. Valid values:
        # 
        # *   T+1
        # *   Immediately
        self.instance_mode = instance_mode
        # The modification time.
        self.modify_time = modify_time
        # The account ID of the modifier.
        self.modify_user = modify_user
        # The name of the task.
        self.name = name
        # The account ID of the task owner.
        self.owner = owner
        # The priority of the task. Valid values: 1 to 8.
        self.priority = priority
        # The workspace ID.
        self.project_id = project_id
        # The rerun interval. Unit: seconds.
        self.rerun_interval = rerun_interval
        # The rerun mode. Valid values:
        # 
        # *   AllDenied: The task cannot be rerun regardless of whether the task is successfully run or fails to run.
        # *   FailureAllowed: The task can be rerun only after it fails to run.
        # *   AllAllowed: The task can be rerun regardless of whether it is successfully run or fails to run.
        self.rerun_mode = rerun_mode
        # The number of times that the task is rerun. This parameter takes effect only if the RerunMode parameter is set to AllAllowed or FailureAllowed.
        self.rerun_times = rerun_times
        # The configurations of the runtime environment, such as the resource group information.
        self.runtime_resource = runtime_resource
        # The timeout period of task running. Unit: seconds.
        self.timeout = timeout
        # The trigger method.
        self.trigger = trigger
        # The type of the task.
        self.type = type
        # The ID of the workflow to which the task belongs.
        self.workflow_id = workflow_id

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.runtime_resource:
            self.runtime_resource.validate()
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_mode is not None:
            result['InstanceMode'] = self.instance_mode

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.rerun_interval is not None:
            result['RerunInterval'] = self.rerun_interval

        if self.rerun_mode is not None:
            result['RerunMode'] = self.rerun_mode

        if self.rerun_times is not None:
            result['RerunTimes'] = self.rerun_times

        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource.to_map()

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()

        if self.type is not None:
            result['Type'] = self.type

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('DataSource') is not None:
            temp_model = main_models.ListDownstreamTasksResponseBodyPagingInfoDownstreamTasksTaskDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceMode') is not None:
            self.instance_mode = m.get('InstanceMode')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RerunInterval') is not None:
            self.rerun_interval = m.get('RerunInterval')

        if m.get('RerunMode') is not None:
            self.rerun_mode = m.get('RerunMode')

        if m.get('RerunTimes') is not None:
            self.rerun_times = m.get('RerunTimes')

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.ListDownstreamTasksResponseBodyPagingInfoDownstreamTasksTaskRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Trigger') is not None:
            temp_model = main_models.ListDownstreamTasksResponseBodyPagingInfoDownstreamTasksTaskTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

class ListDownstreamTasksResponseBodyPagingInfoDownstreamTasksTaskTrigger(DaraModel):
    def __init__(
        self,
        cron: str = None,
        end_time: str = None,
        recurrence: str = None,
        start_time: str = None,
        timezone: str = None,
        type: str = None,
    ):
        # The CRON expression. This parameter takes effect only if the Type parameter is set to Scheduler.
        self.cron = cron
        # The end time of the time range during which the task is periodically scheduled. This parameter takes effect only if the Type parameter is set to Scheduler.
        self.end_time = end_time
        # The running mode of the task after it is triggered. This parameter takes effect only if the Type parameter is set to Scheduler. Valid values:
        # 
        # *   Pause
        # *   Skip
        # *   Normal
        self.recurrence = recurrence
        # The start time of the time range during which the task is periodically scheduled. This parameter takes effect only if the Type parameter is set to Scheduler.
        self.start_time = start_time
        # The time zone.
        self.timezone = timezone
        # The trigger type. Valid values:
        # 
        # *   Scheduler: scheduling cycle-based trigger
        # *   Manual: manual trigger
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron is not None:
            result['Cron'] = self.cron

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.recurrence is not None:
            result['Recurrence'] = self.recurrence

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cron') is not None:
            self.cron = m.get('Cron')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Recurrence') is not None:
            self.recurrence = m.get('Recurrence')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListDownstreamTasksResponseBodyPagingInfoDownstreamTasksTaskRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: str = None,
        image: str = None,
        resource_group_id: str = None,
    ):
        # The default number of compute units (CUs) configured for task running.
        self.cu = cu
        # The ID of the image configured for task running.
        self.image = image
        # The ID of the resource group for scheduling configured for task running.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['Cu'] = self.cu

        if self.image is not None:
            result['Image'] = self.image

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

class ListDownstreamTasksResponseBodyPagingInfoDownstreamTasksTaskDataSource(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the data source.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

