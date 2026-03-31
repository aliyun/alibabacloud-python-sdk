# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetReportFromTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        template_report: main_models.GetReportFromTemplateResponseBodyTemplateReport = None,
    ):
        self.request_id = request_id
        self.template_report = template_report

    def validate(self):
        if self.template_report:
            self.template_report.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template_report is not None:
            result['TemplateReport'] = self.template_report.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TemplateReport') is not None:
            temp_model = main_models.GetReportFromTemplateResponseBodyTemplateReport()
            self.template_report = temp_model.from_map(m.get('TemplateReport'))

        return self

class GetReportFromTemplateResponseBodyTemplateReport(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        report_create_end_timestamp: int = None,
        report_create_start_timestamp: int = None,
        report_template_id: str = None,
        report_url: str = None,
        status: str = None,
        template_report_id: str = None,
    ):
        self.account_id = account_id
        self.report_create_end_timestamp = report_create_end_timestamp
        self.report_create_start_timestamp = report_create_start_timestamp
        self.report_template_id = report_template_id
        self.report_url = report_url
        self.status = status
        self.template_report_id = template_report_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.report_create_end_timestamp is not None:
            result['ReportCreateEndTimestamp'] = self.report_create_end_timestamp

        if self.report_create_start_timestamp is not None:
            result['ReportCreateStartTimestamp'] = self.report_create_start_timestamp

        if self.report_template_id is not None:
            result['ReportTemplateId'] = self.report_template_id

        if self.report_url is not None:
            result['ReportUrl'] = self.report_url

        if self.status is not None:
            result['Status'] = self.status

        if self.template_report_id is not None:
            result['TemplateReportId'] = self.template_report_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ReportCreateEndTimestamp') is not None:
            self.report_create_end_timestamp = m.get('ReportCreateEndTimestamp')

        if m.get('ReportCreateStartTimestamp') is not None:
            self.report_create_start_timestamp = m.get('ReportCreateStartTimestamp')

        if m.get('ReportTemplateId') is not None:
            self.report_template_id = m.get('ReportTemplateId')

        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateReportId') is not None:
            self.template_report_id = m.get('TemplateReportId')

        return self

