# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class DescribeDatabaseErrorLogsResponseBody(DaraModel):
    def __init__(
        self,
        error_logs: List[main_models.DescribeDatabaseErrorLogsResponseBodyErrorLogs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array of error logs.
        self.error_logs = error_logs
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of matching error logs.
        self.total_count = total_count

    def validate(self):
        if self.error_logs:
            for v1 in self.error_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ErrorLogs'] = []
        if self.error_logs is not None:
            for k1 in self.error_logs:
                result['ErrorLogs'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_logs = []
        if m.get('ErrorLogs') is not None:
            for k1 in m.get('ErrorLogs'):
                temp_model = main_models.DescribeDatabaseErrorLogsResponseBodyErrorLogs()
                self.error_logs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDatabaseErrorLogsResponseBodyErrorLogs(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        error_info: str = None,
    ):
        # The time when the error log was generated. The time is in UTC and formatted as `yyyy-MM-ddTHH:mm:ssZ` according to the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard.
        # 
        # > The time displayed in the console is 8 hours ahead of the specified UTC time.
        self.create_time = create_time
        # The error information.
        self.error_info = error_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')

        return self

