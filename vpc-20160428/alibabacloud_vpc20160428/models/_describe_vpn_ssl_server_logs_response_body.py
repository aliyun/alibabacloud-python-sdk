# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeVpnSslServerLogsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        data: main_models.DescribeVpnSslServerLogsResponseBodyData = None,
        is_completed: bool = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        # The number of log entries.
        self.count = count
        # Log information list.
        self.data = data
        # Indicates whether the log is accurate. Valid values:
        # 
        # *   **true**: accurate
        # *   **false**: inaccurate
        self.is_completed = is_completed
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.is_completed is not None:
            result['IsCompleted'] = self.is_completed

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeVpnSslServerLogsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('IsCompleted') is not None:
            self.is_completed = m.get('IsCompleted')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVpnSslServerLogsResponseBodyData(DaraModel):
    def __init__(
        self,
        logs: List[str] = None,
    ):
        self.logs = logs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logs is not None:
            result['Logs'] = self.logs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')

        return self

