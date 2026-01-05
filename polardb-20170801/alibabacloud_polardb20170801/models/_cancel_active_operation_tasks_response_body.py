# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelActiveOperationTasksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_ids: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The IDs of O\\&M events that are canceled at a time. Separate multiple IDs with commas (,).
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        return self

