# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetTaskInstanceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_instance: main_models.GetTaskInstanceResponseBodyTaskInstance = None,
    ):
        # The request ID, which is used to locate logs and troubleshoot issues.
        self.request_id = request_id
        # The detailed information about the task instance.
        self.task_instance = task_instance

    def validate(self):
        if self.task_instance:
            self.task_instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_instance is not None:
            result['TaskInstance'] = self.task_instance.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskInstance') is not None:
            temp_model = main_models.GetTaskInstanceResponseBodyTaskInstance()
            self.task_instance = temp_model.from_map(m.get('TaskInstance'))

        return self

class GetTaskInstanceResponseBodyTaskInstance(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        bizdate: int = None,
        create_time: int = None,
        create_user: str = None,
        data_source: main_models.GetTaskInstanceResponseBodyTaskInstanceDataSource = None,
        description: str = None,
        finished_time: int = None,
        id: int = None,
        inputs: main_models.GetTaskInstanceResponseBodyTaskInstanceInputs = None,
        modify_time: int = None,
        modify_user: str = None,
        operation_type: str = None,
        outputs: main_models.GetTaskInstanceResponseBodyTaskInstanceOutputs = None,
        owner: str = None,
        period_number: int = None,
        priority: int = None,
        project_env: str = None,
        project_id: int = None,
        rerun_mode: str = None,
        run_number: int = None,
        runtime: main_models.GetTaskInstanceResponseBodyTaskInstanceRuntime = None,
        runtime_resource: main_models.GetTaskInstanceResponseBodyTaskInstanceRuntimeResource = None,
        script: main_models.GetTaskInstanceResponseBodyTaskInstanceScript = None,
        started_time: int = None,
        status: str = None,
        tags: List[main_models.GetTaskInstanceResponseBodyTaskInstanceTags] = None,
        task_id: int = None,
        task_name: str = None,
        task_type: str = None,
        timeout: int = None,
        trigger_recurrence: str = None,
        trigger_time: int = None,
        trigger_type: str = None,
        unified_workflow_instance_id: int = None,
        waiting_resource_time: int = None,
        waiting_trigger_time: int = None,
        workflow_id: int = None,
        workflow_instance_id: int = None,
        workflow_instance_type: str = None,
        workflow_name: str = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The business date.
        self.bizdate = bizdate
        # The creation time.
        self.create_time = create_time
        # The account ID of the user who created the instance.
        self.create_user = create_user
        # The data source information associated with the instance.
        self.data_source = data_source
        # The description.
        self.description = description
        # The completion time.
        self.finished_time = finished_time
        # The unique identifier of the node instance.
        self.id = id
        # The input information.
        self.inputs = inputs
        # The modification time.
        self.modify_time = modify_time
        # The account ID of the user who modified the instance.
        self.modify_user = modify_user
        # The type of the most recent operation on the instance.
        self.operation_type = operation_type
        # The output information.
        self.outputs = outputs
        # The account ID of the node owner.
        self.owner = owner
        # The period number. Indicates which scheduling cycle of the day the task instance is in.
        self.period_number = period_number
        # The running priority of the task. Minimum value: 1. Maximum value: 8. A larger value indicates a higher priority. Default value: 1.
        self.priority = priority
        # The project environment. Valid values:
        # - Prod: Production.
        # - Dev: Development.
        self.project_env = project_env
        # The project ID.
        self.project_id = project_id
        # The rerun configuration of the task. Valid values:
        # - AllDenied: reruns are not allowed regardless of whether the task fails or succeeds.
        # - AllAllowed: reruns are allowed regardless of whether the task fails or succeeds.
        # - FailureAllowed: reruns are allowed only when the task fails.
        self.rerun_mode = rerun_mode
        # The current run number. The value starts from 1 by default.
        self.run_number = run_number
        # The runtime information of the instance.
        self.runtime = runtime
        # The resource group information associated with the instance.
        self.runtime_resource = runtime_resource
        # The running script information.
        self.script = script
        # The start time of the run.
        self.started_time = started_time
        # The instance running status. Valid values:
        # - NotRun: Not run.
        # - Running: Running.
        # - WaitTime: Waiting for the TriggerTime to arrive.
        # - CheckingCondition: Checking branch conditions.
        # - WaitResource: Waiting for resources.
        # - Failure: Execution failed.
        # - Success: Execution succeeded.
        # - Checking: Submitted for data quality check.
        # - WaitTrigger: Waiting for an external trigger. Trigger-based nodes enter this status after the waiting time elapses.
        self.status = status
        # The list of node tags.
        self.tags = tags
        # The ID of the corresponding task.
        self.task_id = task_id
        # The name of the corresponding task.
        self.task_name = task_name
        # The type of the corresponding task.
        self.task_type = task_type
        # The timeout period for task execution. Unit: seconds.
        # 
        # Note: The scheduling system rounds the configured value to the nearest hour.
        self.timeout = timeout
        # The running mode when triggered. This parameter takes effect when TriggerType is set to Scheduler. Valid values:
        # 
        # - Normal: a normal scheduled task that is scheduled on a regular basis.
        # - Manual: a manual task that is not scheduled on a regular basis.
        # - Pause: a paused task that is scheduled on a regular basis but is set to failed when scheduling starts.
        # - Skip: a dry-run task that is scheduled on a regular basis but is set to succeeded when scheduling starts.
        # - SkipUnchoose: a task that is not selected in a temporary workflow. This value exists only in temporary workflows. The task is set to succeeded when scheduling starts.
        # - SkipCycle: a weekly or monthly task whose running cycle has not arrived. The task is scheduled on a regular basis but is set to succeeded when scheduling starts.
        # - ConditionUnchoose: a downstream node that is not selected by an upstream branch (IF) node. The task directly becomes a dry run.
        # - RealtimeDeprecated: an expired periodic instance generated in real time. The task is set to succeeded.
        # - PauseCalendar: the instance is paused because a calendar is referenced.
        # - SkipCalendar: the instance is a dry run because a calendar is referenced.
        self.trigger_recurrence = trigger_recurrence
        # The scheduled trigger time.
        self.trigger_time = trigger_time
        # The trigger type. You can obtain the trigger type from the Trigger.Type response parameter of the GetTask operation. Valid values:
        # - Scheduler: triggered by a scheduling cycle.
        # - Manual: manually triggered.
        self.trigger_type = trigger_type
        # The unified workflow instance ID. All task instances within the same business date under a single trigger share the same value for this field.
        self.unified_workflow_instance_id = unified_workflow_instance_id
        # The time when the instance entered the waiting-for-resource state.
        self.waiting_resource_time = waiting_resource_time
        # The time when the instance entered the waiting-for-scheduled-time state.
        self.waiting_trigger_time = waiting_trigger_time
        # The ID of the workflow to which the task instance belongs.
        self.workflow_id = workflow_id
        # The ID of the workflow instance to which the task instance belongs.
        self.workflow_instance_id = workflow_instance_id
        # The type of the workflow instance to which the task instance belongs. Valid values:
        # - SmokeTest: test.
        # - SupplementData: data backfill.
        # - Manual: manual task.
        # - ManualWorkflow: manual workflow.
        # - Normal: periodic scheduling.
        # - ManualFlow: manually executed business flow.
        self.workflow_instance_type = workflow_instance_type
        # The name of the workflow to which the task instance belongs.
        self.workflow_name = workflow_name

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.inputs:
            self.inputs.validate()
        if self.outputs:
            self.outputs.validate()
        if self.runtime:
            self.runtime.validate()
        if self.runtime_resource:
            self.runtime_resource.validate()
        if self.script:
            self.script.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time

        if self.id is not None:
            result['Id'] = self.id

        if self.inputs is not None:
            result['Inputs'] = self.inputs.to_map()

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.outputs is not None:
            result['Outputs'] = self.outputs.to_map()

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.period_number is not None:
            result['PeriodNumber'] = self.period_number

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.rerun_mode is not None:
            result['RerunMode'] = self.rerun_mode

        if self.run_number is not None:
            result['RunNumber'] = self.run_number

        if self.runtime is not None:
            result['Runtime'] = self.runtime.to_map()

        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource.to_map()

        if self.script is not None:
            result['Script'] = self.script.to_map()

        if self.started_time is not None:
            result['StartedTime'] = self.started_time

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.trigger_recurrence is not None:
            result['TriggerRecurrence'] = self.trigger_recurrence

        if self.trigger_time is not None:
            result['TriggerTime'] = self.trigger_time

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.unified_workflow_instance_id is not None:
            result['UnifiedWorkflowInstanceId'] = self.unified_workflow_instance_id

        if self.waiting_resource_time is not None:
            result['WaitingResourceTime'] = self.waiting_resource_time

        if self.waiting_trigger_time is not None:
            result['WaitingTriggerTime'] = self.waiting_trigger_time

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id

        if self.workflow_instance_type is not None:
            result['WorkflowInstanceType'] = self.workflow_instance_type

        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('DataSource') is not None:
            temp_model = main_models.GetTaskInstanceResponseBodyTaskInstanceDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Inputs') is not None:
            temp_model = main_models.GetTaskInstanceResponseBodyTaskInstanceInputs()
            self.inputs = temp_model.from_map(m.get('Inputs'))

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('Outputs') is not None:
            temp_model = main_models.GetTaskInstanceResponseBodyTaskInstanceOutputs()
            self.outputs = temp_model.from_map(m.get('Outputs'))

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PeriodNumber') is not None:
            self.period_number = m.get('PeriodNumber')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RerunMode') is not None:
            self.rerun_mode = m.get('RerunMode')

        if m.get('RunNumber') is not None:
            self.run_number = m.get('RunNumber')

        if m.get('Runtime') is not None:
            temp_model = main_models.GetTaskInstanceResponseBodyTaskInstanceRuntime()
            self.runtime = temp_model.from_map(m.get('Runtime'))

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.GetTaskInstanceResponseBodyTaskInstanceRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('Script') is not None:
            temp_model = main_models.GetTaskInstanceResponseBodyTaskInstanceScript()
            self.script = temp_model.from_map(m.get('Script'))

        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetTaskInstanceResponseBodyTaskInstanceTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('TriggerRecurrence') is not None:
            self.trigger_recurrence = m.get('TriggerRecurrence')

        if m.get('TriggerTime') is not None:
            self.trigger_time = m.get('TriggerTime')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('UnifiedWorkflowInstanceId') is not None:
            self.unified_workflow_instance_id = m.get('UnifiedWorkflowInstanceId')

        if m.get('WaitingResourceTime') is not None:
            self.waiting_resource_time = m.get('WaitingResourceTime')

        if m.get('WaitingTriggerTime') is not None:
            self.waiting_trigger_time = m.get('WaitingTriggerTime')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')

        if m.get('WorkflowInstanceType') is not None:
            self.workflow_instance_type = m.get('WorkflowInstanceType')

        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')

        return self

class GetTaskInstanceResponseBodyTaskInstanceTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The label key.
        self.key = key
        # The label value.
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

class GetTaskInstanceResponseBodyTaskInstanceScript(DaraModel):
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

class GetTaskInstanceResponseBodyTaskInstanceRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: str = None,
        image: str = None,
        resource_group_id: str = None,
    ):
        # The compute unit (CU) consumption configured for the task.
        self.cu = cu
        # The image ID configured for the task.
        self.image = image
        # The identifier of the schedule resource group configured for the task.
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

