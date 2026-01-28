# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchDeletePracticeTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        idempotent_id: str = None,
        task_ids_shrink: str = None,
    ):
        self.idempotent_id = idempotent_id
        self.task_ids_shrink = task_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.idempotent_id is not None:
            result['idempotentId'] = self.idempotent_id

        if self.task_ids_shrink is not None:
            result['taskIds'] = self.task_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('idempotentId') is not None:
            self.idempotent_id = m.get('idempotentId')

        if m.get('taskIds') is not None:
            self.task_ids_shrink = m.get('taskIds')

        return self

