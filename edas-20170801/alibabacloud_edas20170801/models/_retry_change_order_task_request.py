# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RetryChangeOrderTaskRequest(DaraModel):
    def __init__(
        self,
        retry_status: bool = None,
        task_id: str = None,
    ):
        # The retry status.
        self.retry_status = retry_status
        # The ID of the change order task.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.retry_status is not None:
            result['RetryStatus'] = self.retry_status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetryStatus') is not None:
            self.retry_status = m.get('RetryStatus')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

