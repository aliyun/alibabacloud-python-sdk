# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportCustomizeReportRequest(DaraModel):
    def __init__(
        self,
        export_type: str = None,
        report_id: int = None,
    ):
        # The type of the security report that you want to export. Valid values:
        # 
        # *   **HTML**
        # *   **PDF**
        # 
        # >  The default value is HTML. PDF is supported only for security reports in version 2.0.0.
        self.export_type = export_type
        # The ID of the security report.
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
        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        return self

