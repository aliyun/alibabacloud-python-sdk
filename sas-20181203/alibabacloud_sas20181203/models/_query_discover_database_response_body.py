# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDiscoverDatabaseResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_progress: int = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The progress of the database scan task in percentage.
        self.task_progress = task_progress

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_progress is not None:
            result['TaskProgress'] = self.task_progress

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskProgress') is not None:
            self.task_progress = m.get('TaskProgress')

        return self

