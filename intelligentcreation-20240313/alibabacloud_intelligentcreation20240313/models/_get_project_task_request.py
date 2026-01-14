# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProjectTaskRequest(DaraModel):
    def __init__(
        self,
        idempotent_id: str = None,
        task_id: str = None,
    ):
        self.idempotent_id = idempotent_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.idempotent_id is not None:
            result['IdempotentId'] = self.idempotent_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdempotentId') is not None:
            self.idempotent_id = m.get('IdempotentId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

