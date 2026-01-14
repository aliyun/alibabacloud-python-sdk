# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchCreateAICoachTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_ids: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.task_ids is not None:
            result['taskIds'] = self.task_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')

        return self

