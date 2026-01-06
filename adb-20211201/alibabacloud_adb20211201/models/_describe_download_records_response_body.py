# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeDownloadRecordsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        records: List[main_models.DescribeDownloadRecordsResponseBodyRecords] = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The queried download tasks.
        self.records = records
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.DescribeDownloadRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDownloadRecordsResponseBodyRecords(DaraModel):
    def __init__(
        self,
        download_id: int = None,
        exception_msg: str = None,
        file_name: str = None,
        status: str = None,
        url: str = None,
    ):
        # The download job ID.
        self.download_id = download_id
        # The error message returned if the download job failed.
        self.exception_msg = exception_msg
        # The name of the downloaded file.
        self.file_name = file_name
        # The status of the download job. Valid values:
        # 
        # *   **running**
        # *   **finished**
        # *   **failed**
        self.status = status
        # The download URL of the file.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_id is not None:
            result['DownloadId'] = self.download_id

        if self.exception_msg is not None:
            result['ExceptionMsg'] = self.exception_msg

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.status is not None:
            result['Status'] = self.status

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadId') is not None:
            self.download_id = m.get('DownloadId')

        if m.get('ExceptionMsg') is not None:
            self.exception_msg = m.get('ExceptionMsg')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

