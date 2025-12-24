# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeDiagnosticReportAttributesResponseBody(DaraModel):
    def __init__(
        self,
        attributes: str = None,
        creation_time: str = None,
        end_time: str = None,
        finished_time: str = None,
        metric_results: main_models.DescribeDiagnosticReportAttributesResponseBodyMetricResults = None,
        metric_set_id: str = None,
        report_id: str = None,
        request_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        severity: str = None,
        start_time: str = None,
        status: str = None,
    ):
        # The extended attributes of the diagnostic report.
        self.attributes = attributes
        # The time when the diagnostic report was created.
        self.creation_time = creation_time
        # The end of the reporting period of the diagnostic report. The value is the EndTime value that was passed in when you called the [CreateDiagnosticReport](https://help.aliyun.com/document_detail/442490.html) operation to create the diagnostic report.
        self.end_time = end_time
        # The time when the diagnostic report was complete.
        self.finished_time = finished_time
        # The results of all diagnostic metrics in the diagnostic metric set.
        self.metric_results = metric_results
        # The ID of the diagnostic metric set.
        self.metric_set_id = metric_set_id
        # The ID of the diagnostic report, which is the unique identifier of the report.
        self.report_id = report_id
        # The request ID.
        self.request_id = request_id
        # The resource ID.
        self.resource_id = resource_id
        # The type of the resource. ResourceType can only be set to instance, which indicates that only instances are supported.
        self.resource_type = resource_type
        # The severity level of the diagnostic report. The value of this parameter is determined by the highest severity level of all diagnostic metrics. Valid values:
        # 
        # *   Unknown: The diagnostic has not started, failed to run, or exited unexpectedly without a diagnosis.
        # *   Normal: No exceptions were detected.
        # *   Info: Diagnostic information was recorded and may be related to exceptions.
        # *   Warn: Diagnostic information was recorded and may indicate potential exceptions.
        # *   Critical: Critical exceptions were detected.
        self.severity = severity
        # The beginning of the reporting period of the diagnostic report. The value is the StartTime value that was passed in when you called the [CreateDiagnosticReport](https://help.aliyun.com/document_detail/442490.html) operation to create the diagnostic report.
        self.start_time = start_time
        # The state of the diagnostic report. Valid values:
        # 
        # *   InProgress: The diagnostic is in progress.
        # *   Finished: The diagnostic is complete.
        # *   Failed: The diagnostic failed.
        self.status = status

    def validate(self):
        if self.metric_results:
            self.metric_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time

        if self.metric_results is not None:
            result['MetricResults'] = self.metric_results.to_map()

        if self.metric_set_id is not None:
            result['MetricSetId'] = self.metric_set_id

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        if m.get('MetricResults') is not None:
            temp_model = main_models.DescribeDiagnosticReportAttributesResponseBodyMetricResults()
            self.metric_results = temp_model.from_map(m.get('MetricResults'))

        if m.get('MetricSetId') is not None:
            self.metric_set_id = m.get('MetricSetId')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

class DescribeDiagnosticReportAttributesResponseBodyMetricResults(DaraModel):
    def __init__(
        self,
        metric_result: List[main_models.DescribeDiagnosticReportAttributesResponseBodyMetricResultsMetricResult] = None,
    ):
        self.metric_result = metric_result

    def validate(self):
        if self.metric_result:
            for v1 in self.metric_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MetricResult'] = []
        if self.metric_result is not None:
            for k1 in self.metric_result:
                result['MetricResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metric_result = []
        if m.get('MetricResult') is not None:
            for k1 in m.get('MetricResult'):
                temp_model = main_models.DescribeDiagnosticReportAttributesResponseBodyMetricResultsMetricResult()
                self.metric_result.append(temp_model.from_map(k1))

        return self

class DescribeDiagnosticReportAttributesResponseBodyMetricResultsMetricResult(DaraModel):
    def __init__(
        self,
        issues: main_models.DescribeDiagnosticReportAttributesResponseBodyMetricResultsMetricResultIssues = None,
        metric_category: str = None,
        metric_id: str = None,
        severity: str = None,
        status: str = None,
    ):
        # The diagnosed issues.
        self.issues = issues
        # The category of the diagnostic metric.
        self.metric_category = metric_category
        # The ID of the diagnostic metric.
        self.metric_id = metric_id
        # The severity level of the diagnostic metric. Valid values:
        # 
        # *   Unknown: The diagnostic has not started, failed to run, or exited unexpectedly without a diagnosis.
        # *   Normal: No exceptions were detected.
        # *   Info: Diagnostic information was recorded and may be related to exceptions.
        # *   NotSupport: The version of the guest operating system does support diagnosing the metric.
        # *   Warn: Diagnostic information was recorded and may indicate potential exceptions.
        # *   Critical: Critical exceptions were detected.
        self.severity = severity
        # The state of the diagnostic metric. Valid values:
        # 
        # *   InProgress.
        # *   Finished.
        # *   Failed.
        self.status = status

    def validate(self):
        if self.issues:
            self.issues.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.issues is not None:
            result['Issues'] = self.issues.to_map()

        if self.metric_category is not None:
            result['MetricCategory'] = self.metric_category

        if self.metric_id is not None:
            result['MetricId'] = self.metric_id

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Issues') is not None:
            temp_model = main_models.DescribeDiagnosticReportAttributesResponseBodyMetricResultsMetricResultIssues()
            self.issues = temp_model.from_map(m.get('Issues'))

        if m.get('MetricCategory') is not None:
            self.metric_category = m.get('MetricCategory')

        if m.get('MetricId') is not None:
            self.metric_id = m.get('MetricId')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDiagnosticReportAttributesResponseBodyMetricResultsMetricResultIssues(DaraModel):
    def __init__(
        self,
        issue: List[main_models.DescribeDiagnosticReportAttributesResponseBodyMetricResultsMetricResultIssuesIssue] = None,
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
                temp_model = main_models.DescribeDiagnosticReportAttributesResponseBodyMetricResultsMetricResultIssuesIssue()
                self.issue.append(temp_model.from_map(k1))

        return self

class DescribeDiagnosticReportAttributesResponseBodyMetricResultsMetricResultIssuesIssue(DaraModel):
    def __init__(
        self,
        additional: str = None,
        issue_id: str = None,
        occurrence_time: str = None,
        severity: str = None,
    ):
        # The additional data about the diagnosed issue. The value is a JSON string.
        self.additional = additional
        # The ID of the diagnosed issue, which is the unique identifier of the issue.
        self.issue_id = issue_id
        # The time when the diagnosed issue occurred.
        self.occurrence_time = occurrence_time
        # The severity level of the diagnosed issue. Valid values:
        # 
        # *   Info: Diagnostic information was recorded and may be related to exceptions.
        # *   Warn: Diagnostic information was recorded and may indicate potential exceptions.
        # *   Critical: Critical exceptions were detected.
        self.severity = severity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional is not None:
            result['Additional'] = self.additional

        if self.issue_id is not None:
            result['IssueId'] = self.issue_id

        if self.occurrence_time is not None:
            result['OccurrenceTime'] = self.occurrence_time

        if self.severity is not None:
            result['Severity'] = self.severity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Additional') is not None:
            self.additional = m.get('Additional')

        if m.get('IssueId') is not None:
            self.issue_id = m.get('IssueId')

        if m.get('OccurrenceTime') is not None:
            self.occurrence_time = m.get('OccurrenceTime')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        return self

