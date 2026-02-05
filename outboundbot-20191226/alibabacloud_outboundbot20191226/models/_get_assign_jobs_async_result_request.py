# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAssignJobsAsyncResultRequest(DaraModel):
    def __init__(
        self,
        async_task_id: str = None,
    ):
        # This parameter is required.
        self.async_task_id = async_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_task_id is not None:
            result['AsyncTaskId'] = self.async_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncTaskId') is not None:
            self.async_task_id = m.get('AsyncTaskId')

        return self

