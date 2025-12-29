# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeRunningLogRecordsResponseBody(DaraModel):
    def __init__(
        self,
        engine: str = None,
        items: main_models.DescribeRunningLogRecordsResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The database engine.
        self.engine = engine
        # Details about the operational log entries.
        self.items = items
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeRunningLogRecordsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeRunningLogRecordsResponseBodyItems(DaraModel):
    def __init__(
        self,
        log_records: List[main_models.DescribeRunningLogRecordsResponseBodyItemsLogRecords] = None,
    ):
        self.log_records = log_records

    def validate(self):
        if self.log_records:
            for v1 in self.log_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogRecords'] = []
        if self.log_records is not None:
            for k1 in self.log_records:
                result['LogRecords'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_records = []
        if m.get('LogRecords') is not None:
            for k1 in m.get('LogRecords'):
                temp_model = main_models.DescribeRunningLogRecordsResponseBodyItemsLogRecords()
                self.log_records.append(temp_model.from_map(k1))

        return self

class DescribeRunningLogRecordsResponseBodyItemsLogRecords(DaraModel):
    def __init__(
        self,
        category: str = None,
        conn_info: str = None,
        content: str = None,
        create_time: str = None,
    ):
        # The category of the log entry.
        self.category = category
        # The connection information of the log entry.
        self.conn_info = conn_info
        # The content of the log entry.
        self.content = content
        # The time when the log entry was generated. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.conn_info is not None:
            result['ConnInfo'] = self.conn_info

        if self.content is not None:
            result['Content'] = self.content

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ConnInfo') is not None:
            self.conn_info = m.get('ConnInfo')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        return self

