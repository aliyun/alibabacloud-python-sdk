# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class StartExecutionResponseBody(DaraModel):
    def __init__(
        self,
        execution: main_models.StartExecutionResponseBodyExecution = None,
        request_id: str = None,
    ):
        # The details of the execution.
        self.execution = execution
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.execution:
            self.execution.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution is not None:
            result['Execution'] = self.execution.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Execution') is not None:
            temp_model = main_models.StartExecutionResponseBodyExecution()
            self.execution = temp_model.from_map(m.get('Execution'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class StartExecutionResponseBodyExecution(DaraModel):
    def __init__(
        self,
        counters: Dict[str, Any] = None,
        create_date: str = None,
        current_tasks: List[main_models.StartExecutionResponseBodyExecutionCurrentTasks] = None,
        description: str = None,
        end_date: str = None,
        executed_by: str = None,
        execution_id: str = None,
        is_parent: bool = None,
        loop_mode: str = None,
        mode: str = None,
        outputs: str = None,
        parameters: str = None,
        parent_execution_id: str = None,
        ram_role: str = None,
        resource_group_id: str = None,
        safety_check: str = None,
        start_date: str = None,
        status: str = None,
        status_message: str = None,
        tags: Dict[str, Any] = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        update_date: str = None,
    ):
        # The number of executions.
        self.counters = counters
        # The time when the execution was created.
        self.create_date = create_date
        # The information about in-progress tasks.
        self.current_tasks = current_tasks
        # The description of the execution.
        self.description = description
        # The time when the execution stopped.
        self.end_date = end_date
        # The account ID of the user who started the execution of the template.
        self.executed_by = executed_by
        # The GUID of the execution.
        self.execution_id = execution_id
        # Indicates whether the execution is a parent execution.
        self.is_parent = is_parent
        # The loop mode.
        self.loop_mode = loop_mode
        # The execution mode.
        self.mode = mode
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
        # The security check mode.
        self.safety_check = safety_check
        # The time when the execution was started.
        self.start_date = start_date
        # The status of the execution.
        self.status = status
        # The status information of the execution.
        self.status_message = status_message
        # The tags of the execution.
        self.tags = tags
        # The ID of the template.
        self.template_id = template_id
        # The name of the template.
        self.template_name = template_name
        # The version number of the template.
        self.template_version = template_version
        # The time when the execution was last updated.
        self.update_date = update_date

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

        if self.loop_mode is not None:
            result['LoopMode'] = self.loop_mode

        if self.mode is not None:
            result['Mode'] = self.mode

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

        if self.safety_check is not None:
            result['SafetyCheck'] = self.safety_check

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.status is not None:
            result['Status'] = self.status

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Counters') is not None:
            self.counters = m.get('Counters')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        self.current_tasks = []
        if m.get('CurrentTasks') is not None:
            for k1 in m.get('CurrentTasks'):
                temp_model = main_models.StartExecutionResponseBodyExecutionCurrentTasks()
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

        if m.get('LoopMode') is not None:
            self.loop_mode = m.get('LoopMode')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

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

        if m.get('SafetyCheck') is not None:
            self.safety_check = m.get('SafetyCheck')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

class StartExecutionResponseBodyExecutionCurrentTasks(DaraModel):
    def __init__(
        self,
        task_action: str = None,
        task_execution_id: str = None,
        task_name: str = None,
    ):
        # The action of the task.
        self.task_action = task_action
        # The execution ID of the task.
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

