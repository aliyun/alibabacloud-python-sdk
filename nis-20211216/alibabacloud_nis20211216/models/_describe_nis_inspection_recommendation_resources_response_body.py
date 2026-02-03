# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class DescribeNisInspectionRecommendationResourcesResponseBody(DaraModel):
    def __init__(
        self,
        inspection_report_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resource_list: List[main_models.DescribeNisInspectionRecommendationResourcesResponseBodyResourceList] = None,
        total_count: int = None,
    ):
        self.inspection_report_id = inspection_report_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.resource_list = resource_list
        self.total_count = total_count

    def validate(self):
        if self.resource_list:
            for v1 in self.resource_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceList'] = []
        if self.resource_list is not None:
            for k1 in self.resource_list:
                result['ResourceList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k1 in m.get('ResourceList'):
                temp_model = main_models.DescribeNisInspectionRecommendationResourcesResponseBodyResourceList()
                self.resource_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNisInspectionRecommendationResourcesResponseBodyResourceList(DaraModel):
    def __init__(
        self,
        analysis_data: str = None,
        resource_id: str = None,
        resource_name: str = None,
    ):
        self.analysis_data = analysis_data
        self.resource_id = resource_id
        self.resource_name = resource_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_data is not None:
            result['AnalysisData'] = self.analysis_data

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisData') is not None:
            self.analysis_data = m.get('AnalysisData')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        return self

