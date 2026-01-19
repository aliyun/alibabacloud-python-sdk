# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAIDBClusterTaskLogFilesResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        items: main_models.DescribeAIDBClusterTaskLogFilesResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        page_size: int = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.items = items
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeAIDBClusterTaskLogFilesResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeAIDBClusterTaskLogFilesResponseBodyItems(DaraModel):
    def __init__(
        self,
        sls_log_items: List[main_models.DescribeAIDBClusterTaskLogFilesResponseBodyItemsSlsLogItems] = None,
    ):
        self.sls_log_items = sls_log_items

    def validate(self):
        if self.sls_log_items:
            for v1 in self.sls_log_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SlsLogItems'] = []
        if self.sls_log_items is not None:
            for k1 in self.sls_log_items:
                result['SlsLogItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sls_log_items = []
        if m.get('SlsLogItems') is not None:
            for k1 in m.get('SlsLogItems'):
                temp_model = main_models.DescribeAIDBClusterTaskLogFilesResponseBodyItemsSlsLogItems()
                self.sls_log_items.append(temp_model.from_map(k1))

        return self

class DescribeAIDBClusterTaskLogFilesResponseBodyItemsSlsLogItems(DaraModel):
    def __init__(
        self,
        log_time: str = None,
        message: str = None,
        timestamp: str = None,
    ):
        self.log_time = log_time
        self.message = message
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_time is not None:
            result['LogTime'] = self.log_time

        if self.message is not None:
            result['Message'] = self.message

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

