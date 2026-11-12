# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_internetbankopen20240612 import models as main_models
from darabonba.model import DaraModel

class GetAiReportResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetAiReportResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetAiReportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAiReportResponseBodyData(DaraModel):
    def __init__(
        self,
        report: main_models.GetAiReportResponseBodyDataReport = None,
        report_status: str = None,
    ):
        self.report = report
        self.report_status = report_status

    def validate(self):
        if self.report:
            self.report.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.report is not None:
            result['Report'] = self.report.to_map()

        if self.report_status is not None:
            result['ReportStatus'] = self.report_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Report') is not None:
            temp_model = main_models.GetAiReportResponseBodyDataReport()
            self.report = temp_model.from_map(m.get('Report'))

        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')

        return self



class GetAiReportResponseBodyDataReport(DaraModel):
    def __init__(
        self,
        content_expires_at: str = None,
        download_url: str = None,
        report_id: str = None,
        url_expires_at: str = None,
    ):
        self.content_expires_at = content_expires_at
        self.download_url = download_url
        self.report_id = report_id
        self.url_expires_at = url_expires_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_expires_at is not None:
            result['ContentExpiresAt'] = self.content_expires_at

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.url_expires_at is not None:
            result['UrlExpiresAt'] = self.url_expires_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentExpiresAt') is not None:
            self.content_expires_at = m.get('ContentExpiresAt')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('UrlExpiresAt') is not None:
            self.url_expires_at = m.get('UrlExpiresAt')

        return self

