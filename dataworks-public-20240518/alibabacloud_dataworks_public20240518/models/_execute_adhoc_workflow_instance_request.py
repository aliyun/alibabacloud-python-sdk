# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ExecuteAdhocWorkflowInstanceRequest(DaraModel):
    def __init__(
        self,
        biz_date: int = None,
        env_type: str = None,
        name: str = None,
        owner: str = None,
        project_id: int = None,
        tasks: List[main_models.ExecuteAdhocWorkflowInstanceRequestTasks] = None,
    ):
        # The data timestamp.
        self.biz_date = biz_date
        # The environment of the workspace. Valid values:
        # 
        # *   Prod: production environment
        # *   Dev: development environment
        self.env_type = env_type
        # The name of the workflow instance.
        # 
        # This parameter is required.
        self.name = name
        # The account ID of the owner.
        # 
        # This parameter is required.
        self.owner = owner
        # The workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The tasks.
        # 
        # This parameter is required.
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.ExecuteAdhocWorkflowInstanceRequestTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class ExecuteAdhocWorkflowInstanceRequestTasks(DaraModel):
    def __init__(
        self,
        client_unique_code: str = None,
        data_source: main_models.ExecuteAdhocWorkflowInstanceRequestTasksDataSource = None,
        dependencies: List[main_models.ExecuteAdhocWorkflowInstanceRequestTasksDependencies] = None,
        inputs: main_models.ExecuteAdhocWorkflowInstanceRequestTasksInputs = None,
        name: str = None,
        outputs: main_models.ExecuteAdhocWorkflowInstanceRequestTasksOutputs = None,
        owner: str = None,
        runtime_resource: main_models.ExecuteAdhocWorkflowInstanceRequestTasksRuntimeResource = None,
        script: main_models.ExecuteAdhocWorkflowInstanceRequestTasksScript = None,
        timeout: int = None,
        type: str = None,
    ):
        # The unique code of the client. This code uniquely identifies a task.
        # 
        # This parameter is required.
        self.client_unique_code = client_unique_code
        # The information about the associated data source.
        self.data_source = data_source
        # The dependency information.
        self.dependencies = dependencies
        # The input information.
        self.inputs = inputs
        # The name of the task.
        # 
        # This parameter is required.
        self.name = name
        # The output information.
        self.outputs = outputs
        # The account ID of the owner.
        # 
        # This parameter is required.
        self.owner = owner
        # The configurations of the runtime environment, such as the resource group information.
        # 
        # This parameter is required.
        self.runtime_resource = runtime_resource
        # The script information.
        self.script = script
        # The timeout period of task running. Unit: seconds.
        self.timeout = timeout
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

        if self.inputs is not None:
            result['Inputs'] = self.inputs.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.outputs is not None:
            result['Outputs'] = self.outputs.to_map()

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource.to_map()

        if self.script is not None:
            result['Script'] = self.script.to_map()

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientUniqueCode') is not None:
            self.client_unique_code = m.get('ClientUniqueCode')

        if m.get('DataSource') is not None:
            temp_model = main_models.ExecuteAdhocWorkflowInstanceRequestTasksDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        self.dependencies = []
        if m.get('Dependencies') is not None:
            for k1 in m.get('Dependencies'):
                temp_model = main_models.ExecuteAdhocWorkflowInstanceRequestTasksDependencies()
                self.dependencies.append(temp_model.from_map(k1))

        if m.get('Inputs') is not None:
            temp_model = main_models.ExecuteAdhocWorkflowInstanceRequestTasksInputs()
            self.inputs = temp_model.from_map(m.get('Inputs'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Outputs') is not None:
            temp_model = main_models.ExecuteAdhocWorkflowInstanceRequestTasksOutputs()
            self.outputs = temp_model.from_map(m.get('Outputs'))

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.ExecuteAdhocWorkflowInstanceRequestTasksRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('Script') is not None:
            temp_model = main_models.ExecuteAdhocWorkflowInstanceRequestTasksScript()
            self.script = temp_model.from_map(m.get('Script'))

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ExecuteAdhocWorkflowInstanceRequestTasksScript(DaraModel):
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

class ExecuteAdhocWorkflowInstanceRequestTasksRuntimeResource(DaraModel):
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

class ExecuteAdhocWorkflowInstanceRequestTasksOutputs(DaraModel):
    def __init__(
        self,
        task_outputs: List[main_models.ExecuteAdhocWorkflowInstanceRequestTasksOutputsTaskOutputs] = None,
        variables: List[main_models.ExecuteAdhocWorkflowInstanceRequestTasksOutputsVariables] = None,
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
                temp_model = main_models.ExecuteAdhocWorkflowInstanceRequestTasksOutputsTaskOutputs()
                self.task_outputs.append(temp_model.from_map(k1))

        self.variables = []
        if m.get('Variables') is not None:
            for k1 in m.get('Variables'):
                temp_model = main_models.ExecuteAdhocWorkflowInstanceRequestTasksOutputsVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class ExecuteAdhocWorkflowInstanceRequestTasksOutputsVariables(DaraModel):
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
        # *   System
        # *   Constant
        # *   NodeOutput
        # *   PassThrough
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

class ExecuteAdhocWorkflowInstanceRequestTasksOutputsTaskOutputs(DaraModel):
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

class ExecuteAdhocWorkflowInstanceRequestTasksInputs(DaraModel):
    def __init__(
        self,
        variables: List[main_models.ExecuteAdhocWorkflowInstanceRequestTasksInputsVariables] = None,
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
                temp_model = main_models.ExecuteAdhocWorkflowInstanceRequestTasksInputsVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class ExecuteAdhocWorkflowInstanceRequestTasksInputsVariables(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the variable.
        self.name = name
        # The value of the variable. You must configure this parameter in the `The ancestor output: The output variable name of the ancestor task` format.
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

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ExecuteAdhocWorkflowInstanceRequestTasksDependencies(DaraModel):
    def __init__(
        self,
        upstream_output: str = None,
    ):
        # The identifier of the output of the ancestor task.
        self.upstream_output = upstream_output

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.upstream_output is not None:
            result['UpstreamOutput'] = self.upstream_output

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpstreamOutput') is not None:
            self.upstream_output = m.get('UpstreamOutput')

        return self

class ExecuteAdhocWorkflowInstanceRequestTasksDataSource(DaraModel):
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

