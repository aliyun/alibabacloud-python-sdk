# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class DeleteTableResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_info: main_models.DeleteTableResponseBodyTaskInfo = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the task that is used to delete the table.
        self.task_info = task_info

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskInfo') is not None:
            temp_model = main_models.DeleteTableResponseBodyTaskInfo()
            self.task_info = temp_model.from_map(m.get('TaskInfo'))

        return self

class DeleteTableResponseBodyTaskInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        next_task_id: str = None,
        status: str = None,
        task_id: str = None,
    ):
        # The content of the task.
        self.content = content
        # The ID of the task that is running.
        self.next_task_id = next_task_id
        # The status of the task that is complete.
        self.status = status
        # The ID of the task that is complete.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.next_task_id is not None:
            result['NextTaskId'] = self.next_task_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('NextTaskId') is not None:
            self.next_task_id = m.get('NextTaskId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

