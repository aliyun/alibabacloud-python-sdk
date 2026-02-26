# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class TaskInfo(DaraModel):
    def __init__(
        self,
        code: str = None,
        end_time: str = None,
        message: str = None,
        progress: int = None,
        start_time: str = None,
        status: str = None,
        tags: Dict[str, Any] = None,
        task_id: str = None,
        task_request_definition: str = None,
        task_type: str = None,
        user_data: str = None,
    ):
        # The error code.
        self.code = code
        # The end time of the task.
        self.end_time = end_time
        # The error message.
        self.message = message
        # The progress of the task.
        self.progress = progress
        # The start time of the task.
        self.start_time = start_time
        # The status of the task. Valid values:
        # 
        # *   Running: The task is running.
        # *   Succeeded: The task is successful.
        # *   Failed: The task failed.
        self.status = status
        # The tags of the task. You can search for tasks by tag.
        self.tags = tags
        # The ID of the task.
        self.task_id = task_id
        # The parameter definition in the JSON string format. For more information, see the Request parameters section of the topic about an asynchronous processing task.
        self.task_request_definition = task_request_definition
        # The type of the task.
        self.task_type = task_type
        # The custom user data.
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

        if self.message is not None:
            result['Message'] = self.message

        if self.progress is not None:
            result['Progress'] = self.progress

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

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

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

