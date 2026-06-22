# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeChartDataRequest(DaraModel):
    def __init__(
        self,
        char_id: str = None,
        chart_id: str = None,
        lang: str = None,
        report_id: int = None,
        time_end: int = None,
        time_start: int = None,
    ):
        # The chart ID.
        # 
        # > Call the [DescribeChartList](~~DescribeChartList~~) operation to obtain this parameter. This parameter is required if the report version is 1.0.0.
        self.char_id = char_id
        # The chart ID.
        # 
        # > Call the [DescribeChartList](~~DescribeChartList~~) operation to obtain this parameter. This parameter is required if the report version is 2.0.0.
        self.chart_id = chart_id
        # The language type for the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The report ID.
        # 
        # > Call the [DescribeCustomizeReportList](~~DescribeCustomizeReportList~~) operation to obtain this parameter.
        self.report_id = report_id
        # The end timestamp for statistics. Unit: milliseconds.
        self.time_end = time_end
        # The start timestamp for statistics. Unit: milliseconds.
        self.time_start = time_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.char_id is not None:
            result['CharId'] = self.char_id

        if self.chart_id is not None:
            result['ChartId'] = self.chart_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.time_end is not None:
            result['TimeEnd'] = self.time_end

        if self.time_start is not None:
            result['TimeStart'] = self.time_start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CharId') is not None:
            self.char_id = m.get('CharId')

        if m.get('ChartId') is not None:
            self.chart_id = m.get('ChartId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('TimeEnd') is not None:
            self.time_end = m.get('TimeEnd')

        if m.get('TimeStart') is not None:
            self.time_start = m.get('TimeStart')

        return self

