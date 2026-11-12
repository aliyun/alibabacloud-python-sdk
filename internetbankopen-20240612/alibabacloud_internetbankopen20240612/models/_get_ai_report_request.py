# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAiReportRequest(DaraModel):
    def __init__(
        self,
        call_id: str = None,
        report_id: str = None,
    ):
        self.call_id = call_id
        self.report_id = report_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_id is not None:
            result['callId'] = self.call_id

        if self.report_id is not None:
            result['reportId'] = self.report_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callId') is not None:
            self.call_id = m.get('callId')

        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        return self

