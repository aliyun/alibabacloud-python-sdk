# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetAIWorkflowTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        workflow_task: main_models.GetAIWorkflowTaskResponseBodyWorkflowTask = None,
    ):
        # The ID of the request.
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
            temp_model = main_models.GetAIWorkflowTaskResponseBodyWorkflowTask()
            self.workflow_task = temp_model.from_map(m.get('WorkflowTask'))

        return self

class GetAIWorkflowTaskResponseBodyWorkflowTask(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        finish_time: str = None,
        inputs: str = None,
        node_results: str = None,
        outputs: str = None,
        status: str = None,
        task_id: str = None,
        user_data: str = None,
        version: str = None,
        workflow: main_models.GetAIWorkflowTaskResponseBodyWorkflowTaskWorkflow = None,
    ):
        # The time when the task was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the task was complete. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.finish_time = finish_time
        # The input parameters of the workflow task.
        self.inputs = inputs
        # The results of the workflow nodes. The structure of this JSON varies based on the workflow\\"s configuration.
        self.node_results = node_results
        # The node output.
        self.outputs = outputs
        # The task state.
        # 
        # Valid values:
        # 
        # *   running
        # *   stopped
        # *   failed
        # *   partial-succeeded
        # *   succeeded
        self.status = status
        # The ID of the workflow task.
        self.task_id = task_id
        # The user-defined data.
        self.user_data = user_data
        # The version of the workflow template that was executed.
        self.version = version
        # The workflow template information.
        self.workflow = workflow

    def validate(self):
        if self.workflow:
            self.workflow.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.inputs is not None:
            result['Inputs'] = self.inputs

        if self.node_results is not None:
            result['NodeResults'] = self.node_results

        if self.outputs is not None:
            result['Outputs'] = self.outputs

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.version is not None:
            result['Version'] = self.version

        if self.workflow is not None:
            result['Workflow'] = self.workflow.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')

        if m.get('NodeResults') is not None:
            self.node_results = m.get('NodeResults')

        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('Workflow') is not None:
            temp_model = main_models.GetAIWorkflowTaskResponseBodyWorkflowTaskWorkflow()
            self.workflow = temp_model.from_map(m.get('Workflow'))

        return self

class GetAIWorkflowTaskResponseBodyWorkflowTaskWorkflow(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        graph: str = None,
        modified_time: str = None,
        name: str = None,
        status: str = None,
        type: str = None,
        version: str = None,
        workflow_id: str = None,
    ):
        # The time when the template was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The workflow\\"s topological structure.
        self.graph = graph
        # The time when the template was last modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.modified_time = modified_time
        # The name of the workflow template.
        self.name = name
        # Workflow template status. Valid values:
        # 
        # *   Draft
        # *   Published
        # *   Editing
        self.status = status
        # The scenario type of the template.
        self.type = type
        # The template version.
        self.version = version
        # The ID of the workflow template.
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

        if self.graph is not None:
            result['Graph'] = self.graph

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Graph') is not None:
            self.graph = m.get('Graph')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

