# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCustomizeReportStatusRequest(DaraModel):
    def __init__(
        self,
        pinned_time: int = None,
        report_id: int = None,
        report_status: int = None,
    ):
        # The time when the report is pinned. Unit: milliseconds.
        self.pinned_time = pinned_time
        # The ID of the report.
        # 
        # >  You can call the [DescribeCustomizeReportList](~~DescribeCustomizeReportList~~) operation to query the ID.
        # 
        # This parameter is required.
        self.report_id = report_id
        # The status of the report. Valid values:
        # 
        # *   **0**: disabled.
        # *   **1**: enabled.
        # 
        # This parameter is required.
        self.report_status = report_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pinned_time is not None:
            result['PinnedTime'] = self.pinned_time

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.report_status is not None:
            result['ReportStatus'] = self.report_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PinnedTime') is not None:
            self.pinned_time = m.get('PinnedTime')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')

        return self

