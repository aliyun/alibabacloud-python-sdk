# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeErrorLogsResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeErrorLogsResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # Details about the log entries returned.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of error logs on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('Items') is not None:
            temp_model = main_models.DescribeErrorLogsResponseBodyItems()
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

class DescribeErrorLogsResponseBodyItems(DaraModel):
    def __init__(
        self,
        error_log: List[main_models.DescribeErrorLogsResponseBodyItemsErrorLog] = None,
    ):
        self.error_log = error_log

    def validate(self):
        if self.error_log:
            for v1 in self.error_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ErrorLog'] = []
        if self.error_log is not None:
            for k1 in self.error_log:
                result['ErrorLog'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_log = []
        if m.get('ErrorLog') is not None:
            for k1 in m.get('ErrorLog'):
                temp_model = main_models.DescribeErrorLogsResponseBodyItemsErrorLog()
                self.error_log.append(temp_model.from_map(k1))

        return self

class DescribeErrorLogsResponseBodyItemsErrorLog(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        database: str = None,
        error_info: str = None,
        user: str = None,
        user_ip: str = None,
    ):
        # The time when the error log entry was generated. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.create_time = create_time
        self.database = database
        # The error log information.
        self.error_info = error_info
        self.user = user
        self.user_ip = user_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.database is not None:
            result['Database'] = self.database

        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info

        if self.user is not None:
            result['User'] = self.user

        if self.user_ip is not None:
            result['UserIp'] = self.user_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('UserIp') is not None:
            self.user_ip = m.get('UserIp')

        return self

