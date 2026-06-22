# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListDoctorReportsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDoctorReportsResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The reports.
        self.data = data
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListDoctorReportsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDoctorReportsResponseBodyData(DaraModel):
    def __init__(
        self,
        component_types: List[str] = None,
        date_time: str = None,
        summary_report: main_models.ListDoctorReportsResponseBodyDataSummaryReport = None,
    ):
        # The component types.
        # 
        # Valid values:
        # 
        # - compute
        # 
        #   <!-- -->
        # 
        #   <!-- -->
        # 
        #   <!-- -->
        # 
        # - hive
        # 
        #   <!-- -->
        # 
        #   <!-- -->
        # 
        #   <!-- -->
        # 
        # - hdfs
        # 
        #   <!-- -->
        # 
        #   <!-- -->
        # 
        #   <!-- -->
        # 
        # - yarn
        # 
        #   <!-- -->
        # 
        #   <!-- -->
        # 
        #   <!-- -->
        # 
        # - oss
        # 
        #   <!-- -->
        # 
        #   <!-- -->
        # 
        #   <!-- -->
        # 
        # - hbase
        # 
        #   <!-- -->
        # 
        #   <!-- -->
        # 
        #   <!-- -->
        self.component_types = component_types
        # The date on which the report was generated.
        self.date_time = date_time
        # The summary of the report.
        self.summary_report = summary_report

    def validate(self):
        if self.summary_report:
            self.summary_report.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_types is not None:
            result['ComponentTypes'] = self.component_types

        if self.date_time is not None:
            result['DateTime'] = self.date_time

        if self.summary_report is not None:
            result['SummaryReport'] = self.summary_report.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentTypes') is not None:
            self.component_types = m.get('ComponentTypes')

        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

        if m.get('SummaryReport') is not None:
            temp_model = main_models.ListDoctorReportsResponseBodyDataSummaryReport()
            self.summary_report = temp_model.from_map(m.get('SummaryReport'))

        return self

class ListDoctorReportsResponseBodyDataSummaryReport(DaraModel):
    def __init__(
        self,
        score: int = None,
        suggestion: str = None,
        summary: str = None,
    ):
        # The score.
        self.score = score
        # The optimization suggestion.
        self.suggestion = suggestion
        # The summary of the report.
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.score is not None:
            result['Score'] = self.score

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

