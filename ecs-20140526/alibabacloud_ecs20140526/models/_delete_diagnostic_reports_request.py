# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteDiagnosticReportsRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        report_ids: List[str] = None,
    ):
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of diagnostic report IDs. A maximum of 100 IDs are supported.
        # 
        # This parameter is required.
        self.report_ids = report_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.report_ids is not None:
            result['ReportIds'] = self.report_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReportIds') is not None:
            self.report_ids = m.get('ReportIds')

        return self

