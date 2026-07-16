# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListAITasksResponseBody(DaraModel):
    def __init__(
        self,
        http_status_code: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: str = None,
        tasks: List[main_models.ListAITasksResponseBodyTasks] = None,
    ):
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        # 
        # This parameter is required.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The AI tasks.
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.ListAITasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class ListAITasksResponseBodyTasks(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        prompt: str = None,
        status: str = None,
        status_reason: str = None,
        task_id: str = None,
        task_type: str = None,
        update_time: str = None,
    ):
        # The time when the AI task was created. The time is displayed in UTC. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
        self.create_time = create_time
        # The description of the AI task.
        self.prompt = prompt
        # The state of the AI task.
        # 
        # *   PENDING
        # *   WAITING
        # *   RUNNING
        # *   SUCCESS
        # *   FAILURE
        self.status = status
        # The reason why the AI task is in the state.
        self.status_reason = status_reason
        # The ID of the AI task.
        self.task_id = task_id
        # The type of the AI task.
        # 
        # *   GenerateTemplate: The AI task is used to generate a template.
        # *   FixTemplate: The AI task is used to fix a template.
        self.task_type = task_type
        # The time when the AI task was updated. The time is displayed in UTC. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

