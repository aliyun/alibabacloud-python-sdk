# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNisInspectionRecommendationResourcesRequest(DaraModel):
    def __init__(
        self,
        inspection_report_id: str = None,
        language: str = None,
        max_results: int = None,
        next_token: str = None,
        recommendation_code: str = None,
    ):
        # This parameter is required.
        self.inspection_report_id = inspection_report_id
        self.language = language
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.recommendation_code = recommendation_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id

        if self.language is not None:
            result['Language'] = self.language

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.recommendation_code is not None:
            result['RecommendationCode'] = self.recommendation_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RecommendationCode') is not None:
            self.recommendation_code = m.get('RecommendationCode')

        return self

