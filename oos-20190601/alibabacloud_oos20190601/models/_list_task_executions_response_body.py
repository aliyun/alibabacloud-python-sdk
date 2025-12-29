# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListTaskExecutionsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        task_executions: List[main_models.ListTaskExecutionsResponseBodyTaskExecutions] = None,
    ):
        # The details of the task executions.
        self.max_results = max_results
        # The ID of the request.
        self.next_token = next_token
        # The number of entries returned on each page.
        self.request_id = request_id
        # The execution ID of the child node.
        self.task_executions = task_executions

    def validate(self):
        if self.task_executions:
            for v1 in self.task_executions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TaskExecutions'] = []
        if self.task_executions is not None:
            for k1 in self.task_executions:
                result['TaskExecutions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_executions = []
        if m.get('TaskExecutions') is not None:
            for k1 in m.get('TaskExecutions'):
                temp_model = main_models.ListTaskExecutionsResponseBodyTaskExecutions()
                self.task_executions.append(temp_model.from_map(k1))

        return self

class ListTaskExecutionsResponseBodyTaskExecutions(DaraModel):
    def __init__(
        self,
        child_execution_id: str = None,
        create_date: str = None,
        end_date: str = None,
        execution_id: str = None,
        extra_data: Dict[str, Any] = None,
        loop: Dict[str, Any] = None,
        loop_batch_number: int = None,
        loop_item: str = None,
        outputs: str = None,
        parent_task_execution_id: str = None,
        properties: str = None,
        start_date: str = None,
        status: str = None,
        status_message: str = None,
        task_action: str = None,
        task_execution_id: str = None,
        task_name: str = None,
        template_id: str = None,
        update_date: str = None,
    ):
        # The output of the execution.
        self.child_execution_id = child_execution_id
        # The ID of the execution.
        self.create_date = create_date
        # The execution ID of the parent node.
        self.end_date = end_date
        # The action of the task.
        self.execution_id = execution_id
        # The Input parameters of the task execution.
        self.extra_data = extra_data
        # The ID of the template.
        self.loop = loop
        # The status information of the task execution.
        self.loop_batch_number = loop_batch_number
        # The time when the execution was created.
        self.loop_item = loop_item
        # The status of the task.
        self.outputs = outputs
        # The name of the task.
        self.parent_task_execution_id = parent_task_execution_id
        # Queries task executions. Multiple methods are supported to filter task executions.
        self.properties = properties
        # The elements in the loop task.
        self.start_date = start_date
        # The time when the task execution stopped running.
        self.status = status
        # The additional information.
        self.status_message = status_message
        # The execution ID of the task.
        self.task_action = task_action
        # The time when the execution was last updated.
        self.task_execution_id = task_execution_id
        # The time when the execution started.
        self.task_name = task_name
        # The number of times for which the loop task is run.
        self.template_id = template_id
        # The configuration and statistics information of the loop task. This parameter is returned only for the parent node of the loop task.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.child_execution_id is not None:
            result['ChildExecutionId'] = self.child_execution_id

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id

        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data

        if self.loop is not None:
            result['Loop'] = self.loop

        if self.loop_batch_number is not None:
            result['LoopBatchNumber'] = self.loop_batch_number

        if self.loop_item is not None:
            result['LoopItem'] = self.loop_item

        if self.outputs is not None:
            result['Outputs'] = self.outputs

        if self.parent_task_execution_id is not None:
            result['ParentTaskExecutionId'] = self.parent_task_execution_id

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.status is not None:
            result['Status'] = self.status

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        if self.task_action is not None:
            result['TaskAction'] = self.task_action

        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildExecutionId') is not None:
            self.child_execution_id = m.get('ChildExecutionId')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')

        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')

        if m.get('Loop') is not None:
            self.loop = m.get('Loop')

        if m.get('LoopBatchNumber') is not None:
            self.loop_batch_number = m.get('LoopBatchNumber')

        if m.get('LoopItem') is not None:
            self.loop_item = m.get('LoopItem')

        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')

        if m.get('ParentTaskExecutionId') is not None:
            self.parent_task_execution_id = m.get('ParentTaskExecutionId')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')

        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

