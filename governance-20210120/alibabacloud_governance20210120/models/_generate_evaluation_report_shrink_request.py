# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateEvaluationReportShrinkRequest(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        account_ids_shrink: str = None,
        region_id: str = None,
        report_type: str = None,
    ):
        self.account_id = account_id
        self.account_ids_shrink = account_ids_shrink
        # RegionId
        self.region_id = region_id
        self.report_type = report_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        return self

