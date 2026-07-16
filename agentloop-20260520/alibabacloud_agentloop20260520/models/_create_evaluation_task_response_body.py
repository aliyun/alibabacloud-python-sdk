# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEvaluationTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
        task_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The evaluation task status. After creation, the status is typically `Pending`. After asynchronous orchestration, the status may change to `Running` or `Scheduling`.
        self.status = status
        # The evaluation task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

