# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeDiagnosticReportsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        reports: main_models.DescribeDiagnosticReportsResponseBodyReports = None,
        request_id: str = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The diagnostic reports.
        self.reports = reports
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.reports:
            self.reports.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.reports is not None:
            result['Reports'] = self.reports.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Reports') is not None:
            temp_model = main_models.DescribeDiagnosticReportsResponseBodyReports()
            self.reports = temp_model.from_map(m.get('Reports'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDiagnosticReportsResponseBodyReports(DaraModel):
    def __init__(
        self,
        report: List[main_models.DescribeDiagnosticReportsResponseBodyReportsReport] = None,
    ):
        self.report = report

    def validate(self):
        if self.report:
            for v1 in self.report:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Report'] = []
        if self.report is not None:
            for k1 in self.report:
                result['Report'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.report = []
        if m.get('Report') is not None:
            for k1 in m.get('Report'):
                temp_model = main_models.DescribeDiagnosticReportsResponseBodyReportsReport()
                self.report.append(temp_model.from_map(k1))

        return self

class DescribeDiagnosticReportsResponseBodyReportsReport(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        end_time: str = None,
        finished_time: str = None,
        issues: main_models.DescribeDiagnosticReportsResponseBodyReportsReportIssues = None,
        metric_set_id: str = None,
        report_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        severity: str = None,
        start_time: str = None,
        status: str = None,
    ):
        # The time when the diagnostic report was created.
        self.creation_time = creation_time
        # The end of the time range during which data was queried. The value is the EndTime value that was passed in when you called the [CreateDiagnosticReport](https://help.aliyun.com/document_detail/442490.html) operation to create the diagnostic report.
        self.end_time = end_time
        # The time when the diagnostic was complete.
        self.finished_time = finished_time
        # The diagnosed issues.
        self.issues = issues
        # The ID of the diagnostic metric set.
        self.metric_set_id = metric_set_id
        # The ID of the diagnostic report.
        self.report_id = report_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource.
        self.resource_type = resource_type
        # The severity level of the diagnostic report. Valid values:
        # 
        # *   Unknown: The diagnostic did not start, failed to run, or unexpectedly exited without a diagnosis.
        # *   Normal: No exceptions were detected.
        # *   Info: Diagnostic information was recorded and may be related to exceptions.
        # *   Warn: Diagnostic information was recorded and may indicate exceptions.
        # *   Critical: Critical exceptions were detected.
        self.severity = severity
        # The beginning of the time range during which data was queried. The value is the StartTime value that was passed in when you called the [CreateDiagnosticReport](https://help.aliyun.com/document_detail/442490.html) operation to create the diagnostic report.
        self.start_time = start_time
        # The status of the diagnostic report.
        self.status = status

    def validate(self):
        if self.issues:
            self.issues.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time

        if self.issues is not None:
            result['Issues'] = self.issues.to_map()

        if self.metric_set_id is not None:
            result['MetricSetId'] = self.metric_set_id

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        if m.get('Issues') is not None:
            temp_model = main_models.DescribeDiagnosticReportsResponseBodyReportsReportIssues()
            self.issues = temp_model.from_map(m.get('Issues'))

        if m.get('MetricSetId') is not None:
            self.metric_set_id = m.get('MetricSetId')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDiagnosticReportsResponseBodyReportsReportIssues(DaraModel):
    def __init__(
        self,
        issue: List[main_models.DescribeDiagnosticReportsResponseBodyReportsReportIssuesIssue] = None,
    ):
        self.issue = issue

    def validate(self):
        if self.issue:
            for v1 in self.issue:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Issue'] = []
        if self.issue is not None:
            for k1 in self.issue:
                result['Issue'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.issue = []
        if m.get('Issue') is not None:
            for k1 in m.get('Issue'):
                temp_model = main_models.DescribeDiagnosticReportsResponseBodyReportsReportIssuesIssue()
                self.issue.append(temp_model.from_map(k1))

        return self

class DescribeDiagnosticReportsResponseBodyReportsReportIssuesIssue(DaraModel):
    def __init__(
        self,
        issue_id: str = None,
        metric_category: str = None,
        metric_id: str = None,
        severity: str = None,
    ):
        # The ID of the diagnosed issue, which is the unique identifier of the issue.
        self.issue_id = issue_id
        # The category of the diagnostic metric.
        self.metric_category = metric_category
        # The ID of the diagnostic metric.
        self.metric_id = metric_id
        # The severity level of the diagnostic metric. Valid values:
        # 
        # *   Info: Diagnostic information was recorded and may be related to exceptions.
        # *   Warn: Diagnostic information was recorded and may indicate exceptions.
        # *   Critical: Critical exceptions were detected.
        self.severity = severity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.issue_id is not None:
            result['IssueId'] = self.issue_id

        if self.metric_category is not None:
            result['MetricCategory'] = self.metric_category

        if self.metric_id is not None:
            result['MetricId'] = self.metric_id

        if self.severity is not None:
            result['Severity'] = self.severity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IssueId') is not None:
            self.issue_id = m.get('IssueId')

        if m.get('MetricCategory') is not None:
            self.metric_category = m.get('MetricCategory')

        if m.get('MetricId') is not None:
            self.metric_id = m.get('MetricId')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        return self

