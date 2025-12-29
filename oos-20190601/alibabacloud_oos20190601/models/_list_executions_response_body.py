# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListExecutionsResponseBody(DaraModel):
    def __init__(
        self,
        executions: List[main_models.ListExecutionsResponseBodyExecutions] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the task executions.
        self.executions = executions
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of the executions.
        self.total_count = total_count

    def validate(self):
        if self.executions:
            for v1 in self.executions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Executions'] = []
        if self.executions is not None:
            for k1 in self.executions:
                result['Executions'].append(k1.to_map() if k1 else None)

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
        self.executions = []
        if m.get('Executions') is not None:
            for k1 in m.get('Executions'):
                temp_model = main_models.ListExecutionsResponseBodyExecutions()
                self.executions.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListExecutionsResponseBodyExecutions(DaraModel):
    def __init__(
        self,
        category: str = None,
        counters: Dict[str, Any] = None,
        create_date: str = None,
        current_tasks: List[main_models.ListExecutionsResponseBodyExecutionsCurrentTasks] = None,
        description: str = None,
        end_date: str = None,
        executed_by: str = None,
        execution_id: str = None,
        is_parent: bool = None,
        last_successful_trigger_time: str = None,
        last_trigger_outputs: str = None,
        last_trigger_status: str = None,
        last_trigger_status_message: str = None,
        last_trigger_time: str = None,
        mode: str = None,
        next_schedule_time: str = None,
        outputs: str = None,
        parameters: Dict[str, Any] = None,
        parent_execution_id: str = None,
        ram_role: str = None,
        resource_group_id: str = None,
        resource_status: str = None,
        safety_check: str = None,
        start_date: str = None,
        status: str = None,
        status_message: str = None,
        status_reason: str = None,
        tags: Dict[str, Any] = None,
        targets: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        update_date: str = None,
        waiting_status: str = None,
    ):
        # The type of the execution template. Valid values: Other, TimerTrigger, EventTrigger, and AlarmTrigger.
        self.category = category
        # The number of tasks that are counted by execution status.
        self.counters = counters
        # The time when the execution was created.
        self.create_date = create_date
        # The information about the tasks that are running.
        self.current_tasks = current_tasks
        # The description of the execution.
        self.description = description
        # The time when the execution stops running.
        self.end_date = end_date
        # The account ID of the user who started the execution of the template.
        self.executed_by = executed_by
        # The unique ID of the execution.
        self.execution_id = execution_id
        # Indicates whether the execution contains child executions.
        self.is_parent = is_parent
        # The time when the template was last successfully triggered.
        self.last_successful_trigger_time = last_successful_trigger_time
        # The outputs of last trigger.
        self.last_trigger_outputs = last_trigger_outputs
        # The status of the execution after the template was last triggered.
        self.last_trigger_status = last_trigger_status
        # The status message of last trigger.
        self.last_trigger_status_message = last_trigger_status_message
        # The time when the template was last successfully triggered.
        self.last_trigger_time = last_trigger_time
        # The execution mode.
        self.mode = mode
        # The next schedule time for timer trigger execution.
        self.next_schedule_time = next_schedule_time
        # The output of the execution.
        self.outputs = outputs
        # The input parameters of the execution.
        self.parameters = parameters
        # The ID of the parent execution.
        self.parent_execution_id = parent_execution_id
        # The role that started the execution of the template.
        self.ram_role = ram_role
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The status of the resource.
        self.resource_status = resource_status
        # The security check mode. Valid values: Skip, and ConfirmEveryHighRiskAction.
        self.safety_check = safety_check
        # The time when the execution was started.
        self.start_date = start_date
        # The status of the execution. Valid values: Started, Queued, Running, Waiting, Success, Failed, and Cancelled.
        self.status = status
        # The status of the task execution.
        self.status_message = status_message
        # The reason for which the status occurs.
        self.status_reason = status_reason
        # The tags of the execution.
        self.tags = tags
        # The target resource.
        self.targets = targets
        # The ID of the template.
        self.template_id = template_id
        # The name of the template.
        self.template_name = template_name
        # The version number of the template.
        self.template_version = template_version
        # The time when the execution was updated.
        self.update_date = update_date
        # The Waiting state.
        self.waiting_status = waiting_status

    def validate(self):
        if self.current_tasks:
            for v1 in self.current_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.counters is not None:
            result['Counters'] = self.counters

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        result['CurrentTasks'] = []
        if self.current_tasks is not None:
            for k1 in self.current_tasks:
                result['CurrentTasks'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.executed_by is not None:
            result['ExecutedBy'] = self.executed_by

        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id

        if self.is_parent is not None:
            result['IsParent'] = self.is_parent

        if self.last_successful_trigger_time is not None:
            result['LastSuccessfulTriggerTime'] = self.last_successful_trigger_time

        if self.last_trigger_outputs is not None:
            result['LastTriggerOutputs'] = self.last_trigger_outputs

        if self.last_trigger_status is not None:
            result['LastTriggerStatus'] = self.last_trigger_status

        if self.last_trigger_status_message is not None:
            result['LastTriggerStatusMessage'] = self.last_trigger_status_message

        if self.last_trigger_time is not None:
            result['LastTriggerTime'] = self.last_trigger_time

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.next_schedule_time is not None:
            result['NextScheduleTime'] = self.next_schedule_time

        if self.outputs is not None:
            result['Outputs'] = self.outputs

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id

        if self.ram_role is not None:
            result['RamRole'] = self.ram_role

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status

        if self.safety_check is not None:
            result['SafetyCheck'] = self.safety_check

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.status is not None:
            result['Status'] = self.status

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.targets is not None:
            result['Targets'] = self.targets

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        if self.waiting_status is not None:
            result['WaitingStatus'] = self.waiting_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Counters') is not None:
            self.counters = m.get('Counters')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        self.current_tasks = []
        if m.get('CurrentTasks') is not None:
            for k1 in m.get('CurrentTasks'):
                temp_model = main_models.ListExecutionsResponseBodyExecutionsCurrentTasks()
                self.current_tasks.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ExecutedBy') is not None:
            self.executed_by = m.get('ExecutedBy')

        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')

        if m.get('IsParent') is not None:
            self.is_parent = m.get('IsParent')

        if m.get('LastSuccessfulTriggerTime') is not None:
            self.last_successful_trigger_time = m.get('LastSuccessfulTriggerTime')

        if m.get('LastTriggerOutputs') is not None:
            self.last_trigger_outputs = m.get('LastTriggerOutputs')

        if m.get('LastTriggerStatus') is not None:
            self.last_trigger_status = m.get('LastTriggerStatus')

        if m.get('LastTriggerStatusMessage') is not None:
            self.last_trigger_status_message = m.get('LastTriggerStatusMessage')

        if m.get('LastTriggerTime') is not None:
            self.last_trigger_time = m.get('LastTriggerTime')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('NextScheduleTime') is not None:
            self.next_schedule_time = m.get('NextScheduleTime')

        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')

        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')

        if m.get('SafetyCheck') is not None:
            self.safety_check = m.get('SafetyCheck')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Targets') is not None:
            self.targets = m.get('Targets')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        if m.get('WaitingStatus') is not None:
            self.waiting_status = m.get('WaitingStatus')

        return self

class ListExecutionsResponseBodyExecutionsCurrentTasks(DaraModel):
    def __init__(
        self,
        task_action: str = None,
        task_execution_id: str = None,
        task_name: str = None,
    ):
        # The execution template of the task.
        self.task_action = task_action
        # The ID of the task execution.
        self.task_execution_id = task_execution_id
        # The name of the task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_action is not None:
            result['TaskAction'] = self.task_action

        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')

        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

