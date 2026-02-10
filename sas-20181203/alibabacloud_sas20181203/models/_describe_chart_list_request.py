# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeChartListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        project_code: str = None,
        report_id: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The code of the report. Valid value:
        # 
        # *   **customize_report**
        # 
        # This parameter is required.
        self.project_code = project_code
        # The ID of the report.
        # 
        # >  You can call the [DescribeCustomizeReportList](~~DescribeCustomizeReportList~~) operation to query the ID.
        self.report_id = report_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.project_code is not None:
            result['ProjectCode'] = self.project_code

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProjectCode') is not None:
            self.project_code = m.get('ProjectCode')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        return self

