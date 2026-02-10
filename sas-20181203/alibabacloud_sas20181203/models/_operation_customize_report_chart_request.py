# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperationCustomizeReportChartRequest(DaraModel):
    def __init__(
        self,
        chart_ids: str = None,
        report_id: int = None,
    ):
        # The ID of the chart that is included in the report. Separate multiple IDs with commas (,).
        # 
        # >  You can call the [DescribeChartList](~~DescribeChartList~~) operation to query the ID.
        # 
        # This parameter is required.
        self.chart_ids = chart_ids
        # The ID of the report.
        # 
        # >  You can call the [DescribeCustomizeReportList](~~DescribeCustomizeReportList~~) operation to query the ID.
        # 
        # This parameter is required.
        self.report_id = report_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chart_ids is not None:
            result['ChartIds'] = self.chart_ids

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChartIds') is not None:
            self.chart_ids = m.get('ChartIds')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        return self

