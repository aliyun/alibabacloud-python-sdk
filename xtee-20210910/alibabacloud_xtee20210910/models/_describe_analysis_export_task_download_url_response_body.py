# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeAnalysisExportTaskDownloadUrlResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeAnalysisExportTaskDownloadUrlResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returned object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeAnalysisExportTaskDownloadUrlResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeAnalysisExportTaskDownloadUrlResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        download_file_url: str = None,
        execute_time: int = None,
        status: str = None,
    ):
        # Download URL.
        self.download_file_url = download_file_url
        # Download execution time
        self.execute_time = execute_time
        # Task status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_file_url is not None:
            result['downloadFileUrl'] = self.download_file_url

        if self.execute_time is not None:
            result['executeTime'] = self.execute_time

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('downloadFileUrl') is not None:
            self.download_file_url = m.get('downloadFileUrl')

        if m.get('executeTime') is not None:
            self.execute_time = m.get('executeTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

