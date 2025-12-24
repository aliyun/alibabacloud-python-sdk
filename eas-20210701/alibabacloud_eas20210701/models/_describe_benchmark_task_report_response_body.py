# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class DescribeBenchmarkTaskReportResponseBody(DaraModel):
    def __init__(
        self,
        data: Any = None,
        report_url: str = None,
        request_id: str = None,
    ):
        # If the value of ReportType is set to RAW, the details about the stress testing report are returned.
        self.data = data
        # If the value of ReportType is set to Report, the URL of the stress testing report is returned.
        self.report_url = report_url
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.report_url is not None:
            result['ReportUrl'] = self.report_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

