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
        # The task end time based on which the reports are filtered. If you do not specify this parameter, all reports are returned.
        self.end_time = end_time
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of records on each page. Default value: 20. Maximum value: 100.
        self.page_size = page_size
        self.report_type = report_type
        # The task start time based on which the reports are filtered. If you do not specify this parameter, all reports are returned.
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

