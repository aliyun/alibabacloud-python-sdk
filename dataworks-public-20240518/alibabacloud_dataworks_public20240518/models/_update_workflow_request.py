# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateWorkflowRequest(DaraModel):
    def __init__(
        self,
        client_unique_code: str = None,
        dependencies: List[main_models.UpdateWorkflowRequestDependencies] = None,
        description: str = None,
        env_type: str = None,
        id: int = None,
        instance_mode: str = None,
        name: str = None,
        outputs: main_models.UpdateWorkflowRequestOutputs = None,
        owner: str = None,
        parameters: str = None,
        tags: List[main_models.UpdateWorkflowRequestTags] = None,
        tasks: List[main_models.UpdateWorkflowRequestTasks] = None,
        trigger: main_models.UpdateWorkflowRequestTrigger = None,
    ):
        # The unique code of the client. This parameter is used to create a workflow asynchronously and implement the idempotence of the workflow. If you do not specify this parameter when you create the workflow, the system automatically generates a unique code. The unique code is uniquely associated with the workflow ID. If you specify this parameter when you update or delete the workflow, the value of this parameter must be the unique code that is used to create the workflow.
        self.client_unique_code = client_unique_code
        # The dependency information.
        self.dependencies = dependencies
        # The description.
        self.description = description
        # The project environment.
        # 
        # *   Prod
        # *   Dev
        self.env_type = env_type
        # The workflow ID.
        # 
        # This parameter is required.
        self.id = id
        # The instance generation mode.
        # 
        # *   T+1: the next day
        # *   Immediately Note: Periodic instances will only be generated normally if the workflow\\"s scheduled time is more than 10 minutes after the workflow publication time. Real-time instance generation is not available during the batch instance generation period (23:30 to 24:00). While workflows can be published during this time, instances will not be regenerated immediately after submission.
        self.instance_mode = instance_mode
        # The name of the workflow.
        # 
        # This parameter is required.
        self.name = name
        # The output information.
        self.outputs = outputs
        # The account ID of the owner.
        # 
        # This parameter is required.
        self.owner = owner
        # The parameters.
        self.parameters = parameters
        # The tags.
        self.tags = tags
        # Details about tasks.
        self.tasks = tasks
        # The trigger method.
        # 
        # This parameter is required.
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

        if self.instance_mode is not None:
            result['InstanceMode'] = self.instance_mode

        if self.name is not None:
            result['Name'] = self.name

        if self.outputs is not None:
            result['Outputs'] = self.outputs.to_map()

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.parameters is not None:
            result['Parameters'] = self.parameters

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

        self.dependencies = []
        if m.get('Dependencies') is not None:
            for k1 in m.get('Dependencies'):
                temp_model = main_models.UpdateWorkflowRequestDependencies()
                self.dependencies.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceMode') is not None:
            self.instance_mode = m.get('InstanceMode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Outputs') is not None:
            temp_model = main_models.UpdateWorkflowRequestOutputs()
            self.outputs = temp_model.from_map(m.get('Outputs'))

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.UpdateWorkflowRequestTags()
                self.tags.append(temp_model.from_map(k1))

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.UpdateWorkflowRequestTasks()
                self.tasks.append(temp_model.from_map(k1))

        if m.get('Trigger') is not None:
            temp_model = main_models.UpdateWorkflowRequestTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        return self

