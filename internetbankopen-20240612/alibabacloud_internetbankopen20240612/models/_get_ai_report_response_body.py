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
        # The report query result, which contains ReportStatus. The Report object is included only when the report is available.
        self.data = data
        # The unique identity of the request, which is used for Tracing Analysis and troubleshooting. Provide this ID when you troubleshoot exceptions.
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
        # The download information of the available report, which is returned only when ReportStatus is AVAILABLE. The report ownership and the corresponding object version are verified before the download.
        self.report = report
        # The report status. Valid values:
        # - NOT_APPLICABLE: The product does not include a report.
        # - WAITING_DATA: The data call result is not determined.
        # - NO_DATA: No data is found, and no per-use report is generated.
        # - WAITING_PERIOD: The query result for the callId of a periodic product. You must obtain the ReportId by calling ListProductReports and then query the report.
        # - QUEUED: The report task is queued.
        # - RUNNING: The report task is being processed.
        # - AVAILABLE: The report is available, and the Report object is returned in this response.
        # - FAILED: The data call or report generation failed.
        # - EXPIRED: The report content has expired.
        # - UNAVAILABLE: The delivery of the report is suspended.
        # 
        # You can query again later by using the same ID when the status is WAITING_DATA, QUEUED, or RUNNING. Repeated queries do not regenerate the report when the status is FAILED. The Report object is not returned unless the status is AVAILABLE.
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
        # The expiration time of the report content retention period. The time is in UTC RFC 3339 format, ends with Z, and may contain fractional seconds. No download URL is issued after this time. If the delivery is not suspended, EXPIRED is returned. If the delivery is also suspended, UNAVAILABLE is returned preferentially. This is the content expiration time, not the expiration time of a single URL.
        self.content_expires_at = content_expires_at
        # The temporary signed download URL. Use the URL before UrlExpiresAt. The validity period of the signed URL does not exceed 300 seconds and is no later than ContentExpiresAt. If the URL expires but the content has not expired, you can query again to obtain a new URL. The example only shows the URL format and is not a real downloadable link. Use the complete URL in the actual response. Do not concatenate the URL yourself or share it publicly.
        self.download_url = download_url
        # The unique ID of the report. You can use this ID as the reportId parameter to query the report again. This is the report asset ID, not an internal task ID.
        self.report_id = report_id
        # The expiration time of the current DownloadUrl. The time is in UTC RFC 3339 format, ends with Z, and may contain fractional seconds. You cannot use the URL after it expires, and this time is no later than ContentExpiresAt.
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

