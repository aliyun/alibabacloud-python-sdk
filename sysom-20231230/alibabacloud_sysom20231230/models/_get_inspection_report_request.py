# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInspectionReportRequest(DaraModel):
    def __init__(
        self,
        report_id: str = None,
    ):
        self.report_id = report_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.report_id is not None:
            result['reportId'] = self.report_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        return self

