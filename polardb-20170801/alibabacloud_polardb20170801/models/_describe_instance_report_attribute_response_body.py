# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceReportAttributeResponseBody(DaraModel):
    def __init__(
        self,
        latest: bool = None,
        report_description: str = None,
        report_id: str = None,
        report_score: int = None,
        report_status: str = None,
        report_sub_items: List[main_models.DescribeInstanceReportAttributeResponseBodyReportSubItems] = None,
        report_summary: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # Indicates whether the report is the latest one.
        self.latest = latest
        # The detailed description of the inspection report.
        self.report_description = report_description
        # The ID of the instance inspection report.
        self.report_id = report_id
        # The overall score of the inspection report.
        self.report_score = report_score
        # The generation status of the inspection report.
        self.report_status = report_status
        # The check results in the report.
        self.report_sub_items = report_sub_items
        # The overall summary of the inspection report.
        self.report_summary = report_summary
        # The request ID.
        self.request_id = request_id
        # The ID of the inspection task that generated the report.
        self.task_id = task_id

    def validate(self):
        if self.report_sub_items:
            for v1 in self.report_sub_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.latest is not None:
            result['Latest'] = self.latest

        if self.report_description is not None:
            result['ReportDescription'] = self.report_description

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.report_score is not None:
            result['ReportScore'] = self.report_score

        if self.report_status is not None:
            result['ReportStatus'] = self.report_status

        result['ReportSubItems'] = []
        if self.report_sub_items is not None:
            for k1 in self.report_sub_items:
                result['ReportSubItems'].append(k1.to_map() if k1 else None)

        if self.report_summary is not None:
            result['ReportSummary'] = self.report_summary

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Latest') is not None:
            self.latest = m.get('Latest')

        if m.get('ReportDescription') is not None:
            self.report_description = m.get('ReportDescription')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('ReportScore') is not None:
            self.report_score = m.get('ReportScore')

        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')

        self.report_sub_items = []
        if m.get('ReportSubItems') is not None:
            for k1 in m.get('ReportSubItems'):
                temp_model = main_models.DescribeInstanceReportAttributeResponseBodyReportSubItems()
                self.report_sub_items.append(temp_model.from_map(k1))

        if m.get('ReportSummary') is not None:
            self.report_summary = m.get('ReportSummary')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class DescribeInstanceReportAttributeResponseBodyReportSubItems(DaraModel):
    def __init__(
        self,
        risk_level: str = None,
        score: int = None,
        skill_name: str = None,
        summary: str = None,
    ):
        # The risk level of the check item.
        self.risk_level = risk_level
        # The score of the check item.
        self.score = score
        # The name of the inspection skill that generated the check result.
        self.skill_name = skill_name
        # The result summary of the check item.
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.score is not None:
            result['Score'] = self.score

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

