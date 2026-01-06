# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListNodeDependenciesResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListNodeDependenciesResponseBodyPagingInfo = None,
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
            temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListNodeDependenciesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.ListNodeDependenciesResponseBodyPagingInfoNodes] = None,
        page_number: str = None,
        page_size: str = None,
        total_count: str = None,
    ):
        # The list of dependent nodes.
        self.nodes = nodes
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNodeDependenciesResponseBodyPagingInfoNodes(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        data_source: main_models.ListNodeDependenciesResponseBodyPagingInfoNodesDataSource = None,
        description: str = None,
        id: str = None,
        inputs: main_models.ListNodeDependenciesResponseBodyPagingInfoNodesInputs = None,
        modify_time: int = None,
        name: str = None,
        outputs: main_models.ListNodeDependenciesResponseBodyPagingInfoNodesOutputs = None,
        owner: str = None,
        project_id: int = None,
        recurrence: str = None,
        runtime_resource: main_models.ListNodeDependenciesResponseBodyPagingInfoNodesRuntimeResource = None,
        script: main_models.ListNodeDependenciesResponseBodyPagingInfoNodesScript = None,
        strategy: main_models.ListNodeDependenciesResponseBodyPagingInfoNodesStrategy = None,
        tags: List[main_models.ListNodeDependenciesResponseBodyPagingInfoNodesTags] = None,
        task_id: int = None,
        trigger: main_models.ListNodeDependenciesResponseBodyPagingInfoNodesTrigger = None,
    ):
        # The timestamp when the node was created.
        self.create_time = create_time
        # The data source.
        self.data_source = data_source
        # The description of the node.
        self.description = description
        # The unique identifier of the Data Studio node.
        # 
        # >  Prior to SDK version 8.0.0, this field is of type Long. In SDK version 8.0.0 and later, it is of type String. This change does not affect the normal use of the SDK. The parameter is returned based on the type defined in the SDK. Compilation failures caused by the type change may occur only when you upgrade the SDK across version 8.0.0. In this case, you must manually update the data type.
        self.id = id
        # The node input.
        self.inputs = inputs
        # The timestamp when the node was last modified.
        self.modify_time = modify_time
        # The name of the node.
        self.name = name
        # The output of the node.
        self.outputs = outputs
        # The owner of the node.
        self.owner = owner
        # The ID of the workspace to which the node belongs.
        self.project_id = project_id
        # The scheduling type.
        # 
        # Valid values:
        # 
        # *   Normal: Nodes are scheduled as expected.
        # *   Pause: Nodes are paused, and the running of their descendant nodes is blocked.
        # *   Skip: Nodes are dry run. The system does not actually run the nodes but directly prompts that the nodes are successfully run. The running duration of the nodes is 0 seconds. In addition, the nodes do not occupy resources or block the running of their descendant nodes.
        self.recurrence = recurrence
        # The information about the resource group.
        self.runtime_resource = runtime_resource
        # The script information.
        self.script = script
        # The scheduling policy.
        self.strategy = strategy
        # The tags. This parameter is not in use.
        self.tags = tags
        # The ID of the scheduling task.
        self.task_id = task_id
        # The trigger.
        self.trigger = trigger

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.inputs:
            self.inputs.validate()
        if self.outputs:
            self.outputs.validate()
        if self.runtime_resource:
            self.runtime_resource.validate()
        if self.script:
            self.script.validate()
        if self.strategy:
            self.strategy.validate()
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.inputs is not None:
            result['Inputs'] = self.inputs.to_map()

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.outputs is not None:
            result['Outputs'] = self.outputs.to_map()

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.recurrence is not None:
            result['Recurrence'] = self.recurrence

        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource.to_map()

        if self.script is not None:
            result['Script'] = self.script.to_map()

        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataSource') is not None:
            temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodesDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Inputs') is not None:
            temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodesInputs()
            self.inputs = temp_model.from_map(m.get('Inputs'))

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Outputs') is not None:
            temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodesOutputs()
            self.outputs = temp_model.from_map(m.get('Outputs'))

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Recurrence') is not None:
            self.recurrence = m.get('Recurrence')

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodesRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('Script') is not None:
            temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodesScript()
            self.script = temp_model.from_map(m.get('Script'))

        if m.get('Strategy') is not None:
            temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodesStrategy()
            self.strategy = temp_model.from_map(m.get('Strategy'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Trigger') is not None:
            temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodesTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        return self

class ListNodeDependenciesResponseBodyPagingInfoNodesTrigger(DaraModel):
    def __init__(
        self,
        cron: str = None,
        end_time: str = None,
        id: str = None,
        start_time: str = None,
        timezone: str = None,
        type: str = None,
    ):
        # The cron expression for scheduling.
        self.cron = cron
        # The effective end time of the schedule, in the format yyyy-MM-dd HH:mm:ss.
        self.end_time = end_time
        # The unique identifier of the trigger.
        # 
        # >  Prior to SDK version 8.0.0, this field is of type Long. In SDK version 8.0.0 and later, it is of type String. This change does not affect the normal use of the SDK. The parameter is returned based on the type defined in the SDK. Compilation failures caused by the type change may occur only when you upgrade the SDK across version 8.0.0. In this case, you must manually update the data type.
        self.id = id
        # The effective start time of the schedule, in the format yyyy-MM-dd HH:mm:ss.
        self.start_time = start_time
        # The time zone.
        self.timezone = timezone
        # The trigger type.
        # 
        # Valid values:
        # 
        # *   Scheduler: Periodic scheduling.
        # *   Manual: Manual scheduling.
        # *   Streaming: Streaming scheduler.
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

        if self.id is not None:
            result['Id'] = self.id

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

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListNodeDependenciesResponseBodyPagingInfoNodesTags(DaraModel):
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

class ListNodeDependenciesResponseBodyPagingInfoNodesStrategy(DaraModel):
    def __init__(
        self,
        instance_mode: str = None,
        rerun_interval: int = None,
        rerun_mode: str = None,
        rerun_times: int = None,
        timeout: int = None,
    ):
        # The instance generation mode.
        # 
        # *   T+1
        # *   Immediately
        self.instance_mode = instance_mode
        # The interval between retries after failure. Unit: milliseconds.
        self.rerun_interval = rerun_interval
        # The rerun mode.
        # 
        # *   Allowed
        # *   Denied
        # *   FailureAllowed
        self.rerun_mode = rerun_mode
        # The number of retries after failure.
        self.rerun_times = rerun_times
        # The timeout period. Unit: milliseconds.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_mode is not None:
            result['InstanceMode'] = self.instance_mode

        if self.rerun_interval is not None:
            result['RerunInterval'] = self.rerun_interval

        if self.rerun_mode is not None:
            result['RerunMode'] = self.rerun_mode

        if self.rerun_times is not None:
            result['RerunTimes'] = self.rerun_times

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceMode') is not None:
            self.instance_mode = m.get('InstanceMode')

        if m.get('RerunInterval') is not None:
            self.rerun_interval = m.get('RerunInterval')

        if m.get('RerunMode') is not None:
            self.rerun_mode = m.get('RerunMode')

        if m.get('RerunTimes') is not None:
            self.rerun_times = m.get('RerunTimes')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class ListNodeDependenciesResponseBodyPagingInfoNodesScript(DaraModel):
    def __init__(
        self,
        id: str = None,
        path: str = None,
        runtime: main_models.ListNodeDependenciesResponseBodyPagingInfoNodesScriptRuntime = None,
    ):
        # The ID of the script.
        # 
        # >  This field is of type Long in SDK versions prior to 8.0.0, and of type String in SDK version 8.0.0 and later. This change does not affect the normal use of the SDK. The parameter is returned based on the type defined in the SDK. Compilation failures caused by the type change may occur only when you upgrade the SDK across version 8.0.0. In this case, you must manually update the data type.
        self.id = id
        # The script path.
        self.path = path
        # Runtime
        self.runtime = runtime

    def validate(self):
        if self.runtime:
            self.runtime.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.path is not None:
            result['Path'] = self.path

        if self.runtime is not None:
            result['Runtime'] = self.runtime.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Runtime') is not None:
            temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodesScriptRuntime()
            self.runtime = temp_model.from_map(m.get('Runtime'))

        return self

class ListNodeDependenciesResponseBodyPagingInfoNodesScriptRuntime(DaraModel):
    def __init__(
        self,
        command: str = None,
    ):
        # The command used to distinguish node types.
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')

        return self

class ListNodeDependenciesResponseBodyPagingInfoNodesRuntimeResource(DaraModel):
    def __init__(
        self,
        resource_group_id: str = None,
    ):
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

class ListNodeDependenciesResponseBodyPagingInfoNodesOutputs(DaraModel):
    def __init__(
        self,
        node_outputs: List[main_models.ListNodeDependenciesResponseBodyPagingInfoNodesOutputsNodeOutputs] = None,
        tables: List[main_models.ListNodeDependenciesResponseBodyPagingInfoNodesOutputsTables] = None,
        variables: List[main_models.ListNodeDependenciesResponseBodyPagingInfoNodesOutputsVariables] = None,
    ):
        # The node output list.
        self.node_outputs = node_outputs
        # The table list.
        self.tables = tables
        # The variables.
        self.variables = variables

    def validate(self):
        if self.node_outputs:
            for v1 in self.node_outputs:
                 if v1:
                    v1.validate()
        if self.tables:
            for v1 in self.tables:
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
        result['NodeOutputs'] = []
        if self.node_outputs is not None:
            for k1 in self.node_outputs:
                result['NodeOutputs'].append(k1.to_map() if k1 else None)

        result['Tables'] = []
        if self.tables is not None:
            for k1 in self.tables:
                result['Tables'].append(k1.to_map() if k1 else None)

        result['Variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['Variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_outputs = []
        if m.get('NodeOutputs') is not None:
            for k1 in m.get('NodeOutputs'):
                temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodesOutputsNodeOutputs()
                self.node_outputs.append(temp_model.from_map(k1))

        self.tables = []
        if m.get('Tables') is not None:
            for k1 in m.get('Tables'):
                temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodesOutputsTables()
                self.tables.append(temp_model.from_map(k1))

        self.variables = []
        if m.get('Variables') is not None:
            for k1 in m.get('Variables'):
                temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodesOutputsVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class ListNodeDependenciesResponseBodyPagingInfoNodesOutputsVariables(DaraModel):
    def __init__(
        self,
        artifact_type: str = None,
        id: str = None,
        name: str = None,
        node: main_models.ListNodeDependenciesResponseBodyPagingInfoNodesOutputsVariablesNode = None,
        scope: str = None,
        type: str = None,
        value: str = None,
    ):
        # The artifact type.
        self.artifact_type = artifact_type
        # The variable ID.
        # 
        # >  Prior to SDK version 8.0.0, this field is of type Long. In SDK version 8.0.0 and later, it is of type String. This change does not affect the normal use of the SDK. The parameter is returned based on the type defined in the SDK. Compilation failures caused by the type change may occur only when you upgrade the SDK across version 8.0.0. In this case, you must manually update the data type.
        self.id = id
        # The variable name.
        self.name = name
        # The node to which the variable belongs.
        self.node = node
        # The scope of the variable. Valid values:
        # 
        # *   NodeParameter
        # *   NodeContext
        # *   Workflow
        # *   Workspace
        self.scope = scope
        # The type of the variable. Valid values:
        # 
        # *   NoKvVariableExpression
        # *   Constant
        # *   PassThrough
        # *   System
        # *   NodeOutput
        self.type = type
        # The variable name.
        self.value = value

    def validate(self):
        if self.node:
            self.node.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.node is not None:
            result['Node'] = self.node.to_map()

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Node') is not None:
            temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodesOutputsVariablesNode()
            self.node = temp_model.from_map(m.get('Node'))

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListNodeDependenciesResponseBodyPagingInfoNodesOutputsVariablesNode(DaraModel):
    def __init__(
        self,
        output: str = None,
    ):
        # The node output corresponding to the variable.
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

class ListNodeDependenciesResponseBodyPagingInfoNodesOutputsTables(DaraModel):
    def __init__(
        self,
        guid: str = None,
    ):
        # The table ID.
        self.guid = guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.guid is not None:
            result['Guid'] = self.guid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        return self

class ListNodeDependenciesResponseBodyPagingInfoNodesOutputsNodeOutputs(DaraModel):
    def __init__(
        self,
        data: str = None,
    ):
        # The output of the node.
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        return self

class ListNodeDependenciesResponseBodyPagingInfoNodesInputs(DaraModel):
    def __init__(
        self,
        node_outputs: List[main_models.ListNodeDependenciesResponseBodyPagingInfoNodesInputsNodeOutputs] = None,
        tables: List[main_models.ListNodeDependenciesResponseBodyPagingInfoNodesInputsTables] = None,
        variables: List[main_models.ListNodeDependenciesResponseBodyPagingInfoNodesInputsVariables] = None,
    ):
        # The node output list.
        self.node_outputs = node_outputs
        # The table list.
        self.tables = tables
        # The variable list.
        self.variables = variables

    def validate(self):
        if self.node_outputs:
            for v1 in self.node_outputs:
                 if v1:
                    v1.validate()
        if self.tables:
            for v1 in self.tables:
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
        result['NodeOutputs'] = []
        if self.node_outputs is not None:
            for k1 in self.node_outputs:
                result['NodeOutputs'].append(k1.to_map() if k1 else None)

        result['Tables'] = []
        if self.tables is not None:
            for k1 in self.tables:
                result['Tables'].append(k1.to_map() if k1 else None)

        result['Variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['Variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_outputs = []
        if m.get('NodeOutputs') is not None:
            for k1 in m.get('NodeOutputs'):
                temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodesInputsNodeOutputs()
                self.node_outputs.append(temp_model.from_map(k1))

        self.tables = []
        if m.get('Tables') is not None:
            for k1 in m.get('Tables'):
                temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodesInputsTables()
                self.tables.append(temp_model.from_map(k1))

        self.variables = []
        if m.get('Variables') is not None:
            for k1 in m.get('Variables'):
                temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodesInputsVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class ListNodeDependenciesResponseBodyPagingInfoNodesInputsVariables(DaraModel):
    def __init__(
        self,
        artifact_type: str = None,
        id: str = None,
        name: str = None,
        node: main_models.ListNodeDependenciesResponseBodyPagingInfoNodesInputsVariablesNode = None,
        scope: str = None,
        type: str = None,
        value: str = None,
    ):
        # The artifact type.
        self.artifact_type = artifact_type
        # The variable ID.
        # 
        # >  Prior to SDK version 8.0.0, this field is of type Long. In SDK version 8.0.0 and later, it is of type String. This change does not affect the normal use of the SDK. The parameter is returned based on the type defined in the SDK. Compilation failures caused by the type change may occur only when you upgrade the SDK across version 8.0.0. In this case, you must manually update the data type.
        self.id = id
        # The name of the variable.
        self.name = name
        # The node to which the variable belongs.
        self.node = node
        # The scope of the variable. Valid values:
        # 
        # *   NodeParameter
        # *   NodeContext
        # *   Workflow
        # *   Workspace
        self.scope = scope
        # The type of the variable.
        # 
        # *   NoKvVariableExpression
        # *   Constant
        # *   PassThrough
        # *   System
        # *   NodeOutput
        self.type = type
        # The variable name.
        self.value = value

    def validate(self):
        if self.node:
            self.node.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.node is not None:
            result['Node'] = self.node.to_map()

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Node') is not None:
            temp_model = main_models.ListNodeDependenciesResponseBodyPagingInfoNodesInputsVariablesNode()
            self.node = temp_model.from_map(m.get('Node'))

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListNodeDependenciesResponseBodyPagingInfoNodesInputsVariablesNode(DaraModel):
    def __init__(
        self,
        output: str = None,
    ):
        # The output of the node.
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

class ListNodeDependenciesResponseBodyPagingInfoNodesInputsTables(DaraModel):
    def __init__(
        self,
        guid: str = None,
    ):
        # The table ID.
        self.guid = guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.guid is not None:
            result['Guid'] = self.guid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        return self

class ListNodeDependenciesResponseBodyPagingInfoNodesInputsNodeOutputs(DaraModel):
    def __init__(
        self,
        data: str = None,
    ):
        # The output of the node.
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        return self

class ListNodeDependenciesResponseBodyPagingInfoNodesDataSource(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the data source.
        self.name = name
        # The type of the data source.
        self.type = type

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

