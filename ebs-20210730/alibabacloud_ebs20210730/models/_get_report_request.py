# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetReportRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        region_id: str = None,
        report_id: str = None,
        report_type: str = None,
    ):
        # Optional, AppName only takes effect when ReportType=present.
        self.app_name = app_name
        # Region name.
        self.region_id = region_id
        # When ReportType=history, ReportId is required to query historical reports based on ReportId.
        self.report_id = report_id
        # Optional values: history/present.
        self.report_type = report_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        return self

