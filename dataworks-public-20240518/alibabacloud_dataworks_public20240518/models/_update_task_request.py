# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateTaskRequest(DaraModel):
    def __init__(
        self,
        client_unique_code: str = None,
        data_source: main_models.UpdateTaskRequestDataSource = None,
        dependencies: List[main_models.UpdateTaskRequestDependencies] = None,
        description: str = None,
        env_type: str = None,
        id: int = None,
        inputs: main_models.UpdateTaskRequestInputs = None,
        instance_mode: str = None,
        name: str = None,
        outputs: main_models.UpdateTaskRequestOutputs = None,
        owner: str = None,
        rerun_interval: int = None,
        rerun_mode: str = None,
        rerun_times: int = None,
        runtime_resource: main_models.UpdateTaskRequestRuntimeResource = None,
        script: main_models.UpdateTaskRequestScript = None,
        tags: List[main_models.UpdateTaskRequestTags] = None,
        timeout: int = None,
        trigger: main_models.UpdateTaskRequestTrigger = None,
    ):
        # The client unique code of the node, used to uniquely identify a node. This code is used to implement asynchronous operations and idempotence. If not specified during creation, the system automatically generates one, and the code is uniquely bound to the resource ID. When updating or deleting a resource, if this parameter is specified, it must be consistent with the client unique code used during creation.
        self.client_unique_code = client_unique_code
        # The associated data source information.
        self.data_source = data_source
        # The dependency information.
        self.dependencies = dependencies
        # The description.
        self.description = description
        # The project environment. Valid values:
        # - Prod: production.
        # - Dev: development.
        self.env_type = env_type
        # The node ID.
        # 
        # This parameter is required.
        self.id = id
        # The input information.
        self.inputs = inputs
        # The instance generation mode. Valid values:
        # - T+1: The instance is generated the next day.
        # - Immediately: The instance is generated immediately. Note: Only periodic instances whose scheduled time is at least ten minutes after the node publish time are generated normally. During the full instance generation period (22:00 to 24:00), real-time instance generation is not available. You can submit and publish nodes, but new nodes do not automatically generate instances.
        self.instance_mode = instance_mode
        # The name.
        self.name = name
        # The output information.
        self.outputs = outputs
        # The account ID of the node owner.
        self.owner = owner
        # The retry time interval, in milliseconds. The value cannot exceed 1800000.
        self.rerun_interval = rerun_interval
        # Specifies whether the node can be rerun. Valid values:
        # - AllDenied: The node cannot be rerun regardless of whether it succeeds or fails.
        # - FailureAllowed: The node can be rerun only when it fails.
        # - AllAllowed: The node can be rerun regardless of whether it succeeds or fails.
        self.rerun_mode = rerun_mode
        # The number of retries. This parameter takes effect when the node is configured to allow reruns.
        self.rerun_times = rerun_times
        # The environment configuration, such as resource group information.
        self.runtime_resource = runtime_resource
        # The script information.
        self.script = script
        # The list of node tags.
        self.tags = tags
        # The node execution timeout period, in seconds. The value must be greater than 3600.
        self.timeout = timeout
        # The node trigger method.
        self.trigger = trigger

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

        if self.instance_mode is not None:
            result['InstanceMode'] = self.instance_mode

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientUniqueCode') is not None:
            self.client_unique_code = m.get('ClientUniqueCode')

        if m.get('DataSource') is not None:
            temp_model = main_models.UpdateTaskRequestDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        self.dependencies = []
        if m.get('Dependencies') is not None:
            for k1 in m.get('Dependencies'):
                temp_model = main_models.UpdateTaskRequestDependencies()
                self.dependencies.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Inputs') is not None:
            temp_model = main_models.UpdateTaskRequestInputs()
            self.inputs = temp_model.from_map(m.get('Inputs'))

        if m.get('InstanceMode') is not None:
            self.instance_mode = m.get('InstanceMode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Outputs') is not None:
            temp_model = main_models.UpdateTaskRequestOutputs()
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
            temp_model = main_models.UpdateTaskRequestRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('Script') is not None:
            temp_model = main_models.UpdateTaskRequestScript()
            self.script = temp_model.from_map(m.get('Script'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.UpdateTaskRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Trigger') is not None:
            temp_model = main_models.UpdateTaskRequestTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        return self

class UpdateTaskRequestTrigger(DaraModel):
    def __init__(
        self,
        cron: str = None,
        cycle_type: str = None,
        end_time: str = None,
        recurrence: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The cron expression. This parameter takes effect when Type is set to Scheduler.
        self.cron = cron
        # The epoch type. This parameter takes effect when Type is set to Scheduler and the cron expression specifies timed scheduling at a specific hour. Default value: Daily. Valid values:
        # - Daily: daily scheduling.
        # - NotDaily: hourly scheduling.
        self.cycle_type = cycle_type
        # The expiration time of the periodic trigger. This parameter takes effect when Type is set to Scheduler. Format: `yyyy-mm-dd hh:mm:ss`.
        self.end_time = end_time
        # The run mode when triggered. This parameter takes effect when Type is set to Scheduler. Valid values:
        # - Pause: paused.
        # - Skip: dry run.
        # - Normal: normal run.
        self.recurrence = recurrence
        # The effective period of the epoch trigger. This parameter takes effect when Type is set to Scheduler. Format: `yyyy-mm-dd hh:mm:ss`.
        self.start_time = start_time
        # The trigger type. Valid values:
        # - Scheduler: periodic scheduling trigger.
        # - Manual: manual trigger.
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

        if self.cycle_type is not None:
            result['CycleType'] = self.cycle_type

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

        if m.get('CycleType') is not None:
            self.cycle_type = m.get('CycleType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Recurrence') is not None:
            self.recurrence = m.get('Recurrence')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateTaskRequestTags(DaraModel):
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

class UpdateTaskRequestScript(DaraModel):
    def __init__(
        self,
        content: str = None,
        parameters: str = None,
    ):
        # The script content.
        self.content = content
        # The list of script parameters.
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

class UpdateTaskRequestRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: str = None,
        image: str = None,
        resource_group_id: str = None,
    ):
        # The CU consumption configured for the node.
        self.cu = cu
        # The image ID configured for the node.
        self.image = image
        # The identifier of the schedule resource group configured for the node.
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

class UpdateTaskRequestOutputs(DaraModel):
    def __init__(
        self,
        task_outputs: List[main_models.UpdateTaskRequestOutputsTaskOutputs] = None,
        variables: List[main_models.UpdateTaskRequestOutputsVariables] = None,
    ):
        # The list of node output definitions.
        self.task_outputs = task_outputs
        # The list of variable definitions.
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
                temp_model = main_models.UpdateTaskRequestOutputsTaskOutputs()
                self.task_outputs.append(temp_model.from_map(k1))

        self.variables = []
        if m.get('Variables') is not None:
            for k1 in m.get('Variables'):
                temp_model = main_models.UpdateTaskRequestOutputsVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class UpdateTaskRequestOutputsVariables(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # The variable name.
        self.name = name
        # The type. Valid values:
        # - Constant: constant.
        # - PassThrough: parameter node output.
        # - System: variable.
        # - NodeOutput: script output.
        # 
        # This parameter is required.
        self.type = type
        # The variable value.
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

class UpdateTaskRequestOutputsTaskOutputs(DaraModel):
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

class UpdateTaskRequestInputs(DaraModel):
    def __init__(
        self,
        variables: List[main_models.UpdateTaskRequestInputsVariables] = None,
    ):
        # The list of variable definitions.
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
                temp_model = main_models.UpdateTaskRequestInputsVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class UpdateTaskRequestInputsVariables(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # The variable name.
        self.name = name
        # The type. Valid values:
        # - Constant: constant.
        # - PassThrough: parameter node output.
        # - System: variable.
        # - NodeOutput: script output.
        # 
        # This parameter is required.
        self.type = type
        # The variable value.
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

class UpdateTaskRequestDependencies(DaraModel):
    def __init__(
        self,
        type: str = None,
        upstream_output: str = None,
        upstream_task_id: int = None,
    ):
        # The dependency type. Valid values:
        # - CrossCycleDependsOnChildren: cross-cycle dependency on first-level child nodes.
        # - CrossCycleDependsOnSelf: cross-cycle dependency on self.
        # - CrossCycleDependsOnOtherNode: cross-cycle dependency on other nodes.
        # - Normal: same-cycle dependency.
        # 
        # This parameter is required.
        self.type = type
        # The output identifier of the upstream node. This field is returned when the dependency type is same-cycle dependency and input content is configured.
        self.upstream_output = upstream_output
        # The ID of the upstream node. This field is returned when the dependency type is cross-cycle dependency on other nodes, or same-cycle dependency without input content configured. It is not returned in other cases.
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

class UpdateTaskRequestDataSource(DaraModel):
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

