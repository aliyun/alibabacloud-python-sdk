# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class DescribeNisInspectionReportSummaryResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        inspection_report_id: str = None,
        inspection_task_id: str = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        summary: main_models.DescribeNisInspectionReportSummaryResponseBodySummary = None,
    ):
        self.end_time = end_time
        self.inspection_report_id = inspection_report_id
        self.inspection_task_id = inspection_task_id
        self.request_id = request_id
        self.start_time = start_time
        self.status = status
        self.summary = summary

    def validate(self):
        if self.summary:
            self.summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id

        if self.inspection_task_id is not None:
            result['InspectionTaskId'] = self.inspection_task_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.summary is not None:
            result['Summary'] = self.summary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')

        if m.get('InspectionTaskId') is not None:
            self.inspection_task_id = m.get('InspectionTaskId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Summary') is not None:
            temp_model = main_models.DescribeNisInspectionReportSummaryResponseBodySummary()
            self.summary = temp_model.from_map(m.get('Summary'))

        return self

class DescribeNisInspectionReportSummaryResponseBodySummary(DaraModel):
    def __init__(
        self,
        check_item_count: int = None,
        check_resource_count: int = None,
        pass_rate_summary: List[main_models.DescribeNisInspectionReportSummaryResponseBodySummaryPassRateSummary] = None,
        risk_summary: List[main_models.DescribeNisInspectionReportSummaryResponseBodySummaryRiskSummary] = None,
    ):
        self.check_item_count = check_item_count
        self.check_resource_count = check_resource_count
        self.pass_rate_summary = pass_rate_summary
        self.risk_summary = risk_summary

    def validate(self):
        if self.pass_rate_summary:
            for v1 in self.pass_rate_summary:
                 if v1:
                    v1.validate()
        if self.risk_summary:
            for v1 in self.risk_summary:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_item_count is not None:
            result['CheckItemCount'] = self.check_item_count

        if self.check_resource_count is not None:
            result['CheckResourceCount'] = self.check_resource_count

        result['PassRateSummary'] = []
        if self.pass_rate_summary is not None:
            for k1 in self.pass_rate_summary:
                result['PassRateSummary'].append(k1.to_map() if k1 else None)

        result['RiskSummary'] = []
        if self.risk_summary is not None:
            for k1 in self.risk_summary:
                result['RiskSummary'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckItemCount') is not None:
            self.check_item_count = m.get('CheckItemCount')

        if m.get('CheckResourceCount') is not None:
            self.check_resource_count = m.get('CheckResourceCount')

        self.pass_rate_summary = []
        if m.get('PassRateSummary') is not None:
            for k1 in m.get('PassRateSummary'):
                temp_model = main_models.DescribeNisInspectionReportSummaryResponseBodySummaryPassRateSummary()
                self.pass_rate_summary.append(temp_model.from_map(k1))

        self.risk_summary = []
        if m.get('RiskSummary') is not None:
            for k1 in m.get('RiskSummary'):
                temp_model = main_models.DescribeNisInspectionReportSummaryResponseBodySummaryRiskSummary()
                self.risk_summary.append(temp_model.from_map(k1))

        return self

class DescribeNisInspectionReportSummaryResponseBodySummaryRiskSummary(DaraModel):
    def __init__(
        self,
        resource_count: int = None,
        risk_count: int = None,
        risk_level: str = None,
        risk_type: str = None,
    ):
        self.resource_count = resource_count
        self.risk_count = risk_count
        self.risk_level = risk_level
        self.risk_type = risk_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.risk_type is not None:
            result['RiskType'] = self.risk_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')

        return self

class DescribeNisInspectionReportSummaryResponseBodySummaryPassRateSummary(DaraModel):
    def __init__(
        self,
        pass_rate: float = None,
        pass_rate_scope: str = None,
    ):
        self.pass_rate = pass_rate
        self.pass_rate_scope = pass_rate_scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pass_rate is not None:
            result['PassRate'] = self.pass_rate

        if self.pass_rate_scope is not None:
            result['PassRateScope'] = self.pass_rate_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PassRate') is not None:
            self.pass_rate = m.get('PassRate')

        if m.get('PassRateScope') is not None:
            self.pass_rate_scope = m.get('PassRateScope')

        return self

