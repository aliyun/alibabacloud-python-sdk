# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeSlowLogRecordsResponseBody(DaraModel):
    def __init__(
        self,
        engine: str = None,
        items: main_models.DescribeSlowLogRecordsResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The database engine.
        self.engine = engine
        # An array that consists of the information about each slow query.
        self.items = items
        # The page number of the returned page. The value is a positive integer that does not exceed the maximum value of the INTEGER data type. Default value: **1**.
        self.page_number = page_number
        # The number of slow query log entries returned on the page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of returned entries.
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
            temp_model = main_models.DescribeSlowLogRecordsResponseBodyItems()
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

class DescribeSlowLogRecordsResponseBodyItems(DaraModel):
    def __init__(
        self,
        log_records: List[main_models.DescribeSlowLogRecordsResponseBodyItemsLogRecords] = None,
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
                temp_model = main_models.DescribeSlowLogRecordsResponseBodyItemsLogRecords()
                self.log_records.append(temp_model.from_map(k1))

        return self

class DescribeSlowLogRecordsResponseBodyItemsLogRecords(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        dbname: str = None,
        docs_examined: int = None,
        execution_start_time: str = None,
        host_address: str = None,
        keys_examined: int = None,
        query_times: str = None,
        return_row_counts: int = None,
        sqltext: str = None,
        table_name: str = None,
    ):
        # The username of the database account that performs the operation.
        self.account_name = account_name
        # The name of the database.
        self.dbname = dbname
        # The number of documents that are scanned during the operation.
        self.docs_examined = docs_examined
        # The start time of the operation. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.execution_start_time = execution_start_time
        # The host IP address that is used to connect to the database.
        self.host_address = host_address
        # The number of rows involved in index scans.
        self.keys_examined = keys_examined
        # The execution time of the statement. Unit: milliseconds.
        self.query_times = query_times
        # The number of rows returned by the SQL statement.
        self.return_row_counts = return_row_counts
        # The SQL statement that is executed during the slow operation.
        self.sqltext = sqltext
        # The name of the collection.
        self.table_name = table_name

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

        if self.docs_examined is not None:
            result['DocsExamined'] = self.docs_examined

        if self.execution_start_time is not None:
            result['ExecutionStartTime'] = self.execution_start_time

        if self.host_address is not None:
            result['HostAddress'] = self.host_address

        if self.keys_examined is not None:
            result['KeysExamined'] = self.keys_examined

        if self.query_times is not None:
            result['QueryTimes'] = self.query_times

        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('DocsExamined') is not None:
            self.docs_examined = m.get('DocsExamined')

        if m.get('ExecutionStartTime') is not None:
            self.execution_start_time = m.get('ExecutionStartTime')

        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')

        if m.get('KeysExamined') is not None:
            self.keys_examined = m.get('KeysExamined')

        if m.get('QueryTimes') is not None:
            self.query_times = m.get('QueryTimes')

        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

