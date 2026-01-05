# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task: main_models.GetTaskResponseBodyTask = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the task.
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task is not None:
            result['Task'] = self.task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Task') is not None:
            temp_model = main_models.GetTaskResponseBodyTask()
            self.task = temp_model.from_map(m.get('Task'))

        return self

class GetTaskResponseBodyTask(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        create_time: int = None,
        create_user: str = None,
        data_source: main_models.GetTaskResponseBodyTaskDataSource = None,
        dependencies: List[main_models.GetTaskResponseBodyTaskDependencies] = None,
        description: str = None,
        env_type: str = None,
        id: int = None,
        inputs: main_models.GetTaskResponseBodyTaskInputs = None,
        instance_mode: str = None,
        modify_time: int = None,
        modify_user: str = None,
        name: str = None,
        outputs: main_models.GetTaskResponseBodyTaskOutputs = None,
        owner: str = None,
        priority: int = None,
        project_env: str = None,
        project_id: int = None,
        rerun_interval: int = None,
        rerun_mode: str = None,
        rerun_times: int = None,
        runtime_resource: main_models.GetTaskResponseBodyTaskRuntimeResource = None,
        script: main_models.GetTaskResponseBodyTaskScript = None,
        sub_tasks: main_models.GetTaskResponseBodyTaskSubTasks = None,
        tags: List[main_models.GetTaskResponseBodyTaskTags] = None,
        timeout: int = None,
        trigger: main_models.GetTaskResponseBodyTaskTrigger = None,
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
        # The dependency information.
        self.dependencies = dependencies
        # The description of the task.
        self.description = description
        # The environment of the workspace. Valid values:
        # 
        # *   Prod: production environment
        # *   Dev: development environment
        self.env_type = env_type
        # The instance ID.
        self.id = id
        # The input information.
        self.inputs = inputs
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
        # The output information.
        self.outputs = outputs
        # The account ID of the task owner.
        self.owner = owner
        # The priority of the task. Valid values: 1 to 8. A larger value indicates a higher priority. Default value: 1.
        self.priority = priority
        # The environment of the workspace. This parameter is deprecated and replaced by the EnvType parameter. Valid values:
        # 
        # *   Prod: production environment
        # *   Dev: development environment
        self.project_env = project_env
        # The workspace ID.
        self.project_id = project_id
        # The rerun interval. Unit: seconds.
        self.rerun_interval = rerun_interval
        # The rerun mode. Valid values:
        # 
        # *   AllDenied: The task cannot be rerun regardless of whether the task is successfully run or fails to be run.
        # *   FailureAllowed: The task can be rerun only after it fails to be run.
        # *   AllAllowed: The task can be rerun regardless of whether the task is successfully run or fails to be run.
        self.rerun_mode = rerun_mode
        # The number of times that the task is rerun. This parameter takes effect only if the RerunMode parameter is set to AllAllowed or FailureAllowed.
        self.rerun_times = rerun_times
        # The configurations of the runtime environment, such as the resource group information.
        self.runtime_resource = runtime_resource
        # The script information.
        self.script = script
        # The configurations of the subtasks, such as a do-while node.
        self.sub_tasks = sub_tasks
        # The tags.
        self.tags = tags
        # The timeout period of task running. Unit: seconds.
        self.timeout = timeout
        # The method to trigger task scheduling.
        self.trigger = trigger
        # The type of the task.
        self.type = type
        # The workflow ID.
        self.workflow_id = workflow_id

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.dependencies:
            for v1 in self.dependencies:
                 if v1:
                    v1.validate()
        if self.inputs:
            self.inputs.validate()
        if self.outputs:
            self.outputs.validate()
        if self.runtime_resource:
            self.runtime_resource.validate()
        if self.script:
            self.script.validate()
        if self.sub_tasks:
            self.sub_tasks.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
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

        result['Dependencies'] = []
        if self.dependencies is not None:
            for k1 in self.dependencies:
                result['Dependencies'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.id is not None:
            result['Id'] = self.id

        if self.inputs is not None:
            result['Inputs'] = self.inputs.to_map()

        if self.instance_mode is not None:
            result['InstanceMode'] = self.instance_mode

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.name is not None:
            result['Name'] = self.name

        if self.outputs is not None:
            result['Outputs'] = self.outputs.to_map()

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

        if self.script is not None:
            result['Script'] = self.script.to_map()

        if self.sub_tasks is not None:
            result['SubTasks'] = self.sub_tasks.to_map()

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

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
            temp_model = main_models.GetTaskResponseBodyTaskDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        self.dependencies = []
        if m.get('Dependencies') is not None:
            for k1 in m.get('Dependencies'):
                temp_model = main_models.GetTaskResponseBodyTaskDependencies()
                self.dependencies.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Inputs') is not None:
            temp_model = main_models.GetTaskResponseBodyTaskInputs()
            self.inputs = temp_model.from_map(m.get('Inputs'))

        if m.get('InstanceMode') is not None:
            self.instance_mode = m.get('InstanceMode')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Outputs') is not None:
            temp_model = main_models.GetTaskResponseBodyTaskOutputs()
            self.outputs = temp_model.from_map(m.get('Outputs'))

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
            temp_model = main_models.GetTaskResponseBodyTaskRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('Script') is not None:
            temp_model = main_models.GetTaskResponseBodyTaskScript()
            self.script = temp_model.from_map(m.get('Script'))

        if m.get('SubTasks') is not None:
            temp_model = main_models.GetTaskResponseBodyTaskSubTasks()
            self.sub_tasks = temp_model.from_map(m.get('SubTasks'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetTaskResponseBodyTaskTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Trigger') is not None:
            temp_model = main_models.GetTaskResponseBodyTaskTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

class GetTaskResponseBodyTaskTrigger(DaraModel):
    def __init__(
        self,
        cron: str = None,
        end_time: str = None,
        recurrence: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The CRON expression of the task. This parameter takes effect only if the Type parameter is set to Scheduler.
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
        # The trigger type. Valid values:
        # 
        # *   Scheduler: periodic scheduling
        # *   Manual: manual scheduling
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

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetTaskResponseBodyTaskTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetTaskResponseBodyTaskSubTasks(DaraModel):
    def __init__(
        self,
        sub_tasks: List[main_models.GetTaskResponseBodyTaskSubTasksSubTasks] = None,
        type: str = None,
    ):
        # The subtasks.
        self.sub_tasks = sub_tasks
        # The type of the subtask. Valid values:
        # 
        # *   DoWhile: do-while node
        # *   Combined: node group
        # *   ForEach: for-each node
        self.type = type

    def validate(self):
        if self.sub_tasks:
            for v1 in self.sub_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SubTasks'] = []
        if self.sub_tasks is not None:
            for k1 in self.sub_tasks:
                result['SubTasks'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_tasks = []
        if m.get('SubTasks') is not None:
            for k1 in m.get('SubTasks'):
                temp_model = main_models.GetTaskResponseBodyTaskSubTasksSubTasks()
                self.sub_tasks.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetTaskResponseBodyTaskSubTasksSubTasks(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        create_time: int = None,
        create_user: str = None,
        data_source: main_models.GetTaskResponseBodyTaskSubTasksSubTasksDataSource = None,
        description: str = None,
        env_type: str = None,
        id: int = None,
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
        runtime_resource: main_models.GetTaskResponseBodyTaskSubTasksSubTasksRuntimeResource = None,
        timeout: int = None,
        trigger: main_models.GetTaskResponseBodyTaskSubTasksSubTasksTrigger = None,
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
        # *   Prod: production environment
        # *   Dev: development environment
        self.env_type = env_type
        # The task ID.
        self.id = id
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
        # The environment of the workspace. This parameter is deprecated and replaced by the EnvType parameter. Valid values:
        # 
        # *   Prod: production environment
        # *   Dev: development environment
        self.project_env = project_env
        # The workspace ID.
        self.project_id = project_id
        # The rerun interval. Unit: seconds.
        self.rerun_interval = rerun_interval
        # The rerun mode. Valid values:
        # 
        # *   AllDenied: The task cannot be rerun regardless of whether the task is successfully run or fails to be run.
        # *   FailureAllowed: The task can be rerun only after it fails to be run.
        # *   AllAllowed: The task can be rerun regardless of whether the task is successfully run or fails to be run.
        self.rerun_mode = rerun_mode
        # The number of times that the task is rerun. This parameter takes effect only if the RerunMode parameter is set to AllAllowed or FailureAllowed.
        self.rerun_times = rerun_times
        # The runtime environment configuration of the task, such as the resource group.
        self.runtime_resource = runtime_resource
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
            temp_model = main_models.GetTaskResponseBodyTaskSubTasksSubTasksDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

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
            temp_model = main_models.GetTaskResponseBodyTaskSubTasksSubTasksRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Trigger') is not None:
            temp_model = main_models.GetTaskResponseBodyTaskSubTasksSubTasksTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

class GetTaskResponseBodyTaskSubTasksSubTasksTrigger(DaraModel):
    def __init__(
        self,
        cron: str = None,
        end_time: str = None,
        recurrence: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The CRON expression of the task. This parameter takes effect only if the Type parameter is set to Scheduler.
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
        # The trigger type. Valid values:
        # 
        # *   Scheduler: periodic scheduling
        # *   Manual: manual scheduling
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

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetTaskResponseBodyTaskSubTasksSubTasksRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: str = None,
        image: str = None,
        resource_group_id: str = None,
    ):
        # The default number of CUs configured for task running.
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

class GetTaskResponseBodyTaskSubTasksSubTasksDataSource(DaraModel):
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

class GetTaskResponseBodyTaskScript(DaraModel):
    def __init__(
        self,
        content: str = None,
        parameters: str = None,
    ):
        # The script content.
        self.content = content
        # The script parameters.
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        return self

class GetTaskResponseBodyTaskRuntimeResource(DaraModel):
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

class GetTaskResponseBodyTaskOutputs(DaraModel):
    def __init__(
        self,
        task_outputs: List[main_models.GetTaskResponseBodyTaskOutputsTaskOutputs] = None,
        variables: List[main_models.GetTaskResponseBodyTaskOutputsVariables] = None,
    ):
        # The task outputs.
        self.task_outputs = task_outputs
        # The variables.
        self.variables = variables

    def validate(self):
        if self.task_outputs:
            for v1 in self.task_outputs:
                 if v1:
                    v1.validate()
        if self.variables:
            for v1 in self.variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TaskOutputs'] = []
        if self.task_outputs is not None:
            for k1 in self.task_outputs:
                result['TaskOutputs'].append(k1.to_map() if k1 else None)

        result['Variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['Variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_outputs = []
        if m.get('TaskOutputs') is not None:
            for k1 in m.get('TaskOutputs'):
                temp_model = main_models.GetTaskResponseBodyTaskOutputsTaskOutputs()
                self.task_outputs.append(temp_model.from_map(k1))

        self.variables = []
        if m.get('Variables') is not None:
            for k1 in m.get('Variables'):
                temp_model = main_models.GetTaskResponseBodyTaskOutputsVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class GetTaskResponseBodyTaskOutputsVariables(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # The name of the variable.
        self.name = name
        # The type. Valid values:
        # 
        # *   Constant: constant
        # *   PassThrough: node output
        # *   System: variable
        # *   NodeOutput: script output
        self.type = type
        # The value of the variable.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetTaskResponseBodyTaskOutputsTaskOutputs(DaraModel):
    def __init__(
        self,
        output: str = None,
    ):
        # The identifier of the output.
        self.output = output

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output is not None:
            result['Output'] = self.output

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            self.output = m.get('Output')

        return self

class GetTaskResponseBodyTaskInputs(DaraModel):
    def __init__(
        self,
        variables: List[main_models.GetTaskResponseBodyTaskInputsVariables] = None,
    ):
        # The variables.
        self.variables = variables

    def validate(self):
        if self.variables:
            for v1 in self.variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['Variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.variables = []
        if m.get('Variables') is not None:
            for k1 in m.get('Variables'):
                temp_model = main_models.GetTaskResponseBodyTaskInputsVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class GetTaskResponseBodyTaskInputsVariables(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # The name of the variable.
        self.name = name
        # The type. Valid values:
        # 
        # *   Constant: constant
        # *   PassThrough: node output
        # *   System: variable
        # *   NodeOutput: script output
        self.type = type
        # The value of the variable.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetTaskResponseBodyTaskDependencies(DaraModel):
    def __init__(
        self,
        type: str = None,
        upstream_output: str = None,
        upstream_task_id: str = None,
    ):
        # The dependency type. Valid values:
        # 
        # *   CrossCycleDependsOnChildren: cross-cycle dependency on level-1 descendant nodes
        # *   CrossCycleDependsOnSelf: cross-cycle dependency on the current node
        # *   CrossCycleDependsOnOtherNode: cross-cycle dependency on other nodes
        # *   Normal: same-cycle scheduling dependency
        self.type = type
        # The identifier of the output of the ancestor task. This parameter is returned only if `same-cycle scheduling dependencies` and the node input are configured.
        self.upstream_output = upstream_output
        # The ancestor task ID. This parameter is returned only if `cross-cycle scheduling dependencies` or `same-cycle scheduling dependencies` and the node input are not configured.
        self.upstream_task_id = upstream_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.upstream_output is not None:
            result['UpstreamOutput'] = self.upstream_output

        if self.upstream_task_id is not None:
            result['UpstreamTaskId'] = self.upstream_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpstreamOutput') is not None:
            self.upstream_output = m.get('UpstreamOutput')

        if m.get('UpstreamTaskId') is not None:
            self.upstream_task_id = m.get('UpstreamTaskId')

        return self

class GetTaskResponseBodyTaskDataSource(DaraModel):
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

