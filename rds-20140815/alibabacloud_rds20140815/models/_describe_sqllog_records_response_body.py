# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeSQLLogRecordsResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeSQLLogRecordsResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The details about each SQL audit log entry.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of SQL audit log entries on the current page.
        self.page_record_count = page_record_count
        # The ID of the request.
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
            temp_model = main_models.DescribeSQLLogRecordsResponseBodyItems()
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

class DescribeSQLLogRecordsResponseBodyItems(DaraModel):
    def __init__(
        self,
        sqlrecord: List[main_models.DescribeSQLLogRecordsResponseBodyItemsSQLRecord] = None,
    ):
        self.sqlrecord = sqlrecord

    def validate(self):
        if self.sqlrecord:
            for v1 in self.sqlrecord:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SQLRecord'] = []
        if self.sqlrecord is not None:
            for k1 in self.sqlrecord:
                result['SQLRecord'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sqlrecord = []
        if m.get('SQLRecord') is not None:
            for k1 in m.get('SQLRecord'):
                temp_model = main_models.DescribeSQLLogRecordsResponseBodyItemsSQLRecord()
                self.sqlrecord.append(temp_model.from_map(k1))

        return self

class DescribeSQLLogRecordsResponseBodyItemsSQLRecord(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        dbname: str = None,
        execute_time: str = None,
        host_address: str = None,
        return_row_counts: int = None,
        sqltext: str = None,
        thread_id: str = None,
        total_execution_times: int = None,
    ):
        # The username of the account that is recorded in the SQL audit log entry.
        self.account_name = account_name
        # The database name.
        self.dbname = dbname
        # The time at which the SQL statement was executed. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.execute_time = execute_time
        # The IP address of the client that is connected to the instance.
        self.host_address = host_address
        # The number of SQL audit log entries that are returned.
        self.return_row_counts = return_row_counts
        # The SQL statement.
        self.sqltext = sqltext
        # The thread ID.
        self.thread_id = thread_id
        # The execution duration of the SQL statement. Unit: microseconds.
        self.total_execution_times = total_execution_times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time

        if self.host_address is not None:
            result['HostAddress'] = self.host_address

        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        if self.thread_id is not None:
            result['ThreadID'] = self.thread_id

        if self.total_execution_times is not None:
            result['TotalExecutionTimes'] = self.total_execution_times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')

        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')

        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        if m.get('ThreadID') is not None:
            self.thread_id = m.get('ThreadID')

        if m.get('TotalExecutionTimes') is not None:
            self.total_execution_times = m.get('TotalExecutionTimes')

        return self

