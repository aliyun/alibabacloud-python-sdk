# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCheckProcessResponseBody(DaraModel):
    def __init__(
        self,
        finish_count: int = None,
        request_id: str = None,
        status_code: str = None,
        task_id: str = None,
        total_count: int = None,
    ):
        # The total number of assets on which the task is complete.
        self.finish_count = finish_count
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The status code of the Cloud Security Posture Management (CSPM) task. Valid values:
        # 
        # *   0: The task is being initialized. The system is calculating the total number of subtasks.
        # *   1: The task is being executed. You can query the total number of tasks and the number of completed tasks.
        # *   2: The task is successful.
        # *   3: The task times out.
        # *   4: The task is invalid. Check whether assets exist.
        # *   5: No task record is found. Check whether the TaskId parameter is valid.
        self.status_code = status_code
        # The ID of the task.
        self.task_id = task_id
        # The total number of assets on which the task is performed.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finish_count is not None:
            result['FinishCount'] = self.finish_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishCount') is not None:
            self.finish_count = m.get('FinishCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

