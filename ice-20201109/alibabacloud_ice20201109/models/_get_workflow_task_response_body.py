# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetWorkflowTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        workflow_task: main_models.GetWorkflowTaskResponseBodyWorkflowTask = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the workflow task.
        self.workflow_task = workflow_task

    def validate(self):
        if self.workflow_task:
            self.workflow_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.workflow_task is not None:
            result['WorkflowTask'] = self.workflow_task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WorkflowTask') is not None:
            temp_model = main_models.GetWorkflowTaskResponseBodyWorkflowTask()
            self.workflow_task = temp_model.from_map(m.get('WorkflowTask'))

        return self

class GetWorkflowTaskResponseBodyWorkflowTask(DaraModel):
    def __init__(
        self,
        activity_results: str = None,
        create_time: str = None,
        finish_time: str = None,
        status: str = None,
        task_id: str = None,
        task_input: str = None,
        user_data: str = None,
        workflow: main_models.GetWorkflowTaskResponseBodyWorkflowTaskWorkflow = None,
    ):
        # The results for all nodes of the workflow task.
        self.activity_results = activity_results
        # The time when the task was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the task was complete. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.finish_time = finish_time
        # The task state.
        # 
        # Valid values:
        # 
        # *   Init: The task is being initialized.
        # *   Failed: The task failed.
        # *   Canceled: The task is canceled.
        # *   Processing: The task is in progress.
        # *   Succeed: The task is successful.
        self.status = status
        # The ID of the workflow task.
        self.task_id = task_id
        # The input of the workflow task.
        self.task_input = task_input
        # The user-defined field that was specified when the workflow task was submitted.
        self.user_data = user_data
        # The workflow Information.
        self.workflow = workflow

    def validate(self):
        if self.workflow:
            self.workflow.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_results is not None:
            result['ActivityResults'] = self.activity_results

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_input is not None:
            result['TaskInput'] = self.task_input

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.workflow is not None:
            result['Workflow'] = self.workflow.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityResults') is not None:
            self.activity_results = m.get('ActivityResults')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskInput') is not None:
            self.task_input = m.get('TaskInput')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('Workflow') is not None:
            temp_model = main_models.GetWorkflowTaskResponseBodyWorkflowTaskWorkflow()
            self.workflow = temp_model.from_map(m.get('Workflow'))

        return self

class GetWorkflowTaskResponseBodyWorkflowTaskWorkflow(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        modified_time: str = None,
        name: str = None,
        status: str = None,
        type: str = None,
        workflow_id: str = None,
    ):
        # The time when the workflow was created.
        self.create_time = create_time
        # The time when the workflow was last modified.
        self.modified_time = modified_time
        # The workflow name.
        self.name = name
        # The workflow state.
        # 
        # Valid values:
        # 
        # *   Active
        # *   Inactive
        self.status = status
        # The workflow type.
        # 
        # Valid values:
        # 
        # *   Customize: custom workflow.
        # *   System: system workflow.
        # *   Common: user-created workflow.
        self.type = type
        # The workflow ID.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

