# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStandAloneReportsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        report_type: str = None,
        start_time: str = None,
    ):
        # The end of the query\\"s time range. The time must be in UTC and in the `YYYY-MM-DDTHH:mm:ssZ` format. If omitted, no end time filter is applied.
        self.end_time = end_time
        # The number of the page to return. The default value is 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default: 20. Maximum: 100.
        self.page_size = page_size
        self.report_type = report_type
        # The start of the query\\"s time range. The time must be in UTC and in the `YYYY-MM-DDTHH:mm:ssZ` format. If omitted, no start time filter is applied.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

