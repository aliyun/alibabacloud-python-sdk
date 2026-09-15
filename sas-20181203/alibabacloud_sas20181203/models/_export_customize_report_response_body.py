# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportCustomizeReportResponseBody(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        export_date: str = None,
        export_id: int = None,
        export_status: str = None,
        file_name: str = None,
        report_id: int = None,
        request_id: str = None,
        url_expired_time: int = None,
    ):
        # The download URL of the report.
        self.download_url = download_url
        # The time when the report was generated. Format: YYYY-MM-DD.
        self.export_date = export_date
        # The ID of the export report task.
        self.export_id = export_id
        # The status of the export node. Valid values:
        # - **fail**: The export failed.
        # - **exporting**: The export is in progress.
        # - **success**: The export succeeded.
        self.export_status = export_status
        # The name of the exported file.
        self.file_name = file_name
        # The ID of the security report.
        self.report_id = report_id
        # The request ID, which is a unique identifier that Alibaba Cloud generates for the request. You can use the ID to troubleshoot issues.
        self.request_id = request_id
        # The UNIX timestamp when the report download URL expires. Unit: seconds.
        self.url_expired_time = url_expired_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.export_date is not None:
            result['ExportDate'] = self.export_date

        if self.export_id is not None:
            result['ExportId'] = self.export_id

        if self.export_status is not None:
            result['ExportStatus'] = self.export_status

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.url_expired_time is not None:
            result['UrlExpiredTime'] = self.url_expired_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ExportDate') is not None:
            self.export_date = m.get('ExportDate')

        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')

        if m.get('ExportStatus') is not None:
            self.export_status = m.get('ExportStatus')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UrlExpiredTime') is not None:
            self.url_expired_time = m.get('UrlExpiredTime')

        return self

