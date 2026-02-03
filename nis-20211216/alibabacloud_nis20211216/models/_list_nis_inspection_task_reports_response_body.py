# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class ListNisInspectionTaskReportsResponseBody(DaraModel):
    def __init__(
        self,
        inspection_report_list: List[main_models.ListNisInspectionTaskReportsResponseBodyInspectionReportList] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.inspection_report_list = inspection_report_list
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.inspection_report_list:
            for v1 in self.inspection_report_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InspectionReportList'] = []
        if self.inspection_report_list is not None:
            for k1 in self.inspection_report_list:
                result['InspectionReportList'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inspection_report_list = []
        if m.get('InspectionReportList') is not None:
            for k1 in m.get('InspectionReportList'):
                temp_model = main_models.ListNisInspectionTaskReportsResponseBodyInspectionReportList()
                self.inspection_report_list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNisInspectionTaskReportsResponseBodyInspectionReportList(DaraModel):
    def __init__(
        self,
        inspection_report_id: str = None,
    ):
        self.inspection_report_id = inspection_report_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')

        return self

