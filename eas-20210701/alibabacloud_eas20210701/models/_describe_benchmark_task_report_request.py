# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBenchmarkTaskReportRequest(DaraModel):
    def __init__(
        self,
        report_type: str = None,
    ):
        # The report type of the stress testing task. Valid values: RAW and Report.
        self.report_type = report_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.report_type is not None:
            result['ReportType'] = self.report_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        return self

