# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelSqlPatternCompareReportResponseBody(DaraModel):
    def __init__(
        self,
        cancel_time: str = None,
        canceled: bool = None,
        report_id: int = None,
        request_id: str = None,
    ):
        # The time when the report was first canceled. The time is in UTC in the yyyy-MM-ddTHH:mmZ format.
        self.cancel_time = cancel_time
        # Indicates whether the report is canceled. The value true is returned when the report is successfully canceled or canceled again.
        self.canceled = canceled
        # The SQL Pattern comparison report ID.
        self.report_id = report_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancel_time is not None:
            result['CancelTime'] = self.cancel_time

        if self.canceled is not None:
            result['Canceled'] = self.canceled

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CancelTime') is not None:
            self.cancel_time = m.get('CancelTime')

        if m.get('Canceled') is not None:
            self.canceled = m.get('Canceled')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