class UpdateWorkflowRequestTrigger(DaraModel):
    def __init__(
        self,
        cron: str = None,
        end_time: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The Cron expression. This parameter takes effect only if the Type parameter is set to Scheduler.
        self.cron = cron
        # The expiration time of periodic triggering. Takes effect only when type is set to Scheduler. The value of this parameter is in the`yyyy-mm-dd hh:mm:ss` format.
        self.end_time = end_time
        # The time when periodic triggering takes effect. This parameter takes effect only if the Type parameter is set to Scheduler. The value of this parameter is in the`yyyy-mm-dd hh:mm:ss` format.
        self.start_time = start_time
        # The trigger type. Valid values:
        # 
        # *   Scheduler: periodically triggered
        # *   Manual
        # 
        # This parameter is required.
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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateWorkflowRequestTasks(DaraModel):
    def __init__(
        self,
        base_line_id: int = None,
        client_unique_code: str = None,
        data_source: main_models.UpdateWorkflowRequestTasksDataSource = None,
        dependencies: List[main_models.UpdateWorkflowRequestTasksDependencies] = None,
        description: str = None,
        env_type: str = None,
        id: int = None,
        inputs: main_models.UpdateWorkflowRequestTasksInputs = None,
        name: str = None,
        outputs: main_models.UpdateWorkflowRequestTasksOutputs = None,
        owner: str = None,
        rerun_interval: int = None,
        rerun_mode: str = None,
        rerun_times: int = None,
        runtime_resource: main_models.UpdateWorkflowRequestTasksRuntimeResource = None,
        script: main_models.UpdateWorkflowRequestTasksScript = None,
        tags: List[main_models.UpdateWorkflowRequestTasksTags] = None,
        timeout: int = None,
        trigger: main_models.UpdateWorkflowRequestTasksTrigger = None,
        type: str = None,
    ):
        # The baseline ID.
        self.base_line_id = base_line_id
        # The client-side unique token for the task, used to ensure asynchronous processing and idempotency. If not specified during creation, the system will automatically generate one. This token is uniquely associated with the resource ID. If provided when updating or deleting resources, this parameter must match the client token used during creation.
        self.client_unique_code = client_unique_code
        # The information about the associated data source.
        self.data_source = data_source
        # The dependency information. Note: If this parameter is left empty or set to an empty array, all dependency configurations will be deleted.
        self.dependencies = dependencies
        # The description of the task.
        self.description = description
        # The project environment.
        # 
        # *   Prod
        # *   Dev
        self.env_type = env_type
        # The ID of the task. Specifying this field triggers a full update for the corresponding task. If left unspecified, a new task will be created.
        self.id = id
        # The input information. By default, all input information is deleted if this parameter is set to null.
        self.inputs = inputs
        # The name of the task.
        # 
        # This parameter is required.
        self.name = name
        # The output information. By default, all output information is deleted if this parameter is set to null.
        self.outputs = outputs
        # The account ID of the owner.
        # 
        # This parameter is required.
        self.owner = owner
        # The retry interval in seconds.
        self.rerun_interval = rerun_interval
        # Configuration for whether the task can be rerun.
        # 
        # *   AllDenied: The task cannot be rerun.
        # *   FailureAllowed: The task can be rerun only after it fails.
        # *   AllAllowed: The task can always be rerun.
        # 
        # This parameter is required.
        self.rerun_mode = rerun_mode
        # The number of retry attempts. Takes effect when the task is configured to allow reruns.
        self.rerun_times = rerun_times
        # Runtime environment configurations, such as resource group information.
        # 
        # This parameter is required.
        self.runtime_resource = runtime_resource
        # The run script information.
        self.script = script
        # The list of task tags. Note: If this field is unspecified or set to an empty array, all existing Tag configurations will be deleted by default.
        self.tags = tags
        # The task execution timeout in seconds.
        self.timeout = timeout
        # The trigger method.
        # 
        # This parameter is required.
        self.trigger = trigger
        # The type of the task.
        # 
        # This parameter is required.
        self.type = type

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
        if self.base_line_id is not None:
            result['BaseLineId'] = self.base_line_id

        if self.client_unique_code is not None:
            result['ClientUniqueCode'] = self.client_unique_code

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

        if self.name is not None:
            result['Name'] = self.name

        if self.outputs is not None:
            result['Outputs'] = self.outputs.to_map()

        if self.owner is not None:
            result['Owner'] = self.owner

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseLineId') is not None:
            self.base_line_id = m.get('BaseLineId')

        if m.get('ClientUniqueCode') is not None:
            self.client_unique_code = m.get('ClientUniqueCode')

        if m.get('DataSource') is not None:
            temp_model = main_models.UpdateWorkflowRequestTasksDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        self.dependencies = []
        if m.get('Dependencies') is not None:
            for k1 in m.get('Dependencies'):
                temp_model = main_models.UpdateWorkflowRequestTasksDependencies()
                self.dependencies.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Inputs') is not None:
            temp_model = main_models.UpdateWorkflowRequestTasksInputs()
            self.inputs = temp_model.from_map(m.get('Inputs'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Outputs') is not None:
            temp_model = main_models.UpdateWorkflowRequestTasksOutputs()
            self.outputs = temp_model.from_map(m.get('Outputs'))

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RerunInterval') is not None:
            self.rerun_interval = m.get('RerunInterval')

        if m.get('RerunMode') is not None:
            self.rerun_mode = m.get('RerunMode')

        if m.get('RerunTimes') is not None:
            self.rerun_times = m.get('RerunTimes')

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.UpdateWorkflowRequestTasksRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('Script') is not None:
            temp_model = main_models.UpdateWorkflowRequestTasksScript()
            self.script = temp_model.from_map(m.get('Script'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.UpdateWorkflowRequestTasksTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Trigger') is not None:
            temp_model = main_models.UpdateWorkflowRequestTasksTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateWorkflowRequestTasksTrigger(DaraModel):
    def __init__(
        self,
        recurrence: str = None,
        type: str = None,
    ):
        # The running mode of the task after it is triggered. This parameter takes effect only if the Type parameter is set to Scheduler. Valid values:
        # 
        # *   Pause
        # *   Skip
        # *   Normal
        # 
        # This parameter is required.
        self.recurrence = recurrence
        # The trigger type. Valid values:
        # 
        # *   Scheduler: periodically triggered
        # *   Manual
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.recurrence is not None:
            result['Recurrence'] = self.recurrence

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Recurrence') is not None:
            self.recurrence = m.get('Recurrence')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateWorkflowRequestTasksTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of a tag.
        # 
        # This parameter is required.
        self.key = key
        # The value of a tag.
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

class UpdateWorkflowRequestTasksScript(DaraModel):
    def __init__(
        self,
        content: str = None,
        parameters: str = None,
    ):
        # The script content.
        self.content = content
        # The script parameter list.
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

class UpdateWorkflowRequestTasksRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: str = None,
        image: str = None,
        resource_group_id: str = None,
    ):
        # The default number of compute units (CUs) configured for task running.
        self.cu = cu
        # The image ID used in the task runtime configuration.
        self.image = image
        # The identifier of the scheduling resource group used in the task runtime configuration.
        # 
        # This parameter is required.
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

class UpdateWorkflowRequestTasksOutputs(DaraModel):
    def __init__(
        self,
        task_outputs: List[main_models.UpdateWorkflowRequestTasksOutputsTaskOutputs] = None,
        variables: List[main_models.UpdateWorkflowRequestTasksOutputsVariables] = None,
    ):
        # The task outputs. By default, all task output information is deleted if this parameter is set to null or not specified.
        self.task_outputs = task_outputs
        # The variables. Note: The settings of all output variables are deleted if this parameter is set to null or not specified.
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
                temp_model = main_models.UpdateWorkflowRequestTasksOutputsTaskOutputs()
                self.task_outputs.append(temp_model.from_map(k1))

        self.variables = []
        if m.get('Variables') is not None:
            for k1 in m.get('Variables'):
                temp_model = main_models.UpdateWorkflowRequestTasksOutputsVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class UpdateWorkflowRequestTasksOutputsVariables(DaraModel):
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
        # *   Constant: constant value.
        # *   PassThrough: node output.
        # *   System: variable.
        # *   NodeOutput: script output.
        # 
        # This parameter is required.
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

class UpdateWorkflowRequestTasksOutputsTaskOutputs(DaraModel):
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

class UpdateWorkflowRequestTasksInputs(DaraModel):
    def __init__(
        self,
        variables: List[main_models.UpdateWorkflowRequestTasksInputsVariables] = None,
    ):
        # The variables. By default, the settings of all input variables are deleted if this parameter is set to null or not specified.
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
                temp_model = main_models.UpdateWorkflowRequestTasksInputsVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class UpdateWorkflowRequestTasksInputsVariables(DaraModel):
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
        # *   Constant: constant value.
        # *   PassThrough: node output.
        # *   System: variable.
        # *   NodeOutput: script output.
        # 
        # This parameter is required.
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

class UpdateWorkflowRequestTasksDependencies(DaraModel):
    def __init__(
        self,
        type: str = None,
        upstream_output: str = None,
        upstream_task_id: int = None,
    ):
        # The dependency type. Valid values:
        # 
        # *   CrossCycleDependsOnChildren: Depends on level-1 downstream nodes across cycles
        # *   CrossCycleDependsOnSelf: Depends on itself across cycles.
        # *   CrossCycleDependsOnOtherNode: Depends on other nodes across cycles.
        # *   Normal: Depends on nodes in the same cycle.
        # 
        # This parameter is required.
        self.type = type
        # The output identifier of the upstream task. (This parameter is returned only if `Normal` is set and the node input is configured.)
        self.upstream_output = upstream_output
        # The ID of the upstream task. (This parameter is returned only if `Normal` or `CrossCycleDependsOnOtherNode` is set and the node input is not configured.)
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

class UpdateWorkflowRequestTasksDataSource(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The data source name.
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

class UpdateWorkflowRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # This parameter is required.
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

class UpdateWorkflowRequestOutputs(DaraModel):
    def __init__(
        self,
        task_outputs: List[main_models.UpdateWorkflowRequestOutputsTaskOutputs] = None,
    ):
        # The task outputs.
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
                temp_model = main_models.UpdateWorkflowRequestOutputsTaskOutputs()
                self.task_outputs.append(temp_model.from_map(k1))

        return self

class UpdateWorkflowRequestOutputsTaskOutputs(DaraModel):
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

class UpdateWorkflowRequestDependencies(DaraModel):
    def __init__(
        self,
        type: str = None,
        upstream_output: str = None,
        upstream_task_id: int = None,
    ):
        # The dependency type. Valid values:
        # 
        # *   CrossCycleDependsOnChildren: Depends on level-1 downstream nodes across cycles
        # *   CrossCycleDependsOnSelf: Depends on itself across cycles.
        # *   CrossCycleDependsOnOtherNode: Depends on other nodes across cycles.
        # *   Normal: Depends on nodes in the same cycle.
        # 
        # This parameter is required.
        self.type = type
        # The output identifier of the upstream task. (This parameter is returned only if `Normal` is set and the node input is configured.)
        self.upstream_output = upstream_output
        # The ID of the upstream task. (This parameter is returned only if `Normal` or `CrossCycleDependsOnOtherNode` is set and the node input is not configured.)
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

