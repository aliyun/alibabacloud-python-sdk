# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDownloadSQLLogsResponseBody(DaraModel):
    def __init__(
        self,
        records: List[main_models.DescribeDownloadSQLLogsResponseBodyRecords] = None,
        request_id: str = None,
    ):
        # List of download records.
        self.records = records
        # Request ID.
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
        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.DescribeDownloadSQLLogsResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDownloadSQLLogsResponseBodyRecords(DaraModel):
    def __init__(
        self,
        download_id: int = None,
        download_url: str = None,
        exception_msg: str = None,
        file_name: str = None,
        status: str = None,
    ):
        # Download record ID.
        self.download_id = download_id
        # Download link.
        self.download_url = download_url
        # Error message.
        self.exception_msg = exception_msg
        # File name.
        self.file_name = file_name
        # Task status, with possible values being:
        # - **running**: Downloading.
        # - **finished**: Completed.
        # - **failed**: Download failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_id is not None:
            result['DownloadId'] = self.download_id

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.exception_msg is not None:
            result['ExceptionMsg'] = self.exception_msg

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadId') is not None:
            self.download_id = m.get('DownloadId')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ExceptionMsg') is not None:
            self.exception_msg = m.get('ExceptionMsg')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

