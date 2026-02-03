# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNisInspectionReportCheckItemsShrinkRequest(DaraModel):
    def __init__(
        self,
        category_code: str = None,
        inspection_report_id: str = None,
        language: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_type_shrink: str = None,
        risk_level_shrink: str = None,
    ):
        self.category_code = category_code
        # This parameter is required.
        self.inspection_report_id = inspection_report_id
        self.language = language
        self.max_results = max_results
        self.next_token = next_token
        self.resource_type_shrink = resource_type_shrink
        self.risk_level_shrink = risk_level_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_code is not None:
            result['CategoryCode'] = self.category_code

        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id

        if self.language is not None:
            result['Language'] = self.language

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_type_shrink is not None:
            result['ResourceType'] = self.resource_type_shrink

        if self.risk_level_shrink is not None:
            result['RiskLevel'] = self.risk_level_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryCode') is not None:
            self.category_code = m.get('CategoryCode')

        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceType') is not None:
            self.resource_type_shrink = m.get('ResourceType')

        if m.get('RiskLevel') is not None:
            self.risk_level_shrink = m.get('RiskLevel')

        return self

