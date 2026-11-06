# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetWorkflowResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        workflow: main_models.GetWorkflowResponseBodyWorkflow = None,
    ):
        # The ID of the request. You can use the ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # The details of the workflow.
        self.workflow = workflow

    def validate(self):
        if self.workflow:
            self.workflow.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.workflow is not None:
            result['Workflow'] = self.workflow.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Workflow') is not None:
            temp_model = main_models.GetWorkflowResponseBodyWorkflow()
            self.workflow = temp_model.from_map(m.get('Workflow'))

        return self

class GetWorkflowResponseBodyWorkflow(DaraModel):
    def __init__(
        self,
        client_unique_code: str = None,
        create_time: int = None,
        create_user: str = None,
        dependencies: List[main_models.GetWorkflowResponseBodyWorkflowDependencies] = None,
        description: str = None,
        env_type: str = None,
        id: int = None,
        modify_time: int = None,
        modify_user: str = None,
        name: str = None,
        outputs: main_models.GetWorkflowResponseBodyWorkflowOutputs = None,
        owner: str = None,
        parameters: str = None,
        project_id: int = None,
        tags: List[main_models.GetWorkflowResponseBodyWorkflowTags] = None,
        tasks: List[main_models.GetWorkflowResponseBodyWorkflowTasks] = None,
        trigger: main_models.GetWorkflowResponseBodyWorkflowTrigger = None,
    ):
        # The client unique code of the workflow, which is used to implement asynchronous and idempotent operations. If you do not specify this parameter when creating the workflow, the system automatically generates a code and uniquely binds it to the resource ID. If you specify this parameter when updating or deleting the resource, it must be the same as the client unique code used during creation.
        self.client_unique_code = client_unique_code
        # The creation time.
        # 
        # The value is a 13-digit number, such as `1710239005403`.
        self.create_time = create_time
        # The account ID of the user who created the workflow.
        self.create_user = create_user
        # The dependency information.
        self.dependencies = dependencies
        # The description.
        self.description = description
        # The project environment. Valid values:
        # - Prod: Production environment.
        # - Dev: Development environment.
        self.env_type = env_type
        # The unique identifier of the workflow.
        self.id = id
        # The update time.
        # 
        # The value is a 13-digit number, such as `1710239005403`.
        self.modify_time = modify_time
        # The account ID of the user who updated the workflow.
        self.modify_user = modify_user
        # The name.
        self.name = name
        # The output information.
        self.outputs = outputs
        # The account ID of the owner.
        self.owner = owner
        # The list of parameters.
        self.parameters = parameters
        # The ID of the project.
        self.project_id = project_id
        # The list of tags.
        self.tags = tags
        # The list of tasks.
        self.tasks = tasks
        # The trigger configuration.
        self.trigger = trigger

    def validate(self):
        if self.dependencies:
            for v1 in self.dependencies:
                 if v1:
                    v1.validate()
        if self.outputs:
            self.outputs.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_unique_code is not None:
            result['ClientUniqueCode'] = self.client_unique_code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

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

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientUniqueCode') is not None:
            self.client_unique_code = m.get('ClientUniqueCode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        self.dependencies = []
        if m.get('Dependencies') is not None:
            for k1 in m.get('Dependencies'):
                temp_model = main_models.GetWorkflowResponseBodyWorkflowDependencies()
                self.dependencies.append(temp_model.from_map(k1))

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

        if m.get('Outputs') is not None:
            temp_model = main_models.GetWorkflowResponseBodyWorkflowOutputs()
            self.outputs = temp_model.from_map(m.get('Outputs'))

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetWorkflowResponseBodyWorkflowTags()
                self.tags.append(temp_model.from_map(k1))

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.GetWorkflowResponseBodyWorkflowTasks()
                self.tasks.append(temp_model.from_map(k1))

        if m.get('Trigger') is not None:
            temp_model = main_models.GetWorkflowResponseBodyWorkflowTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        return self

class GetWorkflowResponseBodyWorkflowTrigger(DaraModel):
    def __init__(
        self,
        cron: str = None,
        end_time: str = None,
        recurrence: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The cron expression. This parameter takes effect only when Type is set to Scheduler.
        self.cron = cron
        # The expiration time of the periodic trigger. This parameter takes effect only when Type is set to Scheduler.
        # 
        # The format is `yyyy-MM-dd HH:mm:ss`, such as `1970-01-01 00:00:00`. The example does not include a time zone identifier.
        self.end_time = end_time
        # The running mode when the trigger is fired. This parameter takes effect only when Type is set to Scheduler. Valid values:
        # - Pause: paused
        # - Skip: dry run
        # - Normal: normal execution
        self.recurrence = recurrence
        # The time when periodic triggering takes effect. This parameter takes effect only when Type is set to Scheduler.
        # 
        # The format is `yyyy-MM-dd HH:mm:ss`, such as `1970-01-01 00:00:00`. The example does not include a time zone identifier.
        self.start_time = start_time
        # The type of the trigger method. Valid values:
        # - Scheduler: triggered by a scheduling cycle
        # - Manual: triggered manually
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

class GetWorkflowResponseBodyWorkflowTasks(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        client_unique_code: str = None,
        create_time: int = None,
        create_user: str = None,
        data_source: main_models.GetWorkflowResponseBodyWorkflowTasksDataSource = None,
        description: str = None,
        env_type: str = None,
        id: int = None,
        modify_time: int = None,
        modify_user: str = None,
        name: str = None,
        owner: str = None,
        priority: int = None,
        project_id: int = None,
        rerun_interval: int = None,
        rerun_mode: str = None,
        rerun_times: int = None,
        runtime_resource: main_models.GetWorkflowResponseBodyWorkflowTasksRuntimeResource = None,
        timeout: int = None,
        trigger_recurrence: str = None,
        type: str = None,
        workflow_id: int = None,
    ):
        # The ID of the baseline.
        self.baseline_id = baseline_id
        # The client unique code of the task, which is used to implement asynchronous and idempotent operations. If you do not specify this parameter when creating the task, the system automatically generates a code and uniquely binds it to the resource ID. If you specify this parameter when updating or deleting the resource, it must be the same as the client unique code used during creation.
        self.client_unique_code = client_unique_code
        # The creation time.
        # 
        # The value is a 13-digit number, such as `1710239005403`.
        self.create_time = create_time
        # The account ID of the user who created the task.
        self.create_user = create_user
        # The associated data source information.
        self.data_source = data_source
        # The description.
        self.description = description
        # The project environment. Valid values:
        # - Prod: Production environment.
        # - Dev: Development environment.
        self.env_type = env_type
        # The ID of the task.
        self.id = id
        # The update time.
        # 
        # The value is a 13-digit number, such as `1710239005403`.
        self.modify_time = modify_time
        # The account ID of the user who updated the task.
        self.modify_user = modify_user
        # The name of the task.
        self.name = name
        # The account ID of the task owner.
        self.owner = owner
        # The priority of the task. Valid values: 1 to 8. A larger value indicates a higher priority. Default value: 1.
        self.priority = priority
        # The ID of the project.
        self.project_id = project_id
        # The retry time interval, in seconds.
        self.rerun_interval = rerun_interval
        # The configuration that specifies whether the task can be rerun. Valid values:
        # - AllDenied: The task cannot be rerun regardless of whether it succeeds or fails.
        # - FailureAllowed: The task can be rerun only when it fails.
        # - AllAllowed: The task can be rerun regardless of whether it succeeds or fails.
        self.rerun_mode = rerun_mode
        # The number of retries. This parameter takes effect only when the task is configured to be rerunnable.
        self.rerun_times = rerun_times
        # The runtime environment configuration, such as the resource group information.
        self.runtime_resource = runtime_resource
        # The timeout period for task execution, in seconds.
        self.timeout = timeout
        # The running mode when the trigger is fired. Valid values:
        # - Pause: paused
        # - Skip: dry run
        # - Normal: normal execution
        self.trigger_recurrence = trigger_recurrence
        # The type of the task.
        self.type = type
        # The ID of the workflow to which the task belongs.
        self.workflow_id = workflow_id

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.runtime_resource:
            self.runtime_resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.client_unique_code is not None:
            result['ClientUniqueCode'] = self.client_unique_code

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

        if self.trigger_recurrence is not None:
            result['TriggerRecurrence'] = self.trigger_recurrence

        if self.type is not None:
            result['Type'] = self.type

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('ClientUniqueCode') is not None:
            self.client_unique_code = m.get('ClientUniqueCode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('DataSource') is not None:
            temp_model = main_models.GetWorkflowResponseBodyWorkflowTasksDataSource()
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

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RerunInterval') is not None:
            self.rerun_interval = m.get('RerunInterval')

        if m.get('RerunMode') is not None:
            self.rerun_mode = m.get('RerunMode')

        if m.get('RerunTimes') is not None:
            self.rerun_times = m.get('RerunTimes')

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.GetWorkflowResponseBodyWorkflowTasksRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('TriggerRecurrence') is not None:
            self.trigger_recurrence = m.get('TriggerRecurrence')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

class GetWorkflowResponseBodyWorkflowTasksRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: str = None,
        image: str = None,
        resource_group_id: str = None,
    ):
        # The CU consumption configured for task execution.
        self.cu = cu
        # The ID of the image configured for task execution.
        self.image = image
        # The identifier of the resource group for scheduling configured for task execution.
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

class GetWorkflowResponseBodyWorkflowTasksDataSource(DaraModel):
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

class GetWorkflowResponseBodyWorkflowTags(DaraModel):
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

class GetWorkflowResponseBodyWorkflowOutputs(DaraModel):
    def __init__(
        self,
        task_outputs: List[main_models.GetWorkflowResponseBodyWorkflowOutputsTaskOutputs] = None,
    ):
        # The list of task output definitions.
        self.task_outputs = task_outputs

    def validate(self):
        if self.task_outputs:
            for v1 in self.task_outputs:
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_outputs = []
        if m.get('TaskOutputs') is not None:
            for k1 in m.get('TaskOutputs'):
                temp_model = main_models.GetWorkflowResponseBodyWorkflowOutputsTaskOutputs()
                self.task_outputs.append(temp_model.from_map(k1))

        return self

class GetWorkflowResponseBodyWorkflowOutputsTaskOutputs(DaraModel):
    def __init__(
        self,
        output: str = None,
    ):
        # The output identifier.
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

class GetWorkflowResponseBodyWorkflowDependencies(DaraModel):
    def __init__(
        self,
        type: str = None,
        upstream_output: str = None,
        upstream_task_id: int = None,
    ):
        # The dependency type. Valid values:
        # - CrossCycleDependsOnChildren: cross-cycle dependency on first-level child nodes
        # - CrossCycleDependsOnSelf: cross-cycle dependency on the node itself
        # - CrossCycleDependsOnOtherNode: cross-cycle dependency on other nodes
        # - Normal: same-cycle dependency
        self.type = type
        # The output identifier of the upstream task. This field is returned when the dependency type is same-cycle dependency and the input content is configured.
        self.upstream_output = upstream_output
        # The ID of the upstream task. This field is returned when the dependency type is cross-cycle dependency on other nodes or same-cycle dependency without input content configured. It is not returned in other cases.
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

