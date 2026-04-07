# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class UpdateTableAddColumnResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_info: main_models.UpdateTableAddColumnResponseBodyTaskInfo = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the request task. After a request task is submitted, it is divided into multiple subtasks that are run in sequence. After the current subtask is complete, the next subtask starts to run. After all subtasks are complete, the request task is complete. If a request task is aborted due to one of the following issues, address the issue based on the error code and initiate the request task again:
        # 
        # *   The request task fails to be submitted.
        # *   After the request task is submitted, a subtask fails to run.
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
            temp_model = main_models.UpdateTableAddColumnResponseBodyTaskInfo()
            self.task_info = temp_model.from_map(m.get('TaskInfo'))

        return self

class UpdateTableAddColumnResponseBodyTaskInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        next_task_id: str = None,
        status: str = None,
        task_id: str = None,
    ):
        # The details about the status of the current subtask.
        # 
        # *   If the current subtask is successful, success is returned.
        # *   If the current subtask fails, the error details are displayed.
        self.content = content
        # The ID of the subtask that you want to run. If this parameter is left empty, all subtasks are complete.
        self.next_task_id = next_task_id
        # The status of the current subtask. Valid values:
        # 
        # *   operating: The subtask is running.
        # *   success: The subtask succeeds.
        # *   failure: The subtask fails to run. For more information about the error details, see the Content parameter.
        self.status = status
        # The ID of the current subtask.
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

