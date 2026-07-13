# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bdrc20230808 import models as main_models
from darabonba.model import DaraModel

class DescribeTaskResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeTaskResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        complete_time: int = None,
        error_message: str = None,
        execution_id: str = None,
        expire_time: int = None,
        progress: int = None,
        request_id: str = None,
        start_time: int = None,
        task_description: str = None,
        task_detail: str = None,
        task_id: str = None,
        task_name: str = None,
        task_priority: str = None,
        task_result: str = None,
        task_status: str = None,
        task_type: str = None,
    ):
        # The completion time, formatted as a Unix timestamp in seconds.
        self.complete_time = complete_time
        # The error message returned if the task fails.
        self.error_message = error_message
        # The execution ID. This parameter is deprecated and always returns an empty string.
        self.execution_id = execution_id
        # The expiration time, formatted as a Unix timestamp in seconds.
        self.expire_time = expire_time
        # The task\\"s progress, measured on a scale of 0 to 10,000.
        self.progress = progress
        # The ID of the request.
        self.request_id = request_id
        # The start time, formatted as a Unix timestamp in seconds.
        self.start_time = start_time
        # The task description.
        self.task_description = task_description
        # The details of the task execution.
        self.task_detail = task_detail
        # The ID of the task.
        self.task_id = task_id
        # The task name.
        self.task_name = task_name
        # The task priority. Valid values: `HIGH` (typically for user-initiated tasks) and `LOW` (typically for background tasks).
        self.task_priority = task_priority
        # The result of the task.
        self.task_result = task_result
        # The status of the task. Valid values: `CREATED` (Created), `RUNNING` (Running), `COMPLETE` (Completed), `FAILED` (Failed), `EXPIRED` (Expired), and `CANCELED` (Canceled).
        self.task_status = task_status
        # The task type. Valid values: `UPDATE_RESOURCES` (updates resources and their statuses) and `CHECK_RULES`.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_description is not None:
            result['TaskDescription'] = self.task_description

        if self.task_detail is not None:
            result['TaskDetail'] = self.task_detail

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_priority is not None:
            result['TaskPriority'] = self.task_priority

        if self.task_result is not None:
            result['TaskResult'] = self.task_result

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskDescription') is not None:
            self.task_description = m.get('TaskDescription')

        if m.get('TaskDetail') is not None:
            self.task_detail = m.get('TaskDetail')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskPriority') is not None:
            self.task_priority = m.get('TaskPriority')

        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

