# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListStreamJobManagerLogsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListStreamJobManagerLogsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The log file entries for JobManager or TaskManager. The logName parameter can be used to retrieve the log content.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the backend exception.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListStreamJobManagerLogsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListStreamJobManagerLogsResponseBodyData(DaraModel):
    def __init__(
        self,
        log_name: str = None,
        mtime: int = None,
        size: int = None,
    ):
        # The original name of the log file, which corresponds to the LogName input parameter of GetStreamLogContent. Pass this value exactly as returned.
        self.log_name = log_name
        # The last modified time of the log file, as a millisecond timestamp since the Unix epoch.
        self.mtime = mtime
        # The size of the log file, in bytes.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_name is not None:
            result['LogName'] = self.log_name

        if self.mtime is not None:
            result['Mtime'] = self.mtime

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')

        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

