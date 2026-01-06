# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeErrorLogRecordsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeErrorLogRecordsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        if m.get('Data') is not None:
            temp_model = main_models.DescribeErrorLogRecordsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeErrorLogRecordsResponseBodyData(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        items_numbers: int = None,
        logs: List[main_models.DescribeErrorLogRecordsResponseBodyDataLogs] = None,
        max_records_per_page: int = None,
        page_numbers: int = None,
        start_time: str = None,
        total_records: int = None,
    ):
        self.end_time = end_time
        self.items_numbers = items_numbers
        self.logs = logs
        self.max_records_per_page = max_records_per_page
        self.page_numbers = page_numbers
        self.start_time = start_time
        self.total_records = total_records

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.items_numbers is not None:
            result['ItemsNumbers'] = self.items_numbers

        result['Logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['Logs'].append(k1.to_map() if k1 else None)

        if self.max_records_per_page is not None:
            result['MaxRecordsPerPage'] = self.max_records_per_page

        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_records is not None:
            result['TotalRecords'] = self.total_records

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ItemsNumbers') is not None:
            self.items_numbers = m.get('ItemsNumbers')

        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.DescribeErrorLogRecordsResponseBodyDataLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('MaxRecordsPerPage') is not None:
            self.max_records_per_page = m.get('MaxRecordsPerPage')

        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalRecords') is not None:
            self.total_records = m.get('TotalRecords')

        return self

class DescribeErrorLogRecordsResponseBodyDataLogs(DaraModel):
    def __init__(
        self,
        category: str = None,
        conn_info: str = None,
        content: str = None,
        create_time: str = None,
        dbinstance_name: str = None,
    ):
        self.category = category
        self.conn_info = conn_info
        self.content = content
        self.create_time = create_time
        self.dbinstance_name = dbinstance_name

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

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

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

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        return self

