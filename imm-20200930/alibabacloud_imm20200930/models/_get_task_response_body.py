# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        end_time: str = None,
        event_id: str = None,
        message: str = None,
        progress: int = None,
        project_name: str = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        tags: Dict[str, Any] = None,
        task_id: str = None,
        task_request_definition: str = None,
        task_type: str = None,
        user_data: str = None,
    ):
        # The error code of the task.
        self.code = code
        # The end time of the task.
        self.end_time = end_time
        # The event ID.
        self.event_id = event_id
        # The error message of the task.
        self.message = message
        # The task progress. Valid values: 0 to 100. Unit: %.
        # 
        # >  This parameter is valid only if the task is in the `Running` state.``
        self.progress = progress
        # The project name.
        self.project_name = project_name
        # The request ID.
        self.request_id = request_id
        # The start time of the task.
        self.start_time = start_time
        # The status of the task. Valid values:
        # 
        # *   RUNNING: The task is running.
        # *   Succeeded: The task is successful.
        # *   Failed: The task failed.
        self.status = status
        # The tags. This parameter is returned only if you specified Tags when you created the task.
        self.tags = tags
        # The task ID.
        self.task_id = task_id
        # The initial request parameters used to create the task.
        self.task_request_definition = task_request_definition
        # The type of the task. For more information, see [Task types](https://help.aliyun.com/document_detail/2743993.html).
        self.task_type = task_type
        # The user data of the task.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.message is not None:
            result['Message'] = self.message

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_request_definition is not None:
            result['TaskRequestDefinition'] = self.task_request_definition

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskRequestDefinition') is not None:
            self.task_request_definition = m.get('TaskRequestDefinition')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

