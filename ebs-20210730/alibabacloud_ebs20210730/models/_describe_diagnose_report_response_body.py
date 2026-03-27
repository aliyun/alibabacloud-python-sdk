# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class DescribeDiagnoseReportResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        reports: List[main_models.DescribeDiagnoseReportResponseBodyReports] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.next_token = next_token
        self.reports = reports
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.reports:
            for v1 in self.reports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Reports'] = []
        if self.reports is not None:
            for k1 in self.reports:
                result['Reports'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.reports = []
        if m.get('Reports') is not None:
            for k1 in m.get('Reports'):
                temp_model = main_models.DescribeDiagnoseReportResponseBodyReports()
                self.reports.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDiagnoseReportResponseBodyReports(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        creation_time: int = None,
        diagnose_end_time: int = None,
        diagnose_start_time: int = None,
        diagnose_type: str = None,
        events: List[main_models.DescribeDiagnoseReportResponseBodyReportsEvents] = None,
        finished_time: int = None,
        region_id: str = None,
        report_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        severity: str = None,
        status: str = None,
    ):
        self.ali_uid = ali_uid
        self.creation_time = creation_time
        self.diagnose_end_time = diagnose_end_time
        self.diagnose_start_time = diagnose_start_time
        self.diagnose_type = diagnose_type
        self.events = events
        self.finished_time = finished_time
        self.region_id = region_id
        self.report_id = report_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.severity = severity
        self.status = status

    def validate(self):
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.diagnose_end_time is not None:
            result['DiagnoseEndTime'] = self.diagnose_end_time

        if self.diagnose_start_time is not None:
            result['DiagnoseStartTime'] = self.diagnose_start_time

        if self.diagnose_type is not None:
            result['DiagnoseType'] = self.diagnose_type

        result['Events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['Events'].append(k1.to_map() if k1 else None)

        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DiagnoseEndTime') is not None:
            self.diagnose_end_time = m.get('DiagnoseEndTime')

        if m.get('DiagnoseStartTime') is not None:
            self.diagnose_start_time = m.get('DiagnoseStartTime')

        if m.get('DiagnoseType') is not None:
            self.diagnose_type = m.get('DiagnoseType')

        self.events = []
        if m.get('Events') is not None:
            for k1 in m.get('Events'):
                temp_model = main_models.DescribeDiagnoseReportResponseBodyReportsEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDiagnoseReportResponseBodyReportsEvents(DaraModel):
    def __init__(
        self,
        description: str = None,
        event_name: str = None,
        recommend_action: str = None,
        recommend_params: str = None,
        severity: str = None,
        start_time: int = None,
    ):
        self.description = description
        self.event_name = event_name
        self.recommend_action = recommend_action
        self.recommend_params = recommend_params
        self.severity = severity
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.recommend_action is not None:
            result['RecommendAction'] = self.recommend_action

        if self.recommend_params is not None:
            result['RecommendParams'] = self.recommend_params

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('RecommendAction') is not None:
            self.recommend_action = m.get('RecommendAction')

        if m.get('RecommendParams') is not None:
            self.recommend_params = m.get('RecommendParams')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