class GetTaskInstanceResponseBodyTaskInstanceRuntime(DaraModel):
    def __init__(
        self,
        gateway: str = None,
        process_id: str = None,
    ):
        # The machine on which the task runs.
        self.gateway = gateway
        # The unique ID of the run.
        self.process_id = process_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway is not None:
            result['Gateway'] = self.gateway

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gateway') is not None:
            self.gateway = m.get('Gateway')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        return self

class GetTaskInstanceResponseBodyTaskInstanceOutputs(DaraModel):
    def __init__(
        self,
        task_outputs: List[main_models.GetTaskInstanceResponseBodyTaskInstanceOutputsTaskOutputs] = None,
        variables: List[main_models.GetTaskInstanceResponseBodyTaskInstanceOutputsVariables] = None,
    ):
        # The list of task output definitions.
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
                temp_model = main_models.GetTaskInstanceResponseBodyTaskInstanceOutputsTaskOutputs()
                self.task_outputs.append(temp_model.from_map(k1))

        self.variables = []
        if m.get('Variables') is not None:
            for k1 in m.get('Variables'):
                temp_model = main_models.GetTaskInstanceResponseBodyTaskInstanceOutputsVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class GetTaskInstanceResponseBodyTaskInstanceOutputsVariables(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # The name of the variable.
        self.name = name
        # The type. Valid values:
        # - Constant: constant.
        # - PassThrough: output of a parameter node.
        # - System: variable.
        # - NodeOutput: script output.
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

class GetTaskInstanceResponseBodyTaskInstanceOutputsTaskOutputs(DaraModel):
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

class GetTaskInstanceResponseBodyTaskInstanceInputs(DaraModel):
    def __init__(
        self,
        variables: List[main_models.GetTaskInstanceResponseBodyTaskInstanceInputsVariables] = None,
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
                temp_model = main_models.GetTaskInstanceResponseBodyTaskInstanceInputsVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class GetTaskInstanceResponseBodyTaskInstanceInputsVariables(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # The name of the variable.
        self.name = name
        # The type. Valid values:
        # - Constant: constant.
        # - PassThrough: output of a parameter node.
        # - System: variable.
        # - NodeOutput: script output.
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

class GetTaskInstanceResponseBodyTaskInstanceDataSource(DaraModel):
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

