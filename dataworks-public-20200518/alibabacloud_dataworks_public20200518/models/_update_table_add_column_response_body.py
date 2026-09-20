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
        # The information about the request task.
        # 
        # After the request task is submitted, it is divided into multiple subtasks that are executed in sequence. The next subtask is executed only after the current subtask succeeds. The request task ends when all subtasks are completed. The request task terminates in the following situations. You must resolve the issue based on the error code and resubmit the request task:
        # - The request task fails to be submitted.
        # - After the request task is submitted, any subtask fails.
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
        # The detailed execution status of the current subtask:
        # - If the execution succeeds, "success" is returned.
        # - If the execution fails, the corresponding error details are returned.
        self.content = content
        # The ID of the subtask to be executed next. If this field is empty, all subtasks have been completed.
        self.next_task_id = next_task_id
        # The status of the current subtask. Valid values:
        # - operating: The subtask is being executed.
        # - success: The subtask is executed.
        # - failure: The subtask failed to be executed. For detailed error information, see the Content parameter.
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

