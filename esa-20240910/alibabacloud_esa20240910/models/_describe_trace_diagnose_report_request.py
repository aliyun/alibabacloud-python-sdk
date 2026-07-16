# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTraceDiagnoseReportRequest(DaraModel):
    def __init__(
        self,
        task_id: str = None,
        trace_id: str = None,
    ):
        # The diagnostic task ID. You must specify at least one of TraceId and TaskId. If neither is specified, the API returns an error.
        self.task_id = task_id
        # The diagnostic trace ID. You must specify at least one of TraceId and TaskId. If neither is specified, the API returns an error.
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

