# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunClusterInspectResponseBody(DaraModel):
    def __init__(
        self,
        report_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The inspection report ID.
        self.report_id = report_id
        # The request ID.
        self.request_id = request_id
        # The inspection task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.report_id is not None:
            result['reportId'] = self.report_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

