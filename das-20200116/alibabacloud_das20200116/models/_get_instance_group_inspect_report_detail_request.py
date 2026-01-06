# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceGroupInspectReportDetailRequest(DaraModel):
    def __init__(
        self,
        report_id: str = None,
    ):
        # This parameter is required.
        self.report_id = report_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.report_id is not None:
            result['ReportId'] = self.report_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        return self

