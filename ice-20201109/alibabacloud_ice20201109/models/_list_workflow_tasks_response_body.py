# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListWorkflowTasksResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        task_list: List[main_models.ListWorkflowTasksResponseBodyTaskList] = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned in this response.
        self.max_results = max_results
        # A pagination token.
        # 
        # This parameter is required.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The media workflow tasks.
        self.task_list = task_list
        # The total number of entries returned. By default, this parameter is not returned.
        self.total_count = total_count

    def validate(self):
        if self.task_list:
            for v1 in self.task_list:
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

        result['TaskList'] = []
        if self.task_list is not None:
            for k1 in self.task_list:
                result['TaskList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_list = []
        if m.get('TaskList') is not None:
            for k1 in m.get('TaskList'):
                temp_model = main_models.ListWorkflowTasksResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListWorkflowTasksResponseBodyTaskList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        finish_time: str = None,
        status: str = None,
        task_id: str = None,
        task_input: str = None,
        user_data: str = None,
        workflow: main_models.ListWorkflowTasksResponseBodyTaskListWorkflow = None,
    ):
        # The time the task was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time the task was completed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.finish_time = finish_time
        # The task state.
        # 
        # **Valid values**:
        # 
        # *   Init: Initializing
        # *   Failed
        # *   Canceled
        # *   Processing
        # *   Succeed
        self.status = status
        # The ID of the workflow task.
        self.task_id = task_id
        # The input data for the workflow task.
        self.task_input = task_input
        # The custom data that was passed when the task was submitted.
        self.user_data = user_data
        # The information about the workflow template.
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
            temp_model = main_models.ListWorkflowTasksResponseBodyTaskListWorkflow()
            self.workflow = temp_model.from_map(m.get('Workflow'))

        return self

class ListWorkflowTasksResponseBodyTaskListWorkflow(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        media_type: str = None,
        modified_time: str = None,
        name: str = None,
        status: str = None,
        type: str = None,
        workflow_id: str = None,
    ):
        # The creation time of the workflow template.
        self.create_time = create_time
        # The source of the media file. Valid values:
        # 
        # *   OSS: an OSS object.
        # *   Media: a media asset.
        self.media_type = media_type
        # The last modification time of the workflow template.
        self.modified_time = modified_time
        # The name of the workflow template.
        self.name = name
        # The status of the workflow template.
        self.status = status
        # The type of the workflow template.
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

        if self.media_type is not None:
            result['MediaType'] = self.media_type

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

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

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

