# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeInspectionTaskReportResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeInspectionTaskReportResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeInspectionTaskReportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeInspectionTaskReportResponseBodyData(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        markdown_text: str = None,
        report_language: str = None,
        status: str = None,
        summary: main_models.DescribeInspectionTaskReportResponseBodyDataSummary = None,
        task_id: str = None,
    ):
        self.instance_ids = instance_ids
        self.markdown_text = markdown_text
        self.report_language = report_language
        self.status = status
        self.summary = summary
        self.task_id = task_id

    def validate(self):
        if self.summary:
            self.summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.markdown_text is not None:
            result['MarkdownText'] = self.markdown_text

        if self.report_language is not None:
            result['ReportLanguage'] = self.report_language

        if self.status is not None:
            result['Status'] = self.status

        if self.summary is not None:
            result['Summary'] = self.summary.to_map()

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('MarkdownText') is not None:
            self.markdown_text = m.get('MarkdownText')

        if m.get('ReportLanguage') is not None:
            self.report_language = m.get('ReportLanguage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Summary') is not None:
            temp_model = main_models.DescribeInspectionTaskReportResponseBodyDataSummary()
            self.summary = temp_model.from_map(m.get('Summary'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class DescribeInspectionTaskReportResponseBodyDataSummary(DaraModel):
    def __init__(
        self,
        error: int = None,
        failed: int = None,
        normal: int = None,
        warning: int = None,
    ):
        self.error = error
        self.failed = failed
        self.normal = normal
        self.warning = warning

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['Error'] = self.error

        if self.failed is not None:
            result['Failed'] = self.failed

        if self.normal is not None:
            result['Normal'] = self.normal

        if self.warning is not None:
            result['Warning'] = self.warning

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Normal') is not None:
            self.normal = m.get('Normal')

        if m.get('Warning') is not None:
            self.warning = m.get('Warning')

        return self

