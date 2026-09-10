# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSqlExecJobRequest(DaraModel):
    def __init__(
        self,
        concurrency: int = None,
        task_id: int = None,
    ):
        # The concurrency level. This is an optional parameter.
        self.concurrency = concurrency
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrency is not None:
            result['concurrency'] = self.concurrency

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

