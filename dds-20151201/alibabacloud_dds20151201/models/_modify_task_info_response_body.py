# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyTaskInfoResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_task_id: str = None,
        request_id: str = None,
        success_count: str = None,
    ):
        # The error code for the failed task. It is the same as that of the ModifyTaskInfo operation.
        self.error_code = error_code
        # The ID of the failed task. The operation returns results after a task fails.
        self.error_task_id = error_task_id
        # The request ID.
        self.request_id = request_id
        # The number of successful tasks.
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_task_id is not None:
            result['ErrorTaskId'] = self.error_task_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorTaskId') is not None:
            self.error_task_id = m.get('ErrorTaskId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        return self

